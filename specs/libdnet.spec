Summary:       Simple portable interface to lowlevel networking routines
Name:          libdnet
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD

%global forgeurl https://github.com/ofalk/%{name}
Version:       1.18.0
%global tag libdnet-%{version}
%forgemeta

Release:       5%{?dist}
URL:           %{forgeurl}
Source:        %{forgesource}

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: check-devel
BuildRequires: python3-Cython
BuildRequires: python3-setuptools

%description
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling (IP filter, ipfw, ipchains,
pf, ...), network interface lookup and manipulation, raw IP
packet and Ethernet frame, and data transmission.

%package devel
Summary:       Header files for libdnet library
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package progs
Summary:       Sample applications to use with libdnet
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description progs
%{summary}.

%package -n python%{python3_pkgversion}-libdnet
%{?python_provide:%python_provide python%{python3_pkgversion}-libdnet}
# Remove before F30
Provides:      %{name}-python = %{version}-%{release}
Provides:      %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes:     %{name}-python < %{version}-%{release}
Summary:       Python bindings for libdnet
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-libdnet
%{summary}.

%prep
%forgeautosetup

%build
autoreconf -i
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

pushd python
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd

%ldconfig_scriptlets

%files
%license LICENSE
%doc THANKS TODO
%{_libdir}/*.so.*

%files devel
%{_bindir}/*
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*.3*

%files progs
%{_sbindir}/*
%{_mandir}/man8/*.8*

%files -n python%{python3_pkgversion}-libdnet
%{python3_sitearch}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.18.0-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.18.0-2
- Rebuilt for Python 3.13

* Sat Mar 09 2024 Richard W.M. Jones <rjones@redhat.com> - 1.18.0-1
- Rebase to 1.18.0 (RHBZ#2268656)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 13 2023 Richard W.M. Jones <rjones@redhat.com> - 1.17.0-1
- Rebase to 1.17.0 (RHBZ#2243862)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.16.4-2
- Rebuilt for Python 3.12

* Wed Apr 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.16.4-1
- Rebase to 1.16.4 (RHBZ#2185292)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.16.3-1
- Rebase to 1.16.3
- Use Fedora forge hosting macros.

* Tue Jan 03 2023 Richard W.M. Jones <rjones@redhat.com> - 1.16.2-1
- Rebase to 1.16.2
- Use setuptools instead of distutils (RHBZ#2154944)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.14-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Richard W.M. Jones <rjones@redhat.com> - 1.14-1
- Rebase to 1.14.
- Use newer upstream fork at https://github.com/ofalk/libdnet
- Drop multilib fix now uptream (RHBZ#342001 RHBZ#1915838).
- Drop unapplied shrext patch, no longer needed.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12-34
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12-32
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 06 2018 Oliver Falk <oliver@linux-kernel.at> - 1.12-29
- Revert - add python subpackage again, but use Python 3 and other upstream
  source (github.com/boundary)

* Tue Oct 02 2018 Oliver Falk <oliver@linux-kernel.at> - 1.12-28
- Remove Python subpackage, since no other package seems to require it (BZ1629814)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12-26
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.12-24
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12-23
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12-22
- Python 2 binary package renamed to python2-libdnet
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-18
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Richard W.M. Jones <rjones@redhat.com> - 1.12-13
- Add patch to fix multilib conflicts in dnet-config (RHBZ#342001).
- Remove RPM cruft from the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Oliver Falk <oliver@linux-kernel.at> - 1.12-10
- Add python bindings in -python subpackage (BZ#815524)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 12 2010 Oliver Falk <oliver@linux-kernel.at> - 1.12-6
- Disable build of static libs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.12-3
- Bump-n-build for GCC 4.3

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.12-2
- Rebuild for BuildID
- Changed license tag to be more conformant

* Thu Feb 15 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.12-1
- New upstream version
- New upstream web site (thanks JPO!)
- Patch for inconsistent shrext variable
- Minor edits for consistency

* Wed Jan 24 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.10-5
- Converted spec to UTF-8 to fix BZ#222794

* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.10-4
- Bump-n-build
- Reverted to 1.10; 1.11 has some serious issues

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> - 1.10-3
- Bump for FC6 rebuild

* Thu Jul 14 2005 Oliver Falk <oliver@linux-kernel.at> - 1.10-2
- Integrate Josщ's patch after reviewing the pkg.

* Fri Jul 08 2005 Oliver Falk <oliver@linux-kernel.at> - 1.10-1
- Build for FE
