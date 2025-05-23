# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/iij/doapi
%global goipath         github.com/iij/doapi
%global commit          0bbf12d6d7dfbba49740730208c418ece866a22b

%gometa

%global common_description %{expand:
Golang binding for DO API.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Golang binding for DO API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/sirupsen/logrus)

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
