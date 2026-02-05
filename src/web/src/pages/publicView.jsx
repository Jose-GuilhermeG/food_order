import { useState , useEffect } from "react"
import { Check , Timer } from "lucide-react"

export default function PublicView(){

    const [currentOrder , setCurrentOrder] = useState({code : 10 , client_name : "Guilherme" })
    const [readyOrders , setReadyOrders ] = useState([])

    return (
        <div className="w-screen h-screen bg-black-gradient flex flex-col justify-around items-center">
            <div className="bg-white p-5 min-w-[40%] min-h-[40%] rounded-2xl flex-col flex justify-center items-center">
                <h1 className="text-6xl text-transparent bg-clip-text bg-orange-gradient font-black text-center leading-20">
                    Pedido Pronto
                    <Check className="inline w-16 h-16 mx-2 text-orange-600 " />
                    <br />
                    #{currentOrder.code}
                    <br />
                    <span className="text-4xl font-serif font-light ">
                        {currentOrder.client_name}
                    </span>
                </h1>
            </div>

            <div className="bg-white p-5 min-w-[40%] min-h-[30%] rounded-2xl">
                <h1 className="text-black text-4xl flex justify-start items-center px-5 ">
                    Sendo Feito <Timer className="inline w-[36px] h-[36px] mx-5"/>
                </h1>
            </div>
        </div>
    )
}