# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/emersion/go-sasl
%global goipath         github.com/emersion/go-sasl
%global commit          0b9dcfb154ac3d7515b08bc2691a0332800edfe9

%gometa

%global common_description %{expand:
A SASL library written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        SASL library written in Go

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