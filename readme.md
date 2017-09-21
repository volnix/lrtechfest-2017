# Being Lazy in the Cloud

AWS out of the box tends makes things more difficult than they need to be. I'll show you some easy ways to simplify your interactions with the AWS cloud that will free up time and make your life easier. Some of my tips may even save you some money!

## whois

My name is Nick Volgas and I'm a software developer turned sys-admin wannabe. I started using AWS for both work and personal projects in 2015 and have spent a large amount of my time automating and tooling myself out of having to work in any way possible. I've gotten both an AWS Solutions Architect Associate certification as well as an AWS DevOps Professional certification. I'm currently the Director of Development at the Information Network of Arkansas and this is my second year presenting at LR Tech Fest.

## Description

AWS provides a wide array of tools and methodologies for hosting your infrastructure in the cloud. Out of the box, however, I've found myself wishing things that should be simple would be just that...simple! I'll walk you through some of the inefficiencies encountered by the normal user and how to overcome those. I'll show you some examples of AWS-provided time savers as well as some home-grown processes. I'll provide any code I demo on my github account for use after my talk and will provide links to write-ups on how to perform each task I demo. Did I mention I will demo each of these LIVE?

## Topics

### CloudFormation

Templated creation of AWS infrastructure

#### Resources

- CloudFormation Templates Bucket
    - [Template](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/templates-bucket.yaml)
    - [Video](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/Videos/Templates%20Bucket.mov)
	- Versioned bucket for account-specific CloudFormation templates that automatically rolls off old versions to cheaper storage tiers
- Static Website
    - [Template](https://github.com/volnix/lrtechfest-2017/blob/master/CloudFormation/templates-bucket.yaml)
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


### Consolidated Billing


### Cost Allocation Tags


### Trusted Advisor


### CloudWatch Logs
