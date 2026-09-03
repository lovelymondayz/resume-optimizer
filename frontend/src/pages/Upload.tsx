export default function Upload() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Upload Resume</h1>
      <div className="bg-white rounded-lg shadow p-6">
        <form className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Resume File</label>
            <input type="file" className="mt-1 block w-full" accept=".pdf,.doc,.docx" />
          </div>
          <button type="submit" className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700">
            Upload & Analyze
          </button>
        </form>
      </div>
    </div>
  )
}
