import json
from pathlib import Path

log_path = Path("/app/access.log")
ips = set()
path_counts = {}
total = 0

if log_path.exists():
    with open(log_path, 'r') as f:
        for line in f:
            if not line.strip(): continue
            total += 1
            parts = line.split()
            if len(parts) > 6:
                ips.add(parts[0])
                req_path = parts[6]
                path_counts[req_path] = path_counts.get(req_path, 0) + 1

top_path = max(path_counts.items(), key=lambda x: x[1])[0] if path_counts else ""

Path("/app/report.json").write_text(json.dumps({
    "total_requests": total,
    "unique_ips": len(ips),
    "top_path": top_path
}))