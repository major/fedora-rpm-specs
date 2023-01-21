# TODO: Package mplrs, the MPI version.

Name:           lrslib
Version:        7.2
Release:        3%{?dist}
Summary:        Reverse search for vertex enumeration/convex hull problems

%global upver 0%(sed 's/\\.//' <<< %{version})

License:        GPL-2.0-or-later
URL:            http://cgm.cs.mcgill.ca/~avis/C/lrs.html
Source0:        http://cgm.cs.mcgill.ca/~avis/C/%{name}/archive/%{name}-%{upver}.tar.gz
# This patch was sent upstream on 31 May 2011.  It fixes some miscellaneous
# bugs.
Patch0:         %{name}-fixes.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
%{name} is a self-contained ANSI C implementation as a callable library
of the reverse search algorithm for vertex enumeration/convex hull
problems and comes with a choice of three arithmetic packages.  Input
file formats are compatible with Komei Fukuda's cdd package (cddlib).
All computations are done exactly in either multiple precision or fixed
integer arithmetic.  Output is not stored in memory, so even problems
with very large output sizes can sometimes be solved.

%package devel
Summary:        Header files and libraries for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Header files and libraries for developing with %{name}.

%package utils
Summary:        Sample programs that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Sample programs that use %{name}.

%prep
%autosetup -n %{name}-%{upver}

# Remove extraneous executable bits
chmod a-x *.{c,h} ine/test/cp4.ine

%build
# The Makefile is too primitive to use.  For one thing, it only builds
# binaries, not libraries.  We do our own thing here.
# Recent changes to the Makefile make it less primitive, but it still does not
# work well for building on a mixture of 32-bit and 64-bit architectures.

# Upstream wants to use 1.0.0 as the soname version number for now.
%global sover 1
%global ver 1.0.0

CFLAGS="%{build_cflags} -DMA -I. -I%{_includedir}/boost"

# Build the individual objects
gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -c -o lrslong1.o lrslong.c
gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -c -o lrslib1.o lrslib.c
gcc $CFLAGS -fPIC -DGMP -c -o lrslibgmp.o lrslib.c
gcc $CFLAGS -fPIC -DGMP -c -o lrsgmp.o lrsgmp.c
gcc $CFLAGS -fPIC -c -o lrsdriver.o lrsdriver.c
%if 0%{?__isa_bits} == 64
gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -DB128 -c -o lrslong2.o lrslong.c
gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -DB128 -c -o lrslib2.o lrslib.c
%endif

# Build the library
%if 0%{?__isa_bits} == 64
gcc $CFLAGS %{build_ldflags} -fPIC -shared -Wl,-soname,liblrs.so.%{sover} \
  -o liblrs.so.%{ver} lrslong1.o lrslong2.o lrslib1.o lrslib2.o lrslibgmp.o \
  lrsgmp.o lrsdriver.o -lgmp
%else
gcc $CFLAGS %{build_ldflags} -fPIC -shared -Wl,-soname,liblrs.so.%{sover} \
  -o liblrs.so.%{ver} lrslong1.o lrslib1.o lrslibgmp.o lrsgmp.o lrsdriver.o \
  -lgmp
%endif
ln -s liblrs.so.%{ver} liblrs.so.%{sover}
ln -s liblrs.so.%{sover} liblrs.so

# Build the binaries
%if 0%{?__isa_bits} == 64
gcc $CFLAGS -DB128 -DSAFE lrs.c -o lrs %{build_ldflags} -L. -llrs
gcc $CFLAGS -DB128 lrs.c -o lrsn %{build_ldflags} -L. -llrs
%else
gcc $CFLAGS -DB32 -DSAFE lrs.c -o lrs %{build_ldflags} -L. -llrs
gcc $CFLAGS -DB32 lrs.c -o lrsn %{build_ldflags} -L. -llrs
%endif
gcc $CFLAGS -DGMP lrs.c -o lrsgmp %{build_ldflags} -L. -llrs -lgmp
gcc $CFLAGS -DGMP lrsnash.c lrsnashlib.c -o lrsnash %{build_ldflags} -L. -llrs \
  -lgmp
gcc $CFLAGS -DLRSLONG -DSAFE lrsnash.c lrsnashlib.c -o lrsnash1 %{build_ldflags} \
  -L. -llrs
%if 0%{?__isa_bits} == 64
gcc $CFLAGS -DLRSLONG -DSAFE -DB128 lrsnash.c lrsnashlib.c -o lrsnash2 \
    %{build_ldflags} -L. -llrs
%endif
gcc $CFLAGS 2nash.c -o lrs-2nash %{build_ldflags}
gcc $CFLAGS buffer.c -o lrs-buffer %{build_ldflags}
gcc $CFLAGS hvref.c -o lrs-hvref %{build_ldflags}
gcc $CFLAGS -DGMP checkpred.c -o lrs-checkpred %{build_ldflags} -L. -llrs -lgmp
gcc $CFLAGS -DGMP inedel.c -o lrs-inedel %{build_ldflags} -L. -llrs -lgmp
gcc $CFLAGS -DGMP setupnash.c -o lrs-setupnash %{build_ldflags} -L. -llrs
gcc $CFLAGS -DGMP setupnash2.c -o lrs-setupnash2 %{build_ldflags} -L. -llrs
gcc $CFLAGS -DLRSMP -Dcopy=copy_dict_1 -Dlrs_mp_init=lrs_mp_init_1 -Dpmp=pmp_1 \
  -Drattodouble=rattodouble_1 -Dreadrat=readrat_1 rat2float.c -o lrs-rat2float \
  %{build_ldflags} -L. -llrs
gcc $CFLAGS float2rat.c -o lrs-float2rat %{build_ldflags}

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a liblrs.so* %{buildroot}%{_libdir}
chmod 0755 %{buildroot}%{_libdir}/lib*.so.%{ver}

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 lrs lrsgmp lrsnash lrsnash1 lrs-* %{buildroot}%{_bindir}
%if 0%{?__isa_bits} == 64
install -p -m 0755 lrsnash2 %{buildroot}%{_bindir}
%endif
ln -s lrs %{buildroot}%{_bindir}/lrsn
ln -s lrs %{buildroot}%{_bindir}/lrsredund
ln -s lrsgmp %{buildroot}%{_bindir}/lrsredundgmp

# Install the header files, but fix up the include directives.
mkdir -p %{buildroot}%{_includedir}/%{name}
sed -r 's|"(lrs.*\.h)"|<lrslib/\1>|' lrslib.h > \
    %{buildroot}%{_includedir}/%{name}/lrslib.h
touch -r lrslib.h %{buildroot}%{_includedir}/%{name}/lrslib.h

sed -e 's|"gmp.h"|<gmp.h>|' lrsgmp.h > \
    %{buildroot}%{_includedir}/%{name}/lrsgmp.h
touch -r lrsgmp.h %{buildroot}%{_includedir}/%{name}/lrsgmp.h

sed -e 's|"lrsrestart.h"|<lrslib/lrsrestart.h>|' lrsdriver.h > \
    %{buildroot}%{_includedir}/%{name}/lrsdriver.h
touch -r lrsdriver.h %{buildroot}%{_includedir}/%{name}/lrsdriver.h

cp -p lrslong.h lrsmp.h lrsnashlib.h lrsrestart.h \
  %{buildroot}%{_includedir}/%{name}

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
cd man/man1
cp -p checkpred.1 %{buildroot}%{_mandir}/man1/lrs-checkpred.1
cp -p {lrs,lrsnash}.1 %{buildroot}%{_mandir}/man1
echo '.so man1/lrs' > %{buildroot}%{_mandir}/man1/lrs-hvref.1
echo '.so man1/lrs' > %{buildroot}%{_mandir}/man1/lrsredund.1
cd ../man5
cp -p *.5 %{buildroot}%{_mandir}/man5
cd ../..

%files
%doc README
%license COPYING
%{_libdir}/liblrs.so.1
%{_libdir}/liblrs.so.1.*

%files devel
%doc chdemo.c lpdemo.c lpdemo1.c lpdemo2.c nashdemo.c vedemo.c
%{_includedir}/%{name}
%{_libdir}/liblrs.so
%{_mandir}/man5/lrs*

%files utils
%{_bindir}/lrs*
%{_mandir}/man1/lrs*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 7.2-2
- Fix a few man page names
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 7.2-1
- Version 072
- Drop unmaintained downstream man pages

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun  4 2021 Jerry James <loganjerry@gmail.com> - 7.1b-1
- Version 071b

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Jerry James <loganjerry@gmail.com> - 7.1a-1
- Version 071a

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 7.1-1
- Version 071
- Drop upstreamed -common patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 7.0-5
- Add -common patch to fix build with -fcommon, for GCC 10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 7.0-3
- Update to version 070a

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Jerry James <loganjerry@gmail.com> - 7.0-1
- New upstream release
- Major spec file overhaul due to upstream combining all 3 versions of the
  library into a single library

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 6.2-10
- BR gcc-c++ instead of gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Jerry James <loganjerry@gmail.com> - 6.2-8
- Rebuild for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 6.2-5
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 6.2-4
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 6.2-2
- Rebuilt for Boost 1.63

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 6.2-1
- New upstream release

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 6.1-4
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 6.1-2
- Rebuilt for Boost 1.60

* Fri Dec  4 2015 Jerry James <jamesjer@diannao.jamezone.org> - 6.1-1
- New upstream release

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 6.0-1
- New upstream release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 5.1-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.1-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 5.1-2
- Bump for rebuild.

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 5.1-1
- New upstream release

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 5.0a-2
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 5.0a-1
- New upstream release

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 5.0-1
- New upstream release
- Drop upstreamed -memleak patch
- Link with RPM_LD_FLAGS
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Jerry James <loganjerry@gmail.com> - 4.3-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 4.2c-4
- Apply patch from Thomas Rehn to fix a memory leak

* Tue Feb 14 2012 Jerry James <loganjerry@gmail.com> - 4.2c-3
- Change subpackage structure based on review

* Wed Aug 24 2011 Jerry James <loganjerry@gmail.com> - 4.2c-2
- Use %%{name} more liberally.
- Use %%global instead of %%define.
- Add man pages.

* Wed Jul 20 2011 Jerry James <loganjerry@gmail.com> - 4.2c-1
- Initial RPM
