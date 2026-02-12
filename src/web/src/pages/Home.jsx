//imports
import { useState, useEffect } from 'react';
import {ShoppingCart, Plus, Minus, X } from 'lucide-react';

//components
import FoodGalary from '../features/food/FoodGalery';
import Banner from '../components/banner/Banner';
import CategoryGalery from '../features/catgory/CategoryGalery';
import FloatButton from '../components/float_button/FloatButton';
import RightSideBar from '../components/side_bar/RightSideBar';
import SimpleSearchInput from '../components/inputs/SearchInput';
import FoodDetail from '../features/food/foodDetail';
import Loader from '../components/loader/Loader';
import ConfirmOrderModal from '../features/modal/ConfirmOrderMoodal';
import GetClientNameModal from '../features/modal/GetClientNameModal';
import ErrModal from '../features/modal/ErrModal';

//services
import { get_all_categories } from '../services/categories_service';
import { register_order } from '../services/order_services';
import { get_food_by_category, search_food } from '../services/food_services';


export default function Home() {
  const [products, setProducts] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [orders, setOrders] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('todos');
  const [isSideBarOpen, setSideBarOpen] = useState(false);
  const [orderNumber, setOrderNumber] = useState(null);
  const [productDetail , setProductDetail] = useState()
  const [openProductDetailModal , setOpenProductDetailModal] = useState(false)
  const [categories , setCategories] = useState([])
  const [clientName , setClientName] = useState()
  const [isFoodReqLoading , setIsFoodReqLoading] = useState(true)
  const [hasErr , setHasErr] = useState(false)

  useEffect(() => {
    const load = async ()=>{
      setIsFoodReqLoading(true)
    try{
      let foods = []
      const all_categories = await get_all_categories()
      setCategories(all_categories.data)

      if (!searchQuery){
        foods =  (await get_food_by_category(selectedCategory)).data.foods
      }
      
      if(searchQuery){
        foods = (await search_food(searchQuery)).data
      }
      setProducts(foods)
      setIsFoodReqLoading(false)
    }
    catch(e){
      console.error(e)
       setHasErr(true)
    }
  }
  load()
  }, [selectedCategory , searchQuery]);


  const addToCart = (product) => {
    const existingItem = orders.find(item => item.id === product.id);
    if (existingItem) {
      setOrders(orders.map(item =>
        item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item
      ));
    } else {
      setOrders([...orders, { ...product, quantity: 1 }]);
    }
  };

  const removeFromCart = (productId) => {
    const existingItem = orders.find(item => item.id === productId);
    if (existingItem.quantity === 1) {
      setOrders(orders.filter(item => item.id !== productId));
    } else {
      setOrders(orders.map(item =>
        item.id === productId ? { ...item, quantity: item.quantity - 1 } : item
      ));
    }
  };

  const totalPrice = orders.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  const totalItems = orders.reduce((sum, item) => sum + item.quantity, 0);

   const handleCheckout = async () => {
     const orders_post_data = []
     orders.forEach(element=>{
      orders_post_data.push({
        food_id : element.id,
        quantity : element.quantity,
        status : "Pendente"
      })
     })
    const postdata = {
      "client_name" : clientName,
      "orders" : orders_post_data
    }
    try{
      const respoonse = await (await register_order(postdata)).data
      setOrderNumber(respoonse.code)
      setOrders([])
    }catch(e){
      console.log(e)
      setHasErr(true)
    }
    setSideBarOpen(false)
  };

  const open_product_detail = (product)=>{
    setProductDetail(product.slug)
    setOpenProductDetailModal(true)
  }


  return (
    <div className="min-h-screen bg-black-gradient">

      <Banner content='Peça Agora' br_content='Retire Rápido.' description='Escolha suas refeições favoritas, pague online e retire no balcão. Simples assim.' />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 relative z-10">
          <SimpleSearchInput searchvalue={searchQuery} set_search_value={setSearchQuery}/>
        <div className="flex overflow-x-auto gap-3 pb-6 mb-8 scrollbar-hide">
          <CategoryGalery categories={categories} set_category={setSelectedCategory} selected_category={selectedCategory}/>
        </div>
      { isFoodReqLoading ? 
        <Loader/> :
        <FoodGalary products={products} add_event={addToCart} on_click={open_product_detail} />
      }
      </div>

       <RightSideBar set_open_state={setSideBarOpen} open_state={isSideBarOpen}>
          <div className="fixed right-0 top-0 h-full w-full max-w-md bg-gradient-to-br from-gray-900 to-black border-l border-red-900/20 z-50 overflow-y-auto shadow-2xl">
            <div className="sticky top-0 bg-black/80 backdrop-blur-xl border-b border-red-900/20 p-6 z-10">
              <div className="flex items-center justify-between mb-2">
                <h2 className="text-2xl font-black text-white">Seu Pedido</h2>
              </div>
              <p className="text-gray-400 text-sm">
                {totalItems} {totalItems === 1 ? 'item' : 'itens'} no carrinho
              </p>
            </div>

            <div className="p-6">
              {orders.length === 0 ? (
                <div className="text-center py-12">
                  <ShoppingCart className="w-16 h-16 text-gray-600 mx-auto mb-4" />
                  <p className="text-gray-400 font-medium">Seu carrinho está vazio</p>
                </div>
              ) : (
                <>
                  <div className="space-y-4 mb-6">
                    {orders.map((item) => (
                      <div
                        key={item.id}
                        className="bg-gray-800 rounded-xl p-4 border border-gray-700"
                      >
                        <div className="flex items-start space-x-4">
                          <img
                            src={item.photo_url}
                            alt={item.name}
                            className="w-20 h-20 rounded-lg object-cover"
                          />
                          <div className="flex-1">
                            <h3 className="text-white font-bold mb-1">{item.name}</h3>
                            <p className="text-red-500 font-black text-lg">
                              R$ {(item.price * item.quantity).toFixed(2)}
                            </p>
                          </div>
                        </div>

                        <div className="flex items-center justify-between mt-3 pt-3 border-t border-gray-700">
                          <div className="flex items-center space-x-3">
                            <button
                              onClick={() => removeFromCart(item.id)}
                              className="bg-gray-700 hover:bg-red-600 p-2 rounded-lg transition-colors"
                            >
                              <Minus className="w-4 h-4 text-white" strokeWidth={3} />
                            </button>
                            <span className="text-white font-bold text-lg w-8 text-center">
                              {item.quantity}
                            </span>
                            <button
                              onClick={() => addToCart(item)}
                              className="bg-gray-700 hover:bg-green-600 p-2 rounded-lg transition-colors"
                            >
                              <Plus className="w-4 h-4 text-white" strokeWidth={3} />
                            </button>
                          </div>
                          <button
                            onClick={() => setOrders(orders.filter(i => i.id !== item.id))}
                            className="text-red-400 hover:text-red-300 text-sm font-bold"
                          >
                            Remover
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>

                  <div className="bg-gradient-to-r from-gray-800 to-gray-900 rounded-xl p-6 border border-red-900/20 mb-6">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-gray-400 font-medium">Subtotal</span>
                      <span className="text-white font-bold">R$ {totalPrice.toFixed(2)}</span>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-gray-700">
                      <span className="text-white font-black text-lg">Total</span>
                      <span className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-orange-500">
                        R$ {totalPrice.toFixed(2)}
                      </span>
                    </div>
                  </div>

                  <button
                    onClick={handleCheckout}
                    className="w-full relative group/checkout"
                  >
                    <div className="absolute inset-0 bg-gradient-to-r from-red-600 to-orange-500 rounded-xl blur opacity-75 group-hover/checkout:opacity-100 transition-opacity"></div>
                    <div className="relative bg-gradient-to-r from-red-600 to-orange-500 text-white py-4 rounded-xl font-black text-lg hover:scale-105 transition-transform">
                      Finalizar Pedido
                    </div>
                  </button>
                </>
              )}
            </div>
          </div>
      </RightSideBar>

      {orderNumber && (
        <ConfirmOrderModal orderNumber={orderNumber} on_click={() => {
                setOrderNumber(null)
                setClientName(null)
          }} />
      )}

     {!clientName && <GetClientNameModal on_submit_envent={(e)=>setClientName(e.target.client_name.value)} />}


      <FloatButton style={{"right" : '5%'  , "bottom" : '5%' , "backgroundColor" : "#101828"}} on_click={()=>setSideBarOpen(true)}>
        {orders.length > 0 && 
          <div className='w-5 h-5 bg-orange-gradient absolute top-0 right-0 rounded-2xl animate-bounce'>
          </div>
        }
        <ShoppingCart className="w-6 h-6 text-white" strokeWidth={2} />
      </FloatButton>

      <FoodDetail state={openProductDetailModal} food_slug={productDetail} set_state={setOpenProductDetailModal} add_envent={addToCart} />
     {hasErr && <ErrModal/>}
    </div>
  );
}