//imports
import React, { useState, useEffect } from 'react';
import { Search, ShoppingCart, Clock, Flame, ChefHat, X, Plus, Minus } from 'lucide-react';

//components
import FoodGalary from '../../features/food/FoodGalery';
import Banner from '../../components/banner/Banner';
import CategoryGalery from '../../features/catgory/CategoryGalery';
import FloatButton from '../../components/float_button/FloatButton';
import RightSideBar from '../../components/side_bar/RightSideBar';
import SimpleSearchInput from '../../components/inputs/SearchInput';
import BasicModal from '../../components/modal/BasicModal';

export default function FoodDeliveryHome() {
  const [products, setProducts] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [orders, setOrders] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [isSideBarOpen, setSideBarOpen] = useState(false);
  const [orderNumber, setOrderNumber] = useState(null);

  useEffect(() => {
        const mockProducts = [
      {
        id: 1,
        name: 'Hambúrguer Artesanal',
        description: 'Blend premium com queijo cheddar, bacon e molho especial',
        price: 28.90,
        category: 'burgers',
        image: 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop',
        prepTime: '15-20 min'
      },
      {
        id: 2,
        name: 'Pizza Margherita',
        description: 'Molho de tomate, mussarela de búfala e manjericão fresco',
        price: 42.00,
        category: 'pizzas',
        image: 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&h=300&fit=crop',
        prepTime: '20-25 min'
      },
      {
        id: 3,
        name: 'Yakissoba Especial',
        description: 'Macarrão oriental com legumes, carne e molho shoyu',
        price: 32.00,
        category: 'asian',
        image: 'https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=400&h=300&fit=crop',
        prepTime: '15-20 min'
      },
      {
        id: 4,
        name: 'Salada Caesar',
        description: 'Alface americana, croutons, parmesão e molho caesar',
        price: 24.00,
        category: 'salads',
        image: 'https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400&h=300&fit=crop',
        prepTime: '10-15 min'
      },
      {
        id: 5,
        name: 'Frango Grelhado',
        description: 'Peito de frango grelhado com arroz integral e legumes',
        price: 29.90,
        category: 'healthy',
        image: 'https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=400&h=300&fit=crop',
        prepTime: '20-25 min'
      },
      {
        id: 6,
        name: 'Tacos Mexicanos',
        description: 'Tortillas com carne moída, guacamole e pico de gallo',
        price: 26.00,
        category: 'mexican',
        image: 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=400&h=300&fit=crop',
        prepTime: '15-20 min'
      }
    ];
    setProducts(mockProducts);

  }, []);

  const categories = [
    { id: 'all', name: 'Todos', icon: '🍽️' },
    { id: 'burgers', name: 'Hambúrgueres', icon: '🍔' },
    { id: 'pizzas', name: 'Pizzas', icon: '🍕' },
    { id: 'asian', name: 'Oriental', icon: '🍜' },
    { id: 'salads', name: 'Saladas', icon: '🥗' },
    { id: 'healthy', name: 'Saudável', icon: '🥙' },
    { id: 'mexican', name: 'Mexicana', icon: '🌮' }
  ];

  const filteredProducts = products.filter(product => {
    const matchesSearch = product.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         product.description.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategory = selectedCategory === 'all' || product.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

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

   const handleCheckout = () => {
    const number = Math.floor(1000 + Math.random() * 9000);
    setOrderNumber(number);
    setOrders([]);
    setSideBarOpen(false)
  };


  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900">

      <Banner content='Peça Agora' br_content='Retire Rápido.' description='Escolha suas refeições favoritas, pague online e retire no balcão. Simples assim.' />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 relative z-10">
          <SimpleSearchInput searchvalue={searchQuery} set_search_value={setSearchQuery}/>
        <div className="flex overflow-x-auto gap-3 pb-6 mb-8 scrollbar-hide">
          <CategoryGalery categories={categories}/>
        </div>

       <FoodGalary products={filteredProducts} add_event={addToCart} />
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
                            src={item.image}
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
        <BasicModal>
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
              onClick={() => setOrderNumber(null)}
              className="w-full bg-gray-800 hover:bg-gray-700 text-white py-3 rounded-xl font-bold transition-colors"
            >
              Fazer Novo Pedido
            </button>
        </BasicModal>
      )}


      <FloatButton style={{"right" : '5%'  , "bottom" : '5%' , "backgroundColor" : "#101828"}} on_click={()=>setSideBarOpen(true)}>
        <ShoppingCart className="w-6 h-6 text-white" strokeWidth={2} />
      </FloatButton>
    </div>
  );
}