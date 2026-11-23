export default function MessageInput({ className = "" }) {
    return (
        <div className={`join ${className}`}>
        <div>
            <label className="input validator join-item">
            <input type="text" placeholder="Send a message" required />
            </label>
            <div className="validator-hint hidden">Enter valid email address</div>
        </div>
        <button className="btn btn-neutral join-item">Send</button>
        </div>
    );
}