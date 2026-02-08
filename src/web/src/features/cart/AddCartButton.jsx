import SimpleButton from "../../components/button/simpleButton";
import { Plus } from "lucide-react";

export default function AddCartButton({content = "Adcionar", on_click ,...props}){
    return (
        <SimpleButton {...props}  on_click={on_click}>
              <Plus className="w-4 h-4" strokeWidth={3} />
              <span>{content}</span>
        </SimpleButton>
    )
}