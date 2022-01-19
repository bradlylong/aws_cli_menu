ec2_info ="aws ec2 describe-instances \
    --filters Name=tag-key,Values=Name \
    --query 'Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==`Name`]|[0].Value,PublicIP:PublicIpAddress,PrivateIP:PrivateIPAddress,State:State.Name}' \
    --output text | tee output.txt > /dev/null 2>&1"
subnet_cidrs = "aws ec2 describe-subnets \
    --query 'Subnets[*].{CIDRs:CidrBlock,Name:Tags[?Key==`Name`]|[0].Value}' \
    --output text | tee output.txt > /dev/null 2>&1"
s3_buckets = "aws s3 ls | cut -d ' ' -f3 | tee output.txt > /dev/null 2>&1"
cloudwatch_alarms = "aws cloudwatch describe-alarms \
    --query 'MetricAlarms[*].{NameSpace:Namespace,Name:AlarmName,Description:AlarmDescription,State:StateValue}' \
    --output text | tee output.txt > /dev/null 2>&1"