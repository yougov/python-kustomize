from dataclasses import dataclass, field
from typing import Optional, List, Union


Quantity = Union[int, float]


@dataclass
class ContainerPort:
    containerPort: Optional[int] = None
    hostIP: Optional[str] = None
    hostPort: Optional[int] = None
    name: Optional[str] = None
    protocol: str = 'TCP'


@dataclass
class ExecAction:
    command: List[str]


@dataclass
class HTTPHeader:
    name: str
    value: str


@dataclass
class EnvVar:
    name: str
    value: str
    # TODO: valueFrom


@dataclass
class HTTPGetAction:
    path: str
    port: int
    httpHeaders: List[HTTPHeader] = field(default_factory=list)
    scheme: str = 'HTTP'


@dataclass
class ResourceRequirements:
    limits: Optional[dict] = None
    requests: Optional[dict] = None


@dataclass
class VolumeMount:
    name: str
    mountPath: str
    readOnly: bool = False
    subPath: str = ''


@dataclass
class Probe:
    initialDelaySeconds: int
    exec: Optional[ExecAction] = None
    httpGet: Optional[HTTPGetAction] = None
    periodSeconds: int = 10
    successThreshold: int = 1
    timeoutSeconds: int = 1
    failureThreshold: int = 3


@dataclass
class Container:
    name: str
    image: str
    livenessProbe: Probe
    readinessProbe: Probe
    startupProbe: Probe
    resources: ResourceRequirements
    ports: Optional[List[ContainerPort]] = None
    volumeMounts: Optional[List[VolumeMount]] = None
    args: Optional[List[str]] = None
    command: Optional[List[str]] = None
    env: Optional[List[EnvVar]] = None
    imagePullPolicy: Optional[str] = None
    stdin: bool = False
    stdinOnce: bool = False
    tty: bool = False
    terminationMessagePath: str = '/dev/termination-log'
    terminationMessagePolicy: str = 'File'
    workingDir: Optional[str] = None


@dataclass
class ObjectMeta:
    labels: dict = field(default_factory=dict)
    annotations: dict = field(default_factory=dict)
    namespace: str = 'default'
    finalizers: Optional[List[str]] = None
    name: Optional[str] = None
    generateName: Optional[str] = None
    # TODO: managedFields
    # TODO: ownerReferences


@dataclass
class KeyToPath:
    key: str
    path: str
    mode: Optional[int] = None


@dataclass
class ConfigMapProjection:
    name: str
    optional: bool = False
    items: Optional[List[KeyToPath]] = None


@dataclass
class SecretProjection:
    name: str
    optional: bool = False
    items: Optional[List[KeyToPath]] = None


@dataclass
class ObjectFieldSelector:
    fieldPath: str
    apiVersion: str = 'v1'


@dataclass
class ResourceFieldSelector:
    resource: str
    containerName: Optional[str] = None
    divisor: Quantity = 1


@dataclass
class DownwardAPIVolumeFile:
    path: str
    fieldRef: ObjectFieldSelector
    resourceFieldRef: ResourceFieldSelector
    mode: Optional[int] = None


@dataclass
class DownwardAPIProjection:
    items: List[DownwardAPIVolumeFile]


@dataclass
class ServiceAccountTokenProjection:
    path: str
    audience: Optional[str] = None
    expirationSeconds: int = 3600


@dataclass
class VolumeProjection:
    configMap: Optional[ConfigMapProjection] = None
    downwardAPI: Optional[DownwardAPIProjection] = None
    secret: Optional[SecretProjection] = None
    serviceAccountToken: Optional[ServiceAccountTokenProjection] = None


@dataclass
class ProjectedVolumeSource:
    sources: List[VolumeProjection]
    defaultMode: Optional[int] = None


@dataclass
class ConfigMapVolumeSource:
    name: str
    defaultMode: Optional[int] = None
    items: Optional[List[KeyToPath]] = None
    optional: bool = False


@dataclass
class SecretVolumeSource:
    secretName: str
    defaultMode: Optional[int] = None
    items: Optional[List[KeyToPath]] = None
    optional: bool = False


@dataclass
class DownwardAPIVolumeSource:
    items: List[DownwardAPIVolumeFile]
    defaultMode: Optional[int] = None


@dataclass
class EmptyDirVolumeSource:
    medium: str = ''
    sizeLimit: Optional[Quantity] = None


@dataclass
class GlusterfsVolumeSource:
    path: str
    endpoints: str
    readOnly: bool = False


@dataclass
class PersistentVolumeClaimVolumeSource:
    claimName: str
    readOnly: bool = False


@dataclass
class HostPathVolumeSource:
    path: str
    type: str = ''


@dataclass
class NFSVolumeSource:
    path: str
    server: str
    readOnly: bool = False


@dataclass
class Volume:
    name: str
    configMap: Optional[ConfigMapVolumeSource] = None
    downwardAPI: Optional[DownwardAPIVolumeSource] = None
    emptyDir: Optional[EmptyDirVolumeSource] = None
    glusterfs: Optional[GlusterfsVolumeSource] = None
    hostPath: Optional[HostPathVolumeSource] = None
    nfs: Optional[NFSVolumeSource] = None
    persistentVolumeClaim: Optional[PersistentVolumeClaimVolumeSource] = None
    projected: Optional[ProjectedVolumeSource] = None
    secret: Optional[SecretVolumeSource] = None
