const mongoose = require ('mongoose');

const JokeSchema = mongoose.Schema({
    setup: String,
    punchline: String,
    
    // For created at and updated at
}, {timestamps:true} )

module.exports = mongoose.model('Joke', JokeSchema)