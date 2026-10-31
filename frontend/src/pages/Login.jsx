import Navbar from "../components/navbar";
import Card from '../components/Card'
import Background from "../components/Background";
import FormField from "../components/FormField";
import FormSubmissionButton from "../components/FormSubmissionButton"
import authService from "../services/authService";

import { useState } from "react";


export default function Login () {
    // maybe here make a mutual function with register cuz pretty similar just "login" instead of "register"
    function handleSubmit(e) {
        e.preventDefault();
        
        const response = authService.submitAuthRequest({
            username: formData.username, 
            password: formData.password,
            authEndpoint: "login",
        })

        if (response.ok) {
            // TODO: link chat screen here

        } else {
            isLoginInvalid(true);
        }
    }

    const [isLoginInvalid, setIsLoginInvalid] = useState(false);

    return (
        <>
            <Background>
                {/* keep Navbar items none here:*/}
                <Navbar />
                <Card className='my-auto mx-auto px-32 py-20 text-center'>
                    <div className="text-black">
                        <h1 className="text-9xl mb-3">Login</h1>
                        <h1 className="text-3xl mb-10">Welcome back.</h1>
                    </div>
                    <form action="" className="flex flex-col gap-4 w-full" onSubmit={handleSubmit}>
                        <FormField placeholder="Enter your Username" label="Username" id="password-input" type="text" className="input-lg w-full" />
                        <FormField placeholder="Enter your password" label="Password" id="username-input" type="password" className="input-lg w-full" />

                        <FormSubmissionButton name="Login"/>
                    </form>

                    {<p className={`text-warning ${(isLoginInvalid)? "visible" : "invisible"}`}>
                            Sorry, invalid login details.
                    </p>}
                </Card>
            </Background>
        </>
    );
}