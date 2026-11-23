import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";
import './index.css'
import Login from './pages/Login.jsx';
import Registration from './pages/Registration.jsx';
import PageNotFound from './pages/PageNotFound.jsx';
import Chat from './pages/Chat.jsx';
import Index from './pages/Index.jsx';
import Layout from './layouts/Layout.jsx';

createRoot(root).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<Layout footer={true} navbarClickableItems={
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

        <Route element={<Layout footer={false} />}>
          <Route path="/login" element={<Login />}/>
          <Route path="/register" element={<Registration />} />
          <Route path="/chat/:id?" element={<Chat />}/>
          <Route path="*" element={<PageNotFound />} />
        </Route>

      </Routes>
    </BrowserRouter>
  </StrictMode>,
);