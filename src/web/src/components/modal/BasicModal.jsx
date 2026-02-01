export default function BasicModal({children , ...props}){
    return (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4" {...props}>
            <div className="bg-gradient-to-br from-gray-900 to-black rounded-2xl p-8 max-w-md w-full border border-red-900/20 shadow-2xl text-center">
                {children}
            </div>
        </div>
    )
}