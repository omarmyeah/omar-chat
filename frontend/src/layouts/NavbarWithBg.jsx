import Background from "../components/Background";
import { Outlet } from "react-router";
import Navbar from "../components/Navbar";

export default function NavbarWithBg() {
    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <Background>
                <Outlet />
            </Background>
        </div>
    );
}