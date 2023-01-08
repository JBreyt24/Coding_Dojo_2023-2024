import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './components/Home'
import Dynamic from './components/Dynamic'

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/home' element = {<Home/>}/>
          <Route path='/:word' element = {<Dynamic/>}/>
          <Route path='/:word/:color/:bgColor' element = {<Dynamic/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
