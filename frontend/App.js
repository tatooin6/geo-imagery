import React, { useState } from "react";
import axios from "axios";

function App() {
    const [imageUrl, setImageUrl] = useState("");

    const fetchImage = async () => {
        try {
            const response = await axios.get("http://localhost:8000/get_image/", {
                params: { start_date: "2022-01-01", end_date: "2022-02-01" }
            });
            setImageUrl(response.data.image_url);
        } catch (error) {
            console.error("Error fetching image:", error);
        }
    };

    return (
        <div className="App">
            <button onClick={fetchImage}>Fetch Image from GEE</button>
            {imageUrl && <img src={imageUrl} alt="GEE Image" />}
        </div>
    );
}

export default App;
