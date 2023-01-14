
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
                console.log(err);
            })
        
        return week_generated;
    }
   
}


export { CookingPlannerAPI }
