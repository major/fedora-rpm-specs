# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/gorilla/websocket
%global goipath         github.com/gorilla/websocket
Version:                1.5.0

%gometa

%global common_description %{expand:
A fast, well-tested and widely used WebSocket implementation for Go.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A fast, well-tested and widely used WebSocket implementation for Go

License:        BSD-2-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
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