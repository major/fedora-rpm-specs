# Generated by go2rpm
# Needs network
%bcond_with check
%global debug_package %{nil}


# https://github.com/hudl/fargo
%global goipath         github.com/hudl/fargo
Version:                1.4.0

%gometa

%global common_description %{expand:
Golang client for Netflix Eureka.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Golang client for Netflix Eureka

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/clbanning/x2j)
BuildRequires:  golang(github.com/franela/goreq)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/op/go-logging)
BuildRequires:  golang(gopkg.in/gcfg.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -e '0,/^# MIT LICENSE/d' README.md > LICENSE

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog

