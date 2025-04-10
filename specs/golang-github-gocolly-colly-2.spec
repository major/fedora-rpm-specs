# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/gocolly/colly
%global goipath         github.com/gocolly/colly/v2
Version:                2.1.0
%global commit          2f09941613011bfde62cbe4a695310b42bf42d41

%gometa

%global common_description %{expand:
Elegant Scraper and Crawler Framework for Golang.}

%global golicenses      LICENSE.txt
%global godocs          _examples CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Elegant Scraper and Crawler Framework for Golang

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/antchfx/htmlquery)
BuildRequires:  golang(github.com/antchfx/xmlquery)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/jawher/mow.cli)
BuildRequires:  golang(github.com/kennygrant/sanitize)
BuildRequires:  golang(github.com/PuerkitoBio/goquery)
BuildRequires:  golang(github.com/saintfish/chardet)
BuildRequires:  golang(github.com/temoto/robotstxt)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/charset)
BuildRequires:  golang(google.golang.org/appengine/urlfetch)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.txt
%doc _examples CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
