# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/naoina/go-stringutil
%global goipath         github.com/naoina/go-stringutil
Version:                0.1.0

%gometa

%global common_description %{expand:
Faster string utilities implementation for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Faster string utilities implementation for Go

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