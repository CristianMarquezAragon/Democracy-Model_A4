"""
Input JSON format (Matrix):
{
  "votes": [
    [a1, b1],
    [a2, b2],
    [a3, b3],
    ...
    [an, bn]
  ]
}

Example votes.json (3 votes):
{
  "votes": [
    [7, 30],
    [365, 1095],
    [2000, 2579]
  ]
}

Mathematical Formulas Used:
---------------------------
1. Weight by Conviction (w_i):
   w_i = 1 - ((b_i - a_i) / 2572)

2. Initial Center of Gravity (T0):
   T0 = sum(w_i * m_i) / sum(w_i)  where m_i = (a_i + b_i) / 2

3. Continuous Dispersion Index (S):
   S = min(1.0, sqrt(sum(w_i * (m_i - T0)^2) / sum(w_i)) / 1286)

4. Lower Group Anchor (T_low):
   T_low = sum(w_i * m_i) / sum(w_i)  for all m_i < T0

5. Gravitational Attraction Force (W):
   W = 0.6375 * (S^2)

6. Final Term Result (T):
   T = (1 - W) * T0 + W * T_low
"""

import json
import math
import sys
import os

D_MIN = 7
D_MAX = 2579
RANGE = 2572
HALF_RANGE = 1286
W_MAX = 0.6375


def format_human_time(days: float) -> str:
    total_days = round(days)
    if total_days <= 0:
        return "0 days"
    
    years = total_days // 365
    rem = total_days % 365
    months = rem // 30
    d = rem % 30
    
    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months > 1 else ''}")
    if d > 0:
        parts.append(f"{d} day{'s' if d > 1 else ''}")
        
    return ", ".join(parts) if parts else "0 days"


def calculate_trs(json_data):
    if isinstance(json_data, dict):
        raw_votes = json_data.get("votes", [])
    elif isinstance(json_data, list):
        raw_votes = json_data
    else:
        raise ValueError("Invalid format. Expected list or dict with 'votes'.")

    if not raw_votes:
        raise ValueError("The 'votes' list is empty. Add at least one vote pair like [7, 30].")

    processed = []
    for v in raw_votes:
        a = max(D_MIN, min(D_MAX, float(v[0])))
        b = max(D_MIN, min(D_MAX, float(v[1])))
        if a > b:
            a, b = b, a
            
        m_i = (a + b) / 2.0
        w_i = 1.0 - ((b - a) / RANGE)
        processed.append({"m": m_i, "w": w_i})

    sum_w = sum(p["w"] for p in processed)
    T0 = sum(p["w"] * p["m"] for p in processed) / sum_w if sum_w > 0 else 1293.0

    variance = sum(p["w"] * ((p["m"] - T0) ** 2) for p in processed) / sum_w if sum_w > 0 else 0.0
    sigma = math.sqrt(variance)
    S = min(1.0, sigma / HALF_RANGE)

    low_group = [p for p in processed if p["m"] < T0]
    sum_w_low = sum(p["w"] for p in low_group)
    T_low = sum(p["w"] * p["m"] for p in low_group) / sum_w_low if sum_w_low > 0 else T0

    W = W_MAX * (S ** 2)
    T = (1.0 - W) * T0 + W * T_low

    return {
        "result_days": round(T, 2),
        "result_formatted": format_human_time(T),
        "metrics": {
            "T0_mean_days": round(T0, 2),
            "T_low_anchor_days": round(T_low, 2),
            "dispersion_S": round(S, 4),
            "attraction_W_percent": round(W * 100, 2)
        }
    }


def main():
    if len(sys.argv) > 1:
        json_path = sys.argv[1]
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, "votes.json")

    if not os.path.exists(json_path):
        print(f"Error: File '{json_path}' was not found.")
        print("Please make sure 'votes.json' exists in the same folder as results.py.")
        return

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON formatting in '{json_path}'.")
        print(f"Details: {e}")
        return

    try:
        result = calculate_trs(data)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Calculation Error: {e}")


if __name__ == "__main__":
    main()