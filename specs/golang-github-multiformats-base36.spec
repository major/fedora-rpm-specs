# Generated by go2rpm 1.6.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/multiformats/go-base36
%global goipath         github.com/multiformats/go-base36
Version:                0.1.0

%gometa

%global common_description %{expand:
Optimized codec for []byte <=> base36 string conversion.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Optimized codec for []byte <=> base36 string conversion

# Automatically converted from old format: ASL 2.0 or MIT - review is highly recommended.
License:        Apache-2.0 OR LicenseRef-Callaway-MIT
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
