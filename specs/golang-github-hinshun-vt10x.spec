# Generated by go2rpm 1.1
%bcond_without check

%global debug_package %{nil}

# https://github.com/hinshun/vt10x
%global goipath         github.com/hinshun/vt10x
%global commit          52c1408d37d6fe4e9261f48c11806c7403af2c84

%gometa

%global common_description %{expand:
Package vt10x is a vt10x terminal emulation backend.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Package vt10x is a vt10x terminal emulation backend

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gdamore/tcell)
BuildRequires:  golang(github.com/kr/pty)

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