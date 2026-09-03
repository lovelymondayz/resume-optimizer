import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Analyses from './pages/Analyses'
import Upload from './pages/Upload'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout><Analyses /></Layout>} />
        <Route path="/upload" element={<Layout><Upload /></Layout>} />
      </Routes>
    </BrowserRouter>
  )
}
