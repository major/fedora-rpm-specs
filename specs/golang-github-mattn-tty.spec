# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/mattn/go-tty
%global goipath         github.com/mattn/go-tty
Version:                0.0.4

%gometa

%global common_description %{expand:
Simple tty utility.}

%global golicenses      LICENSE
%global godocs          _example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Simple tty utility

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mattn/go-colorable) >= 0.1.4
BuildRequires:  golang(github.com/mattn/go-isatty) >= 0.0.10
BuildRequires:  golang(github.com/mattn/go-runewidth) >= 0.0.7
BuildRequires:  golang(golang.org/x/sys/unix)

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