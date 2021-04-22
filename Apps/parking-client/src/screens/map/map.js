import React, { useState, useEffect } from 'react'


export default function Map(props) {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/events/", {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }
          })
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },

        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])


    return (
      <p>map</p>
    );

}
