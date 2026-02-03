import { Clock } from 'lucide-react';
import AddCartButton from '../cart/AddCartButton';

export default function FoodCard({product , on_click ,add_event }){
    return (
        <div
              key={product.id}
              onClick={()=>on_click(product)}
              className="group bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl overflow-hidden border border-gray-700 hover:border-red-500/50 transition-all duration-300 hover:shadow-2xl hover:shadow-red-500/20 hover:-translate-y-1 cursor-pointer"
            >
              <div className="relative overflow-hidden h-48">
                <img
                  src={product.photo_url}
                  alt={product.name}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                <div className="absolute bottom-3 left-3 flex items-center space-x-2 bg-black/60 backdrop-blur-sm px-3 py-1.5 rounded-full">
                  <Clock className="w-4 h-4 text-orange-400" />
                  <span className="text-white text-xs font-bold">{product.prepTime}</span>
                </div>
              </div>

              <div className="p-5">
                <h3 className="text-xl font-black text-white mb-2">{product.name}</h3>
                <p className="text-gray-400 text-sm mb-4 line-clamp-2">{product.description}</p>

                <div className="flex items-center justify-between">
                  <div className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-orange-500">
                    R$ {product.price.toFixed(2)}
                  </div>
                  <AddCartButton on_click={(e)=>{
                    e.stopPropagation()
                    add_event(product)
                  }} />
                </div>
              </div>
            </div>
    )
}