# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/valyala/fasttemplate
%global goipath         github.com/valyala/fasttemplate
Version:                1.2.1

%gometa

%global common_description %{expand:
Simple and fast template engine for Go.

Fasttemplate performs only a single task - it substitutes template placeholders
with user-defined values.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Simple and fast template engine for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/valyala/bytebufferpool)

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