kustomization = {
    'commonLabels': {
        'env': 'staging',
    },
    'bases': [
        '../../base',
    ],
    'patchesStrategicMerge': [
        'special_labels',
    ],
}
