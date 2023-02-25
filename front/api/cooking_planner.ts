
class CookingPlannerAPI {

    static API_PROXY_NAME: string = "/cookingplanner";

    constructor() {}

    async generateWeekUnique(axios: any) {
        /**
         * Generate a week with a unique meal strategy.
         * 
         * Call the api backend.
         */
        
        var week_generated = null;
        
        let url : string = CookingPlannerAPI.API_PROXY_NAME + '/week/work/unique';

        await axios.get(url)
            .then((res: { data: any; }) => {
                let data = res.data;
                week_generated = Object.assign({}, data)
            })
            .catch((err: any) => {
                throw new Error(err);
            })
        
        return week_generated;
    }
   
    async createNewAccount(axios: any, email: string, password: string) {
        /**
         * Create a new account.
         * We suppose that we already check the value of the email and 
         * the password before hand. Thus, we will not show error if the
         * email and the password not match the backend checked.
         * 
         * Exceptions: 
         *  - Email already exists in the database (code 409)
         *  - If other issues, we return a server error.
         */
        
        let url : string = CookingPlannerAPI.API_PROXY_NAME + '/auth/register';

        let response = null;

        await axios.post(url, {
            email: email,
            password: password
        }).then((res: any) => {
            response = res;
        }).catch((error: any) => {
            if (error.response.status == 409) {
                throw new Error("The email already exists !");
            }
            throw new Error("Error from the server");
        })

        return response;
    }

    async getProfiles(axios: any) {

        

        let url : string = CookingPlannerAPI.API_PROXY_NAME + '/profile';
        
        await axios.get(url).then((res: any) => {
            console.log(res);
        })

    }

}


export { CookingPlannerAPI }
