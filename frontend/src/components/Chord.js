import React from "react";
import useFetch from "../hooks/useFetch";

const Chord = () => {
  const { degrees, isPending, error } = useFetch(
    "http://localhost:5000/chords/C/degrees"
  );

  return (
    <div className="home">
      {error && <div>{error}</div>}
      {isPending && <div>Loading...</div>}
      {degrees && <div>{degrees}</div>}
    </div>
  );
};

export default Chord;
