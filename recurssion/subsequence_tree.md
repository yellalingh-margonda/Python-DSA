# Recursion Tree for `subsequence([1, 2, 3])`

This diagram shows the recursion tree for generating all subsequences of the array `[1, 2, 3]` using include/exclude logic at each step.

## 🌳 Mermaid Diagram

```mermaid
graph TD
    A["[] (index=0)"] 
    A1["[1] (include 1)"]
    A2["[] (exclude 1)"]

    A --> A1
    A --> A2

    A1a["[1, 2] (include 2)"]
    A1b["[1] (exclude 2)"]
    A1 --> A1a
    A1 --> A1b

    A2a["[2] (include 2)"]
    A2b["[] (exclude 2)"]
    A2 --> A2a
    A2 --> A2b

    A1a1["[1, 2, 3] ✅"]
    A1a2["[1, 2] ✅"]
    A1a --> A1a1
    A1a --> A1a2

    A1b1["[1, 3] ✅"]
    A1b2["[1] ✅"]
    A1b --> A1b1
    A1b --> A1b2

    A2a1["[2, 3] ✅"]
    A2a2["[2] ✅"]
    A2a --> A2a1
    A2a --> A2a2

    A2b1["[3] ✅"]
    A2b2["[] ✅"]
    A2b --> A2b1
    A2b --> A2b2
