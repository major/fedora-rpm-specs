# Generated by go2rpm 1.5.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/artyom/mtab
%global goipath         github.com/artyom/mtab
%global commit          c69458cf5bb138371c6061180ae482fcb8afe721

%gometa

%global golicenses      LICENSE.txt

%global common_description %{expand:
Package to read /proc/self/mounts entries.}

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Package to read /proc/self/mounts entries

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
