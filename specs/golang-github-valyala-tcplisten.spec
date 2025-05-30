# Generated by go2rpm 1.5
# Checks needs to communicate with a third-party system
%bcond_with check
%global debug_package %{nil}


# https://github.com/valyala/tcplisten
%global goipath         github.com/valyala/tcplisten
Version:                1.0.0

%gometa

%global common_description %{expand:
Customizable TCP net.Listener for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Customizable TCP net.Listener for Go

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
