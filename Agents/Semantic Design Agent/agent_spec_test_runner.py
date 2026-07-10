import difflib
from pathlib import Path

base = Path(r"c:\Git\PowerBIAgentTest\Agents\Semantic Design Agent")
spec_file = base / "Semantic Design Agent Runnable Spec.md"
example_dir = base / "Example Animal Flow Live Capacity"

outputs = [
    (example_dir / "OUTPUT 1 — DATA_MODEL_MATRIX_v1.0.md", example_dir / "OUTPUT 1 — DATA_MODEL_MATRIX_AGENT_RUN_v1.0.md"),
    (example_dir / "OUTPUT 2 — SEMANTIC_MODEL_SPEC_v1.0.md", example_dir / "OUTPUT 2 — SEMANTIC_MODEL_SPEC_AGENT_RUN_v1.0.md"),
    (example_dir / "OUTPUT 3 — MEASURE_CONTRACT_v1.0.md", example_dir / "OUTPUT 3 — MEASURE_CONTRACT_AGENT_RUN_v1.0.md"),
]

expected_spec_phrases = [
    "## Performance Considerations",
    "Optimize relationships for query performance",
    "Models use performance-aware design patterns",
    "Keys are simplified to numeric surrogate keys where possible",
]

results = []

print("RUNNING Semantic Design Agent Spec Test Runner")
print(f"Spec file: {spec_file}")
print(f"Example directory: {example_dir}")
print()

if not spec_file.exists():
    raise FileNotFoundError(f"Spec file not found: {spec_file}")

spec_text = spec_file.read_text(encoding="utf-8")
print("Checking spec performance guidance...")
for phrase in expected_spec_phrases:
    found = phrase in spec_text
    print(f" - {'OK' if found else 'MISSING'}: {phrase}")
    results.append((phrase, found))

print()
print("Checking output files...")
for expected, generated in outputs:
    status = "OK" if generated.exists() else "MISSING"
    print(f" - {generated.name}: {status}")
    if not generated.exists():
        results.append((generated.name, False))
        continue
    if not expected.exists():
        print(f"   Expected file missing: {expected}")
        results.append((expected.name, False))
        continue
    expected_lines = expected.read_text(encoding="utf-8").splitlines()
    generated_lines = generated.read_text(encoding="utf-8").splitlines()
    diff = list(difflib.unified_diff(expected_lines, generated_lines, lineterm="", n=3))
    print(f"   Lines: expected={len(expected_lines)} generated={len(generated_lines)}")
    print(f"   Diff chunks: {len(diff)}")
    if len(diff) > 0:
        summary = diff[:20]
        print("   First diff lines:")
        for line in summary:
            print(f"    {line}")
    results.append((generated.name, True))
    results.append((expected.name, True))
    print()

print("\nSUMMARY")
passed = all(value for _, value in results)
print(f" Passed checks: {passed}")
failures = [name for name, ok in results if not ok]
if failures:
    print("Failures:")
    for name in failures:
        print(f" - {name}")
else:
    print("No missing files or missing spec phrases found.")

print("\nDetailed note: this runner validates the updated spec presence and file availability, but it does not execute a live LLM agent.")
