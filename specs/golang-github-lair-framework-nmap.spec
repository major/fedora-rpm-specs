# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/lair-framework/go-nmap
%global goipath         github.com/lair-framework/go-nmap
%global commit          3507e0b0352360eb4a7e7437de7be5c1c3e31fdf

%gometa

%global common_description %{expand:
Nmap XML parsing library for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Nmap XML parsing library

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