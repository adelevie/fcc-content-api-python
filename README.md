The FCC Content API allows you to programmatically access much of the content accessible on [FCC.gov](http://fcc.gov).

fcc-content-api-python is a lightweight Python wrapper for the Federal Communication Commission's Content API.

The FCC Content API is powered by the [Drupal Content API Module](http://drupal.org/project/contentapi).

## Usage

First, familiarize yourself with the [FCC Content API REST Documentation](http://www.fcc.gov/developer/fcc-content-api).

Query parameters map 1-to-1 to the options listed in the link above.

```python
Content().where({"search_string":"broadband"}).where({"limit":1}).all().text
```

## More Info

For more information, please visit the [FCC's Developers page](http://www.fcc.gov/developers) and the [FCC's Github page](http://github.com/fcc).