%{?mingw_package_header}
%global datetag 20210406

Name:           mingw-portaudio
Version:        19
Release:        17.%{datetag}%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library

License:        LGPL-2.0-or-later
URL:            http://www.portaudio.com/
Source0:        http://files.portaudio.com/archives/pa_stable_v%{version}0700_%{datetag}.tgz

# from main portaudio package
Patch3:         portaudio-audacity.patch
# MinGW-specific patches
# Otherwise the library is unusable due to configure assumes MSVC instead of
# MinGW gcc
Patch100:       portaudio-mingw64.patch
Patch101:       portaudio-win-headers.patch

BuildArch:      noarch

BuildRequires:  autoconf automake libtool
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib


%description
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses a callback mechanism to request audio processing. Audio can be
generated in various formats, including 32 bit floating point, and will be
converted to the native format internally.

%package -n mingw32-portaudio
Summary:       %{summary}

%description -n mingw32-portaudio
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses a callback mechanism to request audio processing. Audio can be
generated in various formats, including 32 bit floating point, and will be
converted to the native format internally.

# Win64
%package -n mingw64-portaudio
Summary:       MinGW compiled portaudio for the Win64 target

%description -n mingw64-portaudio
MinGW compiled portaudio for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -n portaudio -p1
autoreconf -fiv


%build
%mingw_configure \
  --enable-shared --disable-static \
  --with-winapi=directx,wdmks,wmme,wasapi
%mingw_make_build


%install
%mingw_make_install

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-portaudio
%{mingw32_bindir}/libportaudio-2.dll
%{mingw32_includedir}/portaudio.h
%{mingw32_includedir}/pa_win_*.h
%{mingw32_libdir}/libportaudio.dll.a
%{mingw32_libdir}/pkgconfig/portaudio-2.0.pc

%files -n mingw64-portaudio
%{mingw64_bindir}/libportaudio-2.dll
%{mingw64_includedir}/portaudio.h
%{mingw64_includedir}/pa_win_*.h
%{mingw64_libdir}/libportaudio.dll.a
%{mingw64_libdir}/pkgconfig/portaudio-2.0.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19-17.20210406
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 Richard Shaw <hobbes1069@gmail.com> - 19-16.20210406
- Update to newer version to address FTBFS.
- Update license identifier to SPDX version.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-15.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-14.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-13.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-12.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-11.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-10.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 19-9.20161030
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-8.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-7.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-6.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-5.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Richard Shaw <hobbes1069@gmail.com> - 19-4.20161030
- Update per reviewer comments.

* Wed May 13 2020 Richard Shaw <hobbes1069@gmail.com> - 19-3.20161030
- Fix library install location again the right way.

* Wed May 13 2020 Richard Shaw <hobbes1069@gmail.com> - 19-2.20161030
- Give up on making portaudio use the right directories for mingw.

* Sun May 13 2018 Richard Shaw <hobbes1069@gmail.com> - 19-1
- Initial packaging.
