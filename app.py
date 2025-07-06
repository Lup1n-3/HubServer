from flask import Flask, render_template, request, redirect, url_for, send_file
import json, os, uuid
import qrcode

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route("/")
def home():
    servers = load_data()
    return render_template("home.html", servers=servers)

@app.route("/server/<id>")
def server_detail(id):
    servers = load_data()
    for s in servers:
        if s["id"] == id:
            return render_template("server.html", server=s)
    return "Servidor no encontrado", 404

@app.route("/add", methods=["GET", "POST"])
def add_server():
    if request.method == "POST":
        data = load_data()
        os.makedirs("static/images", exist_ok=True)
        image = request.files.get("image")
        filename = ""
        if image and image.filename:
            filename = str(uuid.uuid4()) + "_" + image.filename
            image.save(os.path.join("static/images", filename))
        new_server = {
            "id": str(uuid.uuid4()),
            "name": request.form["name"],
            "ip": request.form["ip"],
            "image": filename,
            "services": []
        }
        data.append(new_server)
        save_data(data)
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/server/<id>/add_service", methods=["POST"])
def add_service(id):
    data = load_data()
    icon = request.files.get("icon")
    icon_name = ""
    if icon and icon.filename:
        os.makedirs("static/service_icons", exist_ok=True)
        icon_name = str(uuid.uuid4()) + "_" + icon.filename
        icon.save(os.path.join("static/service_icons", icon_name))

    for s in data:
        if s["id"] == id:
            s["services"].append({
                "sid": str(uuid.uuid4()),
                "name": request.form["name"],
                "address": request.form["address"],
                "icon": icon_name,
                "info": request.form.get("info", "")
            })
            break
    save_data(data)
    return redirect(url_for("server_detail", id=id))

@app.route("/server/<server_id>/delete_service/<sid>")
def delete_service(server_id, sid):
    data = load_data()
    for s in data:
        if s["id"] == server_id:
            s["services"] = [srv for srv in s["services"] if srv["sid"] != sid]
            break
    save_data(data)
    return redirect(url_for("server_detail", id=server_id))

@app.route("/server/<server_id>/edit_service/<sid>", methods=["POST"])
def edit_service(server_id, sid):
    data = load_data()
    for s in data:
        if s["id"] == server_id:
            for srv in s["services"]:
                if srv["sid"] == sid:
                    srv["name"] = request.form["name"]
                    srv["address"] = request.form["address"]
                    srv["info"] = request.form.get("info", "")
                    icon = request.files.get("icon")
                    if icon and icon.filename:
                        icon_name = str(uuid.uuid4()) + "_" + icon.filename
                        icon.save(os.path.join("static/service_icons", icon_name))
                        srv["icon"] = icon_name
                    break
            break
    save_data(data)
    return redirect(url_for("server_detail", id=server_id))

@app.route("/qr/<id>")
def get_qr(id):
    url = request.host_url + "server/" + id
    img = qrcode.make(url)
    path = f"static/images/qr_{id}.png"
    img.save(path)
    return send_file(path, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
