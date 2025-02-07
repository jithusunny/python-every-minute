# python-every-minute
Run a python script every minute for free, without spinning up a server.
- Uses Github Action & cron-job.org

- The python script just pings an web API (free, mock, by Beeceptor)

- Tried Github Action Scheduler.
- Did not get the max frequency of every 5 minutes as mentioned in docs.
- Sometimes 5 mins, sometimes 12 minutes and so on.

- What worked was triggering the Github action from cron-job.org every minute
- we generate a GH token for cron-job.org to use while reaching GH

```
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/dispatches \
  -d '{"event_type": "run-main"}'
```
