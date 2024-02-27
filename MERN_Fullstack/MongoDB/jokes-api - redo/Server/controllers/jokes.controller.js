const Joke = require('../models/jokes.model')

module.exports = {
    // Read All in CRUD
    findAllJokes: (request, response) => {
        Joke.find()
            .then((allJokes) => {
                response.status(200).json(allJokes)
            })
            .catch((err) => {
                response.status(500).json(err);
            })
    },
    // Read One in CRUD (finding by _id)
    findOneJoke: (request, response) => {
        Joke.findOne({_id: request.params.id})
            .then((oneJoke) =>{
                request.status(200).json(oneJoke)
            })
            .catch((err) => {
                response.status(500).json(err)
            })
    },
    // Create in CRUD
    createJoke: (request, response) => {
        Joke.create(request.body)
        .then((newUser) => {
            response.status(201).json(newUser)
        })
        .catch((err) => {
            response.status(500).json(err)
        })
    },
    // Update in CRUD (finding by _id)
    updateJoke: (request, response) => {
        Joke.findOneAndUpdate({_id: request.params.id},
            request.body,
            {new: true, runValidators: true})
            .then((updatedJoke) => {
                response.json(updatedJoke)
            })
            .catch((err) => {
                response.status(500).json(err)
            })
    },
    // Delete in CRUD (finding by _id)
    deleteJoke: (request, response) => {
        Joke.deleteOne({_id: request.params.id})
        .then((result) => {
            request.status(201).json(result)
        })
        .catch((err) => {
            response.status(500).json(err)
        })
    }
}