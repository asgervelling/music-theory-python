import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [degrees, setDegrees] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/chords/Cadd9/degrees", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((res) => {
        return res.json();
      })
      .then((json) => {
        if ("error" in json) {
          console.log("Error: " + json.error);
        } else {
          console.log("Degrees: " + json);
          setDegrees(json);
        }
      })
      .catch((err) => {
        console.log("Fetch error: " + err);
      });
  }, []);

  return (
    <div className="App">
      {degrees}
      {error}
    </div>
  );
}

export default App;
