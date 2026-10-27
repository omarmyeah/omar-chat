import { useState } from 'react'
import Index from './pages/Index'
import Login from './pages/Login'
import Registration from './pages/Registration'
import PageNotFound from './pages/PageNotFound'
import { BrowserRouter, Routes, Route } from "react-router";

export default function App() {
  return (
    <Index />
  );
}