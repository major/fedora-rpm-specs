# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/bep/tmc
%global goipath         github.com/bep/tmc
Version:                0.5.1

%gometa

%global common_description %{expand:
Provides basic roundtrip JSON etc. encoding/decoding of a
map[string]interface{} with custom type adapters.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Basic map[string]interface{} JSON roundtrip with custom adapters

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/frankban/quicktest)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(gopkg.in/yaml.v2)
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
