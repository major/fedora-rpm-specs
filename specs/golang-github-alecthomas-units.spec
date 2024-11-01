# Generated by go2rpm 1.12.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/alecthomas/units
%global goipath         github.com/alecthomas/units
%global commit          9a357b53e9c9395aa5fa9031ac79dc94111814e1

%gometa -L

%global common_description %{expand:
Helpful unit multipliers and functions for Go.}

%global golicenses      COPYING
%global godocs          README.md

Name:           golang-github-alecthomas-units
Version:        0
Release:        %autorelease -p
Summary:        Helpful unit multipliers and functions for Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
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
