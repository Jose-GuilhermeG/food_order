export default function SimpleButton({children , on_click , ...props}){
    return ( <button
                    className="relative group/btn"
                    onClick={on_click}
                    {...props}
                  >
            <div 
              className="relative cursor-pointer bg-gradient-to-r from-red-600 to-orange-500 text-white px-5 py-2.5 rounded-xl font-bold text-sm hover:scale-105 transition-transform flex items-center space-x-2">
              {children}
            </div>
                  </button>
    )
}