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
        <div className="p-5 bg-orange-gradient rounded-2xl w-[50vw]">
            {currentOrder ?
                    <div>
                        <h1 className="text-6xl text-white font-black text-center my-15">
                            Pedido Pronto
                            <Check className="inline w-16 h-16 mx-2 " />
                            <br />
                            <span className="text-4xl font-serif font-black my-5">
                                { currentOrder ? `#${currentOrder.code} - ${currentOrder.client_name}` : "Nenhum Pedido pronto ainda"}
                            </span>
                            
                        </h1>
                    </div>
                :
                <div></div>
            }
                    <div className="text-white px-5 my-10 bg-white p-5 rounded-2xl">
                        <h1 className="text-5xl bg-clip-text bg-orange-gradient text-transparent font-serif font-black">
                            Sendo Feito <Timer className="inline w-[36px] h-[36px] mx-5 text-orange-700"/>
                        </h1>
                        <br />
                        {
                            inPreparation.length ?
                            <ul className="w-full flex flex-col justify-start items-start bg-clip-text bg-orange-gradient text-transparent font-serif">
                                {
                                    inPreparation.map(element=>
                                        <li className="text-3xl font-black tracking-[2.5px] my-2">
                                            #{element.code} - {element.client_name}
                                        </li>)
                                }
                            </ul> :
                            <p className="w-full flex flex-col justify-start items-start bg-clip-text bg-orange-gradient text-transparent font-serif text-3xl font-black tracking-[2.5px] my-2">
                                Nenhum Item sendo feito
                            </p>
                        }
                    </div>
        </div>
        </div>
    )
}