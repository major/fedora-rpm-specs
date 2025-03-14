# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/sacloud/packages-go
%global goipath         github.com/sacloud/packages-go
Version:                0.0.9

%gometa -f

%global common_description %{expand:
Packages à usage général pour SAKURA Cloud API Library}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Packages à usage général pour SAKURA Cloud API Library

License:        Apache-2.0
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
