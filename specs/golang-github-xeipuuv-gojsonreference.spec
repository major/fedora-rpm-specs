# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/xeipuuv/gojsonreference
%global goipath         github.com/xeipuuv/gojsonreference
%global commit          bd5ef7bd5415a7ac448318e64f11a24cd21e594b

%gometa

%global common_description %{expand:
An implementation of JSON Reference.}

%global golicenses      LICENSE-APACHE-2.0.txt
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        JSON Reference implementation in Go

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/xeipuuv/gojsonpointer)

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
