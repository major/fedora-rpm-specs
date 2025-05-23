# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/gosuri/uilive
%global goipath         github.com/gosuri/uilive
Version:                0.0.4

%gometa

%global common_description %{expand:
Uilive is a go library for updating terminal output in realtime.}

%global golicenses      LICENSE
%global godocs          doc example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library for updating terminal output in realtime

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
