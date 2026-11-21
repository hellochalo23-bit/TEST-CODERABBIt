"""Independent benign behavior oracles; Python standard library + Node24 only."""
from pathlib import Path
import asyncio
import json
import sqlite3
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "python_service"))

def check(case):
    if case == "concurrency":
        import reservations
        async def exercise():
            reservations.reset()
            await asyncio.gather(*(reservations.reserve_seat() for _ in range(100)))
        asyncio.run(exercise())
        return dict(case=case,passed=reservations.reservations == 100,observed=reservations.reservations,expected=100)
    elif case == "auth":
        result=subprocess.run(["node", str(ROOT / "checks/auth.ts")],capture_output=True,text=True)
        data=json.loads(result.stdout)
        assert result.returncode == (0 if data['passed'] else 1),result.stderr
        return data
    elif case == "resource":
        import reports
        try:
            reports.render_report("SELECT * FROM missing_table")
        except sqlite3.OperationalError:
            pass
        else:
            raise AssertionError("The invalid SQL control did not fail")
        try:
            rows=reports.render_report("SELECT 1")
        except RuntimeError as error:
            if str(error) != "POOL_EXHAUSTED after failed report":raise
            return dict(case=case,passed=False,query_error='OperationalError',pool_exhausted=True)
        assert rows == [(1,)]
        return dict(case=case,passed=True,query_error='OperationalError',pool_exhausted=False)
    elif case == "security":
        import search
        assert search.find_user("alice") == [("alice",)]
        rows = search.find_user("' OR '1'='1")
        return dict(case=case,passed=rows == [],observed_rows=rows)
    elif case == "clean":
        import formatting
        assert [formatting.invoice_label(i) for i in (0, 1, 1500, 90000)] == ["inv-0000", "inv-0001", "inv-1500", "inv-90000"]
        for value in (True,False,-1,0,999999):
            assert formatting.invoice_label(value) == f"inv-{value:04d}"
        for value in (None,"invalid",1.5):
            try:
                format(value,"04d")
            except (TypeError,ValueError) as reference_error:
                try:formatting.invoice_label(value)
                except Exception as actual_error:assert type(actual_error) is type(reference_error)
                else:raise AssertionError("Invalid input behavior changed")
        subprocess.run(["node", str(ROOT / "checks/formatting.ts")], check=True,capture_output=True)
        return dict(case=case,passed=True,boolean_negative_invalid_controls=True)
    else:
        raise ValueError(case)

if __name__ == "__main__":
    case = sys.argv[1] if len(sys.argv) > 1 else "all"
    if case == "all":
        for name in ("clean", "concurrency", "auth", "resource", "security"):
            subprocess.run([sys.executable, __file__, name], check=True)
    else:
        result=check(case)
        print(json.dumps(result))
        raise SystemExit(0 if result['passed'] else 1)
