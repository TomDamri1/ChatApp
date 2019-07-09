const express = require('express');
const router = express.Router();
const Chat=require('../../models/Chat');

router.get('/:id/:otherid', async (req, res) => {
  console.log("getting req");
  try {
    const chat1 = await Chat.findOne({
      otherID: req.params.otherid,
      ID: req.params.id
    });
    const chat2 = await Chat.findOne({
      otherID: req.params.id,
      ID: req.params.otherid
    });
    if (chat1) {
      res.json(chat1);
    } else if (chat2) {
      res.json(chat2);
    } else {
      res.json(null);
    }
  } catch (err) {
    console.log(err);
  }
});
router.post('/', async (req, res) => {
  console.log(req.body);
  const chat1 = await Chat.findOne({
    otherID: req.body.otherID,
    ID: req.body.ID
  });
  const chat2 = await Chat.findOne({
    otherID: req.body.ID,
    ID: req.body.otherID
  });
  if (chat1) {
    chat1.chat = [...req.body.chat];
    chat1.save();
  } else if (chat2) {
    chat2.chat = [...req.body.chat];
    chat2.save();
  } else {
    const newChat = new Chat({
      ID: req.body.ID,
      otherID: req.body.otherID,
      chat: req.body.chat
    });
    newChat
      .save()
      .then(post => res.json(post))
      .catch(err => console.log(err));
  }
  console.log("responding");
  res.status(200).json({post:"success"});  
});
router.delete('/:id', (req, res) => {
  Profile.findOne({ user: req.user.id }).then(profile => {
    Post.findById(req.params.id)
      .then(post => {
        if (post.user.toString() !== req.user.id) {
          return res.status(401).json({ notauthorized: 'User not authorized' });
        }

        post.remove().then(() => res.json({ success: true }));
      })
      .catch(err => res.status(404).json({ postnotfound: 'No post found' }));
  });
});

module.exports = router;
