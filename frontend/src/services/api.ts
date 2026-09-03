import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
})

export async function getAnalyses() {
  const res = await api.get('/analyses')
  return res.data
}

export async function getAnalysis(id: string) {
  const res = await api.get(`/analyses/${id}`)
  return res.data
}

export async function uploadResume(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  const res = await api.post('/analyze', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return res.data
}
