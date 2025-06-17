import logo from "./logo.svg";
import "./App.css";
//import AppHeader from "./components/AppHeader";
import Cricket from "./components/App";

function App() {
  return (
    <div>
      <Cricket target={200} totalOvers={10} />
      <br></br>
    </div>
  );
}

export default App;
