%{?mingw_package_header}

%global pkgname libsigc++30

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:          mingw-%{pkgname}
Version:       3.6.0
Release:       5%{?dist}
Summary:       MinGW Windows sigc++ 3.0 library

License:       LGPL-2.0-or-later
BuildArch:     noarch
URL:           https://github.com/libsigcplusplus/libsigcplusplus
Source0:       https://download.gnome.org/sources/libsigc++/%{release_version}/libsigc++-%{version}.tar.xz

BuildRequires: meson

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -n libsigc++-%{version}


%build
%mingw_meson
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libsigc-3.0-0.dll
%{mingw32_includedir}/sigc++-3.0/
%{mingw32_libdir}/sigc++-3.0/
%{mingw32_libdir}/libsigc-3.0.dll.a
%{mingw32_libdir}/pkgconfig/sigc++-3.0.pc


%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libsigc-3.0-0.dll
%{mingw64_includedir}/sigc++-3.0/
%{mingw64_libdir}/sigc++-3.0/
%{mingw64_libdir}/libsigc-3.0.dll.a
%{mingw64_libdir}/pkgconfig/sigc++-3.0.pc



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Sandro Mani <manisandro@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.0.7-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Sandro Mani <manisandro@gmail.com> - 3.0.7-1
- Initial package
