import React from "react";
import ReactDOM from "react-dom/client"; // Use ReactDOM from "react-dom/client" in modern React projects
import App from "./App"; // Import the App component
import "./index.css"; // Include your styles

const root = ReactDOM.createRoot(document.getElementById("root")); // React 18 syntax
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
