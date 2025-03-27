import { NavLink } from 'react-router-dom';

const ProjectNavBar = () => {
    return(
        <ul id="project_navbar_container">
            <NavLink to="../projects/software">
                <li id="project_navbar">
                    Software Projects
                </li>
            </NavLink>

            <NavLink to="../projects/other">
                <li id="project_navbar">
                    Other Programming Projects
                </li>
            </NavLink>

        </ul>
    )
}

export default ProjectNavBar