import { NavLink } from 'react-router-dom';

// https://hygraph.com/blog/routing-in-react for design later on
const NavBar = () => {
    return(
        <ul id="main_navbar_container">
            <NavLink to="/">
                <li id="main_navbar">
                    Home
                </li>
            </NavLink>
            <NavLink to="/projects/home">
                <li id="main_navbar">
                    Projects
                </li>
            </NavLink>
            <NavLink to="/resume">
                <li id="main_navbar">
                    Resume
                </li>
            </NavLink>
        </ul>
    )
}

export default NavBar