# 💊 DSA Medicine Reminder: Android app

Your website (`www/index.html`) wrapped as a real Android app with **native alarms**, so reminders ring
when the app is closed, the phone is locked, or after a reboot.

## Get the APK (easiest, no Android Studio needed)
1. Create a free GitHub repo and upload everything in this folder (keep `.github/` and `scripts/`).
2. Open the repo → **Actions** tab → **Build Android APK** → **Run workflow** (it also runs on every push).
3. After ~5 minutes, open the finished run → **Artifacts** → download **DSA-Medicine-Reminder-apk** → unzip → `app-debug.apk`.
4. Copy the APK to your phone and install it (allow "Install unknown apps" when asked).

## Build on your own PC instead
Needs Node 18+, JDK 17 and the Android SDK (Android Studio installs it):
```
bash scripts/build-android.sh
```
APK appears at `android/app/build/outputs/apk/debug/app-debug.apk`.

## First run on the phone (important for background alarms)
1. Open the app → allow **Notifications**.
2. When asked, allow **Alarms & reminders** (exact alarms).
3. Phone Settings → Apps → DSA Medicine Reminder → **Battery → Unrestricted** (Xiaomi/Oppo/Vivo/Samsung: also enable *Autostart* / "Allow background activity").
4. Tap **🔔 Test alarm (10 sec)**, lock the phone, and confirm it rings.

## What changed from your website
- **Data is saved on the phone** (accounts, reminders, login session). Before, everything vanished on refresh.
- Each saved reminder is **scheduled as an Android exact alarm** (loud alarm channel + custom beep + vibration).
- Added **Delete** in the reminder editor (it also cancels the Android alarm).
- Added **Test alarm** and **Alarm permissions** buttons.
- App auto-opens to your calendar if you were logged in.
- Your in-page beeping alarm still works while the app is open.

## Notes
- The WhatsApp OTP is still a simulation, as in your original.
- Reminders only ring for dates/times in the future; past ones are skipped.
- To change the app name/package id, edit `capacitor.config.json`.
- The debug APK is fine for personal use. For Play Store you'd need a signed release build.
