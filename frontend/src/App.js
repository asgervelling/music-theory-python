import "./App.css";
import useFetch from "./hooks/useFetch";

function App() {
  const { degrees, isPending, error } = useFetch(
    "http://localhost:5000/chords/Am7b5/degrees"
  );
  return (
    <div className="App">
      {error && "error"}

      {error && <div>{error}</div>}
      {isPending && <div>Loading...</div>}
      {degrees && <div>{degrees}</div>}
    </div>
  );
}

export default App;
