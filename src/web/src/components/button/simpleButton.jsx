export default function SimpleButton({children , ...props}){
    return ( <button
                    className="relative group/btn"
                    {...props}
                  >
                    <div className="absolute inset-0 bg-gradient-to-r from-red-600 to-orange-500 rounded-xl blur opacity-75 group-hover/btn:opacity-100 transition-opacity"></div>
                    {children}
                  </button>
    )
}