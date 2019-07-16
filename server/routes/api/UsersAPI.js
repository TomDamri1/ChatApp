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
    try{
      const user=await User.findOne({
          ID: req.params.id,
      })
      user.friends.push(req.body.friend)
      user.save();
  }  
  catch(err){
      console.log(err);
  }
  });


router.post('/register', async (req, res) => {
  const user=await User.findOne({
      ID:req.body.id
  })
  if(user){
      res.json({"error":"ID allready exist"})
  }
  else{
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
     .then(()=>res.json({"success":"Registered succsessfully"}))
     .catch(err=>console.log(err))
  }  
 
});
router.post('/login',async(req,res)=>{
  try{
    const user=await User.findOne({
        ID:req.body.id
    })
    if(!user){
        res.json({"Login":"No login found"})
    }
    else if(user.password===req.body.password){
        res.json({"Login":"Logged in successfully "})
    }
    else{
        res.json({"Login":"Login Failed Wrong password"})
    }   
  }
  catch(err){
      console.log(err);
  }

})


module.exports = router;
