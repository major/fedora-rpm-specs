Name:       ibus-fbterm
Version:    1.0.2
Release:    7%{?dist}
Summary:    IBus front-end for fbterm
License:    GPL-3.0-only
URL:        https://github.com/fujiwarat/ibus-fbterm
Source0:    https://github.com/fujiwarat/ibus-fbterm/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0: ibus-fbterm-c99.patch

Requires:      ibus >= 1.5, fbterm >= 1.6
BuildRequires: gcc
BuildRequires: ibus >= 1.5, ibus-devel >= 1.5
BuildRequires: make
BuildRequires: autoconf automake
BuildRequires: vala

%description
ibus-fbterm is a input method for FbTerm based on IBus.

* To utilize framebuffer, user should be added into 'video' group, or install
  fbterm-udevrules package.

%prep
%autosetup -p1
# Trigger recompilation of all Vala sources.
find -name '*.vala' -exec touch {} \;

%build
autoreconf -iv
%configure \
    --prefix=%{_prefix}
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README
%{_bindir}/ibus-fbterm
%{_libexecdir}/ibus-fbterm-backend
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Florian Weimer <fweimer@redhat.com> - 1.0.2-4
- GCC 14 compatibility fix & Vala rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.2-1
- Bump to 1.0.2

* Sun Dec 11 2022 Florian Weimer <fweimer@redhat.com> - 1.0.1-17
- Port to C99
- Run autoreconf during the build.

* Wed Nov 16 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.1-16
- Migrate license tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.1-9
- Add BR: gcc

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.1-1
- Bumped to 1.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.0-1
- Bumped to 1.0.0

* Wed Jul 08 2015 Takao Fujiwara <tfujiwar@redhat.com> - 0.9.1-22
- Added ibus-fbterm-02-preedit-text.patch
- Added ibus-fbterm-03-status-bar.patch

* Tue Jun 23 2015 Takao Fujiwara <tfujiwar@redhat.com> - 0.9.1-21
- Bug 1233481: Updated ibus-fbterm-xx-build-error.patch to work with ibus 1.5.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Takao Fujiwara <tfujiwar@redhat.com> - 0.9.1-14
- Rebuilt for ibus 1.4.99.20120304
- Added ibus-fbterm-xx-build-error.patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Ding-Yi Chen <dchen at redhat.com> - 0.9.1-11
- Rebuild for F-15 to resolve unresolved deps: libibus.so.2

* Wed Sep 29 2010 jkeating - 0.9.1-10
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Ding-Yi Chen <dchen at redhat.com> - 0.9.1-9
- Rebuild for F-12 to resolve unresolved deps: libibus.so.1

* Sun Feb 28 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 0.9.1-7
- Change group tag.
- Remove dist tag in changelog.

* Fri Feb 26 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 0.9.1-6.fc14
- Allow /dev/fb0 (framebuffer) permission and setcap be handled by fbterm and
  fbterm-udevrules.

* Mon Feb 15 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 0.9.1-5
- Fix attribute of framebuffer (fb0) for user access.

* Mon Feb 15 2010 Caius 'kaio' Chance  <k at kaio.me> - 0.9.1-4
- Removed BuildArch tag.

* Fri Jan 22 2010 Caius 'kaio' Chance  <k at kaio.me> - 0.9.1-3
- Fixed for launching on shell other than bash.

* Wed Jan 20 2010 Caius 'kaio' Chance  <k at kaio.me> - 0.9.1-2
- Updated description.
- Added ibus-devel to BuildRequires.

* Wed Jan 20 2010 Caius 'kaio' Chance  <k at kaio.me> - 0.9.1-1
- Introdution.
