import { Loader2 as LoaderIcon } from "lucide-react"

export default function Loader(){
    return (
        <div className="w-16 h-16 m-auto my-30">
           <LoaderIcon color="white" className="animate-spin w-full h-full" />
        </div>
    )
}