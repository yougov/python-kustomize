import pytest


@pytest.fixture
def some_container_port():
    from kustomize import templates

    return templates.ContainerPort(
        containerPort=1234,
    )


@pytest.fixture
def some_exec_action():
    from kustomize import templates

    return templates.ExecAction(
        command=['echo'],
    )


@pytest.fixture
def some_probe(some_exec_action):
    from kustomize import templates

    return templates.Probe(
        exec=some_exec_action,
        initialDelaySeconds=123,
    )


@pytest.fixture
def some_resource_requirements():
    from kustomize import templates

    return templates.ResourceRequirements()


@pytest.fixture
def some_volume_mount():
    from kustomize import templates

    return templates.VolumeMount(
        name='some-volume-mount',
        mountPath='/some/path',
    )


@pytest.fixture
def some_object_field_selector():
    from kustomize import templates

    return templates.ObjectFieldSelector(
        fieldPath='some-field-path',
    )


@pytest.fixture
def some_resource_field_selector():
    from kustomize import templates

    return templates.ResourceFieldSelector(
        resource='some-resource',
    )


@pytest.fixture
def some_downward_api_volume_file(
    some_object_field_selector,
    some_resource_field_selector,
):
    from kustomize import templates

    return templates.DownwardAPIVolumeFile(
        path='/some/path',
        fieldRef=some_object_field_selector,
        resourceFieldRef=some_resource_field_selector,
    )


@pytest.fixture
def some_container(
    some_container_port,
    some_probe,
    some_resource_requirements,
    some_volume_mount,
):
    from kustomize import templates

    return templates.Container(
        name='some-container',
        image='some-image',
        ports=[some_container_port],
        livenessProbe=some_probe,
        readinessProbe=some_probe,
        startupProbe=some_probe,
        resources=some_resource_requirements,
        volumeMounts=[some_volume_mount],
    )


@pytest.fixture
def some_volume():
    from kustomize import templates

    return templates.Volume(
        name='some-volume',
    )
