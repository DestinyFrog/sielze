class Point {
    constructor({ id = null, latitude, longitude }) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    static create_ghost_point(way, latitude, longitude) {

    }

    async save() {
        // const res = await fetch(`/way/<uuid:uid>/add_point`)
    }
}

class Way {
    constructor({ uid, points }) {
        this.uid = uid;
        this.points = points.map((point) => new Point(point));

        this.process = null;
        this.timer = 30000;
    }

    start() {
        this.process = requestAnimationFrame();
    }

    _loop() {
        navigator.geolocation.getCurrentPosition(
            (pos) => {
                const { latitude, longitude } = pos.coords;
                
            },
            (err) => {
                console.error(err);
            },
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0,
            }
        );

        setTimeout(() => {
            this.process = requestAnimationFrame(() => this._loop());
        });
    }

    stop() {
        if (this.process) {
            cancelAnimationFrame(this.process);
            this._save();
        } else {
            throw new Error("No Process to Cancel");
        }
    }

    _save() {}

    draw(map) {
        const pathCoords = this.points.map(({ latitude, longitude }) => [
            latitude,
            longitude,
        ]);
        return (pathLine = L.polyline(pathCoords).addTo(map));
    }

    static async loadAll() {
        const req = await fetch("/way");
        const data = await req.json();
        return data.map((way) => new Way(way));
    }
}

export default Way;
