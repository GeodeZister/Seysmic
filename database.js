const express = require('express');
const mysql = require('mysql');
const cors = require('cors');
const bcrypt = require('bcryptjs');

const app = express();
app.use(cors());
app.use(express.json());

// Налаштування підключення до бази даних
const connection = mysql.createConnection({
  host: '127.0.0.1', // або IP-адреса вашого сервера MySQL
  user: 'root', // ваш MySQL користувач
  password: 'admin1', // ваш пароль
  database: 'Seysmo' // назва вашої бази даних
});

connection.connect(err => {
  if (err) {
    console.error('Помилка при підключенні до бази даних: ' + err.stack);
    return;
  }

  console.log('Підключено до бази даних MySQL з ID ' + connection.threadId);
});

// Route to fetch seismic data
app.get('/api/events', (req, res) => {
    let station = req.query.station || 'NDNU'; // Default to 'NDNU' if no station is specified
    const query = "SELECT time, mag, type, seismogram1, description1, depth, seismogram2, description2, place FROM geoevents WHERE place = ?";
    connection.query(query, [station], (err, results) => {
        if (err) {
            res.status(500).send('Server error: ' + err.message);
        } else {
            res.json(results);
        }
    });
});


// Запуск сервера
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Сервер запущено на порту ${PORT}`);
});
