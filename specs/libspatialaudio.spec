%global commit0 d926a2ee469a3fefd50a9364fb9ac6fb484c3f70
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20200406

Name:           libspatialaudio
Version:        3.1
Release:        22.%{date0}git%{?shortcommit0}%{?dist}
Summary:        Ambisonic encoding / decoding and binauralization library

License:        LGPL-2.1-or-later
URL:            https://github.com/videolabs/libspatialaudio
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/videolabs/libspatialaudio/pull/41
# Needed to fix the VLC build
Patch1:         0001-Fix-MySofa-library-directory-detection.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libmysofa)


%description
libspatialaudio is an open-source and cross-platform C++ library for
Ambisonic encoding and decoding, filtering and binaural rendering. It is
targetted to render High-Order Ambisonic (HOA) and VR/3D audio samples
in multiple environments, from headphones to classic loudspeakers. Its
binaural rendering can be used for classical 5.1/7.1 spatial channels
as well as Ambisonics inputs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# sofa_hrtf.h includes mysofa.h
Requires:       pkgconfig(libmysofa)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
%cmake \
  -DBUILD_STATIC_LIBS=OFF

%cmake_build


%install
%cmake_install



%files
%license LICENSE
%doc README.md
%{_libdir}/libspatialaudio.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libspatialaudio.so
%{_libdir}/pkgconfig/spatialaudio.pc


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-22.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-21.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Nicolas Chauvet <kwizart@gmail.com> - 3.1-20.20200406gitd926a2e
- Revert to 20200406 snapshot

* Tue Oct 22 2024 Nicolas Chauvet <kwizart@gmail.com> - 3.1-19.20240506git0b6b25e
- Bump

* Mon Oct 07 2024 Nicolas Chauvet <kwizart@gmail.com> - 3.1-18.20240506git0b6b25e
- Update snapshot

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1-17.20200406gitd926a2e
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-16.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 06 2024 Robert-André Mauchin <zebob.m@gmail.com> - 3.1-15.20200406gitd926a2e
- Add patch to fix MySofa library directory detection

* Tue Apr 09 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.1-14.20200406gitd926a2e
- Add libmysofa devel dependency

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Nicolas Chauvet <kwizart@gmail.com> - 3.1-10.20200406gitd926a2e
- Revert previous update to avoid API breakage with vlc-3.x

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3.20200406gitd926a2e
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2.20200406gitd926a2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1-1.20200406gitd926a2e
- Initial spec file
