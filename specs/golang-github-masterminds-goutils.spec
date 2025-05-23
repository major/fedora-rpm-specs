# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/Masterminds/goutils
%global goipath         github.com/Masterminds/goutils
Version:                1.1.0

%gometa

%global common_description %{expand:
GoUtils is a Go implementation of some string manipulation libraries of Apache
Commons. This is an open source project aimed at providing Go users with
utility functions to manipulate strings in various ways.}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        String manipulation libraries of Apache Commons

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/Masterminds/goutils/pull/32
Patch0:         0001-Explicitly-convert-digits-to-runes-before-strings.patch

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
