## AuthorExercise — The Most Dangerous Writing (Desktop)

Bir yazı uygulaması: 5 saniye boyunca yazmayı bırakırsanız, o ana kadar yazdıklarınız silinir. “The Most Dangerous Writing App” fikrinden esinlenmiştir. Tkinter ile masaüstünde çalışır.

—

## 🇹🇷 Türkçe

### Özellikler
- 5 saniyelik hareketsizlikte metni otomatik silme
- Anlık yazma ile sayaç sıfırlama
- Son ekranda tahmini kelime sayısı gösterimi
- Final ekrandaki kelime sayısına tıklayınca, yazının TAMAMI masaüstüne `article.txt` olarak indirilir
- Kaydet (masaüstüne `article.txt`) ve Yeniden Başlat butonları
- PyInstaller ile tek dosya `.exe` oluşturma desteği

### Ekran Görüntüsü
![Final ekranı](images/final.jpg)

### Kurulum
Önkoşullar:
- Python 3.8+
- Pillow (PIL)

Kurulum:
```bash
pip install Pillow
# Linux için Tkinter gerekiyorsa: sudo apt-get install python3-tk
```

### Çalıştırma
```bash
python main.py
```

### Derleme (PyInstaller)
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

Oluşan çalıştırılabilir `dist/AuthorExercise` altında bulunur.

### Yapılandırma
- Zaman aşımı: Yazmaya her tuşta 5 saniye olarak sıfırlanır. Süreyi değiştirmek için `utils.py` içinde `start_write` metodundaki değeri güncelleyebilirsiniz (ör. `self.time = 10`).
- Font ve boyut: `utils.py` → `placeholder()` içindeki `self.font` değerini düzenleyin.
- Kayıt konumu: `utils.py` → `downland_text()` masaüstüne kaydeder; dosya adını/konumunu özelleştirebilirsiniz.

### Bilinen Konular
- `images/canvas.png` yoksa final ekran görüntüsü yüklenemez. Dosyanın mevcut olduğundan emin olun veya try/except ile görseli opsiyonel yapın.
- Linux dağıtımlarında Tkinter yüklü olmayabilir; `python3-tk` paketini eklemeniz gerekir.

### Lisans ve İlham
Bu proje, “The Most Dangerous Writing App” konseptinden esinlenmiştir. Lisansınızı depoya ekleyin (örn. MIT).

—

## 🇬🇧 English

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


