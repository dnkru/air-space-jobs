<div className="fixed inset-0 bg-black/80 flex justify-center items-center z-50">
  <div className="bg-gray-900 p-6 rounded-2xl shadow-2xl max-w-lg w-full relative border border-gray-700">
    <button className="absolute top-3 right-3 p-2 bg-gray-800 rounded-full hover:bg-gray-700" onClick={onClose}>
      <X className="w-5 h-5 text-gray-300" />
    </button>
    <h2 className="text-2xl font-bold mb-2 text-blue-300">{job.title}</h2>
    {job.code && <p className="text-sm text-gray-400">AFSC: {job.code}</p>}
    <p className="text-gray-200 mb-4">{job.summary}</p>
    {job.mapped_title && (
      <p className="text-sm text-indigo-400">
        Space Force Equivalent: {job.mapped_title}
      </p>
    )}
    {job.url && (
      <a
        href={job.url}
        target="_blank"
        rel="noreferrer"
        className="inline-block mt-4 px-5 py-2 bg-blue-600 text-white rounded-xl font-semibold tracking-wide hover:bg-blue-700 transition"
      >
        View Official Page
      </a>
    )}
  </div>
</div>
