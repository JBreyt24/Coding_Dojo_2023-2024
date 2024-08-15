import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './components/Home'
import Form from './components/Form'
import Dynamic from './components/Dynamic'
function App() {

  return (
    <>
      <h1>Routing Intro</h1>
      <BrowserRouter>
        <Routes>
          <Route path='/' element = {<Home/>}/>
          <Route path='form' element = {<Form/>}/> 
          <Route path='/dynamic/:name' element = {<Dynamic/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
