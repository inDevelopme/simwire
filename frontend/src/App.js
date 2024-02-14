// Importing modules
import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';
import Navbar from "./navbar";
import './styles.css'
import Pricing from "./pages/pricing";
import About from "./pages/about";
import Home from "./pages/home";
import {Route,Routes} from "react-router-dom"
import LoginForm from "./pages/login";
import Desktop from "./pages/desktop";
function App() {
    return (
        <>
            <Navbar />
            <div className="container">
                <Routes>
                    <Route path="/" element={<Home/>} />
                    <Route path="/pricing" element={<Pricing/>} />
                    <Route path="/about" element={<About/>} />
                    <Route path="/login" element={<LoginForm/>} />
                    <Route path="/desktop" element={<Desktop/>} />
                </Routes>
            </div>
        </>
    )
}

export default App;
