# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/moul/http2curl
%global goipath         moul.io/http2curl
%global forgeurl        https://github.com/moul/http2curl
Version:                2.3.0

%gometa

%global common_description %{expand:
Convert Golang's http.Request to curl commands.}

%global golicenses      LICENSE-APACHE LICENSE-MIT COPYRIGHT
%global godocs          README.md AUTHORS

Name:           %{goname}
Release:        %autorelease
Summary:        Convert Golang's http.Request to curl commands

# Upstream license specification: MIT and Apache-2.0
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
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

