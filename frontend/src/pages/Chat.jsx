import Searchbar from "../components/Searchbar";
import ContactsSidebar from "../components/Sidebar";
import MessagesDisplay from "../components/MessagesDisplay";
import MessageInput from "../components/MessageInput";

export default function Chat() {
    return (
        <>
            <div className="grid grid-cols-6 flex-1">
                <div className="col-span-1 border flex flex-col bg-black">
                    {/* Contacts list*/}
                    <h1 className="text-3xl text-center">Contacts</h1>
                    {/* make this functional */}
                    <Searchbar />
                    <ContactsSidebar 
                        contacts={[
                            {
                                name: 'malek',
                                id: 1,
                            },
                            {
                                name: 'Ziyad',
                                id: 2,
                            },
                            {
                                name: 'Usayd',
                                id: 0,
                            } 
                        ]}
                    />
                </div>
                <div className="col-span-5 flex flex-1">
                    <div className="grid grid-rows-12 w-full h-full bg-white/40">
                        <div className="row-span-11 flex flex-1">
                            <MessagesDisplay className="flex flex-1" />
                        </div>
                        <div className="row-span-1">
                            <MessageInput className={"w-full"}/>
                        </div>
                    </div>
                    {/* Chat place */}
                </div>
            </div>
        </>
    );
}