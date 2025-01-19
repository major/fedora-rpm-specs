%global _configure_disable_silent_rules 1

Name:		libdrm-armada
Version:	2.0.0
Release:	16.20190424git607c697%{?dist}
Summary:	DRM driver for Marvell Armada displays

# Automatically converted from old format: GPLv2 and MIT - review is highly recommended.
License:	GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:		http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
# git clone http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
# cd libdrm-armada
# git reset --hard 607c697
# autoreconf -fi
# ./configure
# make dist
Source0:	libdrm_armada-%{version}.tar.bz2
Patch0:		libdrm-armada-c99.patch

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	gcc
BuildRequires: make

%description
Marvell Armada libdrm buffer object management module.


%package devel
Summary:	Development files for libdrm-armada


%description devel
Development files for libdrm-armada.


%prep
%autosetup -p1 -n libdrm_armada-%{version}


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%{_libdir}/libdrm_armada.so.0*
%license COPYING


%files devel
%{_includedir}/libdrm
%{_libdir}/libdrm_armada.so
%{_libdir}/pkgconfig/libdrm_armada.pc
%exclude %{_libdir}/libdrm_armada.la


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-15.20190424git607c697
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Florian Weimer <fweimer@redhat.com> - 2.0.0-9.20190424git607c697
- Port to C99 (#2155412)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.0.0-1.20190424git607c697
- Dropped the group tag
- Adjusted the release tag snapshot date

* Wed Apr 24 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.0.0-1.20180720git607c697
- Initial packaging
