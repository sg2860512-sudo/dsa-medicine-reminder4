"""Run after `npx cap add android`: adds permissions, alarm sound, notification icon."""
import pathlib, re, shutil, sys
root = pathlib.Path(__file__).resolve().parent.parent
manifest = root / "android/app/src/main/AndroidManifest.xml"
if not manifest.exists():
    sys.exit("android/ project not found - run `npx cap add android` first")

text = manifest.read_text(encoding="utf-8")
perms = [
    "android.permission.INTERNET",
    "android.permission.POST_NOTIFICATIONS",
    "android.permission.SCHEDULE_EXACT_ALARM",
    "android.permission.USE_EXACT_ALARM",
    "android.permission.RECEIVE_BOOT_COMPLETED",
    "android.permission.VIBRATE",
    "android.permission.WAKE_LOCK",
]
add = ""
for p in perms:
    if p not in text:
        add += f'    <uses-permission android:name="{p}" />\n'
if add:
    text = text.replace("</manifest>", add + "</manifest>")
# keep the activity usable on lock screen when an alarm opens it
if "showWhenLocked" not in text:
    text = text.replace("<activity", '<activity android:showWhenLocked="true" android:turnScreenOn="true"', 1)
manifest.write_text(text, encoding="utf-8")

res = root / "android/app/src/main/res"
(res / "raw").mkdir(parents=True, exist_ok=True)
(res / "drawable").mkdir(parents=True, exist_ok=True)
shutil.copy(root / "android-res/raw/alarm.wav", res / "raw/alarm.wav")
shutil.copy(root / "android-res/drawable/ic_stat_bell.xml", res / "drawable/ic_stat_bell.xml")
print("Android project patched.")
