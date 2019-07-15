const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const Userchema = new Schema({
  ID: {
    type: String,
    required: true
  },
  name: {
    type: String,
    required: true
  },
  lastname:{  
      type: String,
    required: true
},

motherboard: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  },
  friends: [{
    type: String,
    required: true
  },]

});

module.exports = Post = mongoose.model('chat', ChatSchema);
