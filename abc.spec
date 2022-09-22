# Upstream doesn't make releases.  We have to check the code out of git.
%global owner    berkeley-abc
%global gittag   a9237f50ea01efdd62f86d334a38ffbe80a3d141
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20220731

# WARNING: When updating to a newer snapshot, because upstream doesn't do
# shared library versioning, run abipkgdiff (from libabigail) against the
# old and new binary and debuginfo packages to detect abi changes that would
# require bumping the shared library version, e.g.,
#   abipkgdiff --d1 abc-libs-debuginfo-<old>.rpm \
#              --d1 abc-debuginfo-<old>.rpm \
#              --d2 abc-libs-debuginfo-<new>.rpm \
#              --d2 abc-debuginfo-<new>.rpm \
#              --devel1 abc-devel-<old>.rpm \
#              --devel2 abc-devel-<new>.rpm \
#              abc-libs-<old>.rpm abc-libs-<new>.rpm
# If the shared library version is bumped, remember to rebuild dependent
# packages, finding them using e.g.
#   repoquery --whatrequires abc-libs
# This should be done for each branch in which abc-libs will be updated.

Name:           abc
Version:        1.01
Release:        35.git%{gitdate}%{?dist}
Summary:        Sequential logic synthesis and formal verification

# The ABC code itself is MIT-Modern-Variant.
# The bundled CUDD code is BSD-3-Clause.
# The bundled glucose code is MIT.
# The bundled minisat code is MIT.
# The bundled satoko code is BSD-2-Clause
License:        MIT-Modern-Variant AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://people.eecs.berkeley.edu/~alanmi/abc/abc.htm
Source0:        https://github.com/%{owner}/%{name}/archive/%{gittag}/%{name}-%{shorttag}.tar.gz
# Man page created by Jerry James using upstream text; hence, it is covered by
# the same copyright and license as the code.
Source1:        %{name}.1
# Fedora-specific patch: do not use the bundled libraries
Patch0:         %{name}-bundlelib.patch
# Fedora-specific patch: build a shared library instead of a static library
Patch1:         %{name}-sharedlib.patch
# Fix a minor header issue
Patch2:         %{name}-header.patch
# Set an soname on the library
Patch3:         %{name}-build.patch
# Fix sprintf calls that can overflow their buffers
Patch4:         %{name}-format.patch
# Fix an out-of-bounds array access in the gia code
# https://github.com/berkeley-abc/abc/pull/89
Patch5:         %{name}-gia.patch
# Prevent a possible buffer overflow
Patch6:         %{name}-overflow.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
ABC is a growing software system for synthesis and verification of
binary sequential logic circuits appearing in synchronous hardware
designs.  ABC combines scalable logic optimization based on And-Inverter
Graphs (AIGs), optimal-delay DAG-based technology mapping for look-up
tables and standard cells, and innovative algorithms for sequential
synthesis and verification.

ABC provides an experimental implementation of these algorithms and a
programming environment for building similar applications.  Future
development will focus on improving the algorithms and making most of
the packages stand-alone.  This will allow the user to customize ABC for
their needs as if it were a toolbox rather than a complete tool.

%package libs
Summary:        Library for sequential synthesis and verification
# ABC includes a bundled and modified version of CUDD 2.4.2.  The CUDD package
# is no longer available from Fedora since the disappearance of the upstream
# web site (and the last released version was 3.0.0).
Provides:       bundled(cudd) = 2.4.2
# ABC includes a bundled and modified version of glucose (which version?)
Provides:       bundled(glucose)
# ABC includes a bundled and modified version of minisat (which version?).
Provides:       bundled(minisat2)
# ABC includes a bundled and modified version of satoko (which version?).
Provides:       bundled(satoko)

%description libs
This package contains the core functionality of ABC as a shared library.

%package devel
Summary:        Headers and libraries for developing with ABC
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing applications that use ABC.

%prep
%autosetup -p0 -n %{name}-%{gittag}

# Do not use the bundled bzip2, zlib, or Windows libraries
rm -fr lib src/misc/{bzlib,zlib}

# Set the version number in the man page
sed 's/@VERSION@/%{version} (%{gitdate})/' %{SOURCE1} > %{name}.1
touch -r %{SOURCE1} %{name}.1

# Do not override Fedora optimization flags
sed -i 's/ -O//' Makefile

%build
export CFLAGS="%{build_cflags} -DNDEBUG"
%ifarch s390x
CFLAGS="$CFLAGS -DEPD_BIG_ENDIAN"
%endif
export CXXFLAGS="$CFLAGS"
export ABC_MAKE_VERBOSE=1
export ABC_USE_STDINT_H=1
%cmake -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES
%cmake_build

%install
# %%cmake_install does not install anything.  Install by hand.

# Install the binary
cd %{_vpath_builddir}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -pd lib%{name}.so* %{buildroot}%{_libdir}
cd -

# Install the header files
cd src
mkdir -p %{buildroot}%{_includedir}/%{name}
tar -cBf - $(find -O3 . -name \*.h) | \
  (cd %{buildroot}%{_includedir}/%{name}; tar -xBf -)
cd -

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md readmeaig
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%files libs
%license copyright.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 1.01-35.git20220731
- Update to latest git snapshot
- Convert License field to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-34.git20211229
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-33.git20211229
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Jerry James <loganjerry@gmail.com> - 1.01-32.git20211229
- Update to latest git snapshot
- Drop upstreamed -strict-aliasing patch

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-31.git20210328
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Jerry James <loganjerry@gmail.com> - 1.01-30.git20210328
- Update to latest git snapshot
- Add patches: -strict-aliasing, -overflow
- Avoid bogus rpaths

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-29.git20201126
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.01-28.git20201126
- Update to latest git snapshot

* Mon Jul 27 2020 Jerry James <loganjerry@gmail.com> - 1.01-27.git20200720
- Update to latest git snapshot
- Add -gia patch to fix crash
- Adapt to cmake changes in Rawhide

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-27.git20200127
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.01-26.git20200127
- Update to latest git snapshot

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-25.git20191217
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Jerry James <loganjerry@gmail.com> - 1.01-24.git20191217
- Update to latest git snapshot
- Add -giaDeep patch to fix build failure

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-23.git20190608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Jerry James <loganjerry@gmail.com> - 1.01-22.git20190608
- Update to latest git snapshot
- Add -build and -format patches
- Build with cmake
- Enable CUDD support

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.01-21.git20181121
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-20.git20181121
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 1.01-19.git20181121
- Update to latest git snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-18.git20180708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jerry James <loganjerry@gmail.com> - 1.01-17.git20180708
- Update to latest git snapshot

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 1.01-16.hg20180228
- Update to latest mercurial snapshot
- BR gcc-c++ instead of gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-15.hg20180129
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Jerry James <loganjerry@gmail.com> - 1.01-14.hg20180129
- Update to latest mercurial snapshot

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-13.hg20160905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-12.hg20160905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-11.hg20160905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.01-10.hg20160905
- Rebuild for readline 7.x

* Sat Sep 10 2016 Eric Smith <brouhaha@fedoraproject.org> - 1.01-9.hg20160905
- Update to latest mercurial snapshot

* Fri Feb  5 2016 Jerry James <loganjerry@gmail.com> - 1.01-8.hg20160203
- Update to latest mercurial snapshot
- Drop the python2 subpackage; upstream moved support to a separate project

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-7.hg20150306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6.hg20150306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.01-5.hg20150306
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jerry James <loganjerry@gmail.com> - 1.01-4.hg20150306
- Update to latest mercurial snapshot

* Thu Jan  1 2015 Jerry James <loganjerry@gmail.com> - 1.01-3.hg20150101
- Update to latest mercurial snapshot
- Fix installation of header files

* Wed Dec  3 2014 Jerry James <loganjerry@gmail.com> - 1.01-2.hg20141130
- Drop unnecessary jquery Provides
- Fix file permissions

* Mon Dec  1 2014 Jerry James <loganjerry@gmail.com> - 1.01-1.hg20141130
- Initial RPM
