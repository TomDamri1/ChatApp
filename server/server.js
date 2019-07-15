const express = require('express');
const connectDB = require('./config/db');
const chat = require('./routes/api/ChatAPI');
const users=require('./routes/api/UsersAPI');
const app = express();
const server = require('http').createServer(app);
global.io = require('socket.io')(server);

//connect Database
connectDB();
app.use(express.json({ extended: false }));
app.get('/', (req, res) => res.send('API RUNNING'));
app.use('/api/chat', chat);
app.use('/api/users',users);
const PORT = process.env.PORT || 5000;

server.listen(PORT, function(){
  console.log('listening on port ' + PORT);
  
  io.on('connection', function (socket) {
    console.log("USER CONNECTED...");
  });
  
});