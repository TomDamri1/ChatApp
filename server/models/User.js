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
    type: String
  },
  CPU:{
    type:String
  },
  password: {
    type: String,
    required: true
  },
  externalIP:{
    type:String
  },
  internalIP:{
    type:String
  },
  friends: [String]

});

module.exports = Post = mongoose.model('user', UserSchema);
