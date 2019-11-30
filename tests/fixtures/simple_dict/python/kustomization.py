my_kustomization = {
    'commonLabels': {
        'app': 'hello',
    },
    'resources': [
        'deployment:my_deployment',
        'service:my_service',
        'configMap:my_config_map',
    ],
}
