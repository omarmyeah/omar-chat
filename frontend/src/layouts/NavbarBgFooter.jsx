import Background from "../components/Background";
import Navbar from "../components/navbar";
import Footer from "../components/Footer";
import { Outlet } from "react-router";

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