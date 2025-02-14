
function handle_error(err) {
	console.error(err)
}

const guarulhos_pos = [-23.454163, -46.534096];

var map = L.map("map").setView(guarulhos_pos, 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

class Point {
    constructor({ id = null, latitude, longitude, created_on }) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.created_on = created_on;
    }

    print() {
        return `id ${this.id}\nlat ${this.latitude}\nlong ${
            this.longitude
        }\ncreated ${this.created_on.toString()}`;
    }
}

class Way {
    constructor({ uid = null, points = [] }) {
        this.uid = uid;
        this.points = points.map((point) => new Point(point));
        this.lines = null;

        this.process = null;
        this.time = 10000;
    }

    get isFake() {
        return this.uid != null;
    }

    start() {
        this.process = requestAnimationFrame(() => this._loop());
    }

    _loop() {
        navigator.geolocation.getCurrentPosition(
            (pos) => this.add_point(pos),
            handle_error,
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0,
            }
        );

        setTimeout(() => {
            this.process = requestAnimationFrame(() => this._loop());
        }, this.time);
    }

    stop() {
        if (this.process) {
            cancelAnimationFrame(this.process);
            this.save()
			.catch(handle_error)
        } else {
            throw new Error("No Process to Cancel");
        }
    }

    add_point(pos) {
        const { latitude, longitude } = pos.coords;
        const created_on = new Date();
        const new_point = new Point({ latitude, longitude, created_on });
        console.log(new_point.print());
        this.points = [...this.points, new_point];
        this.draw();
    }

    draw() {
        const pathCoords = this.points.map(({ latitude, longitude }) => [
            latitude,
            longitude,
        ]);

        this.lines = new L.polyline(pathCoords).addTo(map);
    }

    async save() {
        const body = {
            points: this.points,
        };

        const res = await fetch("/way", {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
        });

		await res.json()
    }

    static async loadAll() {
        const req = await fetch("/way");
        const data = await req.json();
        return data.map((way) => new Way(way));
    }
}

navigator.geolocation.getCurrentPosition(
    (pos) => {
        const { latitude, longitude } = pos.coords;
        map.setView([latitude, longitude], 13);
        L.marker([latitude, longitude]).addTo(map);
    },
    handle_error,
    {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
    }
);

const button_new_way = document.getElementById("button-new-way");
let current_way = null;

button_new_way.addEventListener("click", () => {
    if (!current_way) {
        current_way = new Way({});
        current_way.start();
        button_new_way.textContent = "STOP";
    } else {
        current_way.stop();
        current_way = null;
        button_new_way.textContent = "START";
    }
});

Way.loadAll()
    .then((ways) => {
        ways.forEach((way) => way.draw(map));
    })
    .catch(handle_error);
