#!/usr/bin/env bash
# Builds a debug APK. Needs: Node 18+, JDK 17, Android SDK (ANDROID_HOME set).
set -euo pipefail
cd "$(dirname "$0")/.."
npm install
[ -d android ] || npx cap add android
python3 scripts/patch_android.py
npx @capacitor/assets generate --android --assetPath assets || echo "Icon generation skipped (default icon used)"
npx cap sync android
cd android
chmod +x gradlew
./gradlew assembleDebug
echo
echo "APK ready: android/app/build/outputs/apk/debug/app-debug.apk"
