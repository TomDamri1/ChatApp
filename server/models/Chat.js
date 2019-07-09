const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ChatSchema = new Schema({
  ID: {
    type: String,
    required: true
  },
  otherID: {
    type: String,
    required: true
  },
  chat: [
    {
      senderName: {
        type: String
      },
      text: {
        type: String
      }
    }
  ]
});

module.exports = Post = mongoose.model('chat', ChatSchema);
