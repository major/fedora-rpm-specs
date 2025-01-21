Summary:	Macros for aclocal to install configuration files
Summary(pl):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.21
Release:	7%{?dist}
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:	LicenseRef-Callaway-GPLv3-with-exceptions
Source0:	https://downloads.sourceforge.net/project/courier/sysconftool/%{version}/%{name}-%{version}.tar.bz2
Source1:	https://downloads.sourceforge.net/project/courier/sysconftool/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:	https://www.courier-mta.org/KEYS.bin
URL:		https://www.courier-mta.org/sysconftool/
BuildArch:	noarch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnupg2
BuildRequires:  make
BuildRequires:	perl-generators

%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl
sysconftool jest narzędziem, które pomaga instalować pliki
konfiguracyjne aplikacji. sysconftool pozwala na wymienienie
istniejących aplikacji na nowsze wersje bez straty starszych wersji
plików konfiguracyjnych.

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

# make the symlinks relative
ln -sf ../share/sysconftool/sysconftoolcheck %{buildroot}%{_bindir}/
ln -sf ../share/sysconftool/sysconftoolize.pl %{buildroot}%{_bindir}/sysconftoolize

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog *.html NEWS
%{_bindir}/sysconftoolcheck
%{_bindir}/sysconftoolize
%{_datadir}/sysconftool
%{_mandir}/man1/sysconftool.1*
%{_mandir}/man1/sysconftoolcheck.1*
%{_mandir}/man1/sysconftoolize.1*
%{_mandir}/man7/sysconftool.7*
%{_datadir}/aclocal/sysconftool.m4

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.21-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.21-1
- update to 0.21 (#2142594)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 08 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.19-1
- update to 0.19 (#2092189)
- switch to HTTPS in URLs
- verify source GPG signature

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Dominik Mierzejewski <rpm@greysector.net> 0.18-1
- update to 0.18 (#1941115)
- sort BRs alphabetically
- use modern macros
- use license macro

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 13 2013 Dominik Mierzejewski <rpm@greysector.net> 0.17-1
- updated to 0.17
- drop obsolete spec constructs and unnecessary macros
- clean up file list
- include HTML docs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.16-5
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Dominik Mierzejewski <rpm@greysector.net> 0.16-1
- updated to 0.16
- license changed to GPLv3 with OpenSSL exception

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 08 2010 Dominik Mierzejewski <rpm@greysector.net> 0.15-7
- fix source URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.15-4
- fix license tag

* Mon Sep 18 2006 Dominik Mierzejewski <rpm@greysector.net> 0.15-3
- mass rebuild
- simplify autotools invocation

* Sun Jul 30 2006 Dominik Mierzejewski <rpm@greysector.net> 0.15-2
- bump the release to fix tag and build

* Sun Jan 08 2006 Dominik Mierzejewski <rpm@greysector.net> 0.15-1
- FE compliance
- updated to 0.15

* Sat Jun 18 2005 Dominik Mierzejewski <rpm@greysector.net> 0.14-1
- adapted for Fedora Core from PLD spec
