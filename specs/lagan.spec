Name:           lagan
Version:        2.0
Release:        44%{?dist}
Summary:        Local, global, and multiple alignment of DNA sequences

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://lagan.stanford.edu
Source0:        http://lagan.stanford.edu/lagan_web/lagan20.tar.gz
Patch0:         lagan20-chris.patch
Patch1:         lagan20-gcc10.patch
Patch2:         lagan-c99.patch
BuildRequires:  perl-generators
BuildRequires:  gcc-c++
BuildRequires: make


%description
LAGAN toolkit is a set of tools for local, global, and multiple alignment of
DNA sequences.  Please visit http://lagan.stanford.edu for publications
describing LAGAN and its components.

The 4 main parts of LAGAN are:

1. CHAOS local alignment tool
2. LAGAN pairwise global alignment tool
3. MLAGAN multiple global alignment tool.
4. Shuffle-LAGAN pairwise global alignment


%prep
%setup -q -n lagan20
%patch -P0 -p1 -b .chris
%patch -P1 -p1 -b .gcc10
%patch -P2 -p1

sed -i 's/^CC .*$/CC = gcc $(RPM_OPT_FLAGS)/;
        s/^CPP .*$/CPP = g++ $(RPM_OPT_FLAGS)/' Makefile
sed -i 's|getenv ("LAGAN_DIR")|"%_libdir/lagan"|g' src/*.c src/utils/*.c
sed -i 's|getenv ("LAGAN_DIR")|"%_libdir/lagan"|g' src/utils/*.cpp
sed -i 's|$ENV{LAGAN_DIR}|"%_libdir/lagan"|g' *.pl src/*.pl utils/*.pl src/utils/*.pl
sed -i 's|$LAGAN_DIR|%_libdir/lagan|g' Readmes/README.shuffle src/*.c
sed -i 's/getline/GetLine/g' src/anchors.c
sed -i 's/^inline /inline __attribute__ ((always_inline)) /' src/fchaos.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/filebuffer.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/utils/scorecontigs.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/utils/overlay.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/utils/cstat.c
sed -i 's/^int indeces/extern int indeces/' src/thrtrie.h
sed -i '/^int nnodes=0;/aint indeces[256];' src/thrtrie.c
rm prolagan
chmod -x src/glocal/*


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir $RPM_BUILD_ROOT/%_libdir/lagan/utils
install -m755 chaos ${RPM_BUILD_ROOT}%{_bindir}
install -m755 mlagan ${RPM_BUILD_ROOT}%{_bindir}
install -m755 prolagan ${RPM_BUILD_ROOT}%{_bindir}
install -m755 lagan.pl ${RPM_BUILD_ROOT}%{_bindir}/lagan
install -m755 slagan.pl ${RPM_BUILD_ROOT}%{_bindir}/slagan
for f in anal_gloc.pl anchors glocal order rechaos.pl \
  supermap.pl xmfa2mfa.pl; do
  install -m755 $f $RPM_BUILD_ROOT/%_libdir/lagan
done
for f in bin2bl bin2mf cextract cmerge2.pl contigorder cstat dotplot \
  draft.pl fa2xfa getbounds getcontigpos getlength getoverlap Glue \
  mextract.pl mf2bin.pl mpretty.pl mproject.pl mrunfile.pl mrunpairs.pl \
  mrun.pl mviz.pl rc scorealign scorecontigs seqmerge overlay; do
  install -m755 utils/$f $RPM_BUILD_ROOT/%_libdir/lagan/utils
done
install -m644 *.txt *.score $RPM_BUILD_ROOT/%_libdir/lagan
rm -f Readmes/*.chris



%files
%doc Readmes/* sample.*
%_bindir/chaos
%_bindir/lagan
%_bindir/mlagan
%_bindir/slagan
%_bindir/prolagan
%_libdir/lagan/



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-43
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Florian Weimer <fweimer@redhat.com> - 2.0-37
- C99 compatibility fixes (#2160661)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Christian Iseli <Christian.Iseli@unil.ch> - 2.0-31
- Fix FTBFS due to variable multiple definition issues (bz 1799571)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Jeff Law <law@redhat.com> - 2.0-29
- Fix another inline vs static inline issue for gcc-10/LTO

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 2.0-28
- Fix inline vs static inline issue for gcc-10

* Tue Sep 10 2019 Christian Iseli <Christian.Iseli@unil.ch> - 2.0-27
- Fix FTBFS due to inlining issue (bz 1729180)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Christian Iseli <Christian.Iseli@unil.ch> - 2.0-24
- Fix FTBFS due to missing BuildRequires gcc-c++ (bz 1604535)
- Fix typo shown by rpmlint

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Christian Iseli <Christian.Iseli@unil.chg> - 2.0-19
- Fix FTBFS bugzilla 1307708

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-16
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 5 2009 Christian Iseli <Christian.Iseli@licr.org> - 2.0-5
- Add fix for getline() conflicting with stdio.h definition in new glibc

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 2.0-3
- Rebuild for F-11

* Sun Jan 27 2008 Christian Iseli <Christian.Iseli@licr.org> - 2.0-2
- Update patch to fix gcc-4.3 compilation issues.

* Tue Sep 18 2007 Christian Iseli <Christian.Iseli@licr.org> - 2.0-1
- New upstream release.

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> - 1.21-4
- Fix License tag.

* Tue Sep 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.21-3
- Rebuild for FC 6.

* Wed Feb 15 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.21-2
- Rebuild for FE 5.

* Mon Jan 30 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.21-1
- Use _libdir instead of _libexecdir and kill all LAGAN_DIR refs.

* Thu Nov 17 2005 Christian Iseli <Christian.Iseli@licr.org> - 1.21-0
- Create spec file.
