# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/adrg/xdg
%global goipath         github.com/adrg/xdg
Version:                0.5.3

%gometa

%global common_description %{expand:
Go implementation of the XDG Base Directory Specification and XDG user
directories.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go implementation of the XDG Base Directory Specification and XDG user directories

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/stretchr/testify)

%description
%{common_description}

%gopkg

%prep
%goprep

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
