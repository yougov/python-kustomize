kustomization = {
    'commonLabels': {
        'app': 'hello',
    },
    'resources': [
        'deployment',
        'service',
        'configMap',
    ],
    'patchesJson6902': [
        {
            'target': {
                'version': 'v1',
                'kind': 'Deployment',
                'name': 'my-deployment',
            },
            'path': 'add_init_container',
        },
    ]
}
