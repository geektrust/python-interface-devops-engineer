from datetime import datetime, timezone, timedelta
from typing import Iterable, List, Dict, Any
from collections import defaultdict

class Main:
    #
    # ---------------------------------------------------------------------------
    # Implement your solution here
    #
    # ---------------------------------------------------------------------------
    def aggregate_health_checks(self, health_checks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Aggregate health check results per service and determine service
        status.
        Args:
        health_checks: List of health check dictionaries with keys:
        service_name, instance_id, timestamp, status,
        response_time_ms
        Returns:
        List of service health summaries sorted by status priority and
        availability
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Implement aggregate_health_checks")
 