# Generated by go2rpm 1
# fork has diverged from upstream while relying on said upstream for comparison
# in test: https://github.com/pingcap/errors/issues/14
%global debug_package %{nil}

%bcond_with check

# https://github.com/pingcap/errors
%global goipath         github.com/pingcap/errors
Version:                0.11.4

%gometa

%global common_description %{expand:
Simple error handling primitives.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Simple error handling primitives

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/pkg/errors)
%endif

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
