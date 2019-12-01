kustomization = {
    'commonLabels': {
        'env': 'production',
    },
    'bases': [
        '../../base',
    ],
    'patches': [
        'replica_count',
    ],
}
