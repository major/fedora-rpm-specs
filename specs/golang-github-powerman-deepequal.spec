# Generated by go2rpm 1.5.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/powerman/deepequal
%global goipath         github.com/powerman/deepequal
Version:                0.1.0

%gometa

%global common_description %{expand:
Go package with improved reflect.DeepEqual.}

%global golicenses      LICENSE LICENSE-go
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go package with improved reflect.DeepEqual

# Upstream license specification: BSD-3-Clause and MIT
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
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
