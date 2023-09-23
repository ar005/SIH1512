import {Link} from "react-router-dom";
// import Button from '@mui/material/Button';
import Button from '@mui/material/Button';
// import 'bootstrap/dist/css/bootstrap.min.css';

export const Navbar=()=>{
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark"style={{justifyContent: "center"}}>
          <Link to="/" class='link'><Button size="large" variant="elevated" sx={{color : '#1976D2',borderColor: '#1976D2',backgroundColor: 'black'}}>Home</Button></Link>
          <Link to="/about" class='link'><Button size="large" variant="elevated" sx={{color : '#1976D2', borderColor: '#1976D2',backgroundColor: 'black'}}>About</Button></Link>
        </nav>
    )
}