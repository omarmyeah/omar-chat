import Background from "../components/Background";
import Navbar from "../components/navbar";
import FormSubmissionButton from "../components/FormSubmissionButton";
import { NavLink } from "react-router";

export default function PageNotFound() {
    return (
        <Background>
            <Navbar />
            <div className="flex justify-center items-center min-h-screen gap-12">
                <div className=" text-center">
                    <h1 className="text-8xl mb-10">404 Not found.</h1>
                    <NavLink to="/" end>
                        <FormSubmissionButton name="Go home" method="" className="w-3/4 text-xl"/>
                    </NavLink>
                </div>
                <div className="">
                    <img src="404.png" alt="" />
                </div>
            </div>
        </Background>
    );
}