import BasicModal from "../../components/modal/BasicModal"
import { X } from "lucide-react"

export default function ErrModal({...props}){
    return (
        <BasicModal {...props}>
            <h1 className='text-3xl text-white font-black'>
              Ocorreu um erro inesperado
            </h1>
            <div className='m-auto border-red-600 border w-fit p-2 rounded-full my-10'>
              <X color='red' className='w-10 h-10'/>
            </div>
      </BasicModal>
    )
}