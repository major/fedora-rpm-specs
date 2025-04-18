# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/clbanning/x2j
%global goipath         github.com/clbanning/x2j
Version:                1.1
%global tag             1.1

%gometa

%global common_description %{expand:
Unmarshal an anonymous xml doc to map[string]interface{} and json, and extract
values (using wildcards, if necessary).}

%global golicenses      LICENSE
%global godocs          examples README

Name:           %{goname}
Release:        %autorelease
Summary:        Unmarshal an anonymous xml doc to map[string]interface{} and json

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}
# Dead upstream, downstream patch only
Patch0:         0001-Remove-redundant-newlines-in-Println-statement.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
