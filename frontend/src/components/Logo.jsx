import '../index.css'

export default function Logo({ className = 'text-3xl' }) {
    return (
        <p className={className}>
            Omar <span className="text-primary">Chat.</span>
        </p>
    );
}