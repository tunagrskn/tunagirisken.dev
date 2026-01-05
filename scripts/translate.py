#!/usr/bin/env python3
"""
Hugo Multilingual Auto-Translator
----------------------------------
Bu script Türkçe içeriklerinizi otomatik olarak İngilizceye çevirir.

Kullanım:
    python scripts/translate.py --api-provider deepl --api-key YOUR_API_KEY
    python scripts/translate.py --api-provider openai --api-key YOUR_API_KEY
    python scripts/translate.py --api-provider google --api-key YOUR_API_KEY

Özellikler:
    - Sadece değişen dosyaları çevirir (cache mekanizması)
    - YAML frontmatter'ı korur
    - Hugo shortcode'larını korur
    - Markdown formatını korur
"""

import os
import sys
import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import requests
except ImportError:
    print("❌ 'requests' kütüphanesi bulunamadı. Lütfen yükleyin: pip install requests")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("❌ 'pyyaml' kütüphanesi bulunamadı. Lütfen yükleyin: pip install pyyaml")
    sys.exit(1)


class TranslationCache:
    """Çeviri önbellek mekanizması - gereksiz API çağrılarını önler"""
    
    def __init__(self, cache_file: str = ".translation_cache.json"):
        self.cache_file = cache_file
        self.cache = self._load_cache()
    
    def _load_cache(self) -> Dict:
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_cache(self):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def get_file_hash(self, content: str) -> str:
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def is_cached(self, source_file: str, content_hash: str) -> bool:
        return source_file in self.cache and self.cache[source_file].get('hash') == content_hash
    
    def get_cached_translation(self, source_file: str) -> str:
        return self.cache[source_file].get('translation', '')
    
    def update_cache(self, source_file: str, content_hash: str, translation: str):
        self.cache[source_file] = {
            'hash': content_hash,
            'translation': translation
        }
        self._save_cache()


class ContentParser:
    """Markdown içeriğini parse eder ve çeviri için hazırlar"""
    
    @staticmethod
    def extract_frontmatter(content: str) -> Tuple[Dict, str]:
        """YAML frontmatter'ı ayırır"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return frontmatter, body
        return {}, content
    
    @staticmethod
    def protect_shortcodes(text: str) -> Tuple[str, Dict[str, str]]:
        """Hugo shortcode'larını korur ve placeholder ile değiştirir"""
        shortcode_pattern = r'(\{\{<[^>]+>\}\}|\{\{%[^%]+%\}\})'
        placeholders = {}
        counter = 0
        
        def replacer(match):
            nonlocal counter
            placeholder = f"___SHORTCODE_{counter}___"
            placeholders[placeholder] = match.group(0)
            counter += 1
            return placeholder
        
        protected_text = re.sub(shortcode_pattern, replacer, text)
        return protected_text, placeholders
    
    @staticmethod
    def restore_shortcodes(text: str, placeholders: Dict[str, str]) -> str:
        """Shortcode'ları geri yerleştirir"""
        for placeholder, shortcode in placeholders.items():
            text = text.replace(placeholder, shortcode)
        return text
    
    @staticmethod
    def translate_frontmatter(frontmatter: Dict, translator) -> Dict:
        """Frontmatter'daki çevrilmesi gereken alanları çevirir"""
        translatable_fields = ['title', 'description']
        translated = frontmatter.copy()
        
        for field in translatable_fields:
            if field in translated and isinstance(translated[field], str):
                translated[field] = translator.translate(translated[field])
        
        return translated


class Translator:
    """Çeviri API'leri için temel sınıf"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def translate(self, text: str, source_lang: str = "TR", target_lang: str = "EN") -> str:
        raise NotImplementedError


class DeepLTranslator(Translator):
    """DeepL API çevirici"""
    
    API_URL = "https://api-free.deepl.com/v2/translate"
    
    def translate(self, text: str, source_lang: str = "TR", target_lang: str = "EN") -> str:
        data = {
            'auth_key': self.api_key,
            'text': text,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'preserve_formatting': '1'
        }
        
        response = requests.post(self.API_URL, data=data)
        response.raise_for_status()
        
        result = response.json()
        return result['translations'][0]['text']


class OpenAITranslator(Translator):
    """OpenAI GPT API çevirici"""
    
    API_URL = "https://api.openai.com/v1/chat/completions"
    
    def translate(self, text: str, source_lang: str = "Turkish", target_lang: str = "English") -> str:
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        prompt = f"""Translate the following {source_lang} text to {target_lang}. 
Maintain the markdown formatting, technical terms, and structure. 
Only return the translation, no explanations:

{text}"""
        
        data = {
            'model': 'gpt-4',
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0.3
        }
        
        response = requests.post(self.API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        return result['choices'][0]['message']['content'].strip()


class GoogleTranslator(Translator):
    """Google Cloud Translation API çevirici"""
    
    API_URL = "https://translation.googleapis.com/language/translate/v2"
    
    def translate(self, text: str, source_lang: str = "tr", target_lang: str = "en") -> str:
        params = {
            'key': self.api_key,
            'q': text,
            'source': source_lang,
            'target': target_lang,
            'format': 'text'
        }
        
        response = requests.post(self.API_URL, params=params)
        response.raise_for_status()
        
        result = response.json()
        return result['data']['translations'][0]['translatedText']


def get_translator(provider: str, api_key: str) -> Translator:
    """Çeviri sağlayıcısını döndürür"""
    translators = {
        'deepl': DeepLTranslator,
        'openai': OpenAITranslator,
        'google': GoogleTranslator
    }
    
    if provider not in translators:
        raise ValueError(f"Desteklenmeyen çeviri sağlayıcısı: {provider}")
    
    return translators[provider](api_key)


def translate_file(
    source_path: Path,
    target_path: Path,
    translator: Translator,
    cache: TranslationCache,
    force: bool = False
):
    """Tek bir dosyayı çevirir"""
    
    # Dosyayı oku
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Cache kontrolü
    content_hash = cache.get_file_hash(content)
    if not force and cache.is_cached(str(source_path), content_hash):
        print(f"⚡ Cache'den alınıyor: {source_path.name}")
        translated_content = cache.get_cached_translation(str(source_path))
    else:
        print(f"🔄 Çevriliyor: {source_path.name}")
        
        # Frontmatter ve body'yi ayır
        frontmatter, body = ContentParser.extract_frontmatter(content)
        
        # Shortcode'ları koru
        protected_body, placeholders = ContentParser.protect_shortcodes(body)
        
        # Frontmatter'ı çevir
        translated_frontmatter = ContentParser.translate_frontmatter(frontmatter, translator)
        
        # Body'yi çevir
        translated_body = translator.translate(protected_body)
        
        # Shortcode'ları geri yerleştir
        translated_body = ContentParser.restore_shortcodes(translated_body, placeholders)
        
        # Birleştir
        translated_content = "---\n"
        translated_content += yaml.dump(translated_frontmatter, allow_unicode=True, sort_keys=False)
        translated_content += "---\n\n"
        translated_content += translated_body
        
        # Cache'e kaydet
        cache.update_cache(str(source_path), content_hash, translated_content)
    
    # Hedef dizini oluştur
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Çevrilmiş içeriği yaz
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print(f"✅ Tamamlandı: {target_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Hugo içeriklerini otomatik olarak çevir',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  %(prog)s --api-provider deepl --api-key YOUR_DEEPL_KEY
  %(prog)s --api-provider openai --api-key YOUR_OPENAI_KEY --force
  %(prog)s --api-provider google --api-key YOUR_GOOGLE_KEY --content-dir content
        """
    )
    
    parser.add_argument(
        '--api-provider',
        required=True,
        choices=['deepl', 'openai', 'google'],
        help='Çeviri API sağlayıcısı'
    )
    
    parser.add_argument(
        '--api-key',
        required=True,
        help='API anahtarı'
    )
    
    parser.add_argument(
        '--content-dir',
        default='content',
        help='İçerik dizini (varsayılan: content)'
    )
    
    parser.add_argument(
        '--source-lang',
        default='tr',
        help='Kaynak dil (varsayılan: tr)'
    )
    
    parser.add_argument(
        '--target-lang',
        default='en',
        help='Hedef dil (varsayılan: en)'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Cache\'i yok say ve tüm dosyaları yeniden çevir'
    )
    
    args = parser.parse_args()
    
    # Dizinleri belirle
    content_dir = Path(args.content_dir)
    source_dir = content_dir / args.source_lang
    target_dir = content_dir / args.target_lang
    
    if not source_dir.exists():
        print(f"❌ Kaynak dizin bulunamadı: {source_dir}")
        sys.exit(1)
    
    # Translator ve cache'i hazırla
    translator = get_translator(args.api_provider, args.api_key)
    cache = TranslationCache()
    
    # Markdown dosyalarını bul
    md_files = list(source_dir.rglob('*.md'))
    
    if not md_files:
        print(f"❌ {source_dir} dizininde markdown dosyası bulunamadı")
        sys.exit(1)
    
    print(f"\n📚 {len(md_files)} dosya bulundu\n")
    
    # Her dosyayı çevir
    for source_file in md_files:
        # Hedef dosya yolunu hesapla
        relative_path = source_file.relative_to(source_dir)
        target_file = target_dir / relative_path
        
        try:
            translate_file(source_file, target_file, translator, cache, args.force)
        except Exception as e:
            print(f"❌ Hata ({source_file.name}): {str(e)}")
            continue
    
    print(f"\n🎉 Çeviri tamamlandı!")
    print(f"📁 Kaynak: {source_dir}")
    print(f"📁 Hedef: {target_dir}")


if __name__ == '__main__':
    main()
