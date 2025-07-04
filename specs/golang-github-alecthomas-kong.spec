# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/alecthomas/kong
%global goipath         github.com/alecthomas/kong
Version:                1.12.0

%gometa -f

%global common_description %{expand:
Kong is a command-line parser for Go.}

%global golicenses      COPYING
%global godocs          _examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Command-line parser for Go

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
