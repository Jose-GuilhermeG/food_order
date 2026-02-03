import CategoryCard from "./CategoryCard";

export default function CategoryGalery({categories , set_category , selected_category , ...props}){

    if(! categories.length) return (
        <div></div>
    )

    return (
        <div 
            className="w-full min-h-[5vh] flex justify-start items-center"
            {...props}
        >
            {categories.map((category , index)=><CategoryCard category_name={category.name} set_category={set_category} category_slug={category.slug} category_icon={category.icon} key={index} is_selected={category.slug == selected_category} />)}
        </div>
    )
}