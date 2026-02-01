import { Search } from "lucide-react"

export default function SimpleSearchInput({set_search_value,searchvalue = undefined,...props}){
    return (
        <div className="bg-gradient-to-r from-gray-800 to-gray-900 rounded-2xl p-6 shadow-2xl border border-red-900/20 mb-8" {...props}>
          <div className="relative">
            <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input
              type="text"
              placeholder="Buscar refeições, ingredientes..."
              value={searchvalue}
              onChange={(e) => set_search_value(e.target.value)}
              className="w-full bg-black/50 text-white placeholder-gray-400 pl-12 pr-4 py-4 rounded-xl border border-gray-700 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/50 transition-all font-medium"
            />
          </div>
        </div>
    )
}