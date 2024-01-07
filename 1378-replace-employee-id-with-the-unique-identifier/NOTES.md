![SQL Joins](https://learnsql.com/blog/learn-and-practice-sql-joins/2.png)
​
Menggunakan implementasi operasi LEFT JOIN.
​
* Tabel di sebelah kiri dari LEFT JOIN adalah tabel yang disebutkan sebelum kata kunci LEFT JOIN, yaitu tabel Employees. Tabel di sebelah kanan adalah EmployeeUNI. Operasi ini menggabungkan data dari kedua tabel berdasarkan kondisi bahwa nilai id di tabel Employees harus sama dengan nilai id di tabel EmployeeUNI.
​
* Jadi, dalam konteks query ini, tabel di sebelah kiri adalah Employees, dan tabel di sebelah kanan adalah EmployeeUNI.
​
* Hasilnya adalah kita mendapatkan daftar semua karyawan dari tabel Employees dan unik_id (jika ada) dari tabel EmployeeUNI. Jika tidak ada unik_id yang sesuai, nilai unique_id akan ditampilkan sebagai NULL.
​
​
​
​