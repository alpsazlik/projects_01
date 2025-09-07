from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

    # 📂 web_site/web.py
    # Bu dosyada sadece Flask (Python) kodları olacak

    from flask import Flask, render_template

    app = Flask(__name__)


    @app.route("/")
    def home():
        return render_template("index.html")  # Ana sayfayı açar


    @app.route("/menu")
    def menu():
        return render_template("menu.html")  # Menü sayfasını açar


    @app.route("/contact")
    def contact():
        return render_template("contact.html")  # İletişim sayfasını açar


    if __name__ == "__main__":
        app.run(debug=True)

