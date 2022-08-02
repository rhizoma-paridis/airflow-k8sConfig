# k8s config

---

```python
config = K8sConfig().buildAffinity().buildResource('512Mi', '512Mi').buildTolerations().build()

# use in airflow task
@task(task_id='affinity', executor_config=config)
def task_with_resource_limits(ds=None):
    print_context(ds)
    return "k8s_test"
```