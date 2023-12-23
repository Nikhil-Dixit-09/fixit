import * as api from '../api'
export const getResponse=(formData)=>async(dispatch)=>{
    try{
        const {data}=await api.getResponse(formData);
        console.log(data);
    }catch(err){
        console.log(err);
    }
}