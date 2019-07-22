const express = require('express');
const router = express.Router();
const User=require('../../models/User');

router.get('/:id', async (req, res) => {
  console.log("getting req");
  try{
     const user=await User.findOne({
         ID: req.params.id,
     })
     res.json(user);
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
      const testuser=await User.findOne({
          ID:req.body.friend
      })
      if(testuser){
        user.friends.push(req.body.friend)
        user.save();
        res.json({"Success":"Friend added successfully"})   
      }
      else{
         res.json({"Failed":true}); 
      }
  }  
  catch(err){
      console.log(err);
  }
  });

router.delete('/removefriend/:id',async(req,res)=>{

    try{
        const user=await User.findOne({
            ID: req.params.id,
        })
        const newfriends=user.friends.filter(friend=>{
           return friend!==req.body.friend
        })
        user.friends=newfriends;
        user.save();
        res.json({"Success":"Friend removed successfully"})
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
        friends:[],
        isLogged:false
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
        user.isLogged=true;
        newUser.save()
       .then(()=>res.json({"Login":"Logged in successfully "}))
    }
    else{
        res.json({"Login":"Login Failed Wrong password"})
    }   
  }
  catch(err){
      console.log(err);
  }

})

router.post("/logout/:id",async(req,res)=>{
    try{
        const user=await User.findOne({
            ID:req.params.id
        })
        user.isLogged=false;
        newUser.save()
       .then(()=>res.json({"Login":"Logged out successfully "}))
    }
    catch(err){
        console.log(err);
    }



})

router.post("/update/:id",async(req,res)=>{
   try{
       const user=await User.findOne({
           ID:req.params.id
       })
       if(!user){
          res.json({"Login":"No login found"})
       }
       else{
        user.externalIP=req.body.externalIP
        user.internalIP=req.body.internalIP
        user.CPU=req.body.CPU
        user.motherboard=req.body.motherboard
        user.save();
        res.json({"Success":"Updated successfully"})
       }
   
   }
   catch(err){
       console.log(err);
   }
   
})


module.exports = router;
