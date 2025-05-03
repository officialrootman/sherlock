from flask import Flask, request, jsonify

app = Flask(__name__)

# JSON'daki siteler
SITES = [
    "https://twitter.com/{}",
    "https://github.com/{}",
    "https://www.instagram.com/{}",
    "https://discord.com/users/{}"
    # Buraya diğer siteleri ekleyebilirsin...
]

@app.route("/get_profiles", methods=["GET"])
def get_profiles():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Lütfen bir kullanıcı adı girin"}), 400

    profiles = [site.format(username) for site in SITES]
    return jsonify({"profiles": profiles})

if __name__ == "__main__":
    app.run(debug=True)
