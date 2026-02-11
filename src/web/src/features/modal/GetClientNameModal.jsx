import BasicModal from "../../components/modal/BasicModal";
import SimpleButton from "../../components/button/simpleButton";

export default function GetClientNameModal({on_submit_envent , ...props}){
    return (
    <BasicModal {...props}>
        <form onSubmit={(e)=>{
          e.preventDefault()
          on_submit_envent(e)
        }}>
          <h1 className='text-3xl font-black text-white mb-3'>
            Seu Nome
          </h1>
          <input type="text" name='client_name' className='w-[95%] border border-white rounded-2xl my-5 text-white px-5 py-2' required />
          <div>
            <SimpleButton >
                <span>Confirmar</span>
            </SimpleButton>
          </div>
        </form>
    </BasicModal>
    )
}