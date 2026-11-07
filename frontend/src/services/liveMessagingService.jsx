import useWebSocket from "react-use-websocket";

export const useLiveMessaging = (onMessage) => {const { sendMessage, lastMessage, readyState } = useWebSocket(
        "ws://localhost:8000/ws",
        {
            onOpen: () => console.log("ws Conn. opened"),
            onClose: () => console.log("ws Conn. closed"),
            onError: (e) => console.error(`There was an error: ${e}`),
            shouldReconnect: (closeEvent) => false,
            onMessage: onMessage,
        }
    )   
    /*
    sendMessage allows u to send to ws-server so we return that, 
    we also return lastMessage because it's the last message received.

    for sendMessage, in this specific example, pass JSON.stringify with the required keys.
    */
    return { sendMessage, lastMessage, readyState }
}