# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/jackc/chunkreader/v2
%global goipath         github.com/jackc/chunkreader/v2
Version:                2.0.1

%gometa

%global common_description %{expand:
Package Chunkreader provides an io.Reader wrapper that minimizes IO reads and
memory allocations.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        io.Reader wrapper that minimizes IO reads and memory allocations

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