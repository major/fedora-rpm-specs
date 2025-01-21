Name:           tintin 
Version:        2.02.30
Release:        7%{?dist}
Summary:        TinTin++, aka tt++, is a free MUD client
License:        GPL-3.0-only
URL:            http://%{name}.mudhalla.net/
Source0:        https://github.com/scandum/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# Build
BuildRequires:  bash
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  sed
# Runtime
BuildRequires:  gnutls-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel

%description
TinTin++, aka tt++, is a free MUD client for Mac OS X, Linux, and Windows. The
Windows port named WinTin++ (using the PuTTY terminal) is available for
those who do not use Cygwin (A Linux/Unix emulator for Windows) and runs on
Windows XP, Windows Vista, and Windows 7. Besides MUDs, TinTin++ also works
well with MUSH, Rogue, BBS, and Linux servers.

%package doc
Summary:        TinTin++ documentation and examples
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
BuildArch:      noarch

%description doc
TinTin++, aka tt++, MUD client documentation and examples.

%prep
%autosetup -n tt
find . -type f -exec chmod 644 {} +
chmod a+x src/configure

%build
cd src
%configure
%make_build

%install
cd src
%make_install

%files
%license COPYING
%doc CREDITS FAQ README TODO
%doc mods
%{_bindir}/tt++

%files doc
%license COPYING
%doc SCRIPTS
%doc docs/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.02.30-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Petr Šabata <contyk@redhat.com> - 2.02.30-1
- 2.02.30 bump
- License correction; GPLv3 since 2.01.8
- SPDX migration

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 Petr Šabata <contyk@redhat.com> - 2.02.05-1
- 2.02.05 bump

* Sat Oct 31 2020 zsh:1: command not found: rpm - 2.02.04-1
- 2.02.04 bump
- Now hosted on GitHub
- Switch to using the unified build macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Petr Šabata <contyk@redhat.com> - 2.02.03-1
- 2.02.03 bump

* Wed Apr 15 2020 Petr Šabata <contyk@redhat.com> - 2.02.02-1
- 2.02.02 bump

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Petr Šabata <contyk@redhat.com> - 2.01.7-1
- 2.01.7 bump

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Petr Šabata <contyk@redhat.com> - 2.01.6-1
- 2.01.6 bump

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Petr Šabata <contyk@redhat.com> - 2.01.4-1
- 2.01.4 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Petr Šabata <contyk@redhat.com> - 2.01.3-1
- 2.01.3 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Petr Šabata <contyk@redhat.com> - 2.01.2-1
- 2.01.2 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.01.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Petr Šabata <contyk@redhat.com> - 2.01.1-3
- Build tintin++ with gnutls (#1291508)
- Correct the dep list; hopefully we got everything

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Petr Šabata <contyk@redhat.com> - 2.01.1-1
- 2.01.1 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Petr Šabata <contyk@redhat.com> - 2.01.0-1
- 2.01 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Petr Šabata <contyk@redhat.com> - 2.00.9-1
- 2.00.9 bump
- Fix the source file permissions once again

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.00.8-2
- Rebuild against PCRE 8.30

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 2.00.8-1
- 2.00.8 bump

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Petr Sabata <contyk@redhat.com> - 2.00.7-1
- 2.00.7 bump
- Removing now obsolete defattr

* Mon Mar 14 2011 Petr Sabata <psabata@redhat.com> - 2.00.6-1
- 2.00.6 bump
- Removing obsolete attr definitions and utf8 conversion
- Upstream now supports DESTDIR, removing the DESTDIR patch

* Wed Feb 16 2011 Petr Sabata <psabata@redhat.com> - 2.00.5-4
- Changed documentation files structure, removed chmod's in favor of attr's
- Thanks to William Lima

* Tue Feb 15 2011 Petr Sabata <psabata@redhat.com> - 2.00.5-3
- igr.mods now gets converted to proper utf8

* Tue Feb 15 2011 Petr Sabata <psabata@redhat.com> - 2.00.5-2
- Source corrected
- Description spelling corrected
- TODO and Changelogs packaged, COPYING added to the doc package
- Changed build section, added DESTDIR patch

* Tue Feb 15 2011 Petr Sabata <psabata@redhat.com> - 2.00.5-1
- Package prepared for review
