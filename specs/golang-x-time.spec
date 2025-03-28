# Generated by go2rpm 1.12.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/golang/time
%global goipath         golang.org/x/time
%global forgeurl        https://github.com/golang/time
Version:                0.9.0

%gometa -L

%global common_description %{expand:
This library provides supplementary Go time packages.}

%global golicenses      LICENSE PATENTS
%global godocs          CONTRIBUTING.md README.md

Name:           golang-x-time
Release:        %autorelease
Summary:        Go supplementary time packages

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
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
