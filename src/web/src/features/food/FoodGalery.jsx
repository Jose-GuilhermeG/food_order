import FoodCard from "./FoodCard"


export default function FoodGalary({products , on_click , add_event}){
    if (!products.length) return(
        <div>
            <h1 className="text-white text-3xl font-bold text-center py-10 ">
                    Nenhum Produto no Momento
            </h1>
        </div>
    )
    return(
         <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pb-12">
            {products.map((product , index) => (
                <FoodCard product={product} key={index} add_event={add_event} on_click={on_click} />
            ))}
        </div>
    )
}