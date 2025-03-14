# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/brunoscheufler/aws-ecs-metadata-go
%global goipath         github.com/brunoscheufler/aws-ecs-metadata-go
%global forgeurl        https://github.com/brunoscheufler/aws-ecs-metadata-go
%global commit          67e37ae746cd12f6ddd5dbebd31ff4a1ecd062cf

%gometa

%global common_description %{expand:
A minimal wrapper library to fetch Elastic Container Service (ECS) Task metadata
from any Go service running in container provisioned by AWS Fargate.

Based on the Fargate platform version, you'll have access to different versions
of the Task Metadata Endpoint. If you're running on 1.4.0, you'll be able to
access Version 4, Fargate 1.3.0 and later support Version 3 of the endpoint.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Retrieve AWS ECS Task metadata

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
