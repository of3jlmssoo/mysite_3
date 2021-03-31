kind: PersistentVolume
apiVersion: v1
metadata:
  annotations:
    ibm.io/mountstatus: attaching
    ibm.io/network-storage-id: '224985744'
    ibm.io/nodename: 10.148.25.187
    pv.kubernetes.io/provisioned-by: ibm.io/ibmc-block
    volume.beta.kubernetes.io/storage-class: ''
  selfLink: /api/v1/persistentvolumes/pvc-17e12669-46f4-4ab3-ae51-c608b98ea6d7
  resourceVersion: '735392'
  name: pvc-17e12669-46f4-4ab3-ae51-c608b98ea6d7
  uid: 49a10a4f-c46b-4a86-95d6-8d444df3dd62
  creationTimestamp: '2021-03-31T05:12:17Z'
  managedFields:
    - manager: kube-controller-manager
      operation: Update
      apiVersion: v1
      time: '2021-03-31T05:12:17Z'
      fieldsType: FieldsV1
      fieldsV1:
        'f:status':
          'f:phase': {}
    - manager: provisioner
      operation: Update
      apiVersion: v1
      time: '2021-03-31T05:12:17Z'
      fieldsType: FieldsV1
      fieldsV1:
        'f:metadata':
          'f:annotations':
            .: {}
            'f:ibm.io/network-storage-id': {}
            'f:pv.kubernetes.io/provisioned-by': {}
            'f:volume.beta.kubernetes.io/storage-class': {}
          'f:labels':
            'f:failure-domain.beta.kubernetes.io/region': {}
            'f:StorageType': {}
            'f:billingType': {}
            'f:CapacityGb': {}
            'f:ibm-cloud.kubernetes.io/iaas-provider': {}
            .: {}
            'f:Datacenter': {}
            'f:failure-domain.beta.kubernetes.io/zone': {}
            'f:IOPS': {}
        'f:spec':
          'f:accessModes': {}
          'f:capacity':
            .: {}
            'f:storage': {}
          'f:claimRef':
            .: {}
            'f:apiVersion': {}
            'f:kind': {}
            'f:name': {}
            'f:namespace': {}
            'f:resourceVersion': {}
            'f:uid': {}
          'f:flexVolume':
            .: {}
            'f:driver': {}
            'f:fsType': {}
            'f:options':
              .: {}
              'f:Lun': {}
              'f:TargetPortal': {}
              'f:VolumeID': {}
              'f:volumeName': {}
          'f:persistentVolumeReclaimPolicy': {}
          'f:storageClassName': {}
          'f:volumeMode': {}
    - manager: ibmc-block
      operation: Update
      apiVersion: v1
      time: '2021-03-31T05:12:22Z'
      fieldsType: FieldsV1
      fieldsV1:
        'f:metadata':
          'f:annotations':
            'f:ibm.io/mountstatus': {}
            'f:ibm.io/nodename': {}
  finalizers:
    - kubernetes.io/pv-protection
  labels:
    CapacityGb: '20'
    Datacenter: wdc04
    IOPS: '10'
    StorageType: Endurance
    billingType: hourly
    failure-domain.beta.kubernetes.io/region: us-east
    failure-domain.beta.kubernetes.io/zone: wdc04
    ibm-cloud.kubernetes.io/iaas-provider: softlayer
spec:
  capacity:
    storage: 20Gi
  flexVolume:
    driver: ibm/ibmc-block
    fsType: ext4
    options:
      Lun: '10'
      TargetPortal: '10.201.14.202,10.201.14.203'
      VolumeID: '224985744'
      volumeName: pvc-17e12669-46f4-4ab3-ae51-c608b98ea6d7
  accessModes:
    - ReadWriteOnce
  claimRef:
    kind: PersistentVolumeClaim
    namespace: myproject
    name: postgresql
    uid: 17e12669-46f4-4ab3-ae51-c608b98ea6d7
    apiVersion: v1
    resourceVersion: '734922'
  persistentVolumeReclaimPolicy: Delete
  storageClassName: ibmc-block-gold
  volumeMode: Filesystem
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: failure-domain.beta.kubernetes.io/zone
              operator: In
              values:
                - wdc04
            - key: failure-domain.beta.kubernetes.io/region
              operator: In
              values:
                - us-east
status:
  phase: Bound
