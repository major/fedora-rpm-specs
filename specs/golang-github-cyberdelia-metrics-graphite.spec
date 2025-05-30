# Generated by go2rpm 1.3
# Needs network
%bcond_with check
%global debug_package %{nil}


# https://github.com/cyberdelia/go-metrics-graphite
%global goipath         github.com/cyberdelia/go-metrics-graphite
%global commit          39f87cc3b432bbb898d7c643c0e93cac2bc865ad

%gometa

%global common_description %{expand:
This is a reporter for the go-metrics library which will post the metrics to
Graphite. It was originally part of the go-metrics library itself, but has been
split off to make maintenance of both the core library and the client easier.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Graphite client for the go-metrics

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/rcrowley/go-metrics)

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
