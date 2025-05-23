# Generated by go2rpm 1.13.0.post0
%bcond_without check
%global debug_package %{nil}

# https://github.com/sethvargo/go-retry
%global goipath         github.com/sethvargo/go-retry
Version:                0.2.4

%gometa -L -f

%global common_description %{expand:
Go library for retrying with configurable backoffs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-sethvargo-retry
Release:        %autorelease
Summary:        Go library for retrying with configurable backoffs

License:        Apache-2.0
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
