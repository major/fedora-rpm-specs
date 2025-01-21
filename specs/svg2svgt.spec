Name:           svg2svgt
Version:        0.9.6
Release:        22%{?commit:.git%shortcommit}%{?dist}
Summary:        SVG to SVG Tiny converter

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/manisandro/svg2svgt
Source0:        https://github.com/manisandro/svg2svgt/archive/v{%version}/%{name}-%{version}.tar.gz

# Add missing include
Patch0:         svg2svgt_includes.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-qt5-qttools-tools
BuildRequires: mingw32-qt5-qtsvg
BuildRequires: mingw32-qt5-qtxmlpatterns

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-qt5-qttools-tools
BuildRequires: mingw64-qt5-qtsvg
BuildRequires: mingw64-qt5-qtxmlpatterns

Requires:       hicolor-icon-theme

%description
Library and tools to convert SVG images to SVG Tiny, the subset of SVG
implemented by QtSvg.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{name}-%{?commit:%commit}%{!?commit:%version}


%build
# Native build
%cmake
%cmake_build

# MinGW build
%mingw_cmake
%mingw_make_build


%install
%cmake_install

%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/{applications,icons,metainfo}/
rm -rf %{buildroot}%{mingw64_datadir}/{applications,icons,metainfo}/

%find_lang %{name} --with-qt


%mingw_debug_install_post


%check
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%ctest


%files -f %{name}.lang
%license LICENSE.LGPL
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_libdir}/lib%{name}.so.*
%dir %{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n mingw32-%{name}
%license LICENSE.LGPL
%{mingw32_bindir}/%{name}.exe
%{mingw32_bindir}/%{name}-gui.exe
%{mingw32_bindir}/lib%{name}-0.dll
%{mingw32_datadir}/%{name}/
%{mingw32_includedir}/%{name}/
%{mingw32_libdir}/lib%{name}.dll.a
%{mingw32_libdir}/pkgconfig/%{name}.pc

%files -n mingw64-%{name}
%license LICENSE.LGPL
%{mingw64_bindir}/%{name}.exe
%{mingw64_bindir}/%{name}-gui.exe
%{mingw64_bindir}/lib%{name}-0.dll
%{mingw64_datadir}/%{name}/
%{mingw64_includedir}/%{name}/
%{mingw64_libdir}/lib%{name}.dll.a
%{mingw64_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.6-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.9.6-15
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 0.9.6-14
- Make mingw subpackages noarch

* Sat Feb 19 2022 Sandro Mani <manisandro@gmail.com> - 0.9.6-13
- Add mingw subpackage

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 0.9.6-8
- Use __cmake_in_source_build

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.6-2
- Remove obsolete scriptlets

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-1
- Update to 0.9.6

* Wed Aug 30 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.3.git5760c9d
- Added %%{?_smp_mflags} to make check

* Tue Aug 29 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.2.git5760c9d
- Added desktop and appdata files
- Add -Wl,--as-needed

* Mon Aug 28 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.1.git7a182a9
- Initial package
