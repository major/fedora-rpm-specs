# Generated by go2rpm 1.11.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/go-openapi/errors
%global goipath         github.com/go-openapi/errors
Version:                0.22.0

%gometa -L

%global common_description %{expand:
Package Errors provides an Error interface and several concrete types
implementing this interface to manage API errors and JSON-schema validation
errors.

A middleware handler ServeError() is provided to serve the errors types it
defines.

It is used throughout the various Go-openapi toolkit libraries.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           golang-github-openapi-errors
Release:        %autorelease
Summary:        Openapi toolkit common errors

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
