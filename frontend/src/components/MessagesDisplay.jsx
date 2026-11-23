export default function MessagesDisplay({ className = ""}) { //{ messages, userId, friendId, className }
    // userId is the id of local user, friendId is id of the person they're sending message to. 
    // this is required for deciding if messages are gnna be on right or left.
    return (
        // Card cuz we want the messages display to be kinda transparent.
        <div className={`${className}`}>
            <h1>Hi</h1>
        </div>
    );
}