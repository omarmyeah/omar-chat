import Background from "../components/Background";
import { Outlet } from "react-router";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

// 
export default function Layout({ navbarClickableItems = undefined, footer = true}) {
    return (
        <div className="h-screen flex flex-col">
            <Navbar clickableItems={navbarClickableItems} />
            <Background>
                <Outlet />
            </Background>
            {footer && <Footer />}
        </div>
    );
}