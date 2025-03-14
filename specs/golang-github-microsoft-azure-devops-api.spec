# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/microsoft/azure-devops-go-api
%global goipath         github.com/microsoft/azure-devops-go-api
Version:                v7.1.0
%global tag             azuredevops/v7.1.0

%gometa -f

%global common_description %{expand:
Go APIs for interacting with and managing Azure DevOps.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go APIs for interacting with and managing Azure DevOps

License:        MIT
URL:            %{gourl}
Source:         %{gosource}
# Fix build on Go 1.24.
# Submitted upstream as https://github.com/microsoft/azure-devops-go-api/pull/189
Patch0001:      0001-Fix-build-with-Go-1.24.patch

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
