import CategoryCard from "./CategoryCard";

export default function CategoryGalery({categories , ...props}){

    if(! categories.length) return (
        <div></div>
    )

    return (
        <div 
            className="w-full min-h-[5vh] flex justify-start items-center"
            {...props}
        >
            {categories.map((category , index)=><CategoryCard category_name={category.name} category_icon={category.icon} key={index} />)}
        </div>
    )
}