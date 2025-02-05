Name:           waifu2x-converter-cpp
Version:        5.3.4
Release:        16%{?dist}
Summary:        Image Super-Resolution for Anime-style art using OpenCL and OpenCV

# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/DeadSix27/waifu2x-converter-cpp
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

# Add soname versioning
Patch0:         waifu2x-converter-cpp-5.3-set_soversion.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  opencv-devel
Recommends:     beignet
Recommends:     mesa-libOpenCL

Provides:       bundled(picojson)
Provides:       bundled(tclap)

%description
Image Super-Resolution for Anime-style art using OpenCL and OpenCV.

This is a reimplementation of waifu2x (original) converter function,
in C++, using OpenCV.

%package        devel
Summary:        Development files for waifu2x-converter-cpp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for waifu2x-converter-cpp.

%prep
%autosetup -p1
# Fix ARM build
sed -i 's|-mfloat-abi=hard -mfloat-abi=softfp|-mfloat-abi=hard|' CMakeLists.txt

%build
%cmake3 -DINSTALL_MODELS=true ..
%cmake3_build

%install
%cmake3_install

%files
%license LICENSE include/picojson_LICENSE.txt include/tclap/tclap_LICEENSE.txt
%doc README.md
%{_bindir}/waifu2x-converter-cpp
%{_libdir}/libw2xc.so.1*
%{_datadir}/waifu2x-converter-cpp

%files devel
%{_includedir}/w2xconv.h
%{_libdir}/libw2xc.so

%changelog
* Tue Feb 04 2025 Sérgio Basto <sergio@serjux.com> - 5.3.4-16
- Rebuild for opencv-4.11.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 5.3.4-14
- convert license to SPDX

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 5.3.4-13
- Rebuild for opencv 4.10.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 5.3.4-11
- Rebuild for opencv 4.9.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 5.3.4-9
- Rebuild for opencv 4.8.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 5.3.4-6
- Rebuild for opencv 4.7.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 5.3.4-4
- Rebuilt for opencv 4.6.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 18:35:59 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 5.3.4-1
- Update to 5.3.4
- Close: rhbz#1920410

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 5.3.3-9
- Rebuilt for OpenCV

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 5.3.3-6
- Rebuilt for OpenCV 4.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 5.3.3-4
- Rebuild for OpenCV 4.2

* Mon Jan 27 2020 Nicolas Chauvet <kwizart@gmail.com>
- Fix build

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 5.3.3-2
- Rebuilt for opencv4

* Thu Dec 05 21:22:55 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.3.3-1
- Release 5.3.3 (#1782267)

* Thu Dec 05 21:22:55 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.3.2-1
- Release 5.3.2 (#1780136)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 21:56:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.3.1-1
- Release 5.3.1 (#1725442)

* Tue Mar 26 16:39:11 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.2.4-1
- Release 5.2.4 (#1692338)

* Sun Mar 17 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.2.3-1
- Release 5.2.3 (#1689455)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 5.2-1
- Initial release
