from dataclasses import asdict

from kustomize import templates


def test_container_port():
    obj = templates.ContainerPort(
        containerPort=1234,
    )

    assert asdict(obj) == {
        'containerPort': 1234,
        'hostIP': None,
        'hostPort': None,
        'name': None,
        'protocol': 'TCP',
    }


def test_exec_action():
    obj = templates.ExecAction(
        command=['echo'],
    )

    assert asdict(obj) == {
        'command': ['echo'],
    }


def test_http_get_action():
    obj = templates.HTTPGetAction(
        path='/ping',
        port=80,
    )

    assert asdict(obj) == {
        'path': '/ping',
        'port': 80,
        'httpHeaders': [],
        'scheme': 'HTTP',
    }


def test_http_header():
    obj = templates.HTTPHeader(
        name='foo',
        value='bar',
    )

    assert asdict(obj) == {
        'name': 'foo',
        'value': 'bar',
    }


def test_probe(some_exec_action):
    obj = templates.Probe(
        exec=some_exec_action,
        initialDelaySeconds=123,
    )

    assert asdict(obj) == {
        'exec': asdict(some_exec_action),
        'failureThreshold': 3,
        'httpGet': None,
        'initialDelaySeconds': 123,
        'periodSeconds': 10,
        'successThreshold': 1,
        'timeoutSeconds': 1,
    }


def test_env_var():
    obj = templates.EnvVar(
        name='FOO',
        value='bar',
    )

    assert asdict(obj) == {
        'name': 'FOO',
        'value': 'bar',
    }


def test_resource_requirements():
    obj = templates.ResourceRequirements()

    assert asdict(obj) == {
        'limits': None,
        'requests': None,
    }


def test_volume_mount():
    obj = templates.VolumeMount(
        name='some-volume-mount',
        mountPath='/some/path',
    )

    assert asdict(obj) == {
        'name': 'some-volume-mount',
        'mountPath': '/some/path',
        'readOnly': False,
        'subPath': '',
    }


def test_container(
    some_container_port,
    some_probe,
    some_resource_requirements,
    some_volume_mount,
):
    obj = templates.Container(
        name='some-container',
        image='some-image',
        ports=[some_container_port],
        livenessProbe=some_probe,
        readinessProbe=some_probe,
        startupProbe=some_probe,
        resources=some_resource_requirements,
        volumeMounts=[some_volume_mount],
    )

    assert asdict(obj) == {
        'name': 'some-container',
        'image': 'some-image',
        'ports': [asdict(some_container_port)],
        'livenessProbe': asdict(some_probe),
        'readinessProbe': asdict(some_probe),
        'startupProbe': asdict(some_probe),
        'resources': asdict(some_resource_requirements),
        'volumeMounts': [asdict(some_volume_mount)],
        'args': None,
        'command': None,
        'env': None,
        'imagePullPolicy': None,
        'stdin': False,
        'stdinOnce': False,
        'tty': False,
        'terminationMessagePath': '/dev/termination-log',
        'terminationMessagePolicy': 'File',
        'workingDir': None,
    }


def test_object_meta():
    obj = templates.ObjectMeta(
        annotations={
            'foo-anotation': 'bar-anotation',
        },
        labels={
            'foo-label': 'bar-label',
        },
    )

    assert asdict(obj) == {
        'annotations': {
            'foo-anotation': 'bar-anotation',
        },
        'labels': {
            'foo-label': 'bar-label',
        },
        'namespace': 'default',
        'finalizers': None,
        'name': None,
        'generateName': None,
    }


def test_key_to_path():
    obj = templates.KeyToPath(
        key='some-key',
        path='/some/path',
    )

    assert asdict(obj) == {
        'key': 'some-key',
        'path': '/some/path',
        'mode': None,
    }


def test_config_map_projection():
    obj = templates.ConfigMapProjection(
        name='some-config-map-projection',
    )

    assert asdict(obj) == {
        'name': 'some-config-map-projection',
        'optional': False,
        'items': None,
    }


def test_object_field_selector():
    obj = templates.ObjectFieldSelector(
        fieldPath='some-field-path',
    )

    assert asdict(obj) == {
        'fieldPath': 'some-field-path',
        'apiVersion': 'v1',
    }


def test_resource_field_selector():
    obj = templates.ResourceFieldSelector(
        resource='some-resource',
    )

    assert asdict(obj) == {
        'resource': 'some-resource',
        'containerName': None,
        'divisor': 1,
    }


def test_downward_api_volume_file(
    some_object_field_selector,
    some_resource_field_selector,
):
    obj = templates.DownwardAPIVolumeFile(
        path='/some/path',
        fieldRef=some_object_field_selector,
        resourceFieldRef=some_resource_field_selector,
    )

    assert asdict(obj) == {
        'path': '/some/path',
        'fieldRef': asdict(some_object_field_selector),
        'resourceFieldRef': asdict(some_resource_field_selector),
        'mode': None,
    }


def test_downward_api_projection(
    some_downward_api_volume_file,
):
    obj = templates.DownwardAPIProjection(
        items=[some_downward_api_volume_file],
    )

    assert asdict(obj) == {
        'items': [asdict(some_downward_api_volume_file)],
    }


def test_secret_projection():
    obj = templates.SecretProjection(
        name='some-secret-projection',
    )

    assert asdict(obj) == {
        'name': 'some-secret-projection',
        'optional': False,
        'items': None,
    }


def test_service_account_token_projection():
    obj = templates.ServiceAccountTokenProjection(
        path='/some/path',
    )

    assert asdict(obj) == {
        'path': '/some/path',
        'audience': None,
        'expirationSeconds': 3600,
    }


def test_volume_projection():
    obj = templates.VolumeProjection()

    assert asdict(obj) == {
        'configMap': None,
        'downwardAPI': None,
        'secret': None,
        'serviceAccountToken': None,
    }


def test_projected_volume_source():
    obj = templates.ProjectedVolumeSource(
        sources=[templates.VolumeProjection()],
    )

    assert asdict(obj) == {
        'sources': [asdict(templates.VolumeProjection())],
        'defaultMode': None,
    }


def test_config_map_volume_source():
    obj = templates.ConfigMapVolumeSource(
        name='some-config-map-volume-source',
    )

    assert asdict(obj) == {
        'name': 'some-config-map-volume-source',
        'defaultMode': None,
        'items': None,
        'optional': False,
    }


def test_secret_volume_source():
    obj = templates.SecretVolumeSource(
        secretName='some-secret-volume-source',
    )

    assert asdict(obj) == {
        'secretName': 'some-secret-volume-source',
        'defaultMode': None,
        'items': None,
        'optional': False,
    }


def test_downward_api_volume_source(some_downward_api_volume_file):
    obj = templates.DownwardAPIVolumeSource(
        items=[some_downward_api_volume_file],
    )

    assert asdict(obj) == {
        'defaultMode': None,
        'items': [asdict(some_downward_api_volume_file)],
    }


def test_empty_dir_volume_source():
    obj = templates.EmptyDirVolumeSource()

    assert asdict(obj) == {
        'medium': '',
        'sizeLimit': None,
    }


def test_glusterfs_volume_source():
    obj = templates.GlusterfsVolumeSource(
        path='/some/path',
        endpoints='some-endpoints',
    )

    assert asdict(obj) == {
        'path': '/some/path',
        'endpoints': 'some-endpoints',
        'readOnly': False,
    }


def test_persistent_volume_claim_volume_source():
    obj = templates.PersistentVolumeClaimVolumeSource(
        claimName='some-name',
    )

    assert asdict(obj) == {
        'claimName': 'some-name',
        'readOnly': False,
    }


def test_host_path_volume_source():
    obj = templates.HostPathVolumeSource(
        path='/some/path',
    )

    assert asdict(obj) == {
        'path': '/some/path',
        'type': '',
    }


def test_nfs_volume_source():
    obj = templates.NFSVolumeSource(
        path='/some/path',
        server='some-server',
    )

    assert asdict(obj) == {
        'path': '/some/path',
        'server': 'some-server',
        'readOnly': False,
    }


def test_volume():
    obj = templates.Volume(
        name='some-volume',
    )

    assert asdict(obj) == {
        'name': 'some-volume',
        'configMap': None,
        'downwardAPI': None,
        'emptyDir': None,
        'glusterfs': None,
        'hostPath': None,
        'nfs': None,
        'persistentVolumeClaim': None,
        'projected': None,
        'secret': None,
    }


# def test_pod_spec(some_container):
#     obj = templates.PodSpec(
#         containers=[some_container],
#     )
#
#     assert asdict(obj) == {
#         'annotations': {
#             'foo-anotation': 'bar-anotation',
#         },
#         'labels': {
#             'foo-label': 'bar-label',
#         },
#         'namespace': 'default',
#         'finalizers': None,
#         'name': None,
#         'generateName': None,
#     }
#
#
# def test_deployment(some_container):
#     result = to_dict(templates.Deployment(
#         metadata=templates.ObjectMeta(
#             namespace='some-namespace',
#             name='some-deployment',
#             annotations={
#                 'foo-anotation': 'bar-anotation',
#             },
#             labels={
#                 'foo-label': 'bar-label',
#             },
#         ),
#         spec=templates.DeploymentSpec(
#             template=templates.PodTemplateSpec(
#                 metadata=templates.ObjectMeta(),
#                 spec=templates.PodSpec(
#                     containers=[
#                         templates.Container(
#                             name='some-container',
#                             image='some-image',
#                             command=['ls', '-lh'],
#                         ),
#                     ],
#                 ),
#             ),
#         ),
#     ))
