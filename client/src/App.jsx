import './App.css'
import { Routes, Route, Navigate } from 'react-router-dom';

import Home from "./pages/home.jsx"
import Projects from "./pages/projects.jsx"
import Resume from "./pages/resume.jsx"
import NoPage from './pages/nopage.jsx';

import Software from './pages/projectspages/software.jsx';
import Other from './pages/projectspages/other.jsx';

import Navbar from './navbar.jsx';

function App() {
  return (
    <>
      <div id="page">
        <Navbar/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/projects" element={<Navigate to="/projects/home" />}/>
          <Route path="/projects/home" element={<Projects/>}/>
          <Route path="/projects/software" element={<Software/>}/>
          <Route path="/projects/other" element={<Other/>}/>
          <Route path="/resume" element={<Resume/>}/>
          <Route path="/*" element={<NoPage/>}/>
        </Routes>
      </div>
      <div id="footer">
        <p>Designed and Developed by: Bernico Jansen Chandra</p>
      </div>
    </>
  )
}

export default App
