%global git_version 26_g604758e_open
%global MAKEARG PSM_HAVE_SCIF=0 MIC=0 arch=$(uname -m)

Name:           infinipath-psm
Summary:        Intel Performance Scaled Messaging (PSM) Libraries
Version:        3.3
Release:        %{git_version}.6%{?dist}.14
# Automatically converted from old format: GPLv2 or BSD - review is highly recommended.
License:        GPL-2.0-only OR LicenseRef-Callaway-BSD
ExclusiveArch:  x86_64
URL:            https://github.com/01org/psm
# Source0 tar ball had been created by run:
# 1) git clone https://github.com/01org/psm.git
# 2) cd psm
# 3) make dist
Source0:        %{name}-%{version}-%{git_version}.tar.gz
Source1:        ipath.rules
Patch1:         0001-fix-a-compilation-issue.patch
Patch3:         remove-executable-permissions-for-header-files.patch
Patch4:         0001-Include-sysmacros.h.patch
Patch5:         0001-Extend-buffer-for-uvalue-and-pvalue.patch
Patch6:         extend-fdesc-array.patch
Patch7:         psm-multiple-definition.patch
Patch8:         infinipath-psm-gcc11.patch
Patch9:         fix-clang-build.patch

Requires:       udev
%if "%{toolchain}" == "clang"
BuildRequires:  clang
%else
BuildRequires:  gcc
%endif
BuildRequires:  libuuid-devel
BuildRequires:  systemd-rpm-macros
BuildRequires: make
Obsoletes:      infinipath-libs <= %{version}-%{release}

%description
The PSM Messaging API, or PSM API, is Intel's low-level
user-level communications interface for the True Scale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%package devel
Summary:        Development files for Intel PSM
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      infinipath-devel <= %{version}-%{release}

%description devel
Development files for the %{name} library.

%prep
%setup -q -n %{name}-%{version}-%{git_version}
%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p0
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
find libuuid -type f -not -name 'psm_uuid.[c|h]' -not -name Makefile -delete

%build
# LTO seems to trigger a post-build failure as some symbols with external scope
# are "leaking".  SuSE has already disabled LTO for this package, but no real
# details about why those symbols are "leaking".  Follow their lead for now
%define _lto_cflags %{nil}

%{set_build_flags}
%make_build PSM_USE_SYS_UUID=1 %{MAKEARG}

%install
%make_install %{MAKEARG}
install -d %{buildroot}%{_udevrulesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-ipath.rules

%ldconfig_scriptlets

%files
%{_udevrulesdir}/60-ipath.rules
%{_libdir}/libpsm_infinipath.so.*
%{_libdir}/libinfinipath.so.*
%license COPYING
%doc README

%files devel
%{_libdir}/libpsm_infinipath.so
%{_libdir}/libinfinipath.so
%{_includedir}/psm.h
%{_includedir}/psm_mq.h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3-26_g604758e_open.6.13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Honggang Li <honggangli@163.com> - 3.3-26_g604758e_open.6.11
- Fix FTBFS in Fedora rawhide/f41
- Resolves: bz2225925

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 3.3-26_g604758e_open.6.2
- Avoid out of bounds array index diagnostic with gcc-11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Jeff Law <law@redhat.com> - 3.3-26_g604758e_open.6
- Disable LTO

* Sun Feb 09 2020 Honggang Li <honli@redhat.com> - 3.3-26_g604758e_open.5
- Fix FTBFS in Fedora rawhide/f32
- Resolves: bz1799521

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Honggang Li <honli@redhat.com> - 3.3-26_g604758e_open.3
- Fix udev rule issues
- Resolves: bz1785112

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-26_g604758e_open.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Honggang Li <honli@redhat.com> - 3.3-26_g604758e_open.1
- Fix FTBFS issue for Fedora rawhide/f30
- Resolves: 1675150

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22_g4abbc60_open.6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22_g4abbc60_open.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Honggang Li <honli@redhat.com> - 3.3-22_g4abbc60_open.6
- Fix partial injection of Fedora build flags.
- Double the sizeof array fdesc to fix a gcc7 compiling issue.
- Resolves: bz1548537

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22_g4abbc60_open.5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan  4 2018 Honggang Li <honli@redhat.com> - 3.3-22_g4abbc60_open.5
- No longer obsoletes libpsm2-compat.
- Resolves: bz1530982

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22_g4abbc60_open.4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22_g4abbc60_open.4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Honggang Li <honli@redhat.com> - 3.3-22_g4abbc60_open.4
- Include sysmacros.
- Extend buffer for two arrays.
- Resolves: bz1423739

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22_g4abbc60_open.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 31 2016 Honggang Li <honli@redhat.com> - 3.3-22_g4abbc60_open.3
- Obsoletes libpsm2-compat.

* Wed Apr 20 2016 Honggang Li <honli@redhat.com> - 3.3-22_g4abbc60_open.2
- Honors RPM_OPT_FLAGS.
- Link against system libuuid package.
- Remove duplicated Conflicts tags.

* Mon Apr 18 2016 Honggang Li <honli@redhat.com> - 3.3-22_g4abbc60_open.1
- Import infinipath-psm for Fedora.
