# Generated by go2rpm 1.12.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/avast/retry-go
%global goipath         github.com/avast/retry-go/v4
Version:                4.6.0

%gometa -L -f

%global common_description %{expand:
Simple golang library for retry mechanism.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           golang-github-avast-retry4
Release:        %autorelease
Summary:        Simple golang library for retry mechanism

License:        MIT
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