import { useState } from 'react'
import './App.css'
import Form from './components/Form'
import Display from './components/Display'

function App() {
  const [movieWatchlist, setMovieWatchlist] = useState([])
  return (
    <>
      <h1>Movie Watch List</h1>
      <Form movieWatchlist = {movieWatchlist} setMovieWatchlist = {setMovieWatchlist}/>
      <Display movieWatchlist = {movieWatchlist} setMovieWatchlist = {setMovieWatchlist}/>
    </>
  )
}

export default App
