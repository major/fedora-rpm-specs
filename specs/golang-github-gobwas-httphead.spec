# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/gobwas/httphead
%global goipath         github.com/gobwas/httphead
Version:                0.1.0

%gometa

%global common_description %{expand:
Tiny HTTP header value parsing library in go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        HTTP header value parsing library

License:        MIT
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
