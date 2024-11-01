import { useState } from 'react'
import axios from "axios";
import './App.css'

function App() {
    const [imageUrl, setImageUrl] = useState("");

    const fetchImage = async () => {
        try {
            const response = await axios.get("http://localhost:8000/get_image/", {
                params: { start_date: "2023-01-01", end_date: "2023-12-31" }
            });
            setImageUrl(response.data.image_url);
        } catch (error) {
            console.error("Error fetching image:", error);
        }
    };

  return (
    <>
      <h1>GEE Image Test</h1>
      <div className="card">
        <div>
            {imageUrl && <img src={imageUrl} alt="GEE Image" />}
        </div>
        <button onClick={fetchImage}>
           Fetch GEE Image
        </button>
      </div>
    </>
  )
}

export default App
