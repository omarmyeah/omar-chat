import axios from "axios";

export const UserInfoPostService() {
    sendUserInfo: async (username, password, authEndpoint) => {
        const response = await axios.post(`/auth/${authEndpoint}`)

        //TODO
    }
}