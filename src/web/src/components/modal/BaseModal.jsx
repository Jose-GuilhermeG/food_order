export default function BaseModal({children , id  , set_open_state ,...props}){

    return (
        <div 
            {...props}
            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" id={id} onClick={(e)=>{
                if(e.target.id == id) set_open_state(false)
            }}
        >
            {children}
        </div>
    )
}