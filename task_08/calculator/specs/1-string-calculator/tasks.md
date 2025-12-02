# Tasks: String Calculator

**Input**: Design documents from `specs/1-string-calculator/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

- [x] T001 Create project structure (`src/`, `tests/`).
- [x] T002 Initialize Python project with Streamlit and pytest dependencies.

---

## Phase 2: User Story 1 - Basic Calculation (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to enter a simple mathematical expression as a string and see the correct numerical result.

**Independent Test**: Input a known expression and verify the output.

### Implementation for User Story 1

- [x] T003 [US1] Implement `calculate` function in `src/calculator.py`.
- [x] T004 [US1] Create Streamlit UI in `src/main.py` to take input and display the result.
- [x] T005 [US1] Add unit tests for `calculate` function in `tests/test_calculator.py`.

---

## Phase 3: User Story 2 - Handle Invalid Expressions (Priority: P2)

**Goal**: As a user, I want to be notified of errors when I enter an invalid mathematical expression.

**Independent Test**: Input various invalid expressions and verify that an error message is displayed.

### Implementation for User Story 2

- [x] T006 [US2] Add error handling to `calculate` function in `src/calculator.py`.
- [x] T007 [US2] Update Streamlit UI in `src/main.py` to display error messages.
- [x] T008 [US2] Add unit tests for error handling in `tests/test_calculator.py`.
