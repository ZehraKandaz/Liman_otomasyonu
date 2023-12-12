import pandas as pd
import tkinter as tk
import time

# TIR sınıfı
class Tir:
    def __init__(self, gelis_zamani, tir_plakasi, ülke, ton_adet_20, ton_adet_30, yük_miktari, maliyet):
        self.yük_bilgisi = {
            "ülke":ülke,
            "ton_adet_20":ton_adet_20,
            "ton_adet_30":ton_adet_30,
            "yük_miktari":yük_miktari,
            "maliyet":maliyet
        }
        self.gelis_zamani = gelis_zamani
        self.tir_plakasi = tir_plakasi

# Gemi sınıfı
class Gemi:
    def __init__(self, gelis_zamani, gemi_adi, kapasite, ülke, ton_adet_20=0, ton_adet_30=0, yük_miktari=0, maliyet=0):
        self.yük_bilgisi = {
            "ülke": ülke,
            "ton_adet_20": ton_adet_20,
            "ton_adet_30": ton_adet_30,
            "yük_miktari": yük_miktari,
            "maliyet": maliyet
        }
        self.gelis_zamani = gelis_zamani
        self.gemi_adi = gemi_adi
        self.kapasite = kapasite

# TIR bilgilerinin dosyadan okunması
df = pd.read_csv("olaylar.csv")
tirlar = []
for index, satir in df.iterrows():
    tir = Tir(satir["geliş_zamanı"], satir["tır_plakası"], satir["ülke"], satir["20_ton_adet"], satir["30_ton_adet"], satir["yük_miktarı"], satir["maliyet"])
    tirlar.append(tir)
sirali_tirlar = sorted(tirlar, key=lambda tir: (tir.gelis_zamani, tir.tir_plakasi))

# Gemi bilgilerinin dosyadan okunması
df2 = pd.read_csv("gemiler.csv")
gemiler = []
for index, satir in df2.iterrows():
    gemi = Gemi(satir["geliş_zamanı"], satir["gemi_adı"], satir["kapasite"], satir["gidecek_ülke"])
    gemiler.append(gemi)

# TIR bilgilerini ekrana basan fonksiyon
def tir_bilgileri():
    plaka = plaka_entry.get()
    tir_label.config(text="")
    for tir in sirali_tirlar:
        if tir.tir_plakasi == plaka:
            message = f"Gelis Zamani: {tir.gelis_zamani}\nÜlke: {tir.yük_bilgisi['ülke']}\n20 Ton Adet: {tir.yük_bilgisi['ton_adet_20']}\n30 Ton Adet: {tir.yük_bilgisi['ton_adet_30']}\nYük Miktari: {tir.yük_bilgisi['yük_miktari']}\nMaliyet: {tir.yük_bilgisi['maliyet']}"
            tir_label.config(text=message, fg="#5c0a0a")
            window.update()
            time.sleep(1.5)

# Gemi bilgilerini ekrana basan fonksiyon            
def gemi_bilgileri():
    ad = str(gemi_adi_entry.get())
    gemi_label.config(text="")
    for gemi in gemiler:
        if str(gemi.gemi_adi) == ad:
            message = f"Gelis Zamani: {gemi.gelis_zamani}\nKapasite: {gemi.kapasite}\nÜlke: {gemi.yük_bilgisi['ülke']}\n20 Ton Adet: {gemi.yük_bilgisi['ton_adet_20']}\n30 Ton Adet: {gemi.yük_bilgisi['ton_adet_30']}\nYük Miktari: {gemi.yük_bilgisi['yük_miktari']}\nMaliyet: {gemi.yük_bilgisi['maliyet']}"
            gemi_label.config(text=gemi_label.cget("text") + "\n" + message, fg="#351d63")
            window.update()


istif_alani = []
limandaki_gemiler = []

def liman_simülasyonu():
    for zaman in range(1, int(sayi_entry.get())+1):
        for tir in sirali_tirlar:
            if tir.gelis_zamani == zaman:
                istif_alani.append({tir.yük_bilgisi["ülke"]:tir.yük_bilgisi["yük_miktari"]})
                message = "TIR limana geldi."
                simülasyon_label.config(text=message, fg="#5c0a0a")
                window.update()
                time.sleep(1)
                message = f"Zaman: {zaman}\nTır Plakası: {tir.tir_plakasi}\nGeliş Zamanı: {tir.gelis_zamani}\nÜlke: {tir.yük_bilgisi['ülke']}\n20 Ton Adet: {tir.yük_bilgisi['ton_adet_20']}\n30 Ton Adet: {tir.yük_bilgisi['ton_adet_30']}\nYük Miktari: {tir.yük_bilgisi['yük_miktari']}\nMaliyet: {tir.yük_bilgisi['maliyet']}"
                simülasyon_label.config(text=message, fg="#5c0a0a")
                window.update()
                time.sleep(1)
                message = "TIR yükünü indirdi."
                simülasyon_label.config(text=message, fg="#5c0a0a")
                window.update()
                message = list(istif_alani[-1].values())[0]
                istif_alani_label.config(text=istif_alani_label.cget("text") + " " + str(message))
                window.update()
                time.sleep(1)
                if tir.yük_bilgisi["yük_miktari"] == 20:
                    tir.yük_bilgisi["ton_adet_20"] = 0
                else:
                    tir.yük_bilgisi["ton_adet_30"] = 0
                tir.yük_bilgisi["yük_miktari"] = 0
                tir.yük_bilgisi["maliyet"] = 0
        for gemi in gemiler:
            if gemi.gelis_zamani == zaman:
                limandaki_gemiler.append(gemi)
                message = "Gemi limana geldi."
                simülasyon_label.config(text=message, fg="#351d63") 
                window.update()
                time.sleep(1)
                message = f"Zaman: {zaman}\nGemi adi: {gemi.gemi_adi}\nGeliş zamani: {gemi.gelis_zamani}\nKapasite: {gemi.kapasite}\nÜlke: {gemi.yük_bilgisi['ülke']}\n20 Ton Adet:{gemi.yük_bilgisi['ton_adet_20']}\n30 Ton Adet: {gemi.yük_bilgisi['ton_adet_30']}\nYük Miktari: {gemi.yük_bilgisi['yük_miktari']}\nMaliyet: {gemi.yük_bilgisi['maliyet']}"
                simülasyon_label.config(text=message, fg="#351d63")
                window.update()
                time.sleep(1)
        for gemi in limandaki_gemiler:
            for yükler in istif_alani:
                if list(yükler.keys())[0] == gemi.yük_bilgisi["ülke"]:
                    if gemi.yük_bilgisi["yük_miktari"] + list(yükler.values())[0] <= gemi.kapasite:
                        gemi.yük_bilgisi["yük_miktari"] += list(yükler.values())[0]
                        if list(yükler.values())[0] == 20:
                            gemi.yük_bilgisi["ton_adet_20"] += 1
                            gemi.yük_bilgisi["maliyet"] += 20000
                        else:
                            gemi.yük_bilgisi["ton_adet_30"] += 1
                            gemi.yük_bilgisi["maliyet"] += 30000
                        message = "Yük gemiye yüklendi."
                        simülasyon_label.config(text=message, fg="#003480")
                        window.update()
                        time.sleep(1)
                        message = f"Zaman: {zaman}\nGemi adi: {gemi.gemi_adi}\nGeliş zamani: {gemi.gelis_zamani}\nKapasite: {gemi.kapasite}\nÜlke: {gemi.yük_bilgisi['ülke']}\n20 Ton Adet: {gemi.yük_bilgisi['ton_adet_20']}\n30 Ton Adet: {gemi.yük_bilgisi['ton_adet_30']}\nYük Miktari: {gemi.yük_bilgisi['yük_miktari']}\nMaliyet: {gemi.yük_bilgisi['maliyet']}"
                        simülasyon_label.config(text=message, fg="#351d63")
                        window.update()
                        time.sleep(1)
                        istif_alani.remove(yükler)
                        message = ""
                        for i in istif_alani:
                            message += str(list(i.values())[0])
                            message += " "
                        istif_alani_label.config(text=message)
                        if gemi.yük_bilgisi["yük_miktari"] >= gemi.kapasite*(95/100):
                            message = "Gemi limandan ayrildi."
                            simülasyon_label.config(text=message, fg="#0a5c0a")
                            window.update()
                            time.sleep(1)
                            limandaki_gemiler.remove(gemi)
        if len(istif_alani) == 0:
            istif_alani_label.config(text="istif alanı boş")
            window.update()
            time.sleep(1)
            istif_alani_label.config(text="")
            window.update()


# Tkinter arayüzü
window = tk.Tk()
window.title("Liman Otomasyonu")
window.config(bg="#949494")

frame = tk.Frame(window, height=100, width=500, bg="black")
frame.pack()

simülasyon_label_baslik = tk.Label(frame, text="Simülasyon", width=100, bg="#949494", anchor="ne")
simülasyon_label_baslik.grid(row=0, column=0)

simülasyon_label = tk.Label(frame, text="", height=20, width=100, bg="#d3d3d3", fg="black")
simülasyon_label.grid(row=1, column=0, padx=10, pady=10)

tir_label_baslik = tk.Label(frame, text="TIR Bilgileri", width=100, bg="#949494", anchor="ne")
tir_label_baslik.grid(row=2, column=0)

tir_label = tk.Label(frame, text="", height=20, width=100, bg="#d3d3d3", fg="black")
tir_label.grid(row=3, column=0, padx=10, pady=10)

gemi_label_baslik = tk.Label(frame, text="Gemi Bilgileri", width=100, bg="#949494", anchor="ne")
gemi_label_baslik.grid(row=2, column=1)

gemi_label = tk.Label(frame, text="", height=20, width=100, bg="#d3d3d3", fg="black")
gemi_label.grid(row=3, column=1, padx=10, pady=10)

istif_alani_label_baslik = tk.Label(frame, text="İstif Alanı", width=100, bg="#949494", anchor="ne")
istif_alani_label_baslik.grid(row=0, column=1)

istif_alani_label = tk.Label(frame, text="", height=20, width=100, bg="#d3d3d3", fg="black")
istif_alani_label.grid(row=1, column=1, padx=10, pady=10)

sayi_label = tk.Label(window, text="Simülasyonu kaçıncı zamana kadar çalıştırmak istediğinizi giriniz:", font="Bold", bg="#949494")
sayi_label.pack()
sayi_entry = tk.Entry(window, bg="black", fg="white", width=30)
sayi_entry.pack()
button1 = tk.Button(window, text="Simülasyonu Başlat", command=liman_simülasyonu, width=25, bg="black", fg="green", activebackground="black", activeforeground="green")
button1.pack()

button2 = tk.Button(window, text="Çıkış", command=quit, width=25, bg="black", fg="red", activebackground="black", activeforeground="red")
button2.pack()

plaka_entry_label = tk.Label(window, text="TIR Plakası:", font="bold", fg="black", bg="#949494")
plaka_entry_label.pack(side=tk.LEFT)
plaka_entry = tk.Entry(window, bg="black", fg="#d3d3d3")
plaka_entry.pack(side=tk.LEFT)
button3 = tk.Button(window, text= "TIR Bilgilerini Göster", fg= "#d3d3d3", bg="black", activeforeground="#E6A8D9", activebackground="black", command=tir_bilgileri)
button3.pack(side=tk.LEFT)

button4 = tk.Button(window, text="Gemi Bilgilerini Göster", fg="#d3d3d3", bg="black", activeforeground="#7FDBFA", activebackground="black", command=gemi_bilgileri)
button4.pack(side=tk.RIGHT)
gemi_adi_entry = tk.Entry(window, bg="black", fg="#d3d3d3")
gemi_adi_entry.pack(side=tk.RIGHT)
gemi_adi_entry_label = tk.Label(window, text="Gemi Adı:", font="bold", fg="black", bg="#949494")
gemi_adi_entry_label.pack(side=tk.RIGHT)

window.mainloop()
