export default function Banner({ content , br_content , description}){
    return (
      <div className="relative overflow-hidden bg-orange-gradient py-16">
        <div className="absolute inset-0 opacity-30"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-5xl sm:text-6xl font-black text-white mb-4 leading-tight">
            {content}.<br /> {br_content}
          </h2>
          <p className="text-xl text-white/90 font-medium max-w-2xl mx-auto">
            {description}
          </p>
        </div>
      </div>
    )
}