# Exchange Rate Analytics Platform

A full-stack system for collecting, analyzing, forecasting, and visualizing
monthly USD exchange rate data with advanced mathematical analysis.

The platform is designed with a clean, modular architecture that separates
data access, business logic, mathematical computation, and presentation layers.

---

## Overview

The system manages historical monthly average USD exchange rates starting from
January 2023, performs trend analysis and forecasting, and provides interactive
visualizations and matrix-based analytics.

It is built to ensure:

- Deterministic calculations
- Clear separation of concerns
- Full test coverage for computational logic
- Maintainable and extensible codebase

---

## Tech Stack

### Backend

- Python 3.11+
- FastAPI
- Pydantic
- pytest
- Pure Python computational modules

### Frontend

- React or Angular
- REST-based API communication
- Charting and table visualization libraries

### Infrastructure

- Docker
- Docker Compose

---

## Core Capabilities

### Data Management

- Persistent storage of monthly average USD exchange rates
- Data model includes month and calculated average
- Designed for periodic monthly updates

### Visualization

- Line graph displaying monthly average exchange rates
- Tabular view with color-based rating:
  - Green → highest average value
  - Red → lowest average value
- Sorting options:
  - By month
  - By average rate (ascending)
- Search and highlighting of specific months

### Forecasting

- Approximate forecast for the next month
- Forecast is based on the rolling average of the previous three months

---

## Advanced Matrix Analytics

The system performs additional analytical operations using matrix-based models:

### Forecast Matrix

- Each cell represents a rolling three-month average

### Difference Matrix

- Difference between actual monthly averages and forecasted values

### Aggregated Analysis

- Additional row calculating the average difference for each three-month window

### Matrix Multiplication

- Multiplication of the forecast matrix by the difference matrix
- Results displayed in a structured tabular format
- Interactive display triggered by user action

---

## Backend Architecture

The backend follows a layered architecture:

- **Controllers**  
  HTTP API layer only (FastAPI routes)

- **Services**  
  Business logic and orchestration

- **Calculations**  
  Pure mathematical logic:
  - averages
  - forecasts
  - matrix construction
  - matrix multiplication

- **Repositories**  
  Database access layer

- **Models**  
  Domain entities

- **Schemas**  
  API data transfer objects (DTOs)

- **Errors**  
  Domain-specific exceptions

This structure ensures:

- Testability
- Maintainability
- Clear responsibility boundaries

---

## Frontend Architecture

- Component-based UI
- Focused solely on presentation and interaction
- No business or mathematical logic on the client side
- Data retrieved exclusively via REST API

---

## Testing Strategy

- Unit tests for all mathematical computations:
  - Averages
  - Forecast calculations
  - Matrix operations
- Service-level tests
- Repository-level tests

All calculations are deterministic and fully covered by tests.

---

## Running the System

```bash
docker-compose up --build
```

## Design Principles

- Clean Code
- Separation of Concerns
- Thin Client, Strong Backend
- Deterministic and testable computations
- Scalable architecture
