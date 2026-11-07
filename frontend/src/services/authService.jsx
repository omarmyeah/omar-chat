import axios from "axios";

const authService =  {
    submitAuthRequest: async (username, password, authEndpoint) => {
        try {
            const response = await axios.post(`/auth/${authEndpoint}`, {
                    username: username,
                    password: password,
            });

            return JSON.parse(response);
        } catch(error) {
            console.error(error);
        }
    }
}

export default authService;