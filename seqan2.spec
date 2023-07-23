%global __cmake_in_source_build 1

# Default ld_as_needed flag breaks executables linkage
%undefine _ld_as_needed

# Tests need Python2 to be executed
%global with_check 0

# Documentation needs Python2 to be built
%global with_doc 0
Obsoletes: seqan2-doc < 0:2.4.0-8

Name:      seqan2
Summary:   C++ library of efficient algorithms and data structures
Version:   2.4.0
Release:   20%{?dist}
License:   BSD
URL:       http://www.seqan.de/
Source0:   https://github.com/seqan/seqan/archive/seqan-v%{version}.tar.gz#/seqan-seqan-v%{version}.tar.gz

# Disable automatic stripping on no-DEVELOP seqan build systems 
Patch0: seqan-disable_stripping.patch

# Set paths of seqan-2.pc and seqan-config.cmake
Patch1: %{name}-set_config_filepath.patch

# Set paths of plot.awk and ps2pswLinks.gawk files
Patch2: %{name}-set_awk_installation.patch

BuildRequires: make
BuildRequires: qt4-devel
BuildRequires: cmake, gcc-c++
BuildRequires: llvm-devel
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: boost-devel
BuildRequires: coin-or-lemon-devel
BuildRequires: libstdc++-static
BuildRequires: python3-devel

## Test
%if 0%{?with_check}
BuildRequires: python3-nose
BuildRequires: python3-pytest
BuildRequires: python3-jinja2
%endif

## Bundled files exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)

%description
SeqAn (version 2.x.x) is an open source C++ library of efficient algorithms
and data structures for the analysis of sequences with the focus on
biological data. 
Our library applies a unique generic design that guarantees high performance, 
generality, extensibility, and integration with other libraries.

As such, it contains algorithms and data structures for

 * string representation and their manipluation,
 * online and indexed string search,
 * efficient I/O of bioinformatics file formats,
 * sequence alignments, and
 * many, many more.


%package apps
Summary: SeqAn (2.x.x) applications

## Seqan apps are licenses under BSD and GPLv3+ and LGPLv3+.
#
# BSD (3-clauses): alf, bs_tools, fiona, fx_tools, gustaf
# insegt, mason2, ngs_roi, param_chooser, rabema, razers3
# sak, sam2matrix, samcat, searchjoin, seqcons2, yara
# ngs_roi, pair_align, ngs_roi.
#
# GPLv3+: rabema.
#
# LGPLv3+: dfi, insegt, micro_razers, pair_align
# param_chooser, razers, razers3, rep_sep, sak
# seqan_tcoffee, sgip, snp_store, splazers, stellar
# tree_recon.
##
# LGPLv3 gives you permission to relicense the code under GPLv3
# BSD (3-clauses) is compatible with GPLv3
# We can use a collective license:
License:  GPLv3+ and BSD and LGPLv3+
Requires: gawk%{?_isa}

# 'seqan2' is the most recent version of 'SeqAn'
Obsoletes: seqan <= 0:1.4.2
Provides:  seqan =  0:%{version}-%{release}

%description apps
All SeqAn applications.

%package headers
Summary: SeqAn (2.x.x) headers only files

# bzip2stream and zipstream libraries are distributed under zlib/libpng
# basic/boost*.h libraries are distributed under Boost
# bam_io/bam_index_bai.h is distributed under MIT
# Although Boost, zlib, MIT are GPL compatible, they're all tagged anyway
License:   GPLv3+ and BSD and MIT and LGPLv3+ and zlib and Boost

Provides: bundled(bzip2stream)
Provides: bundled(zipstream)

%description headers
C headers files of SeqAn, including pkconfig and CMake configuration files.

%package examples
Summary: SeqAn (2.x.x) examples
Requires: %{name}-apps%{?_isa} = %{version}-%{release}
%description examples
Testing files of SeqAn2's apps.

%if 0%{?with_doc}
%package doc
Summary: SeqAn (2.x.x) documentation

# 3L is licensed under MIT
# Less and bootstrap files is licensed under ASL 2.0
# jquery-bbq are licensed under LGPLv3+
License: LGPLv3+ and MIT and ASL 2.0
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
Requires: fontawesome-fonts-web
BuildArch: noarch

# https://github.com/mateuszkocz/3l
Provides: bundled(3l) = 1.4.4

# http://lesscss.org/
Provides: bundled(less) = 1.3.3

# http://twbs.github.com/bootstrap
Provides: bundled(bootstrap) = 3.0.0

Obsoletes: seqan-doc <= 0:1.4.2
Provides:  seqan-doc =  0:%{version}-%{release}
%description doc
Info files of SeqAn2's apps.
%endif

%prep
%autosetup -p0 -n seqan-seqan-v%{version}

## Remove spurious executable permissions
find . -perm /755 -type f \( -name "*.cpp" -o -name "*.h" \) -exec  chmod -x {} ';'

## Renamed each single license file 
for appID in `ls apps/ | grep -v CMakeLists`; do
 cp -p apps/$appID/LICENSE apps/$appID/$appID-LICENSE
done
cp -p apps/rabema/COPYING apps/rabema/rabema-COPYING

# Unbundle font-awesome fonts
rm -rf util/py_lib/seqan/dox/tpl/lib/font-awesome/*

%build
mkdir -p build/library && pushd build/library
SEQAN_OPT_FLAGS="$RPM_OPT_FLAGS"
%cmake \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="$SEQAN_OPT_FLAGS -DNDEBUG" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DCMAKE_INSTALL_DOCDIR:STRING=share/doc/%{name} \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \
 -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
 -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
 -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DSEQAN_BUILD_SYSTEM:STRING=SEQAN_RELEASE_LIBRARY \
 -DSEQAN_DISABLE_VERSION_CHECK:BOOL=ON \
 -DZLIB_INCLUDE_DIR:PATH=%{_includedir} -DZLIB_LIBRARY:FILEPATH=%{_libdir}/libz.so \
 -DBZIP2_INCLUDE_DIR:PATH=%{_includedir} -DBZIP2_LIBRARY:FILEPATH=%{_libdir}/libbz2.so \
 -DLEMON_INCLUDE_DIR:PATH=%{_includedir} -DLEMON_LIBRARY:FILEPATH=%{_libdir}/libemon.so \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir} -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DSPHINX_EXECUTABLE:FILEPATH=%{_bindir}/sphinx-build \
 -DSPHINX_MAN_OUTPUT:BOOL=ON \
 -DSPHINX_TEXT_OUTPUT:BOOL=ON \
 -DYARA_LARGE_CONTIGS:BOOL=OFF ../..
%make_build
popd

mkdir -p build/Release && pushd build/Release
SEQAN_OPT_FLAGS="$RPM_OPT_FLAGS"
%cmake \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="$SEQAN_OPT_FLAGS -DNDEBUG" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DCMAKE_INSTALL_DOCDIR:STRING=share/doc/%{name} \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \
 -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
 -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
 -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DSEQAN_BUILD_SYSTEM:STRING=SEQAN_RELEASE_APPS \
 -DSEQAN_DISABLE_VERSION_CHECK:BOOL=ON \
 -DZLIB_INCLUDE_DIR:PATH=%{_includedir} -DZLIB_LIBRARY:FILEPATH=%{_libdir}/libz.so \
 -DBZIP2_INCLUDE_DIR:PATH=%{_includedir} -DBZIP2_LIBRARY:FILEPATH=%{_libdir}/libbz2.so \
 -DLEMON_INCLUDE_DIR:PATH=%{_includedir} -DLEMON_LIBRARY:FILEPATH=%{_libdir}/libemon.so \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir} -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DYARA_LARGE_CONTIGS:BOOL=OFF \
 -DSPHINX_EXECUTABLE:FILEPATH=%{_bindir}/sphinx-build \
 -DSPHINX_MAN_OUTPUT:BOOL=ON \
 -DSPHINX_TEXT_OUTPUT:BOOL=ON ../..
# Disable parallel Make jobs to prevent compiler errors
make -O -j1

%install
%make_install -C build/library
%make_install -C build/Release

# Unbundle font-awesome fonts
%if 0%{?with_doc}
ln -s %{_datadir}/font-awesome/scss %{buildroot}%{_pkgdocdir}/html/lib/font-awesome/scss
ln -s %{_datadir}/font-awesome/css %{buildroot}%{_pkgdocdir}/html/lib/font-awesome/css
ln -s %{_datadir}/font-awesome/fonts %{buildroot}%{_pkgdocdir}/html/lib/font-awesome/fonts
ln -s %{_datadir}/font-awesome/less %{buildroot}%{_pkgdocdir}/html/lib/font-awesome/less
%endif

## Fix executable permissions
chmod a+x %{buildroot}%{_bindir}/*

# Set permissions and make symlinks of plot.awk and ps2pswLinks.gawk files
ln -s %{_datadir}/%{name}/pdf_plot_helper/plot.awk %{buildroot}%{_bindir}/plot.awk
ln -s %{_datadir}/%{name}/pdf_plot_helper/ps2pswLinks.gawk %{buildroot}%{_bindir}/ps2pswLinks.gawk

## Remove unnecessary files
rm -rf %{buildroot}%{_libexecdir}/seqan2/examples/ngs_roi/R
rm -f %{buildroot}%{_datadir}/doc/seqan2/LICENSE
rm -f %{buildroot}%{_datadir}/doc/seqan2/CHANGELOG.rst
rm -f %{buildroot}%{_datadir}/doc/seqan2/README.rst

%if 0%{?with_check}
%check
pushd build/Release
ctest --force-new-ctest-process -VV --parallel %{?_smp_mflags} -E app_test_fiona
%endif

%files apps
%license LICENSE
%license apps/*/*-LICENSE apps/rabema/rabema-COPYING
%doc README.rst CHANGELOG.rst
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pdf_plot_helper
%defattr(0444, root, root)
%{_datadir}/%{name}/pdf_plot_helper/plot.awk
%{_datadir}/%{name}/pdf_plot_helper/ps2pswLinks.gawk

%files headers
%license include/seqan/LICENSE
%doc README.rst CHANGELOG.rst
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/seqan-2.pc

%files examples
%{_libexecdir}/%{name}/
%exclude %{_libexecdir}/%{name}/examples/*/LICENSE

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc README.rst CHANGELOG.rst
%{_pkgdocdir}/
%endif

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-17
- Drop Java dependency (rhbz#2104101)

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.4.0-16
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-13
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-8
- Switch to Python3
- Disable documentation build
- Disable check

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-6
- Remove build dependency on python2-sphinxcontrib-bibtex

* Sun Oct 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-5
- Undefine ld_as_needed flag

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.4.0-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-1
- Update to version 2.4.0

* Wed Jan 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-0.4.20180103git8a875d
- Fix dependencies

* Tue Jan 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-0.3.20180103git8a875d
- Split off applications in a single sub-package
- Devel rpm renamed seqan-headers

* Sat Jan 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-0.2.20180103git8a875d
- plot.awk/ps2pswLinks.gawk installed in a private share datadir
- plot.awk/ps2pswLinks.gawk symliked in '_bindir'
- Renamed each single license file

* Wed Jan 10 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-0.1.20180103git8a875d
- Pre-released as seqan-2.4.0
- Add gcc-c++ BR
- Remove unnecessary R files
- Unbundle font-awesome
- Apps/libraries licensing commented

* Mon Jan 08 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.2-3.20180103git8a875d
- Documentation still disabled

* Wed Jan 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.2-2.20180103git8a875d
- Build devel commit #8a875d
- Add manually -DNDEBUG flag

* Wed Sep 20 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

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

* Sat Nov 12 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-26
- Skip tests on s390 and ppc

* Sat Nov 12 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-25
- Skip failed tests

* Sat Feb 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-24
- Fixed compiler/linker flags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-22
- Rebuilt for Boost 1.60

* Wed Oct 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-21
- Actived hardened build

* Tue Oct 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-20
- Rebuilt for cmake 3.4.0
- Used %%license

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-19
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sat Jul 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-17
- Parallel make always disabled

* Sat Jul 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-16
- Rebuild for Boost upgrade to 1.58.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-14
- Reduce optimization to -O0 (cc1plus error persists)

* Fri May 15 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-13
- SPEC cleanups

* Fri May 15 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-12
- Removed -pipe flag because of cc1plus error on ARMs

* Thu May 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-11
- Set job=1 to Make on ARMs aarch64 ppc64 ppc64le

* Thu May 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-10
- Downgrading to 1.4.2
- Excluded s390 s390x arches
- Excluded bstools_test on ARMs aarch64 ppc64 ppc64le

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.4.2-9
- Rebuild for boost 1.57.0

* Tue Dec 02 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-8
- Excluded bs_tools test on ARM

* Mon Dec 01 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-7
- Parallel tests not performed on ARM

* Mon Dec 01 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-6
- DBUILD_SHARED_LIBS boolean disabled
- Test enabled

* Tue Nov 25 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-5
- Parallel make excluded on ARM arch

* Tue Nov 25 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-4
- Tests disabled temporarily

* Sat Nov 22 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-3
- Packaged private libraries
- Performed tests
- Splazers and fiona tests excluded

* Sat Nov 22 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-2
- Parallel make excluded on ARM arch

* Fri Nov 21 2014 Antonio Trande <sagitter@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2
- Fixed cmake compiler flags
- Fixed declaration of multiple license
- A doc sub-package is now built

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Antonio Trande <sagitter@fedoraproject.org> 1.4.1-2
- Added 'Provides:bundled(gnulib)'
- Changed find command for executable permissions fixing
- Use %%make_install 
- Fixed wrong-file-end-of-line-encoding warnings
 
* Wed Jun 11 2014 Antonio Trande <sagitter@fedoraproject.org> 1.4.1-1
- First package
