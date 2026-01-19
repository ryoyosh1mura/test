#!/bin/bash
set -e

APP_NAME="MyApp"
PKG_NAME="MyInstaller.pkg"

# 1. pkgbuild
pkgbuild \
  --root build/root \
  --identifier com.example.myapp \
  --version 1.0.0 \
  build/${APP_NAME}.pkg

# 2. synthesize
productbuild \
  --synthesize \
  --package build/${APP_NAME}.pkg \
  distribution.xml

# 3. XML修正
python3 edit_distribution.py

# 4. productbuild
productbuild \
  --distribution distribution.xml \
  --resources Resources \
  --package-path build \
  ${PKG_NAME}
