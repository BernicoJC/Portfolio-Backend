import { useState, useEffect } from 'react'
import Popup from 'reactjs-popup';
import ProjectNavBar from '../../projectsnavbar'

const Other = () => {
    const [projectData, setProjectData] = useState([])

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/projects/game/get`) 
            .then((res) => res.json())  // Parse the response as JSON
            .then((data) => {
                setProjectData(data.reverse());  // Store the data in state
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, []);

    return (
        <div id="content">
            <ProjectNavBar/>
            <h1>Other Programming Projects</h1>
            <h3>These projects include game development and other non-software related projects.</h3>

            <div id="projects_container">
                {
                    projectData.map((game) => (
                        <Popup
                        trigger={<div key={game.id} id="project">
                            <div id="project_image">
                                <img src={game.image}/>
                            </div>
                            
                            <div id="project_titles">
                                <h2>{game.title}</h2>
                                <h3>{game.subtitle}</h3>
                            </div>
                        </div>
                        }
                        modal
                        nested
                        >
                            {
                                close => (
                                    <div key={game.id} id="popup_modal">
                                        <h1>{game.title}</h1>
                                        <img src={game.image} width="40%" />
                                        <h3>{game.description}</h3>
                                        <br></br>
                                        <h3><a href={game.link}>Link to Project</a></h3>
                                        <br></br>
                                        <button onClick={() => close()}>Close</button>
                                    </div>
                                )
                            }
                        </Popup>
                        // <div key={game.id} className="project">
                        //     <h2>{game.title}</h2>
                        //     <h3>{game.subtitle}</h3>
                        //     <h3>{game.description}</h3>
                        //     <img src={game.image} width="20%" />
                        // </div>
                    ))
                }
            </div>
        </div>
    )
}

export default Other