import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";
import './index.css'
import Login from './pages/Login.jsx';
import Registration from './pages/Registration.jsx';
import PageNotFound from './pages/PageNotFound.jsx';
import Chat from './pages/Chat.jsx';
import Index from './pages/Index.jsx';
import NavbarBgFooter from './layouts/NavbarBgFooter.jsx';
import NavbarWithBg from './layouts/NavbarWithBg.jsx';

createRoot(root).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<NavbarBgFooter navbarClickableItems={
          [
            {
              name: 'Login',
              path: '/login'
            },
            {
              name: 'Register',
              path: '/register'
            }
          ]
        } />}>
          <Route path="/" element={<Index />} />
        </Route>
        <Route element={<NavbarWithBg />}>
          <Route path="/login" element={<Login />}/>
          <Route path="/register" element={<Registration />} />
          <Route path="/chat" element={<Chat />}/>
        </Route>
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);