%{?mingw_package_header}

%global pkgname vulkan-tools
%global srcname Vulkan-Tools

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')

Name:          mingw-%{pkgname}
Version:       1.4.304.0
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname}

# volk.h is MIT
License:       Apache-2.0 AND MIT
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz
Source1:       https://github.com/zeux/volk/archive/vulkan-sdk-%{version}.tar.gz#/volk-vulkan-sdk-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-vulkan-headers >= %{baseversion}
BuildRequires: mingw32-vulkan-loader >= %{baseversion}

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-vulkan-headers >= %{baseversion}
BuildRequires: mingw64-vulkan-loader >= %{baseversion}


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version} -a1
cp -a volk-vulkan-sdk-%{version}/LICENSE.md LICENSE_volk.md


%build
# Build volk
pushd volk-vulkan-sdk-%{version}
%mingw_cmake -G Ninja -DVOLK_INSTALL:BOOL=ON
%mingw_ninja -v
DESTDIR=$PWD/dist ninja -C build_win32 install
DESTDIR=$PWD/dist ninja -C build_win64 install
popd

MINGW32_CMAKE_ARGS="-Dvolk_DIR=$PWD/volk-vulkan-sdk-%{version}/dist/%{mingw32_libdir}/cmake/volk" \
MINGW64_CMAKE_ARGS="-Dvolk_DIR=$PWD/volk-vulkan-sdk-%{version}/dist/%{mingw64_libdir}/cmake/volk" \
%mingw_cmake -G Ninja
%mingw_ninja -v


%install
%mingw_ninja_install


%files -n mingw32-%{pkgname}
%license LICENSE.txt LICENSE_volk.md
%{mingw32_bindir}/vkcube.exe
%{mingw32_bindir}/vkcubepp.exe
%{mingw32_bindir}/vulkaninfo.exe

%files -n mingw64-%{pkgname}
%license LICENSE.txt LICENSE_volk.md
%{mingw64_bindir}/vkcube.exe
%{mingw64_bindir}/vkcubepp.exe
%{mingw64_bindir}/vulkaninfo.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.304.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Sandro Mani <manisandro@gmail.com> - 1.4.304.0-1
- Update to 1.4.304.0

* Mon Oct 14 2024 Sandro Mani <manisandro@gmail.com> - 1.3.296.0-1
- Update to 1.3.296.0

* Sat Aug 03 2024 Sandro Mani <manisandro@gmail.com> - 1.3.290.0-1
- Update to 1.3.290.0

* Mon Jul 29 2024 Sandro Mani <manisandro@gmail.com> - 1.3.283.0-1
- Update to 1.3.283.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.280.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 08 2024 Sandro Mani <manisandro@gmail.com> - 1.3.280.0-1
- Update to 1.3.280.0

* Sun Feb 25 2024 Sandro Mani <manisandro@gmail.com> - 1.3.275-1
- Update to 1.3.275

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.268.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.268.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.268.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Sandro Mani <manisandro@gmail.com> - 1.3.268.0-1
- Update to 1.3.268.0

* Tue Sep 12 2023 Sandro Mani <manisandro@gmail.com> - 1.3.261.1-1
- Update to 1.3.261.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.250.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Sandro Mani <manisandro@gmail.com> - 1.3.250.1-1
- Update to 1.3.250.1

* Tue Jun 20 2023 Sandro Mani <manisandro@gmail.com> - 1.3.250.0-1
- Update to 1.3.250.0

* Mon Apr 17 2023 Sandro Mani <manisandro@gmail.com> - 1.3.243.0-1
- Update to 1.3.243.0

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 1.3.239.0-1
- Update to 1.3.239.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.231.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 1.3.231.1-1
- Update to 1.3.231.1

* Fri Sep 16 2022 Sandro Mani <manisandro@gmail.com> - 1.3.224.1-1
- Update to 1.3.224.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.216-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Sandro Mani <manisandro@gmail.com> - 1.3.216-1
- Update to 1.3.216

* Wed Apr 27 2022 Sandro Mani <manisandro@gmail.com> - 1.3.211.0-1
- Update to 1.3.211.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.3.204.0-2
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 1.3.204.0-1
- Update to 1.3.204.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.198.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 1.2.198.0-1
- Update to 1.2.198.0

* Tue Sep 07 2021 Sandro Mani <manisandro@gmail.com> - 1.2.189.0-1
- Update to 1.2.189.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.182.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 1.2.182.0-1
- Update to 1.2.182.0

* Wed May 19 2021 Sandro Mani <manisandro@gmail.com> - 1.2.176.0-1
- Update to 1.2.176.0

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 1.2.162.1-1
- Update to 1.2.162.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.154.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 1.2.154.0-1
- Update to 1.2.154.0

* Mon Aug 10 2020 Sandro Mani <manisandro@gmail.com> - 1.2.148.0-1
- Update to 1.2.148.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.135.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 1.2.135.0-1
- Update to 1.2.135.0

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 1.2.131.1-1
- Update to 1.2.131.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.126.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.1.126.0-1
- Update to 1.1.126.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.1.114.0-2
- Rebuild (Changes/Mingw32GccDwarf2)
- Fix build with python 3.8

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 1.1.114.0-1
- Update to 1.1.114.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 1.1.108.0-1
- Update to 1.1.108.0

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 1.1.106.0-1
- Update to 1.1.106.0

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 1.1.101.0-1
- Update to 1.1.101.0

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 1.1.97.0-1
- Update to 1.1.97.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.82.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Sandro Mani <manisandro@gmail.com> - 1.1.77-1
- Update to 1.1.77
