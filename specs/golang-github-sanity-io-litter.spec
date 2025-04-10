# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/sanity-io/litter
%global goipath         github.com/sanity-io/litter
Version:                1.5.8

%gometa

%global common_description %{expand:
Litter is a pretty printer library for Go data structures to aid in debugging
and testing.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Pretty printer for Go data structures for debugging and testing

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)

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
