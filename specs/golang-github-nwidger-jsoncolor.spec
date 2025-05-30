# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/nwidger/jsoncolor
%global goipath         github.com/nwidger/jsoncolor
Version:                0.3.0

%gometa

%global common_description %{expand:
jsoncolor is a drop-in replacement for encoding/json's Marshal and MarshalIndent
functions which produce colorized output using fatih's color package.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Colorized JSON output for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fatih/color)

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
