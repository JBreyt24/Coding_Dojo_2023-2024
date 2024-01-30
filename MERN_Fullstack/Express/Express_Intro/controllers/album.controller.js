const albums = [
    {id: 1, albumName: 'Iowa', artist: 'Slipknot'},
    {id: 2, albumName: 'The Famous', artist: 'Mobb Deep'},
    {id: 3, albumName: 'Homework', artist: 'Daft Punk'},
    {id: 4, albumName: 'The Best of Sade', artist: 'Sade'},
    {id: 5, albumName: 'Flying Microtonal Banana', artist: 'King Gizzard & the Lizard Wizard'}
]

module.export ={
    // key:value
    allAlbums: (request, response) => {
        // call to the DB to get all the albums
        response.json(albums)
    },
    getOneAlbum: (request, response) => {
        console.log(request.params);
        const id = request.params.id
        const album = albums.filter((album) => album.id == id)
        response.json(album)
    },
    createAlbum: (request, response) => {
        console.log(request.body);
        albums.push(request.body)
        response.json(albums)
    }
}