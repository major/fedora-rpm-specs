# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/reiver/go-telnet
%global goipath         github.com/reiver/go-telnet
%global commit          9ff0b2ab096ebe42bf8e2ffd1366e7ed2223b04c

%gometa

%global common_description %{expand:
Package telnet provides telnet(s) client and server implementations,
for the Go programming language, in a style similar to the "net/http" library
that is part of the Go standard library, including support for middleware.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Telnet(s) client and server implementations

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/reiver/go-oi)

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
