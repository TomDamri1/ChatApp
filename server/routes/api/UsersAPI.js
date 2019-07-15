const express = require('express');
const router = express.Router();
const User=require('../../models/User');

router.get('/:id', async (req, res) => {
  console.log("getting req");
  try{
    const user=await User.findOne({
        id: req.params.id,


    })

    res.json('user');

}

catch(err){
    console.log(err);
}

});

router.post('/addfriend/:id', async (req, res) => {
    console.log("getting req");
    try{
      const user=await User.findOne({
          id: req.params.id,
  
      })
      user.friends.push(req.body.friend)
  }
  
  catch(err){
      console.log(err);
  }
  });


router.post('/register', async (req, res) => {
  const newUser=new User({
      name: req.body.name,
      lastname: req.body.lastname,
      ID: req.body.id,
      motherboard: req.body.motherboard,
      cpu: req.body.cpu,
      password: req.body.password,
      friends:[]
  })
   newUser.save()
   .then(post=>res.json(post))
   .catch(err=>console.log(err))
});


module.exports = router;
