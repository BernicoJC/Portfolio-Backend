import { useState, useRef } from 'react'
import ReCAPTCHA from 'react-google-recaptcha'

const Form = () => {
    const captchaRef = useRef(null)

    const [captchaToken, setCaptchaToken] = useState(null)

    const [formData, setFormData] = useState({
        name:"",
        email:"",
        feedback:""
    })

    const handleToken = (token) => {
        setCaptchaToken(token) 
    }

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    function sendToDb(event){
        event.preventDefault();
        
        fetch(`${import.meta.env.VITE_API_URL}/feedback/add`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            captchaRef.current.reset()
            setCaptchaToken(null)
            window.location.reload()
        })
    }

    return (
        <form onSubmit={sendToDb}>
            <label>Name</label>
            <input type="text" name="name" value={formData.name} onChange={handleChange} placeholder="What should I call you?" required />

            <label>Email</label>
            <input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="How do I contact you?" required />

            <label>Feedback</label>

            <textarea name="feedback" value={formData.feedback} onChange={handleChange} placeholder="What can I do to improve this site?" rows="4" cols="50" required></textarea>


            <ReCAPTCHA sitekey={import.meta.env.VITE_REACT_APP_SITE_KEY} ref={captchaRef} onChange={handleToken}/>


            <button type="submit" disabled={!captchaToken}>Submit</button>
        </form>
    )
}

export default Form