import { useState , useEffect } from "react"
import { Check , Timer } from "lucide-react"

export default function PublicView(){

    const [currentOrder , setCurrentOrder] = useState({code : 10 , client_name : "Guilherme" })
    const [readyOrders , setReadyOrders ] = useState([])
    const [inPreparation , setInPreparation] = useState([])

    return (
        <div className="w-screen h-screen bg-black-gradient flex flex-col justify-center items-center">
                <h1 className="text-6xl text-white font-black text-center my-15">
                    Pedido Pronto
                    <Check className="inline w-16 h-16 mx-2 " />
                    <br />
                    <span className="text-4xl font-serif font-light ">
                        {currentOrder.client_name}
                    </span>
                </h1>
            <p className="bg-orange-gradient text-6xl text-white font-black text-center leading-20 p-5 min-w-[20%] min-h-[10%] rounded-2xl flex-col flex justify-center items-center">
                #{currentOrder.code}
            </p>

                <div className="text-white px-5 my-10 ">
                    <h1 className="text-5xl">
                        Sendo Feito <Timer className="inline w-[36px] h-[36px] mx-5"/>
                    </h1>
                    <br />
                    {
                        inPreparation.length ? 
                        <ul>
                            {
                                inPreparation.map(element=><li>{element}</li>)
                            }
                        </ul> :
                        <p className="my-2 text-2xl mx-2">
                            Nenhum Item sendo feito
                        </p>
                    }   

                </div>
        </div>
    )
}