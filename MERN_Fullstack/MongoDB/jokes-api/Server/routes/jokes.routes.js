const jokesController = require('../controllers/jokes.controller')

module.exports = (app) => {
    app.get('/api/allJokes', jokesController.findAllJokes)
    app.get('/api/findOneJoke/:id', jokesController.findOneJoke)
    app.post('/api/createJoke', jokesController.createJoke)
    app.put('/api/updateJoke/:id', jokesController.updateJoke)
    app.delete('/api/deleteJoke/:id', jokesController.deleteJoke)
}