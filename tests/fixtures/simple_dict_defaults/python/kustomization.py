kustomization = {
    'commonLabels': {
        'app': 'hello',
    },
    'resources': [
        'deployment',
        'service',
        'configMap',
    ],
}
