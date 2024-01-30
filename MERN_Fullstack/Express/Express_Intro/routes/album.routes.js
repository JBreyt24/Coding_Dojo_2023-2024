const AlbumController = require('../controllers/album.controller')

module.export = (app) => {
    app.get('/api/allAlbums', AlbumController.allAlbums)
    app.get('/api/album/:id', AlbumController.getOneAlbum)
    app.get('/api/newAlbum', AlbumController.createAlbum)
} 