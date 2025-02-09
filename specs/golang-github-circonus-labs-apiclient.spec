# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/circonus-labs/go-apiclient
%global goipath         github.com/circonus-labs/go-apiclient
Version:                0.7.10

%gometa

%global common_description %{expand:
Package Apiclient provides methods for interacting with the Circonus API. See
the full Circonus API Documentation at https://login.circonus.com/resources/api
for more information. }

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md examples

Name:           %{goname}
Release:        %autorelease
Summary:        Circonus api client

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)
BuildRequires:  golang(github.com/pkg/errors)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%gopkgfiles

%changelog
%autochangelog
