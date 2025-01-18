Summary:        Open source cryptography library
Name:           beecrypt
Version:        4.2.1
Release:        37%{?dist}
License:        LGPL-2.1-or-later
URL:            https://beecrypt.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         beecrypt-4.1.2-biarch.patch
Patch1:         beecrypt-4.2.1-no-c++.patch
Patch2:         beecrypt-4.2.1-c99.patch
Patch3:         beecrypt-4.2.1-autoconf-c99.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
Obsoletes:      beecrypt-java <= 4.1.2-3

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines
and public key primitives.

%package devel
Summary:        Development files for the beecrypt toolkit and library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The beecrypt-devel package includes header files and libraries necessary
for developing programs which use the beecrypt C toolkit and library. And
beecrypt is a general-purpose cryptography library.

%if 0%{!?_without_apidocs:1}
%package apidocs
Summary:        API documentation for beecrypt toolkit and library
BuildRequires:  tetex-dvips
BuildRequires:  tetex-latex
BuildRequires:  graphviz
BuildRequires:  doxygen

%description apidocs
Beecrypt is a general-purpose cryptography library. This package contains
API documentation for developing applications with beecrypt.
%endif

%prep
%setup -q
%patch -P0 -p1 -b .biarch
%patch -P1 -p1 -b .no-c++
%patch -P2 -p1 -b .c99
%patch -P3 -p1 -b .autoconf-c99
libtoolize
autoreconf -i

%build
%configure --with-cplusplus=no --with-java=no --with-python=no
%make_build

%if 0%{!?_without_apidocs:1}
cd include/beecrypt
doxygen
cd ../..
%endif

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS -o CONTRIBUTORS.utf8
touch -c -r CONTRIBUTORS CONTRIBUTORS.utf8
mv -f CONTRIBUTORS.utf8 CONTRIBUTORS

%ldconfig_scriptlets

%files
%license COPYING COPYING.LIB
%doc AUTHORS BENCHMARKS CONTRIBUTORS NEWS README
%{_libdir}/libbeecrypt.so.*

%files devel
%doc BUGS
%{_includedir}/%{name}
%{_libdir}/libbeecrypt.so

%if 0%{!?_without_apidocs:1}
%files apidocs
%doc docs/html
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Peter Fordham <peter.fordham@gmail.com> - 4.2.1-31
- Fixes for C99 conformance issues.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-22
- Subpackage python2-beecrypt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Robert Scheck <robert@fedoraproject.org> 4.2.1-20
- Update python 2 dependency declarations to new packaging standards,
  see https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.1-18
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.1-17
- Python 2 binary package renamed to python2-beecrypt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Robert Scheck <robert@fedoraproject.org> 4.2.1-7
- Made autoreconf copying the missing auxiliary files (#913900)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 4.2.1-1
- Upgrade to 4.2.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 4.1.2-19
- Rebuild for gcc 4.4 and rpm 4.6

* Sun Dec 07 2008 Robert Scheck <robert@fedoraproject.org> 4.1.2-18
- Rebuild for python 2.6 and libtool 2.2

* Tue May 20 2008 Robert Scheck <robert@fedoraproject.org> 4.1.2-17
- Removed -fomit-frame-pointer to fix debuginfo (#438262 #c5)
- Disabled beecrypt-java subpackage again (#151294, #438262 #c6)

* Wed Mar 19 2008 Robert Scheck <robert@fedoraproject.org> 4.1.2-16
- Changes to match with Fedora Packaging Guidelines (#438262)

* Thu Nov 29 2007 Dennis Gilmore <dennis@ausil.us> - 4.1.2-15
- update sparc64 patch

* Wed Nov 28 2007 Dennis Gilmore <dennis@ausil.us> - 4.1.2-14
- add patch so sparc64 gets lib64

* Wed Aug 22 2007 Panu Matilainen <pmatilai@redhat.com> - 4.1.2-13
- avoid linking against libstdc++ (#165080)
- fix debuginfo contents by building with -g (#250035)
- autoreconf needed for the above, buildrequire autoconf, automake + libtool
- include api documentation in apidocs subpackage
- buildrequire graphviz for generating graphics in apidocs
- license clarification

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 4.1.2-12
- rebuild against python 2.5
- follow python packaging guidelines

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.1.2-10.1.1
- rebuild

* Tue Jun 27 2006 Paul Nasrat <pnasrat@redhat.com> - 4.1.2-10.1
- Fix missing BR

* Mon May 22 2006 Paul Nasrat <pnasrat@redhat.com> - 4.1.2-10
- Make multilib-devel work

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.1.2-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.1.2-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 15 2005 Florian La Roche <laroche@redhat.com>
- Use -with-cplusplus=no. The libs still require libstdc++, so
  this needs further cleanup.

* Tue May 17 2005 Miloslav Trmac <mitr@redhat.com> - 4.1.2-8
- Remove dependencies on private symbols not present in Python 2.4 from
  beecrypt-python

* Tue May 17 2005 Miloslav Trmac <mitr@redhat.com> - 4.1.2-7
- Doh, actually apply the patch

* Tue May 17 2005 Miloslav Trmac <mitr@redhat.com> - 4.1.2-6
- Fix b64encode() for data starting with NUL (#123650)

* Fri Apr 01 2005 Warren Togami <wtogami@redhat.com> 4.1.2-5
- remove huge API docs

* Fri Apr 01 2005 Paul Nasrat <pnasrat@redhat.com> 4.1.2-4
- Obsolete older beecrypt-java

* Tue Mar 29 2005 Paul Nasrat <pnasrat@redhat.com> 4.1.2-3
- Disable beecrypt-java (#151294)

* Fri Mar  4 2005 Jeff Johnson <jbj@redhat.com> 4.1.2-2
- rebuild with gcc4.

* Sat Feb  5 2005 Jeff Johnson <jbj@jbj.org> 4.1.2-1
- upgrade to 4.1.2
- put java components in sub-package.
- check that /usr/lib64 is not used on alpha (#146583).

* Fri Feb  4 2005 Miloslav Trmac <mitr@redhat.com> - 3.1.0-7
- Rebuild against Python 2.4

* Sun Aug 08 2004 Alan Cox <alan@redhat.com> 3.1.0-6
- Build requires libtool (Steve Grubb)

* Fri Jul 02 2004 Elliot Lee <sopwith@redhat.com> 3.1.0-5
- rebuilt
- Add _smp_mflags

* Wed Mar 24 2004 Jeff Johnson <jbj@redhat.com> 3.1.0-3
- fix: extgcd_w problem fixed by upgrading from CVS.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec 22 2003 Jeff Johnson <jbj@jbj.org> 3.1.0-1
- upgrade to 3.1.0.
- recompile against python-2.3.3.

* Mon Jun 30 2003 Jeff Johnson <jbj@redhat.com> 3.0.1-0.20030630
- upstream fixes for DSA and ppc64.

* Mon Jun 23 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-2
- upgrade to 3.0.0 final.
- fix for DSA (actually, modulo inverse) sometimes failing.

* Fri Jun 20 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030619
- avoid asm borkage on ppc64.

* Thu Jun 19 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030618
- rebuild for release bump.

* Tue Jun 17 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030616
- try to out smart libtool a different way.
- use $bc_target_cpu, not $bc_target_arch, to detect /usr/lib64.

* Mon Jun 16 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030615
- use -mcpu=powerpc64 on ppc64.

* Fri Jun 13 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030613
- upgrade to latest snapshot.

* Fri Jun  6 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030605
- rebuild into another tree.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030603
- update to 3.0.0 snapshot, fix mpmod (and DSA) on 64b platforms.

* Mon Jun  2 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030602
- update to 3.0.0 snapshot, merge patches, fix gcd rshift and ppc problems.

* Thu May 29 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030529
- update to 3.0.0 snapshot, fix ia64/x86_64 build problems.

* Wed May 28 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030528
- upgrade to 3.0.0 snapshot, adding rpm specific base64.[ch] changes.
- add PYTHONPATH=.. so that "make check" can test the just built _bc.so module.
- grab cpuinfo and run "make bench".
- continue ignoring "make check" failures, LD_LIBRARY_PATH needed for _bc.so.
- skip asm build failure on ia64 for now.
- ignore "make bench" exit codes too, x86_64 has AES segfault.

* Wed May 21 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030521
- upgrade to 3.0.0 snapshot, including python subpackage.
- ignore "make check" failure for now.

* Fri May 16 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030516
- upgrade to 3.0.0 snapshot, including ia64 and x86_64 fixes.
- add %%check.
- ignore "make check" failure on ia64 for now.

* Mon May 12 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030512
- upgrade to 3.0.0 snapshot.
- add doxygen doco.
- use /dev/urandom as default entropy source.
- avoid known broken compilation for now.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Aug  2 2002 Jeff Johnson <jbj@redhat.com> 2.2.0-6
- install types.h (#68999).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun  5 2002 Jeff Johnson <jbj@redhat.com>
- run ldconfig when installing/erasing (#65974).

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 13 2002 Jeff Johnson <jbj@redhat.com>
- upgrade to latest 2.2.0 (from cvs.rpm.org).

* Mon Jan 21 2002 Jeff Johnson <jbj@redhat.com>
- use the same beecrypt-2.2.0 that rpm is using internally.

* Thu Jan 10 2002 Nalin Dahyabhai <nalin@redhat.com> 2.1.0-1
- initial package
