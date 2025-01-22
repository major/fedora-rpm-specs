# Turn off LTO for architectures where this fails
%ifarch %{arm} %{ix86} s390x
%global _lto_cflags %nil
%endif

# Turn off 4th derivatives for 32-bit targets
%ifarch %{arm} %{ix86}
%global lxcflag -DDISABLE_LXC=ON
%else
%global lxcflag -DDISABLE_LXC=OFF
%endif

# Shared library version
%global soversion 15

Name:           libxc
Summary:        Library of exchange and correlation functionals for density-functional theory
Version:        7.0.0
Release:        3%{?dist}
License:        MPL-2.0
Source0:        https://gitlab.com/libxc/libxc/-/archive/%{version}/%{name}-%{version}.tar.gz
# Don't rebuild libxc for pylibxc
Patch0:         libxc-7.0.0-pylibxc.patch
URL:            http://www.tddft.org/programs/octopus/wiki/index.php/Libxc

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools

%description
libxc is a library of exchange and correlation functionals. Its purpose is to
be used in codes that implement density-functional theory. For the moment, the
library includes most of the local density approximations (LDAs), generalized
density approximation (GGAs), and meta-GGAs. The library provides values for
the energy density and its 1st, 2nd, 3rd, and 4th derivatives.

%package devel
Summary:        Development library and headers for libxc
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake

%description devel
libxc is a library of exchange and correlation functionals. Its purpose is to
be used in codes that implement density-functional theory. For the moment, the
library includes most of the local density approximations (LDAs), generalized
density approximation (GGAs), and meta-GGAs. The library provides values for
the energy density and its 1st, 2nd, 3rd, and 4th derivatives.

This package contains the development headers and library that are necessary
in order to compile programs against libxc.

%package -n python3-%{name}
Summary:        Python3 interface to libxc
Requires:       python3-numpy
Requires:       %{name} = %{version}-%{release}
Obsoletes:      python2-%{name} < %{version}-%{release}
Obsoletes:      python3-%{name} < %{version}-%{release}
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
%else
%{?python_provide:%python_provide python3-%{name}}
%endif
%description -n python3-%{name}
libxc is a library of exchange and correlation functionals. Its purpose is to
be used in codes that implement density-functional theory. For the moment, the
library includes most of the local density approximations (LDAs), generalized
density approximation (GGAs), and meta-GGAs. The library provides values for
the energy density and its 1st, 2nd, 3rd, and 4th derivatives.

This package contains the Python3 interface library to libxc.

%prep
%setup -q
%patch 0 -p1 -b .pylibxc
# Plug in library soversion
sed -i "s|@SOVERSION@|%{soversion}|g;s|@LIBDIR@|%{_libdir}|g" pylibxc/core.py

%build
# Disable var tracking assignments for C sources, since it fails anyhow due to the size of the sources
export CFLAGS="%{optflags} -fno-var-tracking-assignments"
%cmake -DDISABLE_VXC=OFF -DDISABLE_FXC=OFF -DDISABLE_KXC=OFF %{lxcflag} -DENABLE_FORTRAN=ON -DENABLE_PYTHON=ON -DENABLE_XHOST=OFF
%cmake_build

%install
%cmake_install
# Move modules in the right place
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}
# Move python library to the right place
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_libdir}/pylibxc %{buildroot}%{python3_sitearch}

# Remove bibtex bibliography placed in an odd location
rm -f %{buildroot}%{_includedir}/libxc.bib

%ldconfig_scriptlets

# Run tests, don't parallellize them
%check
%ctest --parallel 1

%files
%doc README NEWS AUTHORS ChangeLog.md libxc.bib
%license COPYING
%{_bindir}/xc-info
%{_libdir}/libxc.so.%{soversion}*
%{_libdir}/libxcf03.so.%{soversion}*

%files devel
%{_libdir}/libxc.so
%{_libdir}/libxcf03.so
%{_includedir}/xc*.h
%{_fmoddir}/xc_f03_*.mod
%{_libdir}/pkgconfig/libxc.pc
%{_libdir}/pkgconfig/libxcf03.pc
%{_libdir}/cmake/Libxc/

%files -n python3-%{name}
%{python3_sitearch}/pylibxc/

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 11 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 6.2.2-7
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.2-6
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 6.2.2-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.2.2-1
- Update to 6.2.2.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.2.0-2
- Rebuilt for Python 3.12

* Fri May 26 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.2.0-1
- Update to 6.2.0.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.1.0-1
- Update to 6.1.0.

* Fri Oct 14 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.0.0-1
- Switch to CMake build.
- Update to 6.0.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.2.2-3
- Rebuilt for Python 3.11

* Wed Apr 13 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.2-2
- Forgot to expand one cosmetic macro in the Python interface.

* Tue Feb 01 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.2-1
- Update to 5.2.2.

* Mon Jan 31 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1.

* Fri Jan 21 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.7-1
- Update to 5.1.7.

* Tue Sep 07 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.6-1
- Update to 5.1.6.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.5-2
- Turn off LTO on s390x since it fails on Fedora 33.

* Thu Jun 10 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.5-1
- Update to 5.1.5.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.4-2
- Rebuilt for Python 3.10

* Mon May 10 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.4-1
- Update to 5.1.4.

* Tue Mar 30 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.3-1
- Update to 5.1.3.

* Fri Feb 12 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2.

* Tue Feb 09 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.1-1
- Disable 4th derivatives on 32-bit architectures due to compiler problems.
- Update to 5.1.1.

* Mon Feb 01 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.0-4
- Disable LTO on 32-bit architectures.

* Sun Jan 31 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.0-3
- Disable variable tracking assignments.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.0-1
- Update to version 5.1.0.

* Thu Oct 01 2020 Dominik Mierzejewski <rpm@greysector.net> - 5.0.0-6
- Link with libm directly (rhbz#1883501)

* Tue Sep 08 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.0.0-5
- Enable tests.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.0.0-3
- BR: python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0, enabling support up to 4th derivatives.
- libxcf03 has been replaced by libxcf90; the old non-ISO f90 frontend has
  been deprecated.

* Mon Apr 06 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.3-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.3-1
- Update to 4.3.3.

* Fri Feb 08 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2.

* Wed Feb 06 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1.

* Wed Jan 30 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0.

* Wed Nov 21 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2.3-1
- Remove python2 subpackage from rawhide.
- Update to 4.2.3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0.

* Wed May 09 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1, changing license to MPLv2 and adding Python interface.

* Fri May 04 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-1
- Update to 4.0.5.

* Wed Feb 07 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.4-1
- Update to 4.0.4.

* Mon Nov 20 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2.

* Mon Oct 09 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1.

* Wed Sep 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0, removing single precision libraries.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 3.0.0-3
- Rebuilt for libgfortran soname bump

* Thu Jun 30 2016 Rafael Fonseca <rdossant@redhat.com> - 3.0.0-2
- Fix compilation on ppc64.

* Thu Apr 21 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.2-4
- Drop gfortran requires on -devel.

* Fri Apr 24 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.2-3
- Patch some hybrids.

* Fri Apr 24 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.2-2
- Patch broken makefiles.

* Thu Feb 19 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-2
- Re-enable builds on ppc and ppc64 on EPEL.

* Fri Mar 21 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-1
- Enable single precision routines as well.
- Update to 2.1.0.

* Tue Feb 18 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3.

* Mon Feb 17 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.2-3
- Fix bug with some mgga correlation functionals.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2.

* Wed Mar 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-3
- Fix FTBFS in rawhide.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1.

* Fri Dec 7 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-4
- Clean buildroot at the beginning of %%install.

* Sun Jan 23 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-3
- Update tarball.
- Make requirement on gcc-gfortran in -devel architecture explicit.

* Sat Jan 22 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-2
- Minor review fixes.

* Tue Jan 18 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-1
- Initial specfile.
