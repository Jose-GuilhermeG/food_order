export default function Err404(){
    return (
        <div className="w-screen h-screen bg-black-gradient flex flex-col justify-center items-center">
            <h1 className="text-9xl font-black text-center bg-clip-text text-transparent bg-orange-gradient">
                404
            </h1>
            <p className="text-white text-7xl font-light text-center font-serif">
                Page not found
            </p>
        </div>
    )
}