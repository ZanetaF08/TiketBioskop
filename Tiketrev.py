from os import system
from datetime import datetime
import datetime as dt 

def current_date():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	cur_date = str("%4d-%02d-%02d" % (year, month, hari))
	return cur_date

jlh_pemesanan = 0
pemesanan = {}
studio = {
	1:{
		"jenis": "Regular",
		"harga": 50000,
		"jam" : ["10:15","12:30","14:40","17:20","19:55","22:00"],
		"kursi": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
			16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
		"reserved": [[],[],[],[],[],[]]
	},
	2:{
		"jenis": "VIP",
		"harga": 75000,
		"jam" : ["10:00","12:35","15:00","17:10","19:40","21:50"],
		"kursi": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
		"reserved": [[],[],[],[],[],[]]
	},
	3:{
		"jenis": "VVIP",
		"harga": 120000,
		"jam" : ["10:15","12:45","15:15","17:20","19:55","22:00"],
		"kursi": [1,2,3,4,5,6,7,8],
		"reserved": [[],[],[],[],[],[]]
	},
	4:{
		"jenis": "Regular",
		"harga": 50000,
		"jam" : ["09:40","11:55","14:30","16:50","19:10","21:30"],
		"kursi": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
			16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
		"reserved": [[],[],[],[],[],[]]
	},
	5:{
		"jenis": "VIP",
		"harga": 75000,
		"jam" : ["10:15","13:00","15:15","17:20","19:55","22:00"],
		"kursi": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
		"reserved": [[],[],[],[],[],[]]
	}
}
film = {
	"2020-10-20-F001":{
		"judul" : "Peninsula",
		"tanggal" : current_date(),
		"studio" : [1]
	},
	current_date()+"-F002":{
		"judul" : "Bloodshot",
		"tanggal" : current_date(),
		"studio" : [4,5]
	},
	current_date()+"-F003":{
		"judul" : "My Hero Academia: Heroes Rising",
		"tanggal" : current_date(),
		"studio" : [2]
	},
	current_date()+"-F004":{
		"judul" : "Mulan",
		"tanggal" : current_date(),
		"studio" : [3]
	}
}

def print_film(id_film, print_jadwal = False, jam_tayang = [], studio_par = []):
	print('ID Film: '+id_film)
	print('Judul: '+film[id_film]["judul"])
	#if(print jadwal)
	print("\nSTUDIO")
	print("=========================")
	j_iterasi = len(jam_tayang)
	if len(jam_tayang) == 0:
		j_iterasi = len(film[id_film]["studio"])
	for ind in range(j_iterasi):
		id_studio = film[id_film]["studio"][ind]
		if len(jam_tayang) > 0:
			id_studio = studio_par[ind]
		print('Nomor: '+str(id_studio))
		print('Harga: '+str(studio[id_studio]["harga"]))

		if len(jam_tayang) > 0:
			print('Jam Tayang: '+str(jam_tayang[ind]))
		else:
			print('Jam Tayang: '+str(studio[id_studio]["jam"]))
		print("=========================")

	print()
	#jlh_kursi = len(studio[film[id_film]["studio"]]["kursi"]) - len(film[id_film]["reserved"])fr
	#print('Jumlah Kursi Tersedia: '+str(jlh_kursi)+'\n')

def time_in_range(start, end, n):
	if start <= end:
		return start <= n <= end
	else:
		return start <= n or n <= end

def read_film(all = False):
	system("cls")
	print("DAFTAR FILM\n")
	if not all:
		for id_film in film:
			current = datetime.now()
			c_h = current.hour
			c_m = current.minute
			c_s = current.second
			current_time = dt.time(c_h, c_m, c_s)
			now_tayang = []
			studio_par = []
			for id_studio in film[id_film]["studio"]:
				for jam_tayang in studio[id_studio]["jam"]:
					jam,menit = jam_tayang.split(":")
					t_jam = int(jam)
					start = dt.time(t_jam, int(menit), 0)
					t_jam += 2
					while t_jam > 23:
						t_jam -= 24
					end = dt.time(t_jam+2, int(menit), 0)
					if time_in_range(start, end, current_time):
						now_tayang.append(jam_tayang)
						studio_par.append(id_studio)
						break
			if(len(now_tayang) > 0):
				print_film(id_film, True, now_tayang, studio_par)
	else:
		for id_film in film:
			print_film(id_film)

def check_studio_film(id_studio):
	for id_film in film:
		for studio in film[id_film]["studio"]:
			if studio == id_studio:
				return id_film
	return 0

def read_studio():
	system("cls")
	print("DAFTAR STUDIO\n")
	for id_studio in studio:
		id_film = check_studio_film(id_studio)
		if id_film != 0:
			print("Nomor Studio: Studio "+str(id_studio))
			print("Film: "+film[id_film]["judul"])
			print("Jenis: "+studio[id_studio]["jenis"])
			print("Harga: "+str(studio[id_studio]["harga"])+"\n")

def read_film_n_studio():
	system("cls")
	for id_film_ind in film:
		print_film(id_film_ind, True, [], [])

def input_kursi(iter, pil_studio, indeks_jam, p_k):
	pil_kursi = p_k
	valid = False
	while not valid:
		t_pil_kursi = int(input("Nomor Kursi Pesanan ke-"+str(iter+1)+": "))
		if ((t_pil_kursi not in pil_kursi and t_pil_kursi not
			in studio[pil_studio]["reserved"][indeks_jam]) and
				t_pil_kursi in studio[pil_studio]["kursi"]):
					valid = True
					pil_kursi.append(t_pil_kursi)
		if not valid:
			print("Kursi sudah dipesan atau tidak terdaftar!")
	return pil_kursi

def create_reservation():
	isExists = False
	while not isExists:
		read_film_n_studio()
		print("Buat Pesanan Baru\n")
		pil_film = input("Masukan Pilihan ID Film (0 untuk Kembali): ")
		if pil_film == "0":
 			break
		pil_studio = int(input("Masukan Nomor Pilihan Studio: "))
		pil_jam = input("Masukan Pilihan Jam Tayang: ")
		if pil_film in film and pil_studio in studio and pil_jam in studio[pil_studio]["jam"]:
			indeks_jam = studio[pil_studio]["jam"].index(pil_jam)
			pil_kursi = []
			jlh_kursi = int(input("Masukan Jumlah Kursi: "))
			for iter in range(jlh_kursi):
 				pil_kursi = input_kursi(iter, pil_studio, indeks_jam, pil_kursi)
			total_harga = jlh_kursi * studio[pil_studio]["harga"]
			print('Total Harga: '+str(total_harga))
			jenis_bayar = input('Masukan Jenis Pembayaran: ')

			studio[pil_studio]["reserved"][indeks_jam] += pil_kursi
			global jlh_pemesanan
			num_of_res = jlh_pemesanan + 1
			jlh_pemesanan += 1
			id_res = current_date()+str("-T%03d" % (num_of_res))

			print("\nMasukan Data Diri Pemesan")
			nama = input("Nama: ")
			jen_kel = input("Jenis Kelamin: ")
			no_hp = input("No. Handphone: ")
			alamat = input("Alamat: ")
			email = input("Email: ")
			pemesanan[id_res] = {
				"nama": nama,
				"jen_kel": jen_kel,
				"no_hp": no_hp,
				"alamat": alamat,
				"email": email,
				"id_film": pil_film,
				"id_studio": pil_studio,
				"indeks_jam": indeks_jam,
				"tanggal": current_date(),
				"jumlah": jlh_kursi,
				"total_harga": total_harga,
				"jenis_bayar": jenis_bayar,
				"reserved": pil_kursi
			}
			print("\nPesanan Berhasil Ditambahkan!\n")
			reserve = True
			break

def read_reservation():
	system('cls')
	print("DAFTAR PESANAN")
	for id_res in pemesanan:
		print("ID Pemesanan: "+id_res)
		print("Film: "+film[pemesanan[id_res]["id_film"]]["judul"])
		id_stud = pemesanan[id_res]["id_studio"]
		print("Nomor Studio: "+str(id_stud))
		print("Tanggal: "+pemesanan[id_res]["tanggal"])
		print("Jam Tayang: "+studio[id_stud]["jam"][pemesanan[id_res]["indeks_jam"]])
		print("Jumlah Kursi: "+str(pemesanan[id_res]["jumlah"]))
		print("Kursi Yang Dipesan: "+str(pemesanan[id_res]["reserved"]))
		print("Total Harga: "+str(pemesanan[id_res]["total_harga"]))
		print("Jenis Pembayaran: "+str(pemesanan[id_res]["jenis_bayar"])+"\n")

		print("Data Pemesan")
		print("Nama: "+pemesanan[id_res]["nama"])
		print("Jenis Kelamin: "+pemesanan[id_res]["jen_kel"])
		print("No. Handphone: "+pemesanan[id_res]["no_hp"])
		print("Email: "+pemesanan[id_res]["email"])
		print("Alamat: "+pemesanan[id_res]["alamat"]+"\n")

def update_film():
	valid = False
	up_opt = int(input("Pilih ingin Update Apa? (1 = Pesanan, 2 = Film, 0 = Kembali) : "))
	while not valid and (up_opt == 1 or up_opt == 2):
		isJtExists = False
		if up_opt == 1:
			read_reservation()
			print("Update Jadwal Pesanan Yang Ada\n")
			pil_res = input('Masukan ID Pesanan Yang Di-Update Jadwalnya: ')
			if pil_res in pemesanan:
				res_studio = pemesanan[pil_res]["id_studio"]
				jty_studio = studio[res_studio]["jam"]
				print('\nJadwal Film Yang Tersedia: '+str(jty_studio)+'\n')
				while not isJtExists:
					jam_new = input('Masukan Jam Tayang Terbaru: ')
					if jam_new in jty_studio:
						isJtExists = False
						break
				pil_kursi = []
				indeks_jt_old = pemesanan[pil_res]["indeks_jam"]
				indeks_jt = studio[res_studio]["jam"].index(jam_new)

				print("\nMasukan ulang Nomor Kursi yang ingin Dipesan:")
				for iter in range(pemesanan[pil_res]["jumlah"]):
					pil_kursi = input_kursi(iter, res_studio, indeks_jt, pil_kursi)

				l_dif = list(set(studio[res_studio]["reserved"][indeks_jt_old]) -
					set(pemesanan[pil_res]["reserved"]))
				studio[res_studio]["reserved"][indeks_jt_old] = l_dif

				pemesanan[pil_res]["indeks_jam"] = indeks_jt
				pemesanan[pil_res]["reserved"] = pil_kursi
				studio[res_studio]["reserved"][indeks_jt] += pil_kursi

				valid = True
				print("\nJadwal Pesanan Berhasil Di-Update!\n")
				break
		elif up_opt == 2:
			read_film_n_studio()
			print("Update Jadwal Film Yang Ada\n")
			pil_film = input('Masukan ID Film Yang Di-Update Jadwalnya: ')
			pil_studio = int(input('Masukan ID Studio Yang Di-Update Jadwalnya: '))
			if pil_film in film and pil_studio in film[pil_film]["studio"]:
				while not isJtExists:
					jam = input('Pilih Jam Tayang yang Ingin Diupdate: ')
					if jam in studio[pil_studio]["jam"]:
						isJtExists = True
						break
					else:
						print('Jam Tayang tidak Terdaftar!')
				indeks_jt = studio[pil_studio]["jam"].index(jam)
				jam_new = input('Jam Tayang Baru (hh:mm): ')
				studio[pil_studio]["jam"][indeks_jt] = jam_new
				valid = True
				print("\nJadwal Film Berhasil Di-Update!\n")
				break

def delete_ticket():
	valid = False
	while not valid:
		read_reservation()
		print("Cancel Pesanan Yang Ada\n")
		id_res = input("Masukan ID Pesanan Yang Di-Cancel (0 untuk Kembali): ")
		if id_res == "0":
			break
		if id_res in pemesanan:
			id_res_film = pemesanan[id_res]["id_film"]
			id_res_stud = pemesanan[id_res]["id_studio"]
			indeks_jam = pemesanan[id_res]["indeks_jam"]

			l_dif = list(set(studio[id_res_stud]["reserved"][indeks_jam]) -
				set(pemesanan[id_res]["reserved"]))
			studio[id_res_stud]["reserved"][indeks_jam] = l_dif
			del pemesanan[id_res]
			print("\nPesanan Berhasil Di-Cancel!\n")
			valid = True
			break



def go_to_menu(pil):
	if pil == 1:
		read_film()
	elif pil == 2:
		read_studio()
	elif pil == 3:
		read_film(True)
	elif pil == 4:
		create_reservation()
	elif pil == 5:
		read_reservation()
	elif pil == 6:
		update_film()
	elif pil == 7:
		delete_ticket()
	elif pil == 8:
		return True
	else:
		print('Tidak ada Pilihan')
	system("pause")
	return False

def main():
	exit = False
	while not exit:
		system("cls")
		menu = """WELCOME TO CINEMA XXXXXX
[1] - Tampilkan Film Yang Sedang Tayang
[2] - Lihat Jenis Studio Yang Tersedia
[3] - Lihat Jadwal Film
[4] - Buat Pesanan
[5] - Lihat Pesanan
[6] - Pergantian Jadwal Film / Pesanan
[7] - Cancel Ticket
[8] - Keluar
"""
		print(menu)
		pil = int(input('Pilihan: '))
		exit = go_to_menu(pil)

if __name__ == '__main__':
	main()