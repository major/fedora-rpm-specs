# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://git.sr.ht/~spc/go-log
%global goipath         git.sr.ht/~spc/go-log
%global forgeurl        https://git.sr.ht/~spc/go-log
Version:                0.1.0
%global repo            go-log
%global archivename     %{repo}-%{version}
%global archiveext      tar.gz
%global archiveurl      %{forgeurl}/archive/%{version}.%{archiveext}
%global topdir          %{repo}-%{version}

%gometa

%global common_description %{expand:
Package log implements a simple level logging package that maintains API
compatibility with the standard library log package. It extends the standard
library log.Logger type with a Level type that can be used to define output
verbosity. It adds additional methods that will be printed only if the logger
is configured at or below a given level.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        None

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
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