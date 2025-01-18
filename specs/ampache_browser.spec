# Force out of source build
%undefine __cmake_in_source_build

Name: ampache_browser

# Lib and several dirs use this derived name. A change of this name
# is likely to break API users due to not finding files any longer.
%global vername %{name}_1

Version: 1.0.8
Release: 2%{?dist}
Summary: C++ and Qt based client library for Ampache access

License: GPL-3.0-only
URL: http://ampache-browser.org
Source0: https://github.com/ampache-browser/ampache_browser/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: qt6-qtbase-devel
%else
BuildRequires: gcc-toolset-12
BuildRequires: qt5-qtbase-devel
%endif

%description
Ampache Browser is a library that implements desktop client access to
the Ampache service (http://ampache.org). It provides end-user Qt UI and
has a simple C++ interface that allows easy integration into client
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

%cmake %{?el8:-D USE_QT6=OFF} .
%cmake_build


%install
%cmake_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/lib%{vername}.so.*

%files devel
%dir %{_includedir}/%{vername}
%{_includedir}/%{vername}/%{name}/
%{_libdir}/lib%{vername}.so
%{_libdir}/pkgconfig/%{vername}.pc
%{_libdir}/cmake/%{vername}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan  1 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8.

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.7-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.7-4
- Build with Qt 6.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7.

* Sat Nov  4 2023 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6 for Qt 6 support but build with USE_QT6=OFF.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 (no build needed, just a potential compilation fix).

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct  6 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (only the GCC 10 fix).

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Robert Scheck <robert@fedoraproject.org> - 1.0.2-6
- Added build-time conditionals for RHEL/CentOS 7 (#1846719)
- Corrected build requirement from qt5-devel to qt5-qtbase-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.0.2-4
- Add missing #include for gcc-10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20180408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr  7 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-3.20180408
- Merge fixes from v1.0 branch.
- Replace ldconfig scriptlets with %%ldconfig_scriptlets macro.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Michael Schwendt <mschwendt@fedoraproject.org> 1.0.0-1
- Create package.
