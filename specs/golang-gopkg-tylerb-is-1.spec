# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/tylerstillwater/is
%global goipath         gopkg.in/tylerb/is.v1
%global forgeurl        https://github.com/tylerstillwater/is
Version:                1.5
%global tag             v1.5

%gometa

%global common_description %{expand:
Is provides a quick, clean and simple framework for writing Go tests.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Is provides a quick, clean and simple framework for writing Go tests

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
