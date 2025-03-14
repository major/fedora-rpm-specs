# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/jackc/puddle
%global goipath         github.com/jackc/puddle
Version:                1.1.3

%gometa

%global common_description %{expand:
Generic resource pool for Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Generic resource pool for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
