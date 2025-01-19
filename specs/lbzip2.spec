%global commit b6dc48a7b9bfe6b340ed1f6d72133608ad57144b
%global date 20171011
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lbzip2
Version:        2.5
Release:        32.%{date}git%{shortcommit}%{?dist}
Summary:        Fast, multi-threaded bzip2 utility
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/kjn/lbzip2/
Source0:        https://github.com/kjn/lbzip2/archive/%{commit}/%{name}-%{commit}.tar.gz
# fix build with gnulib newer than 47bae8a, which requires autoconf >= 2.64
Patch0:         lbzip2-gnulib.patch
Patch1: lbzip2-c99.patch

BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  make
BuildRequires:  perl-interpreter


%description
lbzip2 is an independent, multi-threaded implementation of bzip2. It is
commonly the fastest SMP (and uniprocessor) bzip2 compressor and
decompressor.


%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1


%build
build-aux/autogen.sh
%configure --enable-warnings
%make_build V=1


%install
%make_install


%check
%make_build check


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_bindir}/lbzcat
%{_bindir}/lbunzip2
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/lbzcat.1*
%doc %{_mandir}/man1/lbunzip2.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-32.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-31.20171011gitb6dc48a
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-30.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-29.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-28.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-27.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-26.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Florian Weimer <fweimer@redhat.com> - 2.5-25.20171011gitb6dc48a
- Fix C99 compatibility issue

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-24.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022 Jeff Law <jeffreyalaw@gmail.com> - 2.5-23.20171011gitb6dc48a
- Re-enable LTO.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-22.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-21.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-20.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.5-19.20171011gitb6dc48a
- fix FTBFS with recent gnulib

* Fri Aug 21 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.5-18.20171011gitb6dc48a
- opt out of LTO to fix testsuite on s390x (#1871087)

* Fri Aug 21 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.5-17.20171011gitb6dc48a
- disable testsuite on s390x (#1871087)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-16.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15.20171011gitb6dc48a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.5-14.20171011gitb6dc48a
- update to latest git snapshot
- switch URL to github project page, the original seems to have expired
  and got taken over
- use license macro and other modern macros
- add missing build dependencies

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 2.5-10
- Add BR on gcc and make
- Remove Group tag and defattr

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-1
- Update to upstream version 2.5

* Wed Mar 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-4
- Add patch for performance regression during compression

* Wed Mar 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-3
- Fix a typo in compression order block patch

* Wed Mar 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-2
- Add patch fixing block ordering during compression

* Mon Mar 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-1
- Update to upstream version 2.4

* Sun Dec 22 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3-3
- Drop INSTALL from docs.
- Fix bogus dates in %%changelog.
- Use bzipped source tarball.

* Sun Oct 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-2
- Add patch to fix sefgault during decompression
- Resolves: rhbz#1017957
- Update upstream URLs

* Tue Oct 15 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.3-1
- Version bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.2-1
- version bump to 2.2

* Fri Jul 27 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.1-5
- new upstream release fixes gnu lib (gl1)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.1-3
- 829461 - Run unit tests during build

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.1-1
- update to 2.1 security release

* Tue Nov 22 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.0-2
- fixing license to GPLv3+
- fixed dependencies
- better description

* Sat Nov 19 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.0-1
- new package with autotools

* Thu Jun 02 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.23-3
- EPEL package
- removing dash dependency

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Lukas Zapletal <lzap+spam@redhat.com> - 0.23-2
- Updated files section and patches description

* Thu Nov 25 2010 Lukas Zapletal <lzap+spam@redhat.com> - 0.23-1
- Initial packaging done by original author Laszlo Ersek.
