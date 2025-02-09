# Generated by go2rpm 1
%bcond_without check

# https://github.com/robfig/cron
%global goipath         github.com/robfig/cron
Version:                3.0.1
%global debug_package   %{nil}

%gometa

%global common_description %{expand:
A cron library for go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A cron library for go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

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
