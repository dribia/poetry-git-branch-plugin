In DBT projects it can be the case that we want to set the target schema name
based on the current Git branch. In the `profiles.yml` file we can set a
project variable such that

```ỳaml
example_dbt:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: oauth
      project: GCLOUD_PROJECT
      dataset: "{{ env_var('POETRY_GIT_BRANCH') }}"
      location: GCLOUD_LOCATION
```
