import React, {useState} from 'react';

const AlbumForm = (props) => {
    const [title, setTitle] = useState('')
    const [artist, setArtist] = useState('')
    const [releaseYear, setReleaseYear] = useState(1930)
    const [albumSales, setAlbumSales] = useState(0)
    const [genre, setGenre] = useState('')

    // const handleTitle = (event) => {
        // console.log(event);
    //     setTitle(event.target.value);
    // }
    const submitHandler = (event) => {
        event.preventDefault()
        const newAlbum = {
            title,
            artist,
            releaseYear,
            albumSales,
            genre
        }
        console.log('Album', newAlbum);
        setTitle('')
        setArtist('')
        setReleaseYear(1930)
        setAlbumSales(0)
        setGenre('')
    }
    return (
        <div>
            <h1>Add your favorite album</h1>
            <form onSubmit={submitHandler}>
                <div>
                    <label>Title</label>
                    <input type="text" name="title" onChange={(e) => setTitle(e.target.value)} value={title}/>
                    {
                        title.length < 3 && title.length > 0? // -> if (title.length > 3){}
                        <p>Title must be 3 or more characters</p>: // {}
                        // else is represented by a ':'
                        null
                    }
                </div>
                <div>
                    <label>Artist</label>
                    <input type="text" name="artist" onChange={(e) => setArtist(e.target.value)} value={artist}/>
                    {
                        artist.length < 3 && artist.length > 0? 
                        <p>Artist must be 3 or more characters</p>:
                        null
                    }
                </div>
                <div>
                    <label>Release Year</label>
                    <input type="number" name="releaseYear" onChange={(e) => setReleaseYear(e.target.value)} value={releaseYear}/>
                    {
                        releaseYear < 1930? 
                        <p>Release Year 1930 or after</p>:
                        null
                    }
                </div>
                <div>
                    <label>Album Sales</label>
                    <input type="number" name="albumSales" onChange={(e) => setAlbumSales(e.target.value)} value={albumSales}/>
                    {
                        albumSales < 0? 
                        <p>Album sales must be greater than 0</p>:
                        null
                    }
                </div>
                <div>
                    <label>Genre</label>
                    <input type="text" name="genre" onChange={(e) => setGenre(e.target.value)} value={genre}/>
                    {
                        genre.length < 3 && genre.length > 0? 
                        <p>Genre must be 3 or more characters</p>:
                        null
                    }
                </div>
                <button>Add</button>
            </form>
            <h2>Title: {title}</h2>
            <h2>Artist: {artist}</h2>
            <h2>Release Year: {releaseYear}</h2>
            <h2>Album Sales: {albumSales}</h2>
            <h2>Genre: {genre}</h2>
        </div>
)}

export default AlbumForm;

// onChange onSubmit: 2 new synthetic events used in this project