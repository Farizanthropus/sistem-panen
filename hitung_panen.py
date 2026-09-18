# ==========================================================
# SISTEM PENCATATAN HASIL PANEN DIGITAL
# Program Penghitung Total Hasil Panen
# ==========================================================
 
def hitung_total_panen(daftar_hasil):
    """Menghitung total hasil panen (kg) dari beberapa data panen."""
    return sum(daftar_hasil)
 
 
def main():
    hasil_panen = [120, 85, 200, 150, 95]
    total = hitung_total_panen(hasil_panen)
 
    print("=== Sistem Pencatatan Hasil Panen Digital ===")
    print(f"Data hasil panen (kg): {hasil_panen}")
    print(f"Total hasil panen     : {total} kg")
 
 
if __name__ == "__main__":
    main()
