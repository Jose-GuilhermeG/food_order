export default function CategoryCard({ category_name , category_slug , category_icon , set_category , is_selected = false , ...props}){
    return (
       <button
              className={` mx-2 flex-shrink-0 px-6 py-3 rounded-xl font-bold text-sm transition-all cursor-pointer ${
                is_selected ? 'bg-gradient-to-r from-red-600 to-orange-500 text-white shadow-lg shadow-red-500/50 scale-105' : 'bg-gray-800 text-gray-300 hover:bg-gray-700 border border-gray-700'
              }`}
              {...props}
              onClick={()=>set_category(category_slug)}
            >
              <span className="mr-2">{category_icon}</span>
              {category_name}
        </button>
    )
}