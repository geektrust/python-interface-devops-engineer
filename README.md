This is the starter kit for the problem statement defined for interface.ai's Devops role

## Problem Statement

### Service Health Check Aggregator

Your team manages a microservices platform with hundreds of services. Each service has health check endpoints that are polled regularly. You need to aggregate these health check results to determine the overall status of each service.

Each health check result has the following fields:
```
{
    "service_name": str,
    "instance_id": str, # Multiple instances per service
    "timestamp": str, # ISO-8601 UTC, e.g. "2025-01-01T10:03:21Z"
    "status": str, # "healthy", "unhealthy", or "timeout"
    "response_time_ms": int, # Response time in milliseconds (0 if timeout)
}
```

#### Requirements:

1. Aggregate health checks per service within a time window.
2. For each service, compute:

- service_name: str
- total_checks: total number of health checks
- healthy_checks: number of checks with status "healthy"
- unhealthy_checks: number of checks with status "unhealthy"
- timeout_checks: number of checks with status "timeout"
- availability_percent: (healthy_checks / total_checks) * 100, rounded to 2 decimals
- avg_response_time_ms: average response time of healthy checks only (0.0 if none)
- active_instances: number of unique instance_ids seen
- service_status: determined by availability_percent:
    - "healthy" if availability_percent >= 99.0
    - "degraded" if availability_percent >= 95.0 and < 99.0
    - "unhealthy" if availability_percent < 95.0

3. Return a list of dictionaries with exactly these keys:
    ```
    {
        "service_name": str,
        "total_checks": int,
        "healthy_checks": int,
        "unhealthy_checks": int,
        "timeout_checks": int,
        "availability_percent": float,
        "avg_response_time_ms": float,
        "active_instances": int,
        "service_status": str,
    }
    ```

4. Sort output by: service_status priority (unhealthy first, then degraded, then healthy), then by availability_percent ascending (worst first within same status).

#### Assumptions:
- timestamp is always valid in format "%Y-%m-%dT%H:%M:%SZ"
- status is always one of: "healthy", "unhealthy", "timeout"
- response_time_ms is always a non-negative integer

#### How to execute 

```
./run.sh "[{\"service_name\": \"api-gateway\", \"instance_id\": \"i-001\", \"timestamp\": \"2025-01-01T10:00:00Z\", \"status\": \"healthy\", \"response_time_ms\": 45}, {\"service_name\": \"api-gateway\", \"instance_id\": \"i-001\", \"timestamp\": \"2025-01-01T10:01:00Z\", \"status\": \"healthy\", \"response_time_ms\": 52}, {\"service_name\": \"api-gateway\", \"instance_id\": \"i-002\", \"timestamp\": \"2025-01-01T10:00:00Z\", \"status\": \"healthy\", \"response_time_ms\": 38}, {\"service_name\": \"api-gateway\", \"instance_id\": \"i-002\", \"timestamp\": \"2025-01-01T10:01:00Z\", \"status\": \"unhealthy\", \"response_time_ms\": 0}, {\"service_name\": \"user-service\", \"instance_id\": \"i-010\", \"timestamp\": \"2025-01-01T10:00:00Z\", \"status\": \"healthy\", \"response_time_ms\": 120}, {\"service_name\": \"user-service\", \"instance_id\": \"i-010\", \"timestamp\": \"2025-01-01T10:01:00Z\", \"status\": \"healthy\", \"response_time_ms\": 115}]"
```