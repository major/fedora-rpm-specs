# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/ssgelm/cookiejarparser
%global goipath         github.com/ssgelm/cookiejarparser
Version:                1.0.1

%gometa

%global common_description %{expand:
A Go library that parses a curl (netscape) cookiejar file into a Go
http.CookieJar.}

%global golicenses      LICENSE.md
%global godocs          README.md data/cookies.txt

Name:           %{goname}
Release:        %autorelease
Summary:        Parses a curl cookiejar file into a Go http.CookieJar

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/publicsuffix)

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