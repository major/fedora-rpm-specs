# Generated by go2rpm 1.15.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/gohugoio/httpcache
%global goipath         github.com/gohugoio/httpcache
Version:                0.7.0

%gometa -L -f

%global common_description %{expand:
A Transport for http.Client that will cache responses according to the HTTP
RFC.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           golang-github-gohugoio-httpcache
Release:        %autorelease
Summary:        A Transport for http.Client that will cache responses according to the HTTP RFC

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
