import React, {useState} from 'react';

const Form = (props) => {
    const {movieWatchlist, setMovieWatchlist} = props
    const [title, setTitle] = useState ('')
    const [director, setDirector] = useState ('')
    const [genre, setGenre] = useState ('Action')
    const [releaseYear, setReleaseYear] = useState (1920)

    const submitHandler = (e) => {
        e.preventDefault()
        console.log("Submitted");
        const newMovie = {
            title,
            director,
            genre,
            releaseYear,
            hasBeenWatched: false
        }
        setMovieWatchlist([...movieWatchlist, newMovie])
        setTitle("")
        setDirector("")
        setGenre("Action")
        setReleaseYear(1920)


    }
    return (
        <div>
            <h2>Add a movie to your watchlist</h2>
            <form onSubmit = {submitHandler}>
                <div>
                    <label>Title:</label>
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)}/>
                </div>
                <div>
                    <label>Director:</label>
                    <input type="text" value={director} onChange={(e) => setDirector(e.target.value)}/>
                </div>
                <div>
                    <label>Genre:</label>
                    <select onChange = {(e) => setGenre (e.target.value)}>
                        <option value="Action">Action</option>
                        <option value="Drama">Drama</option>
                        <option value="Horror">Horror</option>
                        <option value="Comedy">Comedy</option>
                        <option value="Family">Family</option>
                    </select>
                </div>
                <div>
                    <label>Release Year:</label>
                    <input type="number" value={releaseYear} onChange={(e) => setReleaseYear(e.target.value)}/>
                </div>
                <button>Add Movie</button>
            </form>
        </div>
)}



export default Form;