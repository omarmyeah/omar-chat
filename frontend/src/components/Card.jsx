export default function Card({ className = "", children }) {
    return (
        <div className={`rounded-xl bg-white/50 ${className}`}>
            {children}
        </div>
    );
}
