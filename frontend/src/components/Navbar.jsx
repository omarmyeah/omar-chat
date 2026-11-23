import Logo from "./Logo";
import { NavLink } from "react-router";

export default function Navbar({ clickableItems=[] }) {
  return (
    <>
      <div className="navbar bg-base-100 shadow-sm py-5">
        <div className="flex-1 ml-5">
          <Logo />
        </div>
        <div className="flex-none">
          <ul className="menu menu-horizontal px-1 text-xl">
             {clickableItems && clickableItems.map((item) => {
                itemName = Object.keys(item)[0];
                return (
                <li key={itemName} className="texthover: ">
                  <NavLink to={`/${Object.values(item)[0]}`} className={`hover:text-primary`} end>
                    {itemName}
                  </NavLink>
                </li>
                );
            })}
          </ul>
        </div>
      </div>
    </>
  );
}