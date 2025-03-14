# Generated by go2rpm 1.5.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/moby/spdystream
%global goipath         github.com/moby/spdystream
Version:                0.2.0

%gometa

%global common_description %{expand:
A multiplexed stream library using spdy.}

%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A multiplexed stream library using spdy

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gorilla/websocket)

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
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-1
- convert license to SPDX

* Wed Aug 18 2021 Robert-André Mauchin <zebob.m@gmail.com> 0.2.0-2
- Uncommitted changes

* Sat Aug 14 2021 Robert-André Mauchin <zebob.m@gmail.com> 0.2.0-1
- Initial release
