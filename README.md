# python-every-minute
Run a python script every minute using Github Action + cron-job.org

- Github Action Scheduler is what I tried first.
- Doc said we can schedule it to run every 5 minutes(highest frequency).
- But it was not happening every 5 mins. Sometimes 5 mins, sometimes 12 minutes and so on.
- What worked was setting up a GH action that can be triggered from cron-job.org.
- For this to work, we generate a Github token and make cron-job.org call this every 1 minute
  
```
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/dispatches \
  -d '{"event_type": "run-main"}'
```
