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
                return (
                <li key={item.name} className="texthover: ">
                  <NavLink to={item.path} className={`hover:text-primary`} end>
                    {item.name}
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