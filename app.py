import json
import os
import requests
from sys import stderr
from flask import Flask, request, jsonify ,make_response
import paramiko
from paramiko import SSHClient
from base64 import decodebytes


app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://api.stagingv3.microgen.id/query/api/v1/" + api_key


@app.get("/restarte")
def restarte():
    try:
        url = "http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER|ServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name,host_components/HostRoles/host_name,host_components/HostRoles/public_host_name,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/ha_state,host_components/HostRoles/desired_admin_state,,host_components/metrics/jvm/memHeapUsedM,host_components/metrics/jvm/HeapMemoryMax,host_components/metrics/jvm/HeapMemoryUsed,host_components/metrics/jvm/memHeapCommittedM,host_components/metrics/mapred/jobtracker/trackers_decommissioned,host_components/metrics/cpu/cpu_wio,host_components/metrics/rpc/client/RpcQueueTime_avg_time,host_components/metrics/dfs/FSNamesystem/*,host_components/metrics/dfs/namenode/Version,host_components/metrics/dfs/namenode/LiveNodes,host_components/metrics/dfs/namenode/DeadNodes,host_components/metrics/dfs/namenode/DecomNodes,host_components/metrics/dfs/namenode/TotalFiles,host_components/metrics/dfs/namenode/UpgradeFinalized,host_components/metrics/dfs/namenode/Safemode,host_components/metrics/runtime/StartTime,host_components/metrics/hbase/master/IsActiveMaster,host_components/metrics/hbase/master/MasterStartTime,host_components/metrics/hbase/master/MasterActiveTime,host_components/metrics/hbase/master/AverageLoad,host_components/metrics/master/AssignmentManager/ritCount,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/yarn/Queue,host_components/metrics/yarn/ClusterMetrics/NumActiveNMs,host_components/metrics/yarn/ClusterMetrics/NumLostNMs,host_components/metrics/yarn/ClusterMetrics/NumUnhealthyNMs,host_components/metrics/yarn/ClusterMetrics/NumRebootedNMs,host_components/metrics/yarn/ClusterMetrics/NumDecommissionedNMs&minimal_response=true&_=1667968440999"
        username = "sapujagad"
        password = "kayangan"
        response = requests.get(url, auth=(username, password), timeout=(2))
        x = response.ok
        if x == True:
            return("oke")
        else :
            return("last")
    except:
        hostname = '10.10.65.1'
        port = 8080
        username = "sapujagad"
        password = "kayangan"

        client = SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        command = "echo sudo kayangan | sudo -S ambari-server restart"

        stdin, stdout, stderr = client.exec_command(command)
        # for line in stdout.readlines():
        #     my_dict = {}
        #     my_dict['Set-Cookie']= line
        #     xs = make_response(my_dict)
        return stdout.read()
        # z=stdout.read()
        client.close()
        
@app.get("/test")
def test():
    url = "https://dev-bhagaskarash4zl.microgen.id/api/testcsv"
    response = requests.post(url,json={"firstname":"1"})
    return response.json()                         
                        

if __name__ == "__main__":
    app.run(debug=True)
