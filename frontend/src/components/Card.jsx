export default function Card({ className = "", children }) {
    return (
        <div className={`rounded-xl bg-base-100/50 ${className}`}>
            {children}
        </div>
    );
}
