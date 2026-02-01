import SimpleButton from "../../components/button/simpleButton";
import { Plus } from "lucide-react";

export default function AddCartButton({content = "Adcionar", on_click ,...props}){
    return (
        <SimpleButton {...props}>
            <div 
              onClick={on_click}
              className="relative bg-gradient-to-r from-red-600 to-orange-500 text-white px-5 py-2.5 rounded-xl font-bold text-sm hover:scale-105 transition-transform flex items-center space-x-2">
              <Plus className="w-4 h-4" strokeWidth={3} />
              <span>{content}</span>
            </div>
        </SimpleButton>
    )
}