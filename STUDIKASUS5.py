def hitung_biaya_hotel(jenis, durasi):
    if jenis == "Standard":
        tarif = 200000
    elif jenis == "Deluxe":
        tarif = 350000

    total_biaya_hotel = tarif * durasi
    return total_biaya_hotel

jenis = input("Pilih jenis kamar yang anda inginkan (Standard/Deluxe) : ")

tanggal_checkin = int(input("Tanggal anda check in : "))
bulan_checkin = int(input("Bulan anda check in (angka) : "))
tahun_checkin = int(input("Tahun anda check in : "))

tanggal_checkout = int(input("Tanggal anda check out : "))
bulan_checkout = int(input("Bulan anda check out (angka) : "))
tahun_checkout = int(input("Tahun anda check out : "))

if bulan_checkin == bulan_checkout:
    durasi = tanggal_checkout - tanggal_checkin
else:
    if bulan_checkin == 2:
        hari = 28
    elif bulan_checkin == 4 or bulan_checkin == 6 or bulan_checkin == 9 or bulan_checkin == 11:
        hari = 30
    else:
        hari = 31

    durasi = (hari - tanggal_checkin) + tanggal_checkout

total = hitung_biaya_hotel(jenis, durasi)

print("Jenis kamar :", jenis)
print("Check-in :", tanggal_checkin, "-", bulan_checkin, "-", tahun_checkin)
print("Check-out :", tanggal_checkout, "-", bulan_checkout, "-", tahun_checkout)
print("Durasi :", durasi, "malam")
print("Total biaya : Rp", total)