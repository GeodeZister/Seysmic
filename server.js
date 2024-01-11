const express = require('express');
const path = require('path'); // Додаємо цей рядок
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));





// Використовуйте абсолютний шлях до вашої папки з проектом
app.use(express.static(path.join(__dirname, 'C://Users/Oleksandr/PycharmProjects/Seysmic')));

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
