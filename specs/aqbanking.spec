Name: aqbanking
Summary: A library for online banking functions and financial data import/export
Version: 6.6.0
Release: 2%{?dist}
# Download is PHP form at http://www.aquamaniac.de/sites/download/packages.php
Source0: https://www.aquamaniac.de/rdm/attachments/download/531/aqbanking-%{version}.tar.gz
License: GPL-2.0-only AND GPL-3.0-only
URL: https://www.aquamaniac.de/rdm/projects/aqbanking

%global majmin %(echo %{version} | cut -d. -f1-2)

BuildRequires: gcc-c++
BuildRequires: gwenhywfar-devel >= 5.0.0
BuildRequires: gmp-devel, gettext, libtool
BuildRequires: xmlsec1-gnutls-devel, xmlsec1-devel, libtool-ltdl-devel, libxslt-devel, libxml2-devel
# For AutoReq cmake-filesystem
BuildRequires: cmake
# bug in xmlscec1
BuildRequires: xmlsec1-gnutls, xmlsec1-gcrypt
BuildRequires: make
Requires: libchipcard
Obsoletes: aqhbci <= 1.0.3
Obsoletes: g2banking < 3.7.2-1 
Obsoletes: qbanking < 5.0
Obsoletes: q4banking < 5.0
Obsoletes: python-aqbanking < 6.0

%description 
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package devel
Summary: Development headers for Aqbanking
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gwenhywfar-devel
Obsoletes: aqhbci-devel <= 1.0.3
Obsoletes: g2banking-devel < 3.7.2-1 
Obsoletes: qbanking-devel < 5.0
Obsoletes: q4banking-devel < 5.0

%description devel
This package contains aqbanking-config and header files for writing and
compiling programs using Aqbanking.


%prep
%autosetup -n %{name}-%{version}

# hack to nuke rpaths, slighly less ugly than using overriding LIBTOOL below
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
# avoid detection/use of stuff like x86_64-redhat-linux-gnu-pkg-config -- rdieter
export PKG_CONFIG=/usr/bin/pkg-config

%configure \
  --disable-static \
  --enable-gui-tests=no \
  --with-build-datetime="$(date +%Y%m%d)"

%make_build


%install

%make_install

## unpackaged files
rm -fv %{buildroot}%{_libdir}/lib*.la

pushd tutorials
make clean
rm -rf .deps
rm -f Makefile*
popd

%find_lang %{name}


%check
## meh, requires X server
make check ||:


%ldconfig_scriptlets

%files -f %{name}.lang
%doc %{_datadir}/doc/%{name}
%{_libdir}/libaqbanking.so.44*
# plugins, plugins, plugins
%{_libdir}/aqbanking/
%{_datadir}/aqbanking
%{_bindir}/aqbanking-cli
%{_bindir}/aqebics-tool
%{_bindir}/aqhbci-tool4
%{_bindir}/aqpaypal-tool
%{_bindir}/aqofxconnect-tool

%files devel
%doc doc/0[12]* tutorials
%{_bindir}/aqbanking-config
%{_libdir}/libaqbanking.so
%{_includedir}/aqbanking6/
%{_libdir}/cmake/aqbanking-%{majmin}/
%{_libdir}/pkgconfig/aqbanking.pc
%{_datadir}/aclocal/aqbanking.m4
%{_datadir}/aqbanking/aqbanking/typemaker2
%{_datadir}/aqbanking/typemaker2


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 6.6.0-1
- 6.6.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 6.5.4-2
- migrated to SPDX license

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 6.5.4-1
- 6.5.4

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 6.5.3-2
- Enable libchipcard.

* Thu Aug 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 6.5.3-1
- 6.5.3

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 6.5.2-1
- 6.5.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 6.5.0-1
- 6.5.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 6.4.1-1
- 6.4.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 26 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.9-1
- Update to 6.2.9

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.8-1
- Update to 6.2.8

* Tue Feb 16 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.6-1
- Update to 6.2.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.5-1
- Update to 6.2.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 6.1.4-1
- 6.1.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 6.0.1-1
- aqbanking-6.0.1

* Thu Sep 12 2019 Rex Dieter <rdieter@fedoraproject.org> 5.8.2-1
- aqbanking-5.8.2
- %%files: track sonames

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Bill Nottingham <notting@splat.cc> - 5.7.8-1
- update to 5.7.8

* Mon Mar 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.6.12-7
- .spec cosmetics/cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 5.6.12-5
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Bill Nottingham <notting@splat.cc> - 5.6.12-1
- update to 5.6.12

* Thu Jul 07 2016 Bill Nottingham <notting@splat.cc> - 5.6.10-1
- update to 5.6.10

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.5.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Robert Scheck <robert@fedoraproject.org> - 5.5.1-1
- update to 5.5.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.6-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.6-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Bill Nottingham <notting@redhat.com> - 5.3.6beta-0.1
- update to 5.3.6beta
- COPYING updated, no more tarball munging needed

* Fri Jan 17 2014 Bill Nottingham <notting@redhat.com> - 5.3.2beta-0.2
- bump to 5.3.2beta

* Wed Jan 15 2014 Bill Nottingham <notting@redhat.com> - 5.3.1beta-0.1
- update to latest upstream
- disable aqebics for now

* Thu Dec 12 2013 Bill Nottingham <notting@redhat.com> - 5.0.25-4
- add upstream patches for OFXDirectConnect (#1040224)

* Tue Aug 06 2013 Bill Nottingham <notting@redhat.com> - 5.0.25-3
- Fix for UnversionedDocDirs feature (#993669)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Bill Nottingham <notting@redhat.com> - 5.0.25-1
- update to 5.0.25

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Bill Nottingham <notting@redhat.com> - 5.0.22-2
- update to 5.0.22
- fix up rpaths a little cleaner

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Bill Nottingham <notting@redhat.com> - 5.0.16-1
- update to 5.0.16

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.0.2-3.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 5.0.2-3.1
- rebuild with new gmp

* Mon Feb 21 2011 Bill Nottingham <notting@redhat.com> - 5.0.2-3
- fix -devel obsoletes

* Wed Feb 16 2011 Bill Nottingham <notting@redhat.com> - 5.0.2-2
- remove aqpaypal source

* Fri Feb 11 2011 Bill Nottingham <notting@redhat.com> - 5.0.2-1
- update to latest upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2.4-6
- q4banking: try harder to purge qt3 dep (#626008)

* Sun Aug 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2.4-5
- rebase pkgconfig patch
- q4banking should not depend on qt3 (#626008)
- include %%check section, though currently mostly useless

* Fri Jun 25 2010 Bill Nottingham <notting@redhat.com> - 4.2.4-4
- fix multilib errors (#602879)

* Fri Mar 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2.4-2
- q4banking(-devel) pkgs (#571575)
- better versioned g2banking/kbanking Obsoletes

* Mon Mar  8 2010 Bill Nottingham <notting@redhat.com> - 4.2.4-1
- update to latest upstream 4.2.4

* Thu Jan 21 2010 Bill Nottingham <notting@redhat.com> - 4.2.3-1
- update to latest upstream 4.2.3
- obsolete the dead python-aqbanking package

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Bill Nottingham <notting@redhat.com> - 3.8.2-1
- update to 3.8.2-1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.7.2-2
- Rebuild for Python 2.6

* Tue Sep  9 2008 Bill Nottingham <notting@redhat.com> - 3.7.2-1
- update to 3.7.2
- obsolete the no-longer-existing g2banking/kbanking packages

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.3.3-3
- s/qt-devel/qt3-devel/ (f9+)
- qbanking-devel: Req: qt3-devel
- kbanking-devel: Req: kdelibs3-devel
- omit extraneous: Req: pkgconfig

* Thu Feb 14 2008 Bill Nottingham <notting@redhat.com> - 2.3.3-2
- rebuild for gcc-4.3

* Tue Jan 15 2008 Bill Nottingham <notting@redhat.com> - 2.3.3-1
- update to 2.3.3

* Wed Dec 19 2007 Bill Nottingham <notting@redhat.com> - 2.3.2-4
- kbanking-devel needs to require qbanking-devel (#426265)

* Tue Oct 30 2007 Bill Nottingham <notting@redhat.com> - 2.3.2-3
- fix multilib conflicts (#340671)

* Wed Aug 29 2007 Bill Nottingham <notting@redhat.com> - 2.3.2-2
- Rebuild for selinux ppc32 issue.
- fix build with current glibc/headers

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Wed Jul 11 2007 Bill Nottingham <notting@redhat.com> - 2.3.2-1
- update to 2.3.2

* Mon Jun 25 2007 Bill Nottingham <notting@redhat.com> - 2.2.9-3
- fix some build bogosity

* Wed Jun 20 2007 Bill Nottingham <notting@redhat.com> - 2.2.9-2
- add a dist tag

* Mon Mar 19 2007 Bill Nottingham <notting@redhat.com> - 2.2.9-1
- update to 2.2.9

* Wed Jan 17 2007 Bill Nottingham <notting@redhat.com> - 2.1.0-14
- fix docdir, obsoletes for aqhbci-devel, and %%clean

* Tue Jan 16 2007 Bill Nottingham <notting@redhat.com> - 2.1.0-13
- fix docs
- add PyXML buildreq

* Mon Jan 15 2007 Bill Nottingham <notting@redhat.com> - 2.1.0-12
- fix missing %%defattrs
- fix %%excludes
- other cleanups from review
- use %%{_python_sitelib}
- require automake
- twiddle aqhbci obsoletes

* Sat Jan 13 2007 Bill Nottingham <notting@redhat.com> - 2.1.0-11
- split into a variety of packages

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.1.0-10
- rebuild for python 2.5

* Thu Sep  7 2006 Bill Nottingham <notting@redhat.com> - 2.1.0-9
- rebuild for fixed debuginfo (#205248)

* Fri Sep  1 2006 Bill Nottingham <notting@redhat.com> - 2.1.0-8
- fix multilib conficts (#205204)

* Mon Aug 28 2006 Bill Nottingham <notting@redhat.com> - 2.1.0-4
- rebuild against latest libofx

* Tue Aug  1 2006 Bill Nottingham <notting@redhat.com> - 2.1.0-3
- reenable visibility

* Fri Jul 14 2006 Bill Nottingham <notting@redhat.com> - 2.1.0-2
- port *-config to pkgconfig
- don't use -fvisibility=hidden

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.1.0-1.1
- rebuild

* Tue Jul 11 2006 Bill Nottingham <notting@redhat.com> - 2.1.0-1
- update to 2.1.0

* Mon Jun 12 2006 Bill Nottingham <notting@redhat.com> - 1.8.1beta-5
- buildreq autoconf, libtool

* Tue May 30 2006 Bill Nottingham <notting@redhat.com> - 1.8.1beta-4
- add gettext buildreq (#193348)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.8.1beta-3.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Karsten Hopp <karsten@redhat.de> 1.8.1beta-3
- buildrequire libofx-devel instead of libofx (pulls in libofx)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8.1beta-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Jan 22 2006 Bill Nottingham <notting@redhat.com> 1.8.1beta-2
- add an obsolete (#178554)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Mar  7 2005 Bill Nottingham <notting@redhat.com> 1.0.4beta-2
- rebuild

* Wed Feb  9 2005 Bill Nottingham <notting@redhat.com> 1.0.4beta-1
- initial packaging, adopt upstream specfile
