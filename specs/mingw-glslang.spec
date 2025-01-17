%{?mingw_package_header}

%global pkgname glslang

Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.304.0
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD-3-clause AND GPL-3.0-or-later AND Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{pkgname}
Source0:       %url/archive/vulkan-sdk-%{version}/%{pkgname}-vulkan-sdk-%{version}.tar.gz
# Remove debug suffix for mingw builds
Patch0:        glslang_debug-suffix.patch

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-winpthreads-static

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-winpthreads-static


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
%autosetup -p1 -n %{pkgname}-vulkan-sdk-%{version}


%build
%mingw_cmake -G Ninja -DBUILD_SHARED_LIBS=OFF -DENABLE_OPT=OFF
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-%{pkgname}
%{mingw32_bindir}/glslang.exe
%{mingw32_bindir}/glslangValidator.exe
%{mingw32_bindir}/spirv-remap.exe
%{mingw32_includedir}/glslang/
%{mingw32_libdir}/libGenericCodeGen.a
%{mingw32_libdir}/libMachineIndependent.a
%{mingw32_libdir}/libOSDependent.a
%{mingw32_libdir}/libSPIRV.a
%{mingw32_libdir}/libSPVRemapper.a
%{mingw32_libdir}/libglslang.a
%{mingw32_libdir}/libglslang-default-resource-limits.a
%{mingw32_libdir}/cmake/*

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/glslang.exe
%{mingw64_bindir}/glslangValidator.exe
%{mingw64_bindir}/spirv-remap.exe
%{mingw64_includedir}/glslang/
%{mingw64_libdir}/libGenericCodeGen.a
%{mingw64_libdir}/libMachineIndependent.a
%{mingw64_libdir}/libOSDependent.a
%{mingw64_libdir}/libSPIRV.a
%{mingw64_libdir}/libSPVRemapper.a
%{mingw64_libdir}/libglslang.a
%{mingw64_libdir}/libglslang-default-resource-limits.a
%{mingw64_libdir}/cmake/*


%changelog
* Tue Jan 14 2025 Sandro Mani <manisandro@gmail.com> - 1:1.4.304.0-1
- Update to 1.4.304.0

* Mon Oct 14 2024 Sandro Mani <manisandro@gmail.com> - 1:1.3.296.0-1
- Update to 1.3.296.0

* Sat Aug 03 2024 Sandro Mani <manisandro@gmail.com> - 1:1.3.290.0-1
- Update to 1.3.290.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.283.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 28 2024 Sandro Mani <manisandro@gmail.com> - 1:1.3.283.0-1
- Update to 1.3.283.0

* Mon Apr 08 2024 Sandro Mani <manisandro@gmail.com> - 1:1.3.280.0-1
- Update to 1.3.280.0

* Sat Feb 24 2024 Sandro Mani <manisandro@gmail.com> - 1:1.3.275.0-1
- Update to 1.3.275.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.268.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.268.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Sandro Mani <manisandro@gmail.com> - 1:1.3.268.0-1
- Update to 1.3.268.0

* Tue Sep 12 2023 Sandro Mani <manisandro@gmail.com> - 1:1.3.261.1-1
- Update to 1.3.261.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.250.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Sandro Mani <manisandro@gmail.com> - 1:1.3.250.1-1
- Update to 1.3.250.1

* Tue Jun 20 2023 Sandro Mani <manisandro@gmail.com> - 1:1.3.250.0-1
- Update to 1.3.250.0

* Mon Apr 17 2023 Sandro Mani <manisandro@gmail.com> - 1:1.3.243.0-1
- Update to 1.3.243.0

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 1:1.3.239.0-1
- Update to sdk 1.3.239.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 11.9.0-7
- Update for 1.3.231.1 sdk

* Thu Sep 15 2022 Sandro Mani <manisandro@gmail.com> - 11.9.0-6
- Rebase to vulkan SDK 1.3.224.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 11.9.0-4
- Update to glslang for 1.3.216 sdk

* Wed Apr 27 2022 Sandro Mani <manisandro@gmail.com> - 11.9.0-3.git9bb8cff
- Update to git 9bb8cff

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 11.9.0-2.git2742e95
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 11.9.0-1.git2742e95
- Update to git 2742e95

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.7.0-2.gitc9706bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 11.7.0-1.gitc9706bd
- Update to git c9706bd

* Tue Sep 07 2021 Sandro Mani <manisandro@gmail.com> - 11.6.0-1.git2fb89a0
- Update to git 2fb89a0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-2.gitae2a562
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 11.5.0-1.gitae2a562
- Update to git ae2a562

* Wed May 19 2021 Sandro Mani <manisandro@gmail.com> - 11.4.0-1.git18eef33
- Update to git 18eef33

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 11.0.0-3.gitc594de2
- Update to git c594de2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2.git5743eed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Sandro Mani <manisandro@gmail.com> - 11.0.0-1
- Update to 11.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.13.3559-2.gitc9b28b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 8.13.3559-2.gitc9b28b9
- Update to git c9b28b9

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 8.13.3559-1
- Update to 8.13.3559

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.13.3496-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 7.13.3496-1
- Update to 7.13.3496

* Thu Aug 22 2019 Sandro Mani <manisandro@gmail.com> - 7.12.3352-1
- Update to 7.12.3352

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 7.11.3214.3.giteea3400
- Update to git eea3400

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.11.3214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 7.11.3214-1
- Update to 7.11.3214

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 3.1-0.6.gite0d59bb
- Update to git e0d59bb

* Mon Feb 25 2019 Sandro Mani <manisandro@gmail.com> - 3.1-0.5.git05d12a9
- Update to git 05d12a9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.4.gite0bc65b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 3.1.0-0.3.gite0bc65b
- Update to git e0bc65b

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.2.git3bb4c48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 3.1-0.1.git3bb4c48
- Initial package
