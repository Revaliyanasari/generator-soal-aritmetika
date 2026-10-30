from src.input_data import tampilkan_pesan, minta_jawaban
from src.proses import periksa_jawaban, hitung_nilai
from src.output import buat_soal


def main():
    # Menampilkan judul program
    tampilkan_pesan("===================================")
    tampilkan_pesan("   GENERATOR SOAL ARITMETIKA")
    tampilkan_pesan("===================================")

    # Menampilkan pilihan operasi
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    # Meminta pilihan operasi
    pilihan = input("Masukkan pilihan (1-4): ")

    daftar_operasi = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/"
    }

    # Memvalidasi pilihan operasi
    if pilihan not in daftar_operasi:
        tampilkan_pesan("Pilihan tidak valid.")
        return

    operasi = daftar_operasi[pilihan]

    # Meminta jumlah soal
    try:
        jumlah_soal = int(
            input("Berapa soal yang ingin dikerjakan? ")
        )

        if jumlah_soal <= 0:
            tampilkan_pesan(
                "Jumlah soal harus lebih dari 0."
            )
            return

    except ValueError:
        tampilkan_pesan(
            "Masukkan jumlah soal berupa bilangan bulat."
        )
        return

    # Menyiapkan penghitung jawaban
    jumlah_benar = 0
    jumlah_salah = 0

    # Membuat soal dan memeriksa jawaban
    for nomor in range(1, jumlah_soal + 1):
        soal, jawaban_benar = buat_soal(operasi)

        print(f"\nSoal nomor {nomor}: {soal}")

        jawaban_pengguna = minta_jawaban()

        if periksa_jawaban(
            jawaban_pengguna, jawaban_benar
        ):
            tampilkan_pesan("Benar!")
            jumlah_benar += 1
        else:
            tampilkan_pesan(
                f"Jawaban salah. Jawaban yang benar "
                f"adalah {jawaban_benar}."
            )
            jumlah_salah += 1

    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai(
        jumlah_benar, jumlah_soal
    )

    # Menampilkan hasil latihan
    print("\n========== HASIL LATIHAN ==========")
    print(f"Jumlah soal       : {jumlah_soal}")
    print(f"Jawaban benar     : {jumlah_benar}")
    print(f"Jawaban salah     : {jumlah_salah}")
    print(f"Nilai akhir       : {nilai_akhir:.2f}")
    print("===================================")


if __name__ == "__main__":
    main()