import Navbar from "../components/Navbar";
import Card from '../components/Card'
import Background from "../components/Background";
import FormField from "../components/FormField";
import FormSubmissionButton from "../components/FormSubmissionButton"
import authService from "../services/authService"

import { use, useState } from "react";


export default function Registration () {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        confirmation: ''
    })
    const [isUsernameTaken, setIsUsernameTaken] = useState(false)


    // TODO: use this.
    const isFormValid = formData.username.trim() && formData.email.trim() && formData.password.trim();

    function handleSubmit(e) {
        e.preventDefault();
        
        const response = authService.submitAuthRequest({
            username: formData.username, 
            password: formData.password,
            authEndpoint: "register",
        })

        if (response.ok) {
            // TODO: link chat screen here

        } else {
            setIsUsernameTaken(true);
        }
    }

    function handleChange(e) {
        //
        const { name, value } = e.target();
        setFormData((prev) => ({
            ...prev,
            [name]: value
        }))
    }

    return (
        <>
            <Background>
                {/* keep Navbar items none here:*/}
                <Navbar />
                <Card className='my-auto mx-auto px-20 py-20 text-center'>
                    <div className="text-black">
                        <h1 className="text-6xl mb-3">Registration</h1>
                        <h1 className="text-2xl mb-10">Welcome to the team.</h1>
                    </div>
                    <form action="" className="flex flex-col gap-4 w-full" onSubmit={handleSubmit}>
                        <FormField placeholder="Create a Username" label="Username" id="password-input" type="text" className="input-lg w-full" maxlength/>
                        <FormField placeholder="Create a Password" label="Password" id="username-input" type="password" className="input-lg w-full" />
                        <FormField placeholder="Confirm Password" label="Confirm Password" id="password-confirmation-input" type="password" className="input-lg w-full" />
                        <FormSubmissionButton name="Register"/>
                        {<p className={`text-warning ${(isUsernameTaken)? "visible" : "invisible"}`}>
                            Sorry, this username is already taken.
                        </p>}
                    </form>
                </Card>
            </Background>
        </>
    );
}

// git commit -am "Added errors and added more account-related routes, and started working on live messaging with webSockets. "
// git status -- backend/errors.py