export default function Background({ children, className = "" }) {
    return (
        <div className={`${className} flex flex-col flex-1 bg-linear-to-t from-[#30cfd0] to-[#330867]`}>
            {children}
        </div>
    );
}