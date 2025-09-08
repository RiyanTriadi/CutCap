import tkinter as tk
from tkinter import messagebox
import os
import shutil

# function untuk mengambil video
def takeVideo():
    project_name = entry_project.get().strip()

    if not project_name:
        messagebox.showwarning("Input Kosong", "Nama project tidak boleh kosong!")
        return
    
    user_profile_path = os.path.expanduser('~')
    
    # path video yang diambil
    source_dir = os.path.join(
        user_profile_path,
        'AppData', 'Local', 'CapCut', 'User Data', 'Projects',
        'com.lveditor.draft', project_name, 'Resources', 'combination'
    )

    # path tujuan menyimpan video
    dest_dir = os.path.join(user_profile_path, 'Videos')

    # pencarian dan pemindahan
    try:
        # cek folder ada atau tidak
        if not os.path.isdir(source_dir):
            messagebox.showerror("Error", f"Folder project '{project_name}' tidak ditemukan!\n\nPastikan nama project sudah benar dan sesuai dengan yang ada di CapCut.")
            return

        # cari file video (.mp4) di dalam folder
        video_file_name = None
        for file in os.listdir(source_dir):
            if file.lower().endswith('.mp4'):
                video_file_name = file
                break 

        if not video_file_name:
            messagebox.showerror("Error", "Tidak ada file video (.mp4) yang ditemukan di dalam folder project.")
            return
            
        # buat folder tujuan jika belum ada
        os.makedirs(dest_dir, exist_ok=True)

        # path sumber dan tujuan
        source_file_path = os.path.join(source_dir, video_file_name)
        destination_file_path = os.path.join(dest_dir, f"{project_name}.mp4")

        # copy, pindahkan, dan rename file
        shutil.copy(source_file_path, destination_file_path) 

        messagebox.showinfo("Sukses!", f"Video berhasil diambil dan disimpan sebagai:\n\n{destination_file_path}")

    except Exception as e:
        messagebox.showerror("Terjadi Kesalahan", f"Sebuah error terjadi: {e}")


# GUI (Tampilan)
# main window
root = tk.Tk()
root.title("Take Capcut Vid App")
root.geometry("400x150") # Mengatur ukuran jendela
root.resizable(False, False) # Agar ukuran jendela tidak bisa diubah

# frame
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# label
label_instruksi = tk.Label(main_frame, text="Masukkan Nama Project CapCut:")
label_instruksi.pack()

# textbox
entry_project = tk.Entry(main_frame, width=50)
entry_project.pack(pady=5)

# button save
button_ambil = tk.Button(main_frame, text="Simpan", command=takeVideo)
button_ambil.pack(pady=10)

# run app
root.mainloop()