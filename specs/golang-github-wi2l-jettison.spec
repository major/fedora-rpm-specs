# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/wI2L/jettison
%global goipath         github.com/wI2L/jettison
Version:                0.7.4

%gometa -f

%global common_description %{expand:
Highly configurable, fast JSON encoder for Go.}

%global golicenses      LICENSE LICENSE.golang
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Highly configurable, fast JSON encoder for Go

License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
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
