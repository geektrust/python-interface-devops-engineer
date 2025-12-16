import sys
import json
from main import Main
from typing import Iterable, Dict, Any, List


def call_main():
    """
        ***********************************************
        * This is the driver code. Don't change it!!!
        * *********************************************

        Format of the 'args' array: `<Input 1> <Input 2> <Input 3>`
        Example: ["Input1 Input2 Input3"]

        The code evaluator will execute this code by using the command:
        python main.py "Input1 Input2 Input3"

        So the value of the variable 'input' given below will be the string: "Input1 Input2 Input3"
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    commands = sys.argv[1:]
    main = Main()

    for command in commands:
        data = convert_input(command)
        output = main.aggregate_health_checks(data)
        sorted_output = _sort_results(_normalize(output))
        s = json.dumps(sorted_output, default=lambda x: x.isoformat())
        print(s)


def _normalize(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Normalize records for comparison: round floats."""
    normalized = []
    for r in records:
        norm_record = {}
        for k, v in r.items():
            if isinstance(v, float):
                norm_record[k] = round(v, 2)
            else:
                norm_record[k] = v
        normalized.append(norm_record)
    return normalized

def _status_priority(status: str) -> int:
    """Return sort priority for service status (lower = higher priority)."""
    return {"unhealthy": 0, "degraded": 1, "healthy": 2}.get(status, 3)

def _sort_results(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sort by status priority, then availability ascending."""
    return sorted(records, key=lambda x: (_status_priority(x["service_status"]), x["availability_percent"]))

def convert_input(input_str: str):
    result: Iterable[Dict[str, Any]] = json.loads(input_str)
    return result

if __name__ == "__main__":
    call_main()
