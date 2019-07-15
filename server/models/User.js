const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const UserSchema = new Schema({
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
    
  }]

});

module.exports = Post = mongoose.model('user', UserSchema);
