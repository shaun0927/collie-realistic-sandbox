# Request behavior notes

- Timeout documentation should distinguish connect/read behavior from total request duration.
- URL path handling should preserve meaningful path delimiters.

## Timeout semantics

`timeout` controls inactivity while connecting or reading. It is not a total wall-clock deadline for the whole request lifecycle.
