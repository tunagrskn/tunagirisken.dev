#!/usr/bin/env bash
set -euo pipefail

# ============================================
#  tunagirisken.dev - Build & Package Script
# ============================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
PUBLIC_DIR="$PROJECT_DIR/public"
ZIP_NAME="site.zip"

usage() {
  echo -e "${CYAN}Kullanim:${NC} ./run.sh [komut]"
  echo ""
  echo "  build       Hugo ile siteyi derle (production)"
  echo "  serve       Gelistirme sunucusunu baslat (draft dahil)"
  echo "  clean       public/ klasorunu temizle"
  echo "  zip         Siteyi derle ve site.zip olustur"
  echo "  deploy      Derle, zip'le ve hazirla"
  echo "  help        Bu yardim mesajini goster"
  echo ""
}

check_hugo() {
  if ! command -v hugo &>/dev/null; then
    echo -e "${RED}Hata: hugo kurulu degil!${NC}"
    echo "Kurulum: https://gohugo.io/installation/"
    exit 1
  fi
}

do_clean() {
  echo -e "${YELLOW}» public/ klasoru temizleniyor...${NC}"
  rm -rf "$PUBLIC_DIR"
  rm -f "$PROJECT_DIR/$ZIP_NAME"
  echo -e "${GREEN}✓ Temizlendi.${NC}"
}

do_build() {
  check_hugo
  echo -e "${CYAN}» Hugo ile site derleniyor...${NC}"
  cd "$PROJECT_DIR"
  hugo --minify --gc
  echo -e "${GREEN}✓ Site derlendi → public/${NC}"
}

do_zip() {
  if [ ! -d "$PUBLIC_DIR" ]; then
    echo -e "${YELLOW}» public/ bulunamadi, once derleniyor...${NC}"
    do_build
  fi
  echo -e "${CYAN}» site.zip olusturuluyor...${NC}"
  cd "$PUBLIC_DIR"
  rm -f "$PROJECT_DIR/$ZIP_NAME"
  zip -r "$PROJECT_DIR/$ZIP_NAME" . -x "*.DS_Store"
  SIZE=$(du -h "$PROJECT_DIR/$ZIP_NAME" | cut -f1)
  echo -e "${GREEN}✓ $ZIP_NAME olusturuldu ($SIZE)${NC}"
}

do_serve() {
  check_hugo
  echo -e "${CYAN}» Gelistirme sunucusu baslatiliyor...${NC}"
  cd "$PROJECT_DIR"
  hugo server -D --navigateToChanged
}

do_deploy() {
  do_clean
  do_build
  do_zip
  echo ""
  echo -e "${GREEN}========================================${NC}"
  echo -e "${GREEN}  Deploy paketi hazir: $ZIP_NAME${NC}"
  echo -e "${GREEN}========================================${NC}"
}

# ============================================
#  Ana Akis
# ============================================
case "${1:-help}" in
  build)  do_build  ;;
  serve)  do_serve  ;;
  clean)  do_clean  ;;
  zip)    do_zip    ;;
  deploy) do_deploy ;;
  help|*) usage     ;;
esac
