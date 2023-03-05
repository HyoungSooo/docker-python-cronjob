# docker-python-cronjob

a python cronjob in docker.

in docker-compose.yml
```
  environment:
        - CRON_ENTRY=* * * * *(change here) python <your scirpt path>
```

```
<clone repo>
docker-compose build
```

