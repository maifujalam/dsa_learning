1. What is premtation in pod?
2. Whats are priority class?
3. Whats pod eviction timeout means?
When the kubeket decide to evicet(remove a pod) from a node,the time given to a pod for gracefully shutdown.
Eviction reason could be:- 
  node-pressure on cpu,disk,memory | OR tail applied: noExecute.
  default is: 30s
  Kubelet sends a SIGTERM signal to containers.
  Pod has up to the grace period to shut down.
  If still running after timeout, kubelet sends SIGKILL.
  Controller (Deployment/ReplicaSet) reschedules pod on another node.

4. Whats hard and soft eviction of kubelet?
   --eviction-hard: 
   --eviction-hard=memory.available<100Mi,nodefs.available<10%
   - Start evicting immediately.
   
   --eviction-soft
   --eviction-soft=memory.available<200Mi
   --eviction-soft-grace-period=memory.available=30s
   Here memory is <200Mi for 30 seconds then do sig TERM and then agter 30 sec SIG KILL.
5. 

