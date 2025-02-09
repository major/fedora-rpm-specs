# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/schollz/logger
%global goipath         github.com/schollz/logger
Version:                1.2.0

%gometa

%global common_description %{expand:
Simplistic, opinionated logging for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Simplistic, opinionated logging for Golang

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
