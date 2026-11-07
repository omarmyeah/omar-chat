export default function Sidebar({ items }) {
    return (
        <div className="drawer lg:drawer-open">
            <input id="my-drawer-3" type="checkbox" className="drawer-toggle" />
            <div className="drawer-content flex flex-col items-center justify-center">
                {/* Page content here */}
                <label htmlFor="my-drawer-3" className="btn drawer-button lg:hidden">
                Expand contacts list
                </label>
            </div>
            <div className="drawer-side">
                <label htmlFor="my-drawer-3" aria-label="close sidebar" className="drawer-overlay"></label>
                <ul className="menu bg-base-200 w-80 p-4">
                {/* Sidebar content here */}
                {items.map((item) => {
                    return (<li className="hover:text-primary"><a>{item}</a></li>);
                })}
                </ul>
            </div>
        </div>
    );
}