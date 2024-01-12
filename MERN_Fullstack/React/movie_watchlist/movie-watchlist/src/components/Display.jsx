import React, {useState} from 'react';

const Display = (props) => {
    const {movieWatchlist, setMovieWatchlist} = props


    const toggleWatchlist = (movie) => {
        const updatedMovieWatchlist = movieWatchlist.map((movieFromMap) => {
            if(movieFromMap === movie){
                movieFromMap.hasBeenWatched = !movieFromMap.hasBeenWatched
            }
            return movieFromMap
        })
        setMovieWatchlist(updatedMovieWatchlist)
    }
    const removeFromWatchlist = (movie) => {
        const updatedMovieWatchlist = movieWatchlist.filter((movieFromFilter) => movieFromFilter !== movie)
        setMovieWatchlist(updatedMovieWatchlist)
    }
    return (
        <div>
            <h2>Your Movies</h2>
            {
                movieWatchlist.map((movie, idx) => (
                    <div key= {idx} style={{border: "2px solid red"}}>
                        {
                            movie.hasBeenWatched?
                            <h3 style={{textDecoration: "line-through"}}>Title: {movie.title}</h3>:
                            <h3>Title: {movie.title}</h3>
                        }
                        <h3>Director: {movie.director}</h3>
                        <h3>Genre: {movie.genre}</h3>
                        <h3>Release Year: {movie.releaseYear}</h3>
                        <input type="checkbox" onClick={() => toggleWatchlist(movie)} defaultChecked ={movie.hasBeenWatched}/>
                        <button onClick={() => removeFromWatchlist(movie)}>Remove from Watchlist</button>
                    </div>
                ))
            }
        </div>
    )
}

export default Display;