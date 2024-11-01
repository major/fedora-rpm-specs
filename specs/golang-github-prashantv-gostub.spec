# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/prashantv/gostub
%global goipath         github.com/prashantv/gostub
Version:                1.1.0

%gometa -f


%global common_description %{expand:
Gostub is a library to make stubbing in unit tests easy.}

%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Gostub is a library to make stubbing in unit tests easy

License:        MIT
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
