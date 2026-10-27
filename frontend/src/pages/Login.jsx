import Navbar from "../components/navbar";
import Card from '../components/Card'
import GradientDiv from "../components/GradientDiv";
import FormField from "../components/FormField";
import FormSubmissionButton from "../components/FormSubmissionButton"
import axios from "axios";

export default function Login () {
    function handleSubmit(e) {
        e.preventDefault();
        // TODO
        // Send the info to backend 
        // Using websockets 😱
    }

    return (
        <>
            <GradientDiv>
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
                </Card>
            </GradientDiv>
        </>
    );
}