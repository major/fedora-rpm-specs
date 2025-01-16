%{?mingw_package_header}

%global pkgname spirv-headers
%global srcname SPIRV-Headers

Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.304.0
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       MIT
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       %url/archive/vulkan-sdk-%{version}/%{srcname}-vulkan-sdk-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++


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



%prep
%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}


%build
%mingw_cmake -G Ninja
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-%{pkgname}
%{mingw32_includedir}/spirv/
%{mingw32_datadir}/cmake/SPIRV-Headers/
%{mingw32_datadir}/pkgconfig/SPIRV-Headers.pc


%files -n mingw64-%{pkgname}
%{mingw64_includedir}/spirv/
%{mingw64_datadir}/cmake/SPIRV-Headers/
%{mingw64_datadir}/pkgconfig/SPIRV-Headers.pc


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

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-8
- Update for 1.3.231.1 sdk

* Thu Sep 15 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-7
- Rebase to vulkan SDK 1.3.224.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-5
- Update to spirv headers for 1.3.216 sdk

* Wed Apr 27 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-4.git4995a2f
- Update to git 4995a2f

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-3.gitb42ba6d
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-2.gitb42ba6d
- Build and install through cmake

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 1.5.5-1.gitb42ba6d
- Update to git b42ba6d

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9.git814e728
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 1.5.4-8.git814e728
- Update to git 814e728

* Tue Sep 07 2021 Sandro Mani <manisandro@gmail.com> - 1.5.4-7.git449bc98
- Update to git 449bc98

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6.git07f259e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 1.5.4-5.git07f259e
- Update to git 07f259e

* Wed May 19 2021 Sandro Mani <manisandro@gmail.com> - 1.5.4-4.gitdafead1
- Update to git dafead1

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 1.5.4-3.gitf027d53
- Update to git f027d53

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Sandro Mani <manisandro@gmail.com> - 1.5.4-1
- Update to 1.5.4

* Mon Aug 10 2020 Sandro Mani <manisandro@gmail.com> - 1.5.3-1.git3fdabd0
- Update to git 3fdabd0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4.git2ad0492
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 1.5.1-3.git2ad0492
- Update to git 2ad0492

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2.gitaf64a9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.5.1-1-gitaf64a9e
- Update to 1.5.1 (git af64a9e)

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 1.4.1-3.gite4322e3
- Update to git e4322e3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Sandro Mani <manisandro@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 1.3.3.git03a0815
- Update to git 03a0815

* Mon Feb 11 2019 Sandro Mani <manisandro@gmail.com> - 1.3-3.git8bea0a2
- Update to git 8bea0a2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2.gitff684ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 1.3-1.gitff684ff
- git ff684ff is actually a version 1.3 snapshot

* Mon Jul 30 2018 Sandro Mani <manisandro@gmail.com> - 1.2-0.3.gitff684ff
- Update to git ff684ff

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.2.git12f8de9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 1.2-0.1.git12f8de9
- Initial package
