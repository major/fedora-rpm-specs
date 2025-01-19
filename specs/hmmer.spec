Name:           hmmer
Version:        3.3.2
Release:        10%{?dist}
Summary:        Biosequence analysis using profile hidden Markov models

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://hmmer.org
Source0:        http://eddylab.org/software/hmmer/hmmer-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  make
# HMMER3 requires SSE or VMX vector instructions - Bug 2112825
# VMX only works for big endian in HMMER3
# author says more arch will be supported in HMMER4 (no ETA)
ExcludeArch:    aarch64 ppc64le s390x
Patch0:         hmmer-3.3.2-chris.patch

%description
HMMER is used for searching sequence databases for sequence homologs, and for
making sequence alignments. It implements methods using probabilistic models
called profile hidden Markov models (profile HMMs).

%package easel
Summary: Easel collection of small tools

%description easel

Collection of additional small tools ("miniapps") from the Easel library.

%package doc
Summary: Documentation for hmmer
BuildArch: noarch

%description doc
This package includes documentation files for the hmmer software package.


%prep
%setup -q
%patch -P0 -p1 -b .chris


%build
%configure
make %{?_smp_mflags}


%check
make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
(cd easel; make install DESTDIR=$RPM_BUILD_ROOT)


%files
%license LICENSE
%{_bindir}/hmm*
%{_bindir}/alimask
%{_bindir}/jackhmmer
%{_bindir}/makehmmerdb
%{_bindir}/nhmmer
%{_bindir}/nhmmscan
%{_bindir}/phmmer
%{_mandir}/man1/hmm*
%{_mandir}/man1/alimask*
%{_mandir}/man1/jackhmmer*
%{_mandir}/man1/makehmmerdb*
%{_mandir}/man1/nhmmer*
%{_mandir}/man1/nhmmscan*
%{_mandir}/man1/phmmer*


%files easel
%{_bindir}/easel
%{_bindir}/esl-*
%{_mandir}/man1/esl-*


%files doc
%doc LICENSE README.md RELEASE-%{version}.md Userguide.pdf tutorial/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.2-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Christian Iseli <Christian.Iseli@epfl.ch> - 3.3.2-4
- Add small patch to fix #2148156

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug  1 2022 Christian Iseli <Christian.Iseli@unil.ch> - 3.3.2-2
- Add ExcludeArch #2112825

* Sun Jul 31 2022 Christian Iseli <Christian.Iseli@unil.ch> - 3.3.2-1
- Update to new upstream version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b2-8
- Add missing BuildRequires for perl - needed in the test suite
- #1423711 fix FTBFS

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b2-3
- #1284297 provide -static package as per guidelines
- try to fix build failure on power arch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1b2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b2-1
- Update to new upstream version

* Sat Feb 28 2015 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b1-1
- Update to new upstream version
- Split -devel and -doc subpackages
- perl script fix no longer needed

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Christian Iseli <Christian.Iseli@unil.ch> - 3.0-7
- BuildRoot is no longer necessary
- BuildRequire autoconf and run autoreconf prior to configure (#925551)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Christian Iseli <Christian.Iseli@unil.ch> - 3.0-5
- Fix build failure due to old (perl4) code in the test suite

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Christian Iseli <Christian.Iseli@licr.org> - 3.0-1
- New upstream version 3.0
- License is now GPLv3
- configure defaults to multi-threaded
- make install now uses DESTDIR
- copy manpages (rule missing in Makefile, apparently)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-9
- Rebuild for F-11
- Change URL and Source0 links to new location

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.2-8
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-7
 - Fix License tag to GPLv2+.

* Tue Sep 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-6
 - Rebuild for FC 6.

* Wed Feb 15 2006 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-5
 - Minor spec cleanup.  Rebuild for FE 5.

* Fri Dec 23 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-4
 - Rebuild with gcc-4.1.

* Mon Aug 08 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-3
 - Removed altivec switch for ppc: apparently, it only works using Apple's
   GCC compiler.

* Sat Aug 06 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-2
 - Fix spec file according to review.

* Fri Aug 05 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-1
 - Create spec file.
