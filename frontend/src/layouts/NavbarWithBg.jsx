import Background from "../components/Background";
import Navbar from "../components/navbar";
import { Outlet } from "react-router";


export default function NavbarWithBg({ children }) {
    return (
        <>
            <Navbar />
            <Background>
                <Outlet />
            </Background>
        </>
    );
}