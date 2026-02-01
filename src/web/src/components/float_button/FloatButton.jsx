export default function FloatButton({children , on_click , ...props}){
    return (
        <div
        className="w-fit h-fit p-5 rounded-2xl cursor-pointer bg-white fixed z-30 hover:scale-110 transition-all"
        onClick={on_click} 
        {...props}
        >
            {children}
        </div>
    )
}