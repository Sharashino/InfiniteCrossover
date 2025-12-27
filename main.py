from datetime import datetime
import plistlib
import shutil
import os

userPath = os.path.expanduser('~')
documentsPath = os.path.join(userPath, 'Documents')
plistPath = os.path.join(userPath, 'Library/Preferences/com.codeweavers.CrossOver.plist')
bottlePath = os.path.join(userPath, 'Library/Application Support/CrossOver/Bottles/Steam')
gamesPath = os.path.join(userPath, 'Library/Application Support/CrossOver/Bottles/Steam/drive_c/Program Files (x86)/Steam/steamapps/common')

# set crossover .plist first run date to now
try:
    with open(plistPath, 'rb') as f:
        crossoverFile = plistlib.load(f)

    crossoverFile['FirstRunDate'] = datetime.now()

    with open(plistPath, 'wb') as f:
        plistlib.dump(crossoverFile, f)

    print(f"✓ Updated CrossOver FirstRunDate to {datetime.now()}")
except FileNotFoundError:
    print(f"⚠ CrossOver plist not found at {plistPath}")
except Exception as e:
    print(f"✗ Error updating plist: {e}")

# move all folders inside steamapps/common folder
# into a new folder in user documents
steamCommonBackupPath = os.path.join(documentsPath, 'steam_common')

try:
    os.makedirs(steamCommonBackupPath, exist_ok=True)
    print(f"✓ Created backup folder at {steamCommonBackupPath}")

    if os.path.exists(gamesPath):
        items = os.listdir(gamesPath)
        folders = [item for item in items if os.path.isdir(os.path.join(gamesPath, item))]

        if folders:
            print(f"Found {len(folders)} game folder(s) to move:")

            for folder in folders:
                sourcePath = os.path.join(gamesPath, folder)
                destPath = os.path.join(steamCommonBackupPath, folder)

                try:
                    shutil.move(sourcePath, destPath)
                    print(f"  ✓ Moved: {folder}")
                except Exception as e:
                    print(f"  ✗ Failed to move {folder}: {e}")
        else:
            print("⚠ No folders found in steamapps/common")
    else:
        print(f"⚠ Games path not found: {gamesPath}")

except Exception as e:
    print(f"✗ Error during folder backup: {e}")

# after moving the files delete bottle
try:
    if os.path.exists(bottlePath):
        print(f"\nDeleting Steam bottle at {bottlePath}...")
        shutil.rmtree(bottlePath)
        print("✓ Steam bottle deleted successfully")
    else:
        print(f"⚠ Bottle path not found: {bottlePath}")

except PermissionError:
    print("✗ Permission denied. Try running with sudo or check folder permissions.")
except Exception as e:
    print(f"✗ Error deleting bottle: {e}")

print("\n✓ Script completed!")
