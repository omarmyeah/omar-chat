import Navbar from "../components/navbar";
import Background from "../components/Background"
import Searchbar from "../components/Searchbar";
import Sidebar from "../components/Sidebar";

export default function Chat() {
    return (
        <>
            <Background>
                <Navbar />
                <div className="grid grid-cols-4">
                    <div className="col-span-1 border">
                        {/* Contacts list*/}
                        <h1 className="text-3xl text-center">Contacts</h1>
                        {/* make this functional */}
                        <Searchbar />
                    </div>
                    <div className="col-span-3">
                        {/* Chat place */}
                    </div>
                </div>
                <Sidebar items={["malek", "Saaim", "Ziyad"]}/>
            </Background>
        </>
    );
}