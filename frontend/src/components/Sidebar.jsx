import { NavLink } from "react-router";

export default function ContactsSidebar({ contacts, onClick = (contact) => console.log(contact.name), parentUrl = '/chat' }) {
    console.log(contacts)
    return (
        <div className="bg-black">
            <ul>
                {contacts.map((contact) => (
                    <li 
                        className="py-3 flex flex-col justify-center"
                        key={contact.id}
                    >
                        <NavLink 
                            to={`${parentUrl}/${contact.id}`}
                            className='hover:text-primary'
                        >
                            {contact.name}
                        </NavLink>
                    </li>
                ))}
            </ul>
        </div>
    );
}