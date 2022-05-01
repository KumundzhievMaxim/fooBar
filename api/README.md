# API interface for getting normalized search interest
The functionality represents the API interface to interact with [Google Trends service](https://trends.google.com/trends/?geo=HU). 

# Description
- The API holds 1 endpoint `/search_interest/{keyword}`
- The API documentation `/docs`

## Spin up Local Server
```bash
$ uvicorn main:app --reload 
```

## Sample API response
```bash
{
  "search_score": {
    "2018-01-08-02:00:00": 100,
    "2018-01-25-03:00:00": 100,
    "2018-01-15-03:00:00": 100,
    "2018-01-05-19:00:00": 100,
    "2018-01-29-23:00:00": 100,
    "2018-01-18-02:00:00": 98,
    "2018-01-23-01:00:00": 92,
    "2018-01-23-05:00:00": 91,
    "2018-01-26-23:00:00": 90,
    "2018-01-16-00:00:00": 90,
    "2018-01-29-03:00:00": 89,
    "2018-01-16-04:00:00": 89,
    "2018-01-08-03:00:00": 89,
    "2018-01-15-06:00:00": 88,
    "2018-01-05-20:00:00": 88,
    "2018-01-29-02:00:00": 87,
    "2018-02-01-00:00:00": 86,
    "2018-01-24-02:00:00": 86,
    ...
    }
}
```

