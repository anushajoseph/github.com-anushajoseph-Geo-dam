import { Routes } from "react-router-dom";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Route } from "react-router-dom";
import Home from "./pages/Home";
import ChangeDetection from "./pages/ChangeDetection";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route index path="/" element={<Home />} />
        <Route index path="/changedetection" element={<ChangeDetection />} />
      </Routes>
    </div>
  );
}

export default App;