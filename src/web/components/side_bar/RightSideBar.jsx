import { X } from "lucide-react"

export default function RightSideBar({children , set_open_state ,open_state = true , ...props}){

    if (!open_state) return <div></div>

    return (
         <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" id="sideBar" onClick={(e)=>{
            if(e.target.id == "sideBar") set_open_state(false)
            }}>
            <div 
                className="fixed right-0 top-0 h-full w-full max-w-md bg-gradient-to-br from-gray-900 to-black border-l border-red-900/20 z-50 overflow-y-auto shadow-2xl"
                {...props}
            >   
                <button
                  onClick={() => set_open_state(false)}
                  className="p-2 hover:bg-gray-800 rounded-lg transition-colors z-100 top-5 right-5 fixed"
                >
                  <X className="w-6 h-6 text-gray-400" />
                </button>
                {children}
            </div>
        </div>
    )
}