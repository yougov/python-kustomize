kustomization = {
    'commonLabels': {
        'env': 'staging',
    },
    'bases': [
        '../../base',
    ],
    'patches': [
        'special_labels',
    ],
}
