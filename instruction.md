Read the Apache access log located at `/app/access.log` and generate a JSON summary report at `/app/report.json`.

Your report must contain exactly these three keys:
1. `total_requests`: The total number of request lines in the log.
2. `unique_ips`: The number of unique client IP addresses.
3. `top_path`: The most frequently requested path (string).

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.