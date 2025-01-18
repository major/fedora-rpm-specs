%global major_version 1.10

Name:           botan
Version:        %{major_version}.17
Release:        46%{?dist}
Summary:        Crypto library written in C++

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://botan.randombit.net/
# tarfile is stripped using repack.sh. original tarfile to be found
# here: http://botan.randombit.net/releases/Botan-%%{version}.tgz
Source0:        Botan-%{version}.stripped.tar.gz
Source1:        README.fedora
# Enable only cleared ECC algorithms
Patch0:         botan-1.10.5-ecc-fix.patch
# Make boost_python selectable
Patch1:         botan-boost_python.patch
# Fix wrong path
Patch2:         botan-1.10.13-python-init.patch
# 2to3 doc/conf.py
Patch3:         botan-1.10.17-doc-conf-2to3.patch
# Fix FTBFS
Patch4:         botan-1.10.17-u64bit.patch
# Add RISC-V (riscv64)
# Upstream in later versions:
# https://github.com/randombit/botan/blob/master/src/build-data/arch/riscv64.txt
Patch9:         Botan-1.10.17-add-riscv64.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  make

# do not check .so files in the python_sitelib directories
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#10 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       bzip2-devel
Requires:       zlib-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
%{summary}

This package contains HTML documentation for %{name}.


%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.

Note: The Python binding should be considered alpha software, and the
interfaces may change in the future.


%prep
%setup -q -n Botan-%{version}
%autosetup -p1 -n Botan-%{version}

# These tests will fail.
rm -rf checks/ec_tests.cpp

%build

# we have the necessary prerequisites, so enable optional modules
%global enable_modules bzip2,zlib

# fixme: maybe disable unix_procs, very slow.
%global disable_modules gnump

%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --disable-modules=%{disable_modules} \
        --with-boost-python \
        --with-python-version=dummy.dummy \
        --with-sphinx

# (ab)using CXX as an easy way to inject our CXXFLAGS
make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags}

make -f Makefile.python \
     CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} \
     PYTHON_INC="$(python3-config --includes)" \
     PYTHON_ROOT=. \
     BOOST_PYTHON=boost_python%{python3_version_nodots}

%install
make install \
     DESTDIR=%{buildroot}%{_prefix} \
     DOCDIR=%{buildroot}%{_pkgdocdir} \
     INSTALL_CMD_EXEC="install -p -m 755" \
     INSTALL_CMD_DATA="install -p -m 644"

make -f Makefile.python install \
     PYTHON_SITE_PACKAGE_DIR=%{buildroot}%{python3_sitearch}


# fixups
find doc/examples -type f -exec chmod -x {} \;
mv doc/examples/python doc/python2-examples
cp -a doc/{examples,python2-examples,license.txt} \
   %{buildroot}%{_pkgdocdir}
cp -a %{SOURCE1} %{buildroot}%{_pkgdocdir}
rm -r %{buildroot}%{_pkgdocdir}/manual/{.doctrees,.buildinfo}


%ldconfig_post


%ldconfig_postun


%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/readme.txt
%{_pkgdocdir}/README.fedora
%if 0%{?_licensedir:1}
%exclude %{_pkgdocdir}/license.txt
%license doc/license.txt
%else
%{_pkgdocdir}/license.txt
%endif # licensedir
%{_libdir}/libbotan-%{major_version}.so.*


%files devel
%{_pkgdocdir}/examples
%{_bindir}/botan-config-%{major_version}
%{_includedir}/*
%exclude %{_libdir}/libbotan-%{major_version}.a
%{_libdir}/libbotan-%{major_version}.so
%{_libdir}/pkgconfig/botan-%{major_version}.pc


%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/manual
# next files duplicated on purpose, because -doc doesn't depend on the
# main package
%{_pkgdocdir}/readme.txt
%{_pkgdocdir}/README.fedora
%if 0%{?_licensedir:1}
%exclude %{_pkgdocdir}/license.txt
%license doc/license.txt
%else
%{_pkgdocdir}/license.txt
%endif # licensedir
%{_pkgdocdir}/python2-examples


%files -n python3-%{name}
%{python3_sitearch}/%{name}


%check
make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} check

# these checks would fail
mv checks/validate.dat{,.orig}
awk '/\[.*\]/{f=0} /\[(RC5.*|RC6)\]/{f=1} (f && !/^#/){sub(/^/,"#")} {print}' \
    checks/validate.dat.orig > checks/validate.dat
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./check --validate


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.17-45
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.10.17-43
- Rebuilt for Python 3.13

* Sat Feb 24 2024 David Abdurachmanov <davidlt@rivosinc.com> - 1.10.17-42
- Add support for riscv64

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-39
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.10.17-37
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-36
- Rebuilt for Boost 1.81

* Sun Jan 22 2023 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.17-35
- Add patch to fix FTBFS.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> - .17-32
- Replace obsolete boost-python3-devel build dependency (#2100748)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.10.17-31
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.10.17-30
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 11 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.17-28
- Fix FTBFS on F35 and later.

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-27
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.17-25
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-23
- Rebuilt for Boost 1.75

* Thu Oct 01 2020 Jeff Law <law@redhat.com> - 1.10.17-22
- Re-enable LTO

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 1.10.17-21
- Disable LTO on armv7hl for now.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-19
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-18
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-15
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.17-14
- Remove dependency on OpenSSL (for F31+).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-11
- Use %%{python3_version_nodots} for Boost.Python library name

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-11
- Use boost_python37 for library name

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-11
- Rebuilt for Boost 1.69

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-10
- Remove Python 2 subpackage (#1627321)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-8
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.17-7
- Use ldconfig scriptlet macros.

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-6
- Rebuilt for Python 3.7

* Thu Jun 28 2018 David Abdurachmanov <david.abdurachmanov@gmail.com> - 1.10.17-5
- Switch BR boost-python-devel to boost-python2-devel

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.17-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.10.17-2
- Rebuilt for Boost 1.66

* Mon Oct  2 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.17-1
- Update to 1.10.17.
- Remove obsolete patches.

* Fri Sep 08 2017 Troy Dawson <tdawson@redhat.com> - 1.10.16-2
- Cleanup spec file conditionals

* Sun Aug 13 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.16-1
- Update to 1.10.16.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10.14-8
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10.14-5
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.10.14-4
- Rebuild for Python 3.6

* Sat Dec 10 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.14-3
- Add -std=c++11 to the compilerflags (needed on EPEL7).

* Fri Dec  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.14-2
- Update to 1.10.14.
- Depend on OpenSSL 1.0 compat package for F26+.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.13-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.13-3
- Fix typo.

* Sun Jul  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.13-2
- Provide python2- and python3- subpackages (rhbz#1313786).
- Move python examples to -doc subpackage.

* Fri Apr 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.13-1
- Update to 1.10.13.

* Mon Feb  8 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.12-1
- Update to 1.10.12.
- Mark license.txt with %%license.
- Change %%define -> %%global.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.10.9-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.10.9-8
- Rebuilt for Boost 1.59

* Fri Jul 24 2015 David Tardon <dtardon@redhat.com> - 1.10.9-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-5
- Rebuild for gcc5.

* Fri Feb  6 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-4
- Re-enable cleared ECC. Patch by Tom Callaway <spot@fedoraproject.org>.

* Thu Feb  5 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-3
- Disable gmp engine (see bug 1116406).
- Use _pkgdocdir.

* Thu Feb  5 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-2
- Remove workaround for bug 1186014.

* Sat Jan 31 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-1
- Update to 1.10.9.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Björn Esser <bjoern.esser@gmail.com> - 1.10.8-5
- rebuild for boost 1.55.0 (libboost_python.so.1.55.0)

* Sun May 25 2014 Brent Baude <baude@us.ibm.com> - 1.10.8-4
- Added ppc64le arch support

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.10.8-3
- rebuild for boost 1.55.0

* Mon May 12 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.10.8-2
- Added AArch64 architecture support

* Sat May 10 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.8-1
- Update to 1.10.8.

* Tue Sep  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.5-4
- Re-enable IDEA (rhbz#1003052) and SRP-6.

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 1.10.5-3
- Rebuild for boost 1.54.0

* Fri Jul 26 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.5-2
- Rename the subpackage for the Python binding.

* Fri Jul 26 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.5-1
- Update to 1.10.5.
- Modernize spec file.
- New -doc subpackage containing HTML documentation.
- Package Python binding.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.14-1
- Update to 1.8.14.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-4.2
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8.13-2.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 1.8.13-2.1
- rebuild with new gmp

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.13-2
- Patch to revert the soname change.

* Wed Jul 20 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.13-1
- Update to 1.8.13.

* Sat Jul  2 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.12-1
- Update to 1.8.12.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.11-1
- Update to 1.8.11.

* Sat Sep  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.10-1
- Update to 1.8.10.

* Sun Aug 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-4
- Update README.fedora.

* Fri Aug 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-3
- Also remove RC5 from the tarfile.
- Comment out RC5, RC6 and IDEA validation tests.

* Wed Aug  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-2
- Remove IDEA, RC6, and ECC-related modules from the tarfile,
  see bz 615372.

* Wed Jun 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-1
- Update to 1.8.9.
- Drop patch applied upstream.

* Thu Nov 19 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.8-2
- Add patch from upstream to build with binutils-2.20.51.0.2.
  Fixes bz 538949 (ftbfs).

* Thu Nov  5 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.8-1
- Update to 1.8.8, a bugfix release.

* Thu Sep 10 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.7-1
- Update to 1.8.7. This is mainly a bugfix release.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.8.6-2
- rebuilt with new openssl

* Thu Aug 13 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.6-1
- Update to 1.8.6, which contains new features as well as bugfixes,
  e.g. concerning the /proc-walking entropy source.

* Wed Aug 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.5-2
- Fix changelog.

* Wed Aug 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.5-1
- Update to 1.8.5.
- Use .tbz source file.
- Configuration script uses python now.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.2-1
- Update to 1.8.2.

* Mon Mar 16 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.1-4
- Add missing requirements to -devel package.

* Fri Feb 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.1-3
- Rebuilt again after failed attempt in mass rebuild.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.1-1
- Update to 1.8.1. This is a bugfix release, see
  http://botan.randombit.net/news/releases/1_8_1.html for changes.
- No need to explicitly enable modules that will be enabled by
  configure.pl anyway.

* Mon Jan 19 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-2
- Move api* and tutorial* doc files to -devel package.

* Sat Jan 17 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-1
- New package.
