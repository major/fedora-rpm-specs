%{?mingw_package_header}

%global pkgname spirv-tools
%global srcname SPIRV-Tools

Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.304.0
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       %url/archive/vulkan-sdk-%{version}/%{srcname}-vulkan-sdk-%{version}.tar.gz

# Fix installation dir for cmake modules
Patch0:        spirv-tool_cmake-install.patch

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-spirv-headers
BuildRequires: mingw32-winpthreads
BuildRequires: mingw32-winpthreads-static

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-spirv-headers
BuildRequires: mingw64-winpthreads
BuildRequires: mingw64-winpthreads-static


%description
MinGW Windows %{pkgname}.


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
%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}


%build
MINGW32_CMAKE_ARGS="-DSPIRV-Headers_SOURCE_DIR=%{mingw32_prefix}" \
MINGW64_CMAKE_ARGS="-DSPIRV-Headers_SOURCE_DIR=%{mingw64_prefix}" \
%mingw_cmake -G Ninja -DSPIRV_TOOLS_BUILD_STATIC=OFF -DSPIRV_WERROR=OFF
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-%{pkgname}
%{mingw32_bindir}/libSPIRV-Tools-diff.dll
%{mingw32_bindir}/libSPIRV-Tools-link.dll
%{mingw32_bindir}/libSPIRV-Tools-lint.dll
%{mingw32_bindir}/libSPIRV-Tools-opt.dll
%{mingw32_bindir}/libSPIRV-Tools-reduce.dll
%{mingw32_bindir}/libSPIRV-Tools-shared.dll
%{mingw32_bindir}/libSPIRV-Tools.dll
%{mingw32_bindir}/spirv-as.exe
%{mingw32_bindir}/spirv-cfg.exe
%{mingw32_bindir}/spirv-dis.exe
%{mingw32_bindir}/spirv-lesspipe.sh
%{mingw32_bindir}/spirv-link.exe
%{mingw32_bindir}/spirv-lint.exe
%{mingw32_bindir}/spirv-objdump.exe
%{mingw32_bindir}/spirv-opt.exe
%{mingw32_bindir}/spirv-reduce.exe
%{mingw32_bindir}/spirv-val.exe
%{mingw32_includedir}/spirv-tools/
%{mingw32_libdir}/libSPIRV-Tools-diff.dll.a
%{mingw32_libdir}/libSPIRV-Tools-link.dll.a
%{mingw32_libdir}/libSPIRV-Tools-lint.dll.a
%{mingw32_libdir}/libSPIRV-Tools-opt.dll.a
%{mingw32_libdir}/libSPIRV-Tools-reduce.dll.a
%{mingw32_libdir}/libSPIRV-Tools-shared.dll.a
%{mingw32_libdir}/libSPIRV-Tools.dll.a
%{mingw32_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{mingw32_libdir}/pkgconfig/SPIRV-Tools.pc
%{mingw32_libdir}/cmake/*

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/libSPIRV-Tools-diff.dll
%{mingw64_bindir}/libSPIRV-Tools-link.dll
%{mingw64_bindir}/libSPIRV-Tools-lint.dll
%{mingw64_bindir}/libSPIRV-Tools-opt.dll
%{mingw64_bindir}/libSPIRV-Tools-reduce.dll
%{mingw64_bindir}/libSPIRV-Tools-shared.dll
%{mingw64_bindir}/libSPIRV-Tools.dll
%{mingw64_bindir}/spirv-as.exe
%{mingw64_bindir}/spirv-cfg.exe
%{mingw64_bindir}/spirv-dis.exe
%{mingw64_bindir}/spirv-lesspipe.sh
%{mingw64_bindir}/spirv-link.exe
%{mingw64_bindir}/spirv-lint.exe
%{mingw64_bindir}/spirv-objdump.exe
%{mingw64_bindir}/spirv-opt.exe
%{mingw64_bindir}/spirv-reduce.exe
%{mingw64_bindir}/spirv-val.exe
%{mingw64_includedir}/spirv-tools/
%{mingw64_libdir}/libSPIRV-Tools-diff.dll.a
%{mingw64_libdir}/libSPIRV-Tools-link.dll.a
%{mingw64_libdir}/libSPIRV-Tools-lint.dll.a
%{mingw64_libdir}/libSPIRV-Tools-opt.dll.a
%{mingw64_libdir}/libSPIRV-Tools-reduce.dll.a
%{mingw64_libdir}/libSPIRV-Tools-shared.dll.a
%{mingw64_libdir}/libSPIRV-Tools.dll.a
%{mingw64_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{mingw64_libdir}/pkgconfig/SPIRV-Tools.pc
%{mingw64_libdir}/cmake/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.304.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

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

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 2022.2-6
- Update for 1.3.231.1 sdk

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 2022.2-5
- Rebuild (python-3.11)

* Thu Sep 15 2022 Sandro Mani <manisandro@gmail.com> - 2022.2-4
- Rebase to vulkan SDK 1.3.224.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 2022.2-2
- Update to spirv headers for 1.3.216 sdk

* Wed Apr 27 2022 Sandro Mani <manisandro@gmail.com> - 2022.2-1.git7826e19
- Update to git 7826e19

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2022.1-2.git45dd184
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 2022.1-1.git45dd184
- Update to git 45dd184

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.4-2.git21e3f68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 2201.4-1.git21e3f68
- Update to git 21e3f68

* Tue Sep 07 2021 Sandro Mani <manisandro@gmail.com> - 2021.3-1.git1fbed83
- Update to git 1fbed83

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.2-2.git5dd2f76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 2021.2-1.git5dd2f76
- Update to git 5dd2f76

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2021.1-2.gitdc72924
- Rebuild (python-3.10)

* Wed May 19 2021 Sandro Mani <manisandro@gmail.com> - 2021.1-1.gitdc72924
- Update to git dc72924

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 2020.5-4.gitb27b1af
- Update to git b27b1af

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.5-3.gitf7da527
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Sandro Mani <manisandro@gmail.com> - 2020.5-2.gitf7da527
- Update to git f7da527

* Mon Aug 10 2020 Sandro Mani <manisandro@gmail.com> - 2020.5-1.git92a7165
- Update to git 92a7165

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.5-5.git67f4838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-4.git67f4838
- Rebuild (python-3.9)

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-3.git67f4838
- Update to git 67f4838

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-2.git97f1d48
- Update to git 97f1d48

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-1
- Update to 2019.5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.4-4.git3e4abc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 2019.4-3.git3e4abc9
- Update to git 3e4abc9

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 2019.4-2
- Rebuild (python 3.8)

* Sun Aug 11 2019 Sandro Mani <manisandro@gmail.com> - 2019.4-1
- Update to 2019.4

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 2019.3-4.git3726b50
- Drop unnecessary BR: python2

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 2019.3-3.git3726b50
- Update to git 3726b50

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Sandro Mani <manisandro@gmail.com> - 2019.3-1
- Update to 2019.3

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 2019.2-2
- Switch to python3

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 2019.2-1
- Update to 2019.2

* Mon Feb 11 2019 Sandro Mani <manisandro@gmail.com> - 2019.1-1
- Update to 2019.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Sandro Mani <manisandro@gmail.com> - 2018.4-1
- Update to 2018.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.0-0.2.git26a698c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 2018.3.0-0.1.git26a698c
- Initial package
