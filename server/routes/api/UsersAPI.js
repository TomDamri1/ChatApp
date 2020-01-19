const express = require("express");
const router = express.Router();
const User = require("../../models/User");
const bcrypt = require("bcryptjs");

router.get("/:id", async (req, res) => {
  console.log("getting req");
  try {
    const user = await User.findOne({
      ID: req.params.id
    });
    res.json(user);
  } catch (err) {
    console.log("the error is", err);
  }
});

router.post("/addfriend/:id", async (req, res) => {
  try {
    const user = await User.findOne({
      ID: req.params.id
    });
    const testuser = await User.findOne({
      ID: req.body.friend
    });
    if (testuser) {
      user.friends.push(req.body.friend);
      user.save();
      res.json({ Success: "Friend added successfully" });
    } else {
      res.json({ Failed: true });
    }
  } catch (err) {
    console.log("the error is", err);
  }
});

router.delete("/removefriend/:id", async (req, res) => {
  try {
    const user = await User.findOne({
      ID: req.params.id
    });
    const newfriends = user.friends.filter(friend => {
      return friend !== req.body.friend;
    });
    user.friends = newfriends;
    user.save();
    res.json({ Success: "Friend removed successfully" });
  } catch (err) {loginURL = URL + "api/users/login"

    console.log("the error is", err);
  }
});

router.post("/register", async (req, res) => {
  console.log("enter register");
  const user = await User.findOne({
    ID: req.body.id
  });
  if (user) {
    res.json({ error: "ID allready exist" });
  } else {
    const salt = await bcrypt.genSalt(10);
    let password = await bcrypt.hash(req.body.password, salt);
    const newUser = new User({
      name: req.body.name,
      lastname: req.body.lastname,
      ID: req.body.id,
      motherboard: req.body.motherboard,
      cpu: req.body.cpu,
      password,
      friends: [],
      isLogged: false
    });
    newUser
      .save()
      .then(() => res.json({ success: "Registered succsessfully" }))
      .catch(err => console.log("the error is", err));
  }
});
router.post("/login", async (req, res) => {
  console.log("loging in");
  try {
    let isMatch;
    const user = await User.findOne({
      ID: req.body.id
    });
    console.log(user);
    if (user) {
      isMatch = await bcrypt.compare(req.body.user, user.password);
    }
    console.log(isMatch)
    if (!user) {
      res.json({ Login: "No login found" });
    } else if (isMatch) {
      user.isLogged = true;
      user.save().then(() => res.json({ Login: "Logged in successfully " }));
    } else {
      res.json({ Login: "Login Failed Wrong password" });
    }
  } catch (err) {
    console.log("the error is", err);
  }
});

router.post("/logout/:id", async (req, res) => {
  console.log("logged out route");
  try {
    const user = await User.findOne({
      ID: req.params.id
    });
    user.isLogged = false;
    user.save().then(() => res.json({ Login: "Logged out successfully " }));
  } catch (err) {
    console.log("the error is", err);
  }
});

router.post("/update/:id", async (req, res) => {
  try {
    const user = await User.findOne({
      ID: req.params.id
    });
    if (!user) {
      res.json({ Login: "No login found" });
    } else {
      user.externalIP = req.body.externalIP;
      user.internalIP = req.body.internalIP;
      user.CPU = req.body.CPU;
      user.motherboard = req.body.motherboard;
      user.save();
      res.json({ Success: "Updated successfully" });
    }
  } catch (err) {
    console.log("the error is", err);
  }
});

module.exports = router;
