import { useState , useEffect } from "react"
import { Check , Timer } from "lucide-react"
import { get_ready_order , get_preparing_orders } from "../services/order_services"

export default function PublicView(){

    const [currentOrder , setCurrentOrder] = useState()
    const [inPreparation , setInPreparation] = useState([])

    
    useEffect(()=>{
        const set_ready_order =()=>{
            const ws = get_ready_order()
            ws.onmessage = ((event)=>{
                setCurrentOrder(JSON.parse(event.data))
            })

            return ws
        }

        const set_preparing_orders = ()=>{
            const ws = get_preparing_orders()
            ws.onmessage = (event)=>{
                setInPreparation(JSON.parse(event.data))
            }

            return ws

        }
        
        const ready_order_connection = set_ready_order()
        const preparing_order_connection = set_preparing_orders()
        console.log(inPreparation)
        
        return ()=>{
            ready_order_connection.close()
            preparing_order_connection.close()
        }

    },[])

    if (!currentOrder && !inPreparation.length){
        return (
            <div className="w-screen h-screen bg-black-gradient flex flex-col justify-center items-center">
                <h1 className="text-6xl text-white font-black text-center my-15">
                    Aguardando algum Pedido ficar Pronto
                    <Timer className="inline w-16 h-16 mx-2 " />
                </h1>
            </div>
        )
    }

    return (
        <div className="w-screen h-screen bg-black-gradient flex flex-col justify-center items-center">
                <h1 className="text-6xl text-white font-black text-center my-15">
                    Pedido Pronto
                    <Check className="inline w-16 h-16 mx-2 " />
                    <br />
                    <span className="text-4xl font-serif font-light ">
                        { currentOrder ? currentOrder.client_name : "Nenhum Pedido pronto ainda"}
                    </span>
                </h1>
           {currentOrder ? 
           <p className="bg-orange-gradient text-6xl text-white font-black text-center leading-20 p-5 min-w-[20%] min-h-[10%] rounded-2xl flex-col flex justify-center items-center">
                #{currentOrder.code}
            </p>
            :
            <p></p>
            }

                <div className="text-white px-5 my-10 ">
                    <h1 className="text-5xl">
                        Sendo Feito <Timer className="inline w-[36px] h-[36px] mx-5"/>
                    </h1>
                    <br />
                    {
                        inPreparation.length ? 
                        <ul>
                            {
                                inPreparation.map(element=><li>{element.client_name} #{element.code}</li>)
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