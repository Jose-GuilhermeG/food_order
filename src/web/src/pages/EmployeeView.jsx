//imports
import { useEffect , useState } from "react"

//components


//services
import { get_current_order, get_preparing_orders, set_current_order_as_ready } from "../services/order_services"

export default function EmployeeView() {
    const [currentOrder , setCurrentOrder] = useState() 
    const [preparingOrders , setPreparingOrders] = useState([])

    useEffect(()=>{
        const set_preparing_orders = async ()=>{
            const ws = get_preparing_orders()
            ws.onmessage = (event)=>{
                setPreparingOrders(JSON.parse(event.data))
            }

            return ws
        }

        const set_current_order = async ()=>{
            const ws = get_current_order()
            ws.onmessage = (event)=>{
                setCurrentOrder(JSON.parse(event.data))
                console.log(event.data)
            }

            return ws
        }

        const preparing_ws = set_preparing_orders()
        const current_order_ws = set_current_order()

        return ()=>{
            if(preparing_ws) preparing_ws.close()
            if(current_order_ws) current_order_ws.close()
        }
    },[])

    const set_ready = ()=>[
        set_current_order_as_ready()
    ]

    return (
        <div className="w-screen h-screen bg-black-gradient">
            <h1 className="text-4xl font-black text-white text-center relative top-5">
                Area do funcionario
            </h1>
            <div className="grid grid-cols-2 grid-rows-1 w-4/5 h-[90%] m-auto top-1/20 relative gap-5">
                {currentOrder && <div className="w-full h-[90%] flex flex-col justify-center items-center">
                    <div className="bg-white w-4/5 min-h-[50vh] rounded-2xl my-10 p-5 flex flex-col justify-start items-start gap-5">
                        <h1 className="text-3xl font-black bg-orange-gradient bg-clip-text text-transparent font-serif tracking-[2px]">
                            Pedido atual:
                        </h1>
                        <p className="p-5 text-3xl font-serif bg-orange-gradient bg-clip-text text-transparent">
                            #{currentOrder.code}-{currentOrder.client_name}
                        </p>
                        <ul className="px-2">
                            {currentOrder.orders.map(element=>(
                                <li className="py-2 px-5 text-2xl font-serif bg-orange-gradient bg-clip-text text-transparent">
                                    {element.food.name}
                                </li>
                            ))}
                        </ul>
                    </div>
                    <div className="w-4/5 h-[10vh] bg-white rounded-2xl flex justify-center items-center hover:bg-gray-300">
                        <button className="text-3xl font-black font-serif w-full h-full bg-orange-gradient bg-clip-text text-transparent cursor-pointer" onClick={set_ready}>
                            Marcar como Pronto
                        </button>
                    </div>
                </div>}
                <div className="w-4/5 h-[90%] bg-orange-gradient m-auto rounded-2xl">
                    <h1 className="text-3xl font-black text-white p-5 font-serif tracking-[2px]">
                        Lista de pedidos:
                    </h1>
                    { preparingOrders.length ? 
                    <ul>
                        {preparingOrders.map(element=>
                            <li className="p-5 text-3xl font-serif text-white">
                                #{element.code} - {element.client_name}
                            </li>
                        )}
                    </ul>:
                    <div>
                        <h1 className="text-3xl text-white font-black font-serif text-center my-10">
                            Nenhum pedido no momento
                        </h1>
                    </div>
                    }
                </div>
            </div>
        </div>
    )
}