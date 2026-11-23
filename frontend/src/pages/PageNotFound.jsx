import FormSubmissionButton from "../components/FormSubmissionButton";
import { NavLink } from "react-router";

export default function PageNotFound() {
    return (
        <div className="flex justify-center items-center h-full gap-12">
            <div className=" text-center">
                <h1 className="text-8xl mb-10">404</h1>
                <h1 className="text-5xl mb-3">Page not found.</h1>
                <NavLink to="/" end>
                    <FormSubmissionButton name="Go home" method="" className="w-3/4 text-xl"/>
                </NavLink>
            </div>
            <div className="">
                <img src="404.png" alt="" />
            </div>
        </div>
    );
}