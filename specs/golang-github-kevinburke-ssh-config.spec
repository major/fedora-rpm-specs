# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/kevinburke/ssh_config
%global goipath         github.com/kevinburke/ssh_config
Version:                1.3

%gometa

%global common_description %{expand:
Package ssh_config provides tools for manipulating SSH config files.

Importantly, this parser attempts to preserve comments in a given file, so you
can manipulate a `ssh_config` file from a program, if your heart desires.

The Get() and GetStrict() functions will attempt to read values from
$HOME/.ssh/config, falling back to /etc/ssh/ssh_config. The first argument is
the host name to match on ("example.com"), and the second argument is the key
you want to retrieve ("Port"). The keywords are case insensitive.}

%global golicenses      LICENSE
%global godocs          AUTHORS.txt CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go parser for ssh_config files

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
