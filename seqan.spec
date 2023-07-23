# LTO flags prevent the linker's work
# /usr/bin/ld: error: lto-wrapper failed
%define _lto_cflags %{nil}

# %%_fortify_level
%undefine _fortify_level

Name:      seqan
Summary:   Open source C++ library of efficient algorithms and data structures
Version:   1.4.2
Release:   52%{?dist}
License:   BSD and GPLv3+ and LGPLv3+
URL:       http://www.seqan.de/
Source0:   http://packages.seqan.de/seqan-src/seqan-src-%{version}.tar.gz

## This patch sets a seqan directory for documentation files
Patch0: %{name}-docpath.patch

## These patches exclude tests of splazers, fiona, bs_tools
## They fail beacause unknown reasons
Patch1: %{name}-exclude_splazers_fiona_tests.patch
Patch2: %{name}-exclude_bstools_test.patch

BuildRequires: make
BuildRequires: gcc, gcc-c++
BuildRequires: qt4-devel >= 4.7
BuildRequires: cmake
BuildRequires: llvm-devel
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: boost-devel
BuildRequires: coin-or-lemon-devel
BuildRequires: libstdc++-static
%ifarch %{java_arches}
BuildRequires: java-1.8.0-openjdk-devel
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: gawk

## Bundled files exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)

%description
SeqAn is an open source C++ library of efficient algorithms and data structures 
for the analysis of sequences with the focus on biological data. 
Our library applies a unique generic design that guarantees high performance, 
generality, extensibility, and integration with other libraries. 

%package devel
Summary: SeqAn development files

%description devel
Developer files for SeqAn, in the form for C header files.

%package doc
Summary: SeqAn documentation
BuildArch: noarch

%description doc
Info files of SeqAn's apps.

%prep
%setup -q -n seqan-%{version}
%patch0 -p0
%patch1 -p0

%ifarch %{arm} aarch64 %{power64} s390x
%patch2 -p0
%endif

## Remove spurious executable permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.cpp" -exec chmod 0644 '{}' \;

## Renamed each single license file 
cp -p extras/apps/rep_sep/LICENSE LGPLv3+.txt
cp -p core/apps/rabema/LICENSE GPLv3+.txt
cp -p LICENSE BSD.txt 

## Make install needs this README file
cp -p extras/apps/seqan_flexbar/INFO extras/apps/seqan_flexbar/README

%build
mkdir -p build/Release && pushd build/Release
# cc1plus: out of memory on ARM
%ifarch %{arm} %{ix86}
SEQAN_OPT_FLAGS=$(echo "$RPM_OPT_FLAGS" | sed -e 's/-O2/-O0/g')
SEQAN_OPT_FLAGS="$SEQAN_OPT_FLAGS -fPIC"
%else
SEQAN_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC"
%endif
export CXXFLAGS="-std=c++14 $SEQAN_OPT_FLAGS -lemon"
export LDFLAGS="$RPM_LD_FLAGS -fPIC"
cmake \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="$SEQAN_OPT_FLAGS" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
 -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
 -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_BUILD_TYPE:STRING=Release -DSEQAN_BUILD_SYSTEM=SEQAN_RELEASE_APPS \
 -DSEQAN_HAS_BZIP2=1 -DSEQAN_HAS_ZLIB=1 -DSEQAN_APP_VERSION:STRING=%{version} \
 -DZLIB_INCLUDE_DIR:PATH=%{_includedir} -DZLIB_LIBRARY:FILEPATH="-L%{_libdir} -lz" \
 -DBZIP2_INCLUDE_DIR:PATH=%{_includedir} -DBZIP2_LIBRARY:FILEPATH="-L%{_libdir} -lbz2" \
 -DLEMON_INCLUDE_DIR:PATH=%{_includedir} -DLEMON_LIBRARY:FILEPATH="-L%{_libdir} -lemon" \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir} -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE ../..

## Compiler fails with parallel make
make -j1 all

%install
%make_install -C build/Release

## Put header files in ad-hoc include directory  
mkdir -p %{buildroot}%{_includedir}/seqan
cp -pr extras/include/seqan/* %{buildroot}%{_includedir}/seqan
cp -pr core/include/seqan/* %{buildroot}%{_includedir}/seqan

mkdir -p seqandoc
cp -pr %{buildroot}%{_docdir}/seqan/* seqandoc
rm -rf %{buildroot}%{_docdir}/seqan
rm -f seqandoc/*.txt

## Rename 'join' binary file; it conflicts with the one owned by 'coreutils' package
mv %{buildroot}%{_bindir}/join %{buildroot}%{_bindir}/searchjoin

## Fix executable permissions
find %{buildroot}%{_bindir} -type f -name "*.h" -exec chmod 0755 '{}' \;

%files
%license BSD.txt GPLv3+.txt LGPLv3+.txt
%doc README.rst
%{_bindir}/*

%files doc
%license BSD.txt GPLv3+.txt LGPLv3+.txt
%doc seqandoc

%files devel
%license BSD.txt GPLv3+.txt LGPLv3+.txt
%doc README.rst
%{_includedir}/seqan/

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-51
- Use _fortify_level (rhbz#2161371)
- Reduce optimization level in i686

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-49
- Drop JDK in i686 builds

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.2-48
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 1.4.2-44
- Force C++14 as this code is not C++17 ready

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-43
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-41
- BuildRequires python3-setuptools

* Fri Feb 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Linker flag to liblemon

* Fri Aug 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
- Do not perform the tests (need Python2 tools)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.4.2-36
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-35
- Add gcc-c++ BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.4.2-32
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-30
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-27
- Rebuilt for Boost 1.63

* Sat Nov 12 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-26
- Skip tests on s390 and ppc

* Sat Nov 12 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-25
- Skip failed tests

* Sat Feb 20 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-24
- Fixed compiler/linker flags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-22
- Rebuilt for Boost 1.60

* Wed Oct 21 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-21
- Actived hardened build

* Tue Oct 13 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-20
- Rebuilt for cmake 3.4.0
- Used %%license

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-19
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sat Jul 18 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-17
- Parallel make always disabled

* Sat Jul 18 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-16
- Rebuild for Boost upgrade to 1.58.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-14
- Reduce optimization to -O0 (cc1plus error persists)

* Fri May 15 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-13
- SPEC cleanups

* Fri May 15 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-12
- Removed -pipe flag because of cc1plus error on ARMs

* Thu May 14 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-11
- Set job=1 to Make on ARMs aarch64 ppc64 ppc64le

* Thu May 14 2015 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-10
- Downgrading to 1.4.2
- Excluded s390 s390x arches
- Excluded bstools_test on ARMs aarch64 ppc64 ppc64le

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.4.2-9
- Rebuild for boost 1.57.0

* Tue Dec 02 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-8
- Excluded bs_tools test on ARM

* Mon Dec 01 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-7
- Parallel tests not performed on ARM

* Mon Dec 01 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-6
- DBUILD_SHARED_LIBS boolean disabled
- Test enabled

* Tue Nov 25 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-5
- Parallel make excluded on ARM arch

* Tue Nov 25 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-4
- Tests disabled temporarily

* Sat Nov 22 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-3
- Packaged private libraries
- Performed tests
- Splazers and fiona tests excluded

* Sat Nov 22 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-2
- Parallel make excluded on ARM arch

* Fri Nov 21 2014 Antonio Trande <sagitterATfedoraproject.org> - 1.4.2-1
- Update to 1.4.2
- Fixed cmake compiler flags
- Fixed declaration of multiple license
- A doc sub-package is now built

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Antonio Trande <sagitterATfedoraproject.org> 1.4.1-2
- Added 'Provides:bundled(gnulib)'
- Changed find command for executable permissions fixing
- Use %%make_install 
- Fixed wrong-file-end-of-line-encoding warnings
 
* Wed Jun 11 2014 Antonio Trande <sagitterATfedoraproject.org> 1.4.1-1
- First package
