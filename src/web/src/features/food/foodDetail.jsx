import { X } from "lucide-react";
import AddCartButton from "../cart/AddCartButton";
import BaseModal from "../../components/modal/BaseModal";

export default function FoodDetail({ state , add_envent ,set_state , food , ...props}){

    if (!state) return <div></div>

    const data_food = {...food , photo_url : food.photos[0].photo_url}

    return (
        <BaseModal id="productModal" open_state={state} set_open_state={set_state} {...props} style={{display : 'flex' , justifyItems : 'center' , alignItems : "center"}}>
            <div className="relative bg-gradient-to-br from-gray-900 to-black rounded-2xl max-w-[30vw] h-full max-h-[75vh] w-full border border-red-900/20 shadow-2xl overflow-hidden pb-10 m-auto">
             <button
                  className="p-2 hover:bg-gray-800 rounded-lg transition-colors z-100 fixed cursor-pointer"
                  onClick={()=>set_state(false)}
                >
                  <X className="w-6 h-6 text-gray-400" />
                </button>
                <div className="w-full h-3/6 rounded-2xl flex overflow-hidden">
                    {
                        food.photos.map((photo)=><img src={photo.photo_url} className="min-w-full h-full object-cover object-center rounded-2xl" />)
                    }
                </div>
                <h1 className="text-3xl text-white font-black p-5 text-left mt-10 mx-5">
                    {food.name}
                </h1>
                <span className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-orange-500 p-5 mx-5">
                    R$ {food.price.toFixed(2)}
                  </span>
                <p className="text-white text-left mx-5 p-5 text-wrap max-w-full whitespace-normal wrap-break-word">
                    {food.description}
                </p>
                <AddCartButton style={{width : '90%' , left : '5%' , margin : '10% 0 0 0'}} on_click={()=>{
                    add_envent(data_food)
                    set_state(false)    
                }} />
            </div>
        </BaseModal>
    )
}