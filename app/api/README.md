# 🔌 API Integration Layer

This directory contains the core logic for interfacing with external RESTful services. Each module follows the Single Responsibility Principle, managing both the data retrieval (fetching) and the formatting of the specific data segment.

- **Non-blocking I/O**: All modules utilize `aiohttp.ClientSession` to perform asynchronous requests.
- **Graceful Degradation**: Modules are designed to return a standardized "Service Unavailable" message if an API call fails, preventing a single point of failure from crashing the entire application.