# Advent of Code

## Using the template

Install advent-of-code-data (aocd)

```
pip install advent-of-code-data
```

## Get your session cookie value

Puzzle inputs differ by user. For this reason, you can't get your data with an unauthenticated request. Here's how to get your session cookie for aocd to use:

1. Login on AoC with github or whatever
2. Open browser's developer console (e.g. right click --> Inspect) and navigate to the _Web Storage_ tab
3. Copy the *value* of the session cookie. It's a long hex string.
4. Write it to a plain text file at ~/.config/aocd/token.