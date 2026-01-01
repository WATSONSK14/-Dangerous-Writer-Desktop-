## AuthorExercise — The Most Dangerous Writing (Desktop)

### Features
- Auto-delete text after 5 seconds of inactivity
- Timer resets on every key press
- Final screen displays an estimated word count
- Clicking the word count on the final screen downloads the FULL text to Desktop as `article.txt`
- Save to Desktop (`article.txt`) and Restart buttons
- Ready for PyInstaller one-file builds

### Screenshot
![Final screen](images/final.jpg)

### Setup
Requirements:
- Python 3.8+
- Pillow (PIL)

Install:
```bash
pip install Pillow
# On Linux, if Tkinter is missing: sudo apt-get install python3-tk
```

### Run
```bash
python main.py
```

### Build (PyInstaller)
Windows:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "images/canvas.png;images" --name "AuthorExercise" main.py
```
macOS/Linux:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "images/canvas.png:images" --name "AuthorExercise" main.py
```

The executable will be under `dist/AuthorExercise`.

### Configuration
- Timeout: Update the `self.time` value in `utils.py#start_write` (e.g., `self.time = 10`).
- Font/size: Adjust `self.font` in `utils.py#placeholder()`.
- Save location: Edit `downland_text()` in `utils.py` (defaults to Desktop).

### Known Issues
- If `images/canvas.png` is missing, the final screen image won’t load. Ensure the file exists or handle it with a fallback.
- Some Linux distros require installing Tkinter separately (`python3-tk`).

### License & Credits
Inspired by “The Most Dangerous Writing App”. Add a license to the repo (e.g., MIT).


