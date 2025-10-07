# SuperStringWithExpansion Project

**Course:** 02249 Computationally Hard Problems – Fall 2025  
**Due Date:** November 3, 2025, 21:00  
**Group Members:** Vignesh Sethuraman s252755@student.dtu.dk, Petteri Lauri Markus Raita s253163@student.dtu.dk, Davide Mecugni s253128@student.dtu.dk

## Project Overview

This project analyzes and implements a solution for the **SuperStringWithExpansion** problem, proving its NP-completeness and developing an algorithm with heuristic optimizations.

## Problem Description

Given two alphabets (Σ and Γ), a string s, k strings containing letters from both alphabets, and replacement sets for each letter in Γ, determine if there exists a way to expand all Γ letters such that all k strings become substrings of s.

## Repository Structure

```
├── README.md              # This file
├── report-group-XX.pdf    # Theoretical solutions
├── code-group-XX.zip      # Implementation source code
├── readme-group-XX.txt    # Compilation and execution instructions
├── src/                   # Source code directory
│   ├── main.py            # Main entry point of the implementation
│   └── utils/             # Utility modules for helper functions
├── tex/                   # Latex source files for the report
└── tests/                 # Test cases (test01.SWE - test06.SWE)
```

### How to run the implementation
Run:
```bash
python3 src/main.py < tests/test01.SWE
```
It generates a debug.log file in the root directory. It also prints debugging output to the console.

### How to run tests
Run:
```bash
pytest
```
It runs all the tests in the src/tests/ directory starting or ending by _test.py test_X.py.
## Task Checklist

### Part B: Initial Analysis (5%)
- [ ] Solve test01.SWE manually
- [ ] Provide detailed justification for the answer (YES/NO)
- [ ] Document the reasoning process

### Part C: Formal Language Description (10%)
- [ ] Describe the formal language for .SWE file format
- [ ] Define the underlying alphabet
- [ ] Explain how to solve the word problem for this language
- [ ] Ensure formal language is over a single alphabet

### Part D: Decision to Optimization Conversion (10%)
- [ ] Design algorithm Ao using decision algorithm Ad as subroutine
- [ ] Ensure Ao outputs the sequence r1, r2, ..., rm (or NO)
- [ ] Prove polynomial time complexity (Ad calls count as single steps)
- [ ] Prove correctness of the conversion

### Part E: NP Membership Proof (10%)
- [ ] Design a polynomial-time verifier
- [ ] Show that SuperStringWithExpansion ∈ NP
- [ ] Prove certificate can be verified in polynomial time

### Part F: NP-Completeness Proof (15%)
- [ ] Select reference NP-complete problem from provided list:
  - PartitionInto3-Sets
  - 1-In-3-Satisfiability
  - MinimumCliqueCover
  - Graph-3-Coloring
  - Longest-Common-Subsequence
  - MinimumRectangleTiling
  - Minimum Graph Transformation
  - MinimumDegreeSpanningTree
- [ ] Design polynomial-time reduction from chosen problem to SuperStringWithExpansion
- [ ] Prove reduction correctness
- [ ] Prove reduction runs in polynomial time
- [ ] Conclude NP-completeness

### Part G: Algorithm Design (15%)
- [ ] Design algorithm accepting general input format
- [ ] Ensure correctness (always gives right answer)
- [ ] Ensure termination
- [ ] Include heuristic elements for optimization
- [ ] Target exponential worst-case: O(2^p(n))
- [ ] Document heuristics (e.g., quick NO detection)
- [ ] Describe algorithm in natural language
- [ ] Prove correctness
- [ ] Prove running time bound

### Part H: Complexity Analysis (10%)
- [ ] Analyze worst-case running time for general input
- [ ] Express complexity in terms of input size parameters
- [ ] Consider all input components (|Σ|, |Γ|, |s|, k, |ti|, |Rj|)

### Part I: Implementation (25%)
- [ ] Implement algorithm from Part G
- [ ] Read input from **standard input** (stdin) - NOT command line arguments
- [ ] Parse .SWE file format correctly
- [ ] Handle malformed inputs (output NO)
- [ ] Output solution format: `γi:ri` (one per line)
- [ ] Output NO for NO-instances
- [ ] Test on test01.SWE - test06.SWE
- [ ] Create additional test cases
- [ ] Ensure all DTU Learn tests pass
- [ ] Choose language: Java, C, C++, or Python
- [ ] Write compilation/execution instructions

### Documentation & Submission
- [ ] Write report (report-group-XX.pdf)
- [ ] Include division of labor statement
- [ ] Document individual contributions
- [ ] Create ZIP of source code (code-group-XX.zip)
  - **Important:** ZIP contents, not the containing folder
  - Top level should be project root
- [ ] Write readme-group-XX.txt with:
  - Compilation instructions
  - Execution instructions
  - Usage: program should read from stdin, write to stdout
- [ ] Verify file naming (case-sensitive, replace XX with group number)
- [ ] Ensure no file duplication (don't include report/readme in ZIP)
- [ ] Submit all three files to DTU Learn

## Division of Labor

TBD based on actual contributions. Example:

| Team Member | Tasks | Weight |
|-------------|-------|--------|
|  Vignesh | Parts  | ~X% |
| Petteri  | Parts  | ~X% |
| Davide  | Parts  | ~X% |


## Grading Weights

- **Parts B-F (Theory):** 50%
- **Parts G-H (Algorithm Design & Analysis):** 25%
- **Part I (Implementation):** 25%

## Important Notes

⚠️ **Critical Requirements:**
- Use **stdin** for input, **stdout** for output only
- No command-line arguments or file operations
- No user interaction required
- Correct file naming (case-sensitive)
- ZIP structure must be correct (contents, not folder)

## Test Cases

Test your implementation thoroughly on:
- All provided test cases (test01.SWE - test06.SWE)
- Edge cases (empty strings, single character alphabets, etc.)
- Large instances (stress testing)
- Malformed inputs

## Resources

- Course materials on DTU Learn
- Test files in .SWE format
- NP-completeness reference problems list

---

**Last Updated:** October 7 11.00, 2025 Davide