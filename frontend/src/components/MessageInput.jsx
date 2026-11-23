export default function MessageInput({ className = "" }) {
    return (
        <form className={`grid grid-cols-15 ${className}`}>
            <div className="col-span-14">
                <input 
                    type="text" 
                    className="bg-black p-2 pl-4 rounded-xl w-full" 
                    placeholder="Send a message"
                    required 
                />
            </div>

            <div className="col-span-1 flex flex-1 justify-center">
                <button 
                    type="submit"
                    className="btn bg-base-200 text-white border-2 border-transparent hover:text-primary hover:border hover:border-primary focus-visible:border-2 focus-visible:border-primary rounded-xl w-[95%]"
                >
                    Send
                </button>
            </div>
        </form>
    );
}