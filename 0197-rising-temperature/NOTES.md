1. `SELECT w1.id`: Memilih kolom ID dari tabel Weather dengan alias w1.
​
2. `FROM Weather w1, Weather w2`: Menggunakan tabel Weather dengan alias w1 dan w2, yang menggambarkan self-join (penggabungan dengan dirinya sendiri) untuk membandingkan data cuaca pada dua tanggal berbeda.
​
3. `WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1`: Menerapkan kondisi bahwa perbedaan tanggal antara w1.recordDate dan w2.recordDate harus sama dengan 1 hari. Artinya, kita membandingkan data cuaca pada tanggal sekarang (w1) dengan data cuaca pada tanggal sebelumnya (w2).
​
4. `AND w1.temperature > w2.temperature`: Menambahkan kondisi tambahan bahwa suhu pada tanggal sekarang (w1) harus lebih tinggi daripada suhu pada tanggal sebelumnya (w2).