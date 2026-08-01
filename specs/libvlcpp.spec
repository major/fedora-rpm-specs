# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
# main package has no files, -devel is noarch
%global debug_package %{nil}

Name:           libvlcpp
Version:        3.0.0
Release:        1%{?dist}
Summary:        C++ bindings for libvlc

License:        LGPL-2.1-or-later
URL:            https://code.videolan.org/videolan/libvlcpp
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0:         libvlcpp-pkgconfig.patch

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: vlc-devel
# required for tests
BuildRequires: vlc-plugin-ffmpeg

%description
C++ bindings for libvlc.

%package        devel
Summary:        Development files for %{name}
Requires:       vlc-devel
Provides:       libvlcpp-static = %{version}-%{release}
BuildArch:      noarch

%description    devel
C++ bindings for libvlc.


%prep
%autosetup -p1 -n %{name}-v%{version}

%conf
%meson \
  -Dexamples=enabled \
  -Dtests=enabled \


%build
%meson_build

%install
%meson_install

%check
%meson_test

%files devel
%doc AUTHORS NEWS
%license COPYING
%{_includedir}/vlcpp/
%{_datadir}/pkgconfig/libvlcpp.pc


%changelog
* Wed Jul 29 2026 Dominik Mierzejewski <dominik@greysector.net> - 3.0.0-1
- update to latest stable release (resolves rhbz#2495868)
- enable tests

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0^20240204git44c1f48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0^20240204git44c1f48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0^20240204git44c1f48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0^20240204git44c1f48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 01 2025 Dominik Mierzejewski <dominik@greysector.net> - 0.1.0^20240204git44c1f48-1
- switch versioning to current recommended way
- use SPDX identifier in License:
- add missing dependencies on vlc-devel
- build examples to test vlc linkage
- add missing Provides: libvlcpp-static
- make only the -devel subpackage noarch

* Sun Dec 08 2024 Sérgio Basto <sergio@serjux.com> - 0.1.0-18.20240204git44c1f48
- Update to current snapshot

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-17.20230527gitd76fe06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-16.20230527gitd76fe06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 23 2023 Sérgio Basto <sergio@serjux.com> - 0.1.0-15.20230527gitd76fe06
- Try build it without the hack

* Thu Aug 03 2023 Sérgio Basto <sergio@serjux.com> - 0.1.0-14.20230527gitd76fe06
- Update to current snapshot

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-13.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-12.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-11.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-10.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-9.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-8.e81b9f0git
- Update to current snapshot

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-7.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-6.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-5.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-4.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.0-3.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-2.20180206git
- Update snapshot

* Mon Sep 04 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file
