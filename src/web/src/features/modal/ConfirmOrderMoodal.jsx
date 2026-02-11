import BasicModal from "../../components/modal/BasicModal";

export default function ConfirmOrderModal({ orderNumber , on_click ,...props}){
    return (
        <BasicModal {...props}>
            <div className="w-20 h-20 bg-gradient-to-r from-green-500 to-emerald-500 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg className="w-10 h-10 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h2 className="text-3xl font-black text-white mb-3">Pedido Confirmado!</h2>
            <p className="text-gray-400 mb-6">Seu número de pedido é:</p>
            <div className="bg-gradient-to-r from-red-600 to-orange-500 rounded-xl p-6 mb-6">
              <div className="text-6xl font-black text-white">#{orderNumber}</div>
            </div>
            <p className="text-gray-300 mb-8 font-medium">
              Aguarde ser chamado para retirar seu pedido no balcão.
            </p>
            <button
              onClick={() => on_click()}
              className="w-full bg-gray-800 hover:bg-gray-700 text-white py-3 rounded-xl font-bold transition-colors"
            >
              Fazer Novo Pedido
            </button>
        </BasicModal>
    )
}