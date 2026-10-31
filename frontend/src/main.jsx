import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";
import './index.css'
import App from './App.jsx'
import Login from './pages/Login.jsx';
import Registration from './pages/Registration.jsx';
import PageNotFound from './pages/PageNotFound.jsx';
import Chat from './pages/Chat.jsx';

createRoot(root).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />}/>
        <Route path="/register" element={<Registration />} />
        <Route path="/chat" element={<Chat />}/>
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);