import { useState, useEffect } from "react";

const useFetch = (url) => {
  const [data, setData] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setTimeout(() => {
      fetch(url, {
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
            setError(json.error);
          } else {
            setData(json);
          }
          setIsPending(false);
        })
        .catch((err) => {
          console.log("Fetch error: " + err);
          setIsPending(false);
        });
    }, 1000);

    return () => console.log("cleanup");
  }, [url]);

  return { data, isPending, error };
};

export default useFetch;
