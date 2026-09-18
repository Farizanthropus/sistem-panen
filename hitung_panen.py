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

def hitung_total_panen(daftar_hasil):
    """Menghitung total hasil panen (kg) dari beberapa data panen."""
    return sum(daftar_hasil)
 

def hitung_diskon(total_kg, harga_per_kg, persen_diskon):
    """Menghitung total harga panen setelah dikurangi diskon (%)."""
    total_harga = total_kg * harga_per_kg
    diskon = total_harga * (persen_diskon / 100)
    return total_harga - diskon
 
 
def main():
    hasil_panen = [120, 85, 200, 150, 95]
    total = hitung_total_panen(hasil_panen)
    harga_per_kg = 5000
    total_setelah_diskon = hitung_diskon(total, harga_per_kg, 10)
 
    print("=== Sistem Pencatatan Hasil Panen Digital ===")
    print(f"Data hasil panen (kg)    : {hasil_panen}")
    print(f"Total hasil panen        : {total} kg")
    print(f"Harga setelah diskon 10% : Rp{total_setelah_diskon:,.0f}")

