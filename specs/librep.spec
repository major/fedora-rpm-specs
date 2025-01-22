Name:           librep
Version:        0.92.7
Release:        25%{?dist}
Summary:        A lightweight Lisp environment
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/%{name}/%{name}_%{version}.tar.bz2
Patch0:         librep-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gdbm-devel
BuildRequires:  readline-devel
BuildRequires:  libffi-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  chrpath
BuildRequires:  emacs
BuildRequires: make
Requires:       emacs-filesystem >= %{_emacs_version}


%description
This is a lightweight Lisp environment for UNIX. It contains a Lisp
interpreter, byte-code compiler and virtual machine. Applications may
use the Lisp interpreter as an extension language, or it may be used
for standalone scripts.

Originally inspired by Emacs Lisp, the language dialect combines many
of the Emacs Lisp features while trying to remove some of the main
deficiencies, with features from Common Lisp and Scheme.


%package devel
Summary:        Development files for librep
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig


%description devel
Link libraries and C header files for librep development.


%prep
%autosetup -p1 -n %{name}_%{version}


%build
./autogen.sh --nocfg
%configure --with-readline --enable-shared --disable-static
%make_build
%{_emacs_bytecompile} rep-debugger.el


%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
chrpath --delete %{buildroot}%{_bindir}/rep
install -m 644 rep-debugger.elc %{buildroot}%{_emacs_sitelispdir}
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;

%files
%license COPYING
%doc NEWS README TODO
%{_bindir}/rep
%{_bindir}/rep-remote
%{_libdir}/librep.so.*
%{_libdir}/rep/
%{_datadir}/rep/
%{_datadir}/man/man1/rep-remote.1.gz
%{_datadir}/man/man1/rep.1.gz
%{_infodir}/librep.info.*
%{_emacs_sitelispdir}/rep-debugger.el
%{_emacs_sitelispdir}/rep-debugger.elc
%exclude %{_libdir}/rep/install-aliases
%exclude %{_libdir}/rep/libtool
%exclude %{_libdir}/rep/rules.mk


%files devel
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%{_includedir}/rep/
%{_libdir}/librep.so
%{_libdir}/pkgconfig/librep.pc
%{_libdir}/rep/install-aliases
%{_libdir}/rep/libtool
%{_libdir}/rep/rules.mk
%{_datadir}/man/man1/rep-xgettext.1.gz
%{_datadir}/man/man1/repdoc.1.gz


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.92.7-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 0.92.7-18
- Apply upstream patch to port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.92.7-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 0.92.7-11
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.92.7-8
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.92.7-7
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.92.7-5
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.92.7-2
- Rebuilt for switch to libxcrypt

* Tue Aug 29 2017 Kim B. Heino <b@bbbs.net> - 0.92.7-1
- Upgrade to 0.92.7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.92.6-2
- Rebuild for readline 7.x

* Fri Aug  5 2016 Kim B. Heino <b@bbbs.net> - 0.92.6-1
- Upgrade to 0.92.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Kim B. Heino <b@bbbs.net> - 0.92.5-1
- Upgrade to 0.92.5
- Include emacs files to main package (rhbz#1234558)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov  4 2014 Kim B. Heino <b@bbbs.net> - 0.92.4-1
- Update to 0.92.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Kim B. Heino <b@bbbs.net> - 0.92.3-5
- Fix stack direction on aarch64

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Kim B. Heino <b@bbbs.net> - 0.92.3-1
- Update to 0.92.3

* Tue Sep 04 2012 Dan Horák <dan[at]danny.cz> 0.92.2-6
- fix stack direction on s390(x)

* Thu Aug 09 2012 karsten Hopp <karsten@redhat.com> 0.92.2-5
- fix stack direction on PPC*

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.2-3
- Improve ARM platform detection

* Sun May 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.2-2
- Fix stack direction on ARM platforms
- Cleanup spec

* Mon Mar 26 2012 Kim B. Heino <b@bbbs.net> - 0.92.2-1
- Update to 0.92.2

* Sat Jan 14 2012 Kim B. Heino <b@bbbs.net> - 0.92.1-4
- Force stack direction check on x86_64 for gcc-4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Kim B. Heino <b@bbbs.net> - 0.92.1-2
- Rebuild

* Mon Aug 22 2011 Kim B. Heino <b@bbbs.net> - 0.92.1-1
- Update to 0.92.1

* Tue May  3 2011 Kim B. Heino <b@bbbs.net> - 0.92.0-1
- Update to 0.92.0

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 0.91.1-5
- don't use %%{_host} which can be modified by configure on non-x86 arches

* Tue Apr 12 2011 Kim B. Heino <b@bbbs.net> - 0.91.1-4
- Add emacs-librep subpackage

* Sat Apr  2 2011 Kim B. Heino <b@bbbs.net> - 0.91.1-3
- Fix dynamic loading

* Fri Apr  1 2011 Kim B. Heino <b@bbbs.net> - 0.91.1-2
- Fix Fedora packaging guideline errors

* Thu Mar 31 2011 Kim B. Heino <b@bbbs.net> - 0.91.1-1
- Update to 0.91.1

* Sat Sep 25 2010 Kim B. Heino <b@bbbs.net> - 0.91.0-1
- fix rpath again
- fix doc-files, url, misc fixes

* Sun Jan 10 2010 Kim B. Heino <b@bbbs.net> - 0.90.6-1
- fix devel package, fix rpmlint warnings

* Sat Sep 05 2009 Kim B. Heino <b@bbbs.net>
- add dist-tag, update buildrequires

* Sun Jan 18 2009 Christopher Bratusek <zanghar@freenet.de>
- several updates

* Fri Jan 02 2009 Christopher Bratusek <nano-master@gmx.de>
- source archive is a .tar.bz2

* Thu Dec 18 2008 Christopher Bratusek <nano-master@gmx.de>
- rep.m4 no longer available
- install librep.pc

* Tue Jun 13 2000 John Harper <john@dcs.warwick.ac.uk>
- use better macros

* Wed Nov 10 1999 Michael K. Johnson <johnsonm@redhat.com>
- post{,un} use -p

* Mon Sep 13 1999 Aron Griffis <agriffis@bigfoot.com>
- 0.5 spec file update: added buildroot
