# Grade System

A simple Python application for managing student scores and calculating averages and letter grades.

## Quick start

```bash
cd /workspaces/Python_Concepts/grade-system
source venv/bin/activate
python main.py
```

On Windows, activate the virtual environment with:

```powershell
venv\Scripts\activate
python main.py
```

## Features

- Add students with optional initial scores
- Add individual scores for a student
- Calculate an average grade
- Convert averages to letter grades
- Rank students by average score
- View a single student's report

## Example usage

```python
from grade_system import GradeSystem

system = GradeSystem()
system.add_student("Ava", [90, 85, 95])
system.add_student("Noah", [80, 70, 75])

print(system.top_student())
print(system.student_report("Ava"))
```
