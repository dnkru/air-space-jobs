<div className="min-h-screen bg-gradient-to-b from-gray-900 via-black to-blue-900 text-white font-sans">
  <div className="max-w-6xl mx-auto p-6">
    <header className="text-center mb-8">
      <img src="/emblem.png" alt="Logo" className="mx-auto h-16 mb-3 drop-shadow-lg" />
      <h1 className="text-4xl font-extrabold tracking-wide text-blue-300 uppercase">
        Air & Space Force Enlisted Jobs
      </h1>
      <p className="text-gray-400 mt-2 text-sm">Explore your path. Serve with honor.</p>
    </header>

    <input
      type="text"
      placeholder="Search by title, code, or description..."
      value={search}
      onChange={e => setSearch(e.target.value)}
      className="w-full p-3 rounded-xl bg-gray-800 border border-gray-700 text-white placeholder-gray-400 mb-6 focus:ring-2 focus:ring-blue-500"
    />

    <div className="grid md:grid-cols-3 gap-4">
      {filtered.map(job => (
        <JobCard key={job.title + job.service} job={job} onSelect={setSelected} />
      ))}
    </div>

    {selected && <JobDetail job={selected} onClose={() => setSelected(null)} />}
  </div>
</div>
