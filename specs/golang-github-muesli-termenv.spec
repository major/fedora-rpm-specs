# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/muesli/termenv
%global goipath         github.com/muesli/termenv
Version:                0.15.2

%gometa

%global common_description %{expand:
Advanced ANSI style & color support for your terminal applications.}

%global golicenses      LICENSE
%global godocs          examples README.md ansi_compat.md

Name:           %{goname}
Release:        %autorelease
Summary:        Advanced ANSI style & color support for your terminal applications

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

# examples have extra dependencies
rm -rf examples

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