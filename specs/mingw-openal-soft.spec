%{?mingw_package_header}

%global pkgname openal-soft

# Disable qtgui by default for now
%bcond_with qtgui

Name:           mingw-%{pkgname}
Version:        1.24.2
Release:        1%{?dist}
Summary:        Open Audio Library

# See native spec
License:        LGPL-2.0-or-later AND BSD-3-Clause AND GPL-2.0-or-later AND Apache-2.0 AND (LGPL-2.0-or-later AND BSD-3-Clause) AND MIT AND NCL AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://openal-soft.org/
Source0:        https://openal-soft.org/openal-releases/openal-soft-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  cmake

# Win32 BRs
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-SDL2_mixer
%if %{with qtgui}
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qmake
%endif

# Win64 BRs
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-SDL2_mixer
%if %{with qtgui}
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qmake
%endif

%description
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

# Win32
%package -n mingw32-%{pkgname}
Summary:        MinGW compiled OpenAL Soft library for Win32 target
Provides:       mingw32-openal = %{version}-%{release}

%description -n mingw32-%{pkgname}
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

This package provides the library for the Win32 target.

# Win64
%package -n mingw64-%{pkgname}
Summary:        MinGW compiled OpenAL Soft library for Win64 target
Provides:       mingw64-openal = %{version}-%{release}

%description -n mingw64-%{pkgname}
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

This package provides the library for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -n %{pkgname}-%{version} -p1


%build
%mingw_cmake . -DALSOFT_CPUEXT_NEON:BOOL=OFF -DALSOFT_UTILS=OFF -DALSOFT_EXAMPLES=OFF
%mingw_make_build


%install
%mingw_make_install

install -Dpm644 alsoftrc.sample %{buildroot}%{mingw32_sysconfdir}/openal/alsoft.conf
install -Dpm644 alsoftrc.sample %{buildroot}%{mingw64_sysconfdir}/openal/alsoft.conf


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/OpenAL32.dll
%if %{with qtgui}
%{mingw32_bindir}/alsoft-config.exe
%endif
%{mingw32_sysconfdir}/openal
%{mingw32_includedir}/AL
%{mingw32_libdir}/libOpenAL32.dll.a
%{mingw32_libdir}/cmake/OpenAL/
%{mingw32_libdir}/pkgconfig/openal.pc
%{mingw32_datadir}/openal

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/OpenAL32.dll
%if %{with qtgui}
%{mingw64_bindir}/alsoft-config.exe
%endif
%{mingw64_sysconfdir}/openal
%{mingw64_includedir}/AL
%{mingw64_libdir}/libOpenAL32.dll.a
%{mingw64_libdir}/cmake/OpenAL/
%{mingw64_libdir}/pkgconfig/openal.pc
%{mingw64_datadir}/openal

%changelog
* Sun Feb 02 2025 Sandro Mani <manisandro@gmail.com> - 1.24.2-1
- Update to 1.24.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.23.1-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Sandro Mani <manisandro@gmail.com> - 1.23.1-1
- Update to 1.23.1

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 1.23.0-1
- Update to 1.23.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 1.22.2-1
- Update to 1.22.2

* Tue Apr 26 2022 Sandro Mani <manisandro@gmail.com> - 1.22.0-1
- Update to 1.22.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.21.1-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 12 2021 Sandro Mani <manisandro@gmail.com> - 1.21.1-1
- Update to 1.19.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.18.2-5
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 1.18.2-1
- Update to 1.18.2
- Fix CMakeLists to build correctly (#1582930)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 26 2017 Neal Gompa <ngompa13@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Neal Gompa <ngompa13@gmail.com> - 1.17.2-1
- Initial import (#1396748)
- Initial packaging based on native Fedora version
