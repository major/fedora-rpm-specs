# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/danwakefield/fnmatch
%global goipath         github.com/danwakefield/fnmatch
%global commit          cbb64ac3d964b81592e64f957ad53df015803288

%gometa

%global common_description %{expand:
Fnmatch implementation in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Fnmatch implementation in Go

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
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