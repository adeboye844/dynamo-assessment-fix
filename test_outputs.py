import json
from pathlib import Path

def get_ground_truth():
    """Computes exact values from the log to avoid hardcoding ground truth."""
    log_path = Path("/app/access.log")
    if not log_path.exists():
        return 0, 0, ""
    
    ips = set()
    path_counts = {}
    total = 0
    
    with open(log_path, 'r') as f:
        for line in f:
            if not line.strip(): continue
            total += 1
            parts = line.split()
            if len(parts) > 6:
                ip = parts[0]
                req_path = parts[6]
                ips.add(ip)
                path_counts[req_path] = path_counts.get(req_path, 0) + 1
    
    top_path = max(path_counts.items(), key=lambda x: x[1])[0] if path_counts else ""
    return total, len(ips), top_path

def test_1_total_requests():
    """1. `total_requests`: The total number of request lines in the log."""
    data = json.loads(Path("/app/report.json").read_text())
    expected_total, _, _ = get_ground_truth()
    assert data.get("total_requests") == expected_total, "total_requests value is incorrect or missing"

def test_2_unique_ips():
    """2. `unique_ips`: The number of unique client IP addresses."""
    data = json.loads(Path("/app/report.json").read_text())
    _, expected_ips, _ = get_ground_truth()
    assert data.get("unique_ips") == expected_ips, "unique_ips value is incorrect or missing"

def test_3_top_path():
    """3. `top_path`: The most frequently requested path (string)."""
    data = json.loads(Path("/app/report.json").read_text())
    _, _, expected_top = get_ground_truth()
    assert data.get("top_path") == expected_top, "top_path value is incorrect or missing"