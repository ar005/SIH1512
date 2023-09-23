import { useState } from 'react'
// import 'bootstrap/dist/css/bootstrap.min.css';
// import './App.css'
import {BrowserRouter as Router,Routes,Route} from "react-router-dom"
import {Home} from "./pages/Home"
import {About} from "./pages/About"
import {Navbar} from "./components/Navbar"

function App(){
  return(
    <div>
      <Router>
        {/* <Navbar> */}
          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/about" element={<About/>}/>
            <Route path='*' element={<h1 align="center">Error 404 : Page Not Found</h1>}/>
          </Routes>
        {/* </Navbar> */}
      </Router>
    </div>
  )
}

export default App
