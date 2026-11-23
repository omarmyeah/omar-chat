import Searchbar from "../components/Searchbar";
import ContactsSidebar from "../components/Sidebar";

export default function Chat() {
    return (
        <>
            <div className="grid grid-cols-6 flex-1">
                <div className="col-span-1 border flex flex-col">
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
                <div className="col-span-3">
                    {/* Chat place */}
                </div>
            </div>
        </>
    );
}