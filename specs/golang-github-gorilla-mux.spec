# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/gorilla/mux
%global goipath         github.com/gorilla/mux
Version:                1.8.1

%gometa -L -f

%global common_description %{expand:
Package gorilla/mux implements a request router and dispatcher for matching
incoming requests to their respective handler.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of registered
routes and calls a handler for the route that matches the URL or other
conditions. The main features are:

 - It implements the http.Handler interface so it is compatible with the
   standard http.ServeMux.
 - Requests can be matched based on URL host, path, path prefix, schemes,
   header and query values, HTTP methods or using custom matchers.
 - URL hosts, paths and query values can have variables with an optional
   regular expression.
 - Registered URLs can be built, or "reversed", which helps maintaining
   references to resources.
 - Routes can be used as subrouters: nested routes are only tested if the
   parent route matches. This is useful to define groups of routes that share
   common conditions like a host, a path prefix or other repeated attributes.
   As a bonus, this optimizes request matching.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-gorilla-mux
Release:        %autorelease
Summary:        A powerful HTTP router and URL matcher for building Go web servers

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

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