import { useState } from 'react'
// import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'
import {GiStreetLight} from "react-icons/gi";
import IconButton from '@mui/material/IconButton';
import { IconContext } from 'react-icons';
import {ImSwitch} from 'react-icons/im';
import Tooltip from '@mui/material/Tooltip';
import { Typography } from '@mui/material';
import {Box,AppBar,Toolbar} from '@mui/material';
import {Nav,Navbar,Container,NavDropdown} from 'react-bootstrap';


function Streetlight(props){
  const [mode, setMode] = useState(false)
  const name1='sl '+props.name
  const name2='sl '+(parseInt(props.name)+1)
  return (
    <div class='row' style={{display:'flex'}}>
       
      <div class="lights">
        <IconButton sx={{color:'white'}}><ImSwitch/></IconButton>
        <Tooltip title={<Typography fontSize={20}>{name1} </Typography>}arrow placement='right'> <IconContext.Provider value={{size:70}}><GiStreetLight/></IconContext.Provider> </Tooltip>
      </div>
      

      <div class="lights">
      <Tooltip title={<Typography fontSize={20}>{name2} </Typography>}arrow placement='left'>
        <IconContext.Provider value={{size:70}}>
          <GiStreetLight style={{transform: 'scaleX(-1)' }}/>
          </IconContext.Provider> 
          </Tooltip>
      <IconButton sx={{color:'white'}}><ImSwitch/></IconButton>
      </div>
    </div>
  )
}
const App=()=>{
  return (
    <div>
     {/* Working on Appbar still */}
   
    <div class="maindiv">
      <Streetlight name='1'/>
      <Streetlight name='3'/>
      <Streetlight name='5'/>
    </div>
    </div>
    
  )
}

export default App
