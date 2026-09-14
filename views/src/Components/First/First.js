import React, { useState } from "react"
import styles from "./First.module.scss"

const First = () => {
    const [text, setText] = useState("");
    const [result, setResult] = useState("");

    const handleTranslate = async () => {
        const response = await fetch("http://localhost:5000/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            q: text, 
            source: "en",
            target: "ru",  
            format: "text"
        })
        });
        const data = await response.json();
        setResult(data.translatedText);
    };

    return (
        <div>
        <input value={text} onChange={e => setText(e.target.value)} />
        <button onClick={handleTranslate}>Translate</button>
        <p>{result}</p>
        </div>
    );
}

export default First;
