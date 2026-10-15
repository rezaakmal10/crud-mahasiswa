from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db, init_db

app = Flask(__name__)
app.secret_key = "kunci-rahasia-uts"

init_db()


def validasi(nim, nama, program_studi, angkatan, ipk):
    if not nim or not nama or not program_studi:
        return "NIM, nama, dan program studi wajib diisi."
    if not nim.isdigit():
        return "NIM harus berupa angka."
    if not angkatan.isdigit():
        return "Angkatan harus berupa angka."
    try:
        nilai_ipk = float(ipk.replace(",", "."))
    except ValueError:
        return "IPK harus berupa angka."
    if nilai_ipk < 0.0 or nilai_ipk > 4.0:
        return "IPK harus di antara 0.00 dan 4.00."
    return None


@app.route("/")
def index():
    conn = get_db()
    rows = conn.execute("SELECT * FROM mahasiswa ORDER BY nim").fetchall()
    conn.close()

    tahun_sekarang = datetime.now().year
    mahasiswa = []
    for r in rows:
        m = dict(r)
        m["lama_studi"] = tahun_sekarang - m["angkatan"]
        mahasiswa.append(m)

    return render_template("index.html", mahasiswa=mahasiswa)


@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        nim = request.form.get("nim", "").strip()
        nama = request.form.get("nama", "").strip()
        program_studi = request.form.get("program_studi", "").strip()
        angkatan = request.form.get("angkatan", "").strip()
        ipk = request.form.get("ipk", "").strip()

        error = validasi(nim, nama, program_studi, angkatan, ipk)
        if error:
            flash(error, "error")
            return render_template("form.html", data=request.form)

        conn = get_db()
        sudah_ada = conn.execute(
            "SELECT 1 FROM mahasiswa WHERE nim = ?", (int(nim),)
        ).fetchone()
        if sudah_ada:
            conn.close()
            flash("NIM sudah terdaftar.", "error")
            return render_template("form.html", data=request.form)

        conn.execute(
            "INSERT INTO mahasiswa (nim, nama, program_studi, angkatan, ipk) VALUES (?, ?, ?, ?, ?)",
            (int(nim), nama, program_studi, int(angkatan), float(ipk.replace(",", "."))),
        )
        conn.commit()
        conn.close()
        flash("Mahasiswa berhasil ditambahkan.", "success")
        return redirect(url_for("index"))

    return render_template("form.html", data={})


if __name__ == "__main__":
    app.run(debug=True)