# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/markbates/safe
%global goipath         github.com/markbates/safe
Version:                1.0.1

%gometa

%global common_description %{expand:
Safe for Go.}

%global golicenses      LICENSE
%global godocs          shoulders.md

Name:           %{goname}
Release:        %autorelease
Summary:        Safe for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
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
