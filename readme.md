# Being Lazy in the Cloud

AWS out of the box tends makes things more difficult than they need to be. This repository contains links to all the resources I discuss/demo in my talk at the Little Rock Tech Fest 2017.

## Presentation

[Link](https://prezi.com/view/9sudRK7ama8qMccBEVbC/)

## Topics

### CloudFormation

Templated creation of AWS infrastructure

#### Resources

- CloudFormation Templates Bucket
    - [Template](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/Code/templates-bucket.yaml)
    - [Video](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/Videos/Templates%20Bucket.mov)
    - Versioned bucket for account-specific CloudFormation templates that automatically rolls off old versions to cheaper storage tiers
- Static Website
    - [Template](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/Code/templates-bucket.yaml)
    - [Video](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/Videos/Static%20Site.mov)
    - My personal favorite template - creates an S3 bucket with versioning for static content hosting served out through CloudFront
    - A WAF can be attached to this site if so desired

### Account Switching Made Easy

Simple cross-account management by linking shared accounts to one "master" account and switching roles between the accounts

#### Resources

- [Video](https://github.com/volnix/lrtechfest-2017/blob/master/Cross%20Account/Switching%20Roles.mov)
- [Granting Access for Role Switching](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html)
- [How to Switch Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)
- A more "enterprisey" solution leveraging AWS Directory Service (Active Directory): [Cross-Account Manager](http://docs.aws.amazon.com/solutions/latest/cross-account-manager/overview.html)

### Auto-deletion of EC2 Snapshots

Automatically create EC2 snapshots and then purge them after a certain amount of time using Lambda functions

#### Resources

- [Video](https://github.com/volnix/lrtechfest-2017/blob/master/Snapshots/Videos/snapshots.mov)
- [Creation Code](https://github.com/volnix/lrtechfest-2017/blob/master/Snapshots/Code/create_snapshots.py)
- [Deletion Code](https://github.com/volnix/lrtechfest-2017/blob/master/Snapshots/Code/delete_old_snapshots.py)
    - Remember to fill in your account ID instead of `<YOUR ACCOUNT ID HERE>` or use the account ID search code commented out above

### Consolidated Billing

If you have multiple AWS accounts you can consolidate the billing for them into one "master" account

#### Resources

- [Link](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

### Cost Allocation Tags

Use resource tags for cost breakdown

#### Resources

- [Creating Tags Video](https://github.com/volnix/lrtechfest-2017/blob/master/Cost%20Allocation%20Tagging/Activating%20Tags.mov)

### Trusted Advisor

Use Trusted Advisor to identify cost optimization, performance, security, and fault tolerance shortcomings (requires business-tier support plan or higher)

#### Resources

- [Video](https://github.com/volnix/lrtechfest-2017/blob/master/Trusted%20Advisor/Trusted%20Advisor.mov)

### CloudWatch Logs

CloudWatch logs are an out-of-the-box logging solution with an AWS-provided agent to automatically pipe logs into it

#### Resources

- [Agent Setup](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html)

> **Note:** I have not used this service before so your mileage may vary