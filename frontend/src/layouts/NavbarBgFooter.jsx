import Background from "../components/Background";
import Footer from "../components/Footer";
import { Outlet } from "react-router";
import Navbar from "../components/Navbar";

export default function NavbarBgFooter({ navbarClickableItems = undefined }) {
    return (
        <div className="min-h-screen">
            <Navbar clickableItems={navbarClickableItems} />
            <Background className="pb-10">
                <Outlet />
            </Background>
            <Footer />
        </div>
    );
}

// <Navbar clickableItems={[{'Login':'login'}, {'Register':'register'}]}/>
// git commit -am "Made layouts/ for cleaner layout handling"