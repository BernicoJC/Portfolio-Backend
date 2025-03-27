import Form from "./form"

const Home = () => {
    return (
        <div id="content">
            
            <div id="home_title">    
                <h1>Hi, My Name is Bernico!</h1>
                <img src="/images/bernico.jpg" width="500em"></img>
                <h2>Welcome to my personal website, please enjoy your stay!</h2>
            </div>

            <hr></hr>

            <div id="home_body">
                <div id="about_me">
                    <h2>About Me</h2>
                    <hr></hr>
                    <p>
                    A student pursuing Computer Science bachelor’s degree at the University of California, San Diego (UCSD). Currently, I am a third year here. I'm passionate about software engineering as it lets me channel my logical thinking skills as well as allow me to use my creativity to help solve the worlds' problems. In Particular, I’m most excited about algorithm optimization, debugging, and application development. I am always a hard and smart worker when faced with challenges and I am open-minded to explore new facets of the computer science field.
                    </p>
                </div>
                <hr></hr>
                <div id="form">
                    <h2>Feedback</h2>
                    <hr></hr>
                    <Form />
                </div>
            </div>

        </div>
    )
}

export default Home