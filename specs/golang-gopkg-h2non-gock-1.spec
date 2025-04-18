# Generated by go2rpm 1
# https://github.com/h2non/gock/issues/80
%bcond_with check
%global debug_package %{nil}


# https://github.com/h2non/gock
%global goipath         gopkg.in/h2non/gock.v1
%global forgeurl        https://github.com/h2non/gock
Version:                1.0.16

%gometa

%global goaltipaths     github.com/h2non/gock

%global common_description %{expand:
Versatile HTTP mocking made easy in Go for net/http stdlib package.}

%global golicenses      LICENSE
%global godocs          _examples History.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Expressive HTTP traffic mocking and testing made easy in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/h2non/parth)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/nbio/st)
%endif

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
