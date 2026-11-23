import { NavLink } from "react-router";

export default function ContactsSidebar({ contacts, onClick = (contact) => console.log(contact.name), parentUrl = '/chat' }) {
    console.log(contacts)
    return (
        <div className="">
            <ul className=" flex-col flex-1">
                {contacts.map((contact) => (
                    <li 
                        className="py-3 flex flex-col justify-center items-center hover:text-primary"
                        key={contact.id}
                    >
                        <NavLink 
                            to={`${parentUrl}/${contact.id}`}
                            className="flex flex-1"
                        >
                            {contact.name}
                        </NavLink>
                    </li>
                ))}
            </ul>
        </div>
    );
}