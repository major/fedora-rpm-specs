%define binname aria2c

Name:           aria2
Version:        1.37.0
Release:        6%{?dist}
Summary:        High speed download utility with resuming and segmented downloading
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            http://aria2.github.io/
Source0:        https://github.com/aria2/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  c-ares-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  sqlite-devel
BuildRequires:  git-core

%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent. It also supports Metalink
version 3.0.

Currently it has following features:
- HTTP/HTTPS GET support
- HTTP Proxy support
- HTTP BASIC authentication support
- HTTP Proxy authentication support
- FTP support(active, passive mode)
- FTP through HTTP proxy(GET command or tunneling)
- Segmented download
- Cookie support
- It can run as a daemon process.
- BitTorrent protocol support with fast extension.
- Selective download in multi-file torrent
- Metalink version 3.0 support(HTTP/FTP/BitTorrent).
- Limiting download/upload speed

%prep
%autosetup -S git

%build
%configure CXX="g++" \
           --enable-bittorrent \
           --enable-metalink \
           --enable-epoll\
           --disable-rpath \
           --with-gnutls \
           --with-libcares \
           --with-libxml2 \
           --without-openssl \
           --with-libz \
           --with-sqlite3 \
%if 0%{?fedora}
           --enable-gnutls-system-crypto-policy \
%endif


V=1 make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%check
# fails atm
#make check

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README 
%{_bindir}/%{binname}
%{_mandir}/man1/aria2c.1.gz
%{_mandir}/*/man1/aria2c.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.37.0-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Neil Hanlon <neil@shrug.pw> - 1.37.0-1
- update to 1.37 (fedora#2249918)
- change URL to aria2 organization as it was moved from the prior org

* Sat Oct 28 2023 Neil Hanlon <neil@shrug.pw> - 1.36.0-6
- resolves crash due to undefined behavior in GZipEncoder (rhbz #2119478)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Othman Madjoudj <athmane@fedoraproject.org> - 1.36.0-1
- Update to 1.36.0 (rhbz #1996295)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 1.35.0-4
- No longer force C++11 mode

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Othman Madjoudj <athmane@fedoraproject.org> - 1.35.0-1
- Update to 1.35.0 (rhbz #1758829)
- Drop the backport patches

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 1.34.0-5
- Enable gnutls-system-crypto-policy only in Fedora (rhbz #1704413)

* Wed Mar 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 1.34.0-4
- Fix Password leak for HTTP based authentication CVE-2019-3500 (rhbz #1663991 #1663992 #1663993)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.34.0-1
- Update to 1.34.0 (rhbz #1580169)

* Sun Feb 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.33.1-3
- Refactor BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.33.1-1
- Update to 1.33.1 (rhbz #1514761)

* Wed Nov 08 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.33.0-1
- Update to 1.33.0 (rhbz #1510674)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 19 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.31.0-1
- Update to 1.31.0

* Fri Dec 16 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.30.0-1
- Update o 1.30.0

* Sat Dec 03 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.29.0-1
- Update to 1.29.0

* Sat Oct 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.28.0-1
- Update to 1.28.0

* Mon Oct 03 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.27.1-1
- Updat to 1.27.1

* Fri Sep 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.26.1-1
- Update to 1.26.1

* Sat Aug 27 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Thu Jul 21 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.25.0-1
- Update to 1.25.0
- Enable testsuite exec

* Sat Jun 25 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0

* Fri Jun 10 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.23.0-1
- Update to 1.23.0

* Fri Apr 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0

* Thu Mar 17 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.21.0-1
- Update to 1.21.0
- Remove upstreamed patch

* Tue Feb 16 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.20.0-1
- Update to 1.20.0
- Rebase Use system wide crypto policies patch
- Fix configure options

* Sun Feb 14 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.19.3-4
- Use current ISO C++ name

* Sat Feb 13 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.19.3-3
- Fix build issue with GCC 6.0 (RHBZ #1307327)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.19.3-1
- Update to 1.19.3
- Fix Source and URL since upsteam moved to Github
- Rebase Use system wide crypto policies patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Athmane Madjoudj <athmane@fedoraproject.org> 1.19.0-1
- Update to 1.19.0

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.18.10-4
- Rebuilt for nettle soname bump

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.18.10-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Athmane Madjoudj <athmane@fedoraproject.org> 1.18.10-2
- Add a patch to use system-wide crypto-policies (RHBZ #1179277)

* Fri Feb 27 2015 Athmane Madjoudj <athmane@fedoraproject.org> 1.18.10-1
- Update to 1.18.10 (RHBZ #1123979)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 1.18.6-1
- update to 1.18.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.18.2-1
- upstream release 1.18.2 (rhbz#967784)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.17.0-1
- update to 1.17.0
- drop upstream build patch
- switch to verbose make
- switch to make_install macro

* Wed Mar  6 2013 Tomáš Mráz <tmraz@redhat.com> - 1.16.1-2
- rebuilt with new gnutls

* Fri Jan 25 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.16.1-1
- upstream release 1.16.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Tom Callaway <spot@fedoraproject.org> - 1.14.2-1
- update to 1.14.2
- fix compile issues with gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.14.0-1
- update to 1.14.0
- https://github.com/tatsuhiro-t/aria2/blob/3dc6d2ff6df5a33f6abf47b4e792ea7dd578cf9a/NEWS

* Mon Aug 15 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.12.1-1
- https://github.com/tatsuhiro-t/aria2/commit/bd3956293995bcbbb76e6c8686b4ac8dfd3c9ed4#NEWS
- Additional man page

* Sun May 22 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.11.2-1
- https://github.com/tatsuhiro-t/aria2/commit/f6625f8dc5557e77fcace9bedaf1815c5eaf763f#NEWS
- Drop defattr since it is set by default in recent rpm

* Sun Apr 10 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.11.1-1
- https://github.com/tatsuhiro-t/aria2/blob/8d8fb31a45f66a29c78911293a60a00ac4903795/NEWS

* Tue Feb 22 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.10.9-1
- https://github.com/tatsuhiro-t/aria2/blob/6af3cd82b36190b12102bf3fbc5c07cc494627ad/NEWS

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.10.8-1
- https://github.com/tatsuhiro-t/aria2/blob/6af3cd82b36190b12102bf3fbc5c07cc494627ad/NEWS

* Sat Nov 27 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.10.6-1
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=2479

* Fri Jul 30 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.10.0-1
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=2279
- Dropped clean section

* Tue Jun 08 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.9.4-1
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=2133

* Sat Mar 20 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.9.0-1
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1990 

* Tue Feb 16 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8.2-1
- Several bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1860

* Mon Dec 28 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8.0-1
- Many new features including XML RPC improvements and other bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1778
 
* Mon Dec 07 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.7.1-1
- Option --bt-prioritize-piece=tail will work again
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1721

* Wed Nov 04 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.3-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1616

* Sat Oct 10 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.2-1
- Minor bug fixes and switch XZ compressed source 
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1586

* Thu Oct 08 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.1-1
- Fixes memory leak in HTTP/FTP downloads and other minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1569

* Wed Sep 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1544

* Mon Aug 24 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.2-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1504

* Mon Jul 27 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.1-2
- update source

* Mon Jul 27 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.1-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1494
- Fixed the license tag

* Sun Jul 26 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.0-1
- Mostly minor bug fixes 
- WEB-Seeding support for multi-file torrent
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1476

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Robert Scheck <robert@fedoraproject.org> - 1.3.1-1
- Upgrade to 1.3.1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Michał Bentkowski <mr.ecik at gmail.com> - 1.0.1-2
- New version, 1.0.1
- Forgot to add changelog in last release...

* Tue Jun 24 2008 Tomas Mraz <tmraz@redhat.com> - 0.12.0-5
- rebuild with new gnutls

* Fri Feb 22 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.12.0-4
- Add patch

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12.0-3
- Autorebuild for GCC 4.3

* Mon Dec 31 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.12.0-2
- Get rid of odd locale.alias

* Mon Dec 31 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.12.0-1
- 0.12.0

* Thu Sep 20 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.11.3-1
- 0.11.3

* Fri Aug 24 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.11.2-1
- 0.11.2
- Fix License tag

* Mon Jul 09 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.11.1-1
- Update to 0.11.1

* Sat Apr 28 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.10.2+1-1
- Update to 0.10.2+1

* Tue Feb 20 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.10.1-1
- Update to 0.10.1

* Sun Dec 31 2006 Michał Bentkowski <mr.ecik at gmail.com> - 0.9.0-2
- Small fix in Summary

* Sat Dec 30 2006 Michał Bentkowski <mr.ecik at gmail.com> - 0.9.0-1
- Initial release
