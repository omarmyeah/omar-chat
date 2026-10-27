import GradientDiv from "../components/GradientDiv";
import Navbar from "../components/navbar";

export default function Chat() {
    return (
        <>
            <GradientDiv>
                <Navbar />
                <div className="grid grid-cols-4">
                    <div className="col-span-1">
                        {/* Contacts list*/}
                    </div>
                    <div className="col-span-3">
                        {/* Chat place */}
                    </div>
                </div>
            </GradientDiv>
        </>
    );
}