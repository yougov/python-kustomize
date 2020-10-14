my_kustomization = {
    'commonLabels': {
        'app': 'hello',
    },
    'resources': [
        'deployments.deployment:my_deployment',
        'services.service:my_service',
        'configmaps.configMap:my_config_map',
    ],
}
