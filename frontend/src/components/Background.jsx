export default function Background({ children, className }) {
    return (
        <div className={`${className} min-h-max flex flex-col bg-linear-to-t from-[#30cfd0] to-[#330867]`}>
            {children}
        </div>
    );
}