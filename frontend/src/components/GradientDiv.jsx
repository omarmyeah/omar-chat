export default function GradientDiv({ children }) {
    return (
        <div className="min-h-screen flex flex-col bg-linear-to-t from-[#30cfd0] to-[#330867]">
            {children}
        </div>
    );
}