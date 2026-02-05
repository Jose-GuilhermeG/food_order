import { Route , Routes } from "react-router-dom";

//pages
import Home from "./pages/Home";
import Err404 from "./pages/errors/404";
import PublicView from "./pages/publicView";

export default function MainRoutes(){
    return (
        <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/public/" element={<PublicView/>} />
            <Route path="*" element={<Err404/>} />
        </Routes>
    )
}