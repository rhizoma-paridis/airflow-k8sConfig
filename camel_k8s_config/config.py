from kubernetes.client import models as k8s


class K8sConfig():

    def buildAffinity(self, key="app", operator="In", values=['airflow']):
        self.affinity = k8s.V1Affinity(
            node_affinity=k8s.V1NodeAffinity(
                preferred_during_scheduling_ignored_during_execution=[
                    k8s.V1PreferredSchedulingTerm(
                        weight=1,
                        preference=k8s.V1NodeSelectorTerm(
                            match_expressions=[
                                k8s.V1NodeSelectorRequirement(
                                    key=key, operator=operator, values=values)
                            ]
                        ),
                    )
                ]
            )
        )
        return self

    def buildTolerations(self, key='app', operator='Equal', value='airflow'):
        self.tolerations = [k8s.V1Toleration(
            key=key, operator=operator, value=value)]
        return self

    def buildResource(self, mem_request, mem_limit):

        self.resource = k8s.V1ResourceRequirements(
            requests={'memory': mem_request}, limits={'memory': mem_limit}
        )
        return self

    def build(self):
        container_kwargs = {'name':'base'}
        if hasattr(self, 'resource'):
            container_kwargs.update({"resources": self.resource}) 
            
        pod_args = { attr:getattr(self, attr, None) for attr in ["affinity",'tolerations'] }
        pod_args = {k:v for k,v in pod_args.items() if v}

        return {
            "pod_override": k8s.V1Pod(
                spec=k8s.V1PodSpec(
                    containers=[
                        k8s.V1Container(
                            **container_kwargs
                        )
                    ],
                    **pod_args
                )
            )
        }


if __name__ == '__main__':

    config = K8sConfig().buildAffinity().buildResource('512Mi', '512Mi').buildTolerations().build()
    print(1234)
    print(config)
