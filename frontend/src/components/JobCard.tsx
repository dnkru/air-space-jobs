export default function JobCard({ job, onSelect }: { job: Job; onSelect: (j: Job) => void }) {
  return (
    <div
      className="bg-gray-800 border border-gray-700 p-4 rounded-xl shadow-lg cursor-pointer hover:border-blue-500 hover:shadow-blue-500/30 transition-all"
      onClick={() => onSelect(job)}
    >
      <h2 className="text-lg font-semibold text-blue-300">{job.title}</h2>
      <p className="text-xs text-gray-400 uppercase tracking-wide mb-2">{job.service}</p>
      <p className="text-gray-300 text-sm line-clamp-3">{job.summary}</p>
    </div>
  );
}
