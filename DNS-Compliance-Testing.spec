#!/usr/bin/rpmspec -q
%global commit 4aea40ba0310de10560ba6deaa2d2e6eebbe8f48
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Obtain by Source: date from %%prep
%global date 20230708
%global snapver %{date}git%{shortcommit}

%if 0%{?fedora}
%bcond_without ronn
%else
# EPEL and RHEL do not have rubygem-ronn available
%bcond_with ronn
%endif

Name:		DNS-Compliance-Testing
Version:	0%{?snapver:^%snapver}
Release:	%autorelease
Summary:	DNS Compliance Testing command line tool

License:	MPL-2.0
URL:		https://gitlab.isc.org/isc-projects/DNS-Compliance-Testing
Source0:	%{url}/-/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.bz2
# https://gitlab.isc.org/isc-projects/DNS-Compliance-Testing/-/merge_requests/17
Source1:	mkronn.sed
Source2:	Makefile.doc

# https://gitlab.isc.org/isc-projects/DNS-Compliance-Testing/-/merge_requests/16
Patch1:		0001-Detect-few-functions-presence-in-libresolv.patch

BuildRequires:	gcc make autoconf automake
BuildRequires:	openssl-devel
%if %{with ronn}
BuildRequires:	sed rubygem-ronn
%endif
Requires:	bind-utils

%description
Provide tools to allow Registries and Registrars (amongst others) to
check the DNS protocol compliance of the servers they are delegating
zones to.

Offers genreport command line tool. Can test both authoritative and
recursive servers.

%prep
%autosetup -n %{name}-%{shortcommit} -p1
echo "Source: date $(date "+%04Y%02m%02d" -r %{SOURCE0})"

%if %{with ronn}
	install %{SOURCE1} mkronn.sed
	install %{SOURCE2} Makefile.doc
%endif

%build
autoreconf -fis

%configure
%make_build

%if %{with ronn}
	make -f %{SOURCE2} man
%endif

%install
%make_install

%if %{with ronn}
	install -d %{buildroot}%{_mandir}/man1
	install -p -m 0644 genreport.1 %{buildroot}%{_mandir}/man1/genreport.1
%endif


%check
%{buildroot}%{_bindir}/genreport -D


%files
%doc README genreport.md
%license LICENSE
%{_bindir}/genreport
%if %{with ronn}
%{_mandir}/man1/genreport*
%endif

%changelog
%autochangelog
