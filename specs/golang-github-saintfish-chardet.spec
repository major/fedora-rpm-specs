# Generated by go2rpm 1.2
%bcond_without check

%global debug_package %{nil}

# https://github.com/saintfish/chardet
%global goipath         github.com/saintfish/chardet
%global commit          3af4cd4741ca4f3eb0c407c034571a6fb0ea529c

%gometa

%global common_description %{expand:
Charset detector library for Golang derived from ICU.}

%global golicenses      LICENSE icu-license.html
%global godocs          AUTHORS README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Charset detector library

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