import time
import keyboard
import tkinter as tk
from tkinter import filedialog

def send_word(word, interval_seconds):
    keyboard.write(word)
    keyboard.press_and_release("enter")
    time.sleep(interval_seconds)

def start_typing():
    file_path = file_path_entry.get()
    interval_seconds = float(interval_entry.get())
    
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()

        while True:
            for word in words:
                send_word(word, interval_seconds)
    except KeyboardInterrupt:
        result_label.config(text="Program sonlandırıldı.")
    except ValueError:
        result_label.config(text="Geçerli bir sayı girilmedi.")
    except FileNotFoundError:
        result_label.config(text="Belirtilen dosya bulunamadı.")

# Tkinter penceresini oluştur
window = tk.Tk()
window.title("UwU BOT v1 by felX")
window.configure(bg="black")  # Arka plan rengini siyah yap

# Pencere yüksekliğini ve genişliğini artır
window_width = 400  # Başlangıç genişliği
window_height = 300  # Başlangıç yüksekliği
window.geometry(f"{window_width+100}x{window_height+100}")

# Dosya yolunu seçmek için bir buton ve etiket
file_path_label = tk.Label(window, text="Kullanılacak kelime listesi dosyasını seçin:", bg="black", fg="white")
file_path_label.pack()
file_path_entry = tk.Entry(window)
file_path_entry.pack()
file_path_button = tk.Button(window, text="Dosya Seç", command=lambda: file_path_entry.insert(0, filedialog.askopenfilename()), bg="black", fg="white")
file_path_button.pack()

# Yazma aralığını girmek için bir etiket ve giriş alanı
interval_label = tk.Label(window, text="Kaç saniyede bir kelime yazılmasını istersiniz?", bg="black", fg="white")
interval_label.pack()
interval_entry = tk.Entry(window)
interval_entry.pack()

# Başlat butonu
start_button = tk.Button(window, text="Başlat", command=start_typing, bg="black", fg="white")
start_button.pack()

# Sonuçları göstermek için bir etiket
result_label = tk.Label(window, text="", bg="black", fg="white")
result_label.pack()

# Tkinter penceresini başlat
window.mainloop()
