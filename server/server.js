const express = require('express');
const connectDB = require('./config/db');
const chat=require('./routes/api/ChatAPI');
const app = express();

//connect Database
connectDB();
app.use(express.json({ extended: false }));
app.get('/', (req, res) => res.send('API RUNNING'));
app.use('/api/chat', chat);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
