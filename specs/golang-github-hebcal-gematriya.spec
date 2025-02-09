# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/hebcal/gematriya
%global goipath         github.com/hebcal/gematriya
Version:                1.0.1

%gometa -f


%global common_description %{expand:
Simple Go implementation of gematriya, a system of writing numbers as Hebrew
letters.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Simple Go implementation of gematriya, a system of writing numbers as Hebrew letters

License:        BSD-2-Clause
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
