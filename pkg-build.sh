#!/bin/bash
# brew install yq
set -e

CONFIG="config.yaml"
TMP_DIR=".tmp"
PAYLOAD_DIR="$TMP_DIR/payload"

# --- config 読み込み ---
NAME=$(yq '.name' "$CONFIG")
IDENTIFIER=$(yq '.identifier' "$CONFIG")
VERSION=$(yq '.version' "$CONFIG")
SOURCE=$(yq '.source' "$CONFIG")
INSTALL_ROOT=$(yq '.install_root' "$CONFIG")

PKG_NAME="${NAME}-${VERSION}.pkg"

echo "Building $PKG_NAME"

# --- payload 作成 ---
rm -rf "$PAYLOAD_DIR"
mkdir -p "$PAYLOAD_DIR$(dirname "$INSTALL_ROOT")"

cp -R "$SOURCE" "$PAYLOAD_DIR$INSTALL_ROOT"

# --- pkgbuild ---
pkgbuild \
  --root "$PAYLOAD_DIR" \
  --identifier "$IDENTIFIER" \
  --version "$VERSION" \
  "$PKG_NAME"

echo "Done: $PKG_NAME"
