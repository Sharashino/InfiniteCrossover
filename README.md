# InfiniteCrossOver
Quick script to reset CrossOver trial and backup Steam games.

## Prerequisites

- CrossOver installed at default location
- Default bottle path: `~/Library/Application Support/CrossOver/Bottles/Steam`
- Python 3.x

## Usage
```bash
python main.py
```

### After running the script:

1. **Install new Steam bottle** - Create a fresh bottle with default settings
2. **Prepare steamapps folder**:
   - Start downloading any random game in Steam
   - Stop the download and quit Steam
3. **Move games back** - Copy folders from `~/Documents/steam_common` to the new `steamapps/common` folder
4. **Verify games** - Steam will need to verify all moved games before you can play them
