Name:           hyperhdr
Version:        20.0.0.0
Release:        0.13%{?dist}
Summary:        Ambient lighting

License:        MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/awawa-dev/HyperHDR
Source0:        %{url}/archive/refs/tags/v%{version}beta1/hyperhdr-%{version}beta1.tar.gz
Patch0:         fix.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  mbedtls-devel
BuildRequires:  cmake(flatbuffers)
BuildRequires:  flatbuffers-compiler
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(mdns)

Requires:       hicolor-icon-theme
Requires:       %{name}-common

%description
Open source ambient lighting implementation for television sets based on the
video and audio streams analysis, using performance improvements especially
for USB grabbers.

%package        common
Summary:        LUT files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    common
The %{name}-common package contains LUT files for
%{name}.

%prep
%autosetup -p1 -n HyperHDR-%{version}beta1

#mkdir dependencies/bonjour
#ln -svf %{_includedir}/mdns.h ./dependencies/bonjour/mdns.h
#sed -i  -e 's|file(DOWNLOAD "https://raw.githubusercontent.com/mjansson/mdns/${MJANSSON_MDNS_VERSION}/mdns.h"||' \
#        -e 's|"${CMAKE_SOURCE_DIR}/dependencies/bonjour/mdns.h"||' \
#        -e 's|STATUS MJANSSON_MDNS_STATUS_H)||' CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_CXX_STANDARD=17 \
    -DUSE_SYSTEM_FLATBUFFERS_LIBS:BOOL=ON \
    -DUSE_SYSTEM_MBEDTLS_LIBS:BOOL=ON \
    -DENABLE_MQTT:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DPLATFORM=linux

%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/lut/
tar -xf resources/lut/lut_lin_tables.tar.xz -C %{buildroot}%{_datadir}/%{name}/lut/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_libdir}/libsmart*.so*
%{_userunitdir}/%{name}.service
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%files common
%{_datadir}/%{name}

%changelog
* Sat Feb 08 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 20.0.0.0-0.13
- Rebuilt for flatbuffers 25.1.24

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0.0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 04 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 20.0.0.0-0.11
- Rebuilt for flatbuffers 24.12.24

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 20.0.0.0-0.10
- Rebuilt for mbedTLS 3.6.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0.0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 05 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 20.0.0.0-0.8
- Rebuilt for flatbuffers 24.3.25

* Tue Mar 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 20.0.0.0-0.7
- Rebuilt for flatbuffers 24.3.7

* Wed Feb 28 2024 Vasiliy Glazov <vascom2@gmail.com> - 20.0.0.0-0.6
- Revert to 20.0.0.0.beta1

* Wed Feb 28 2024 Vasiliy Glazov <vascom2@gmail.com> - 20.0.0.0-0.5
- Update to 20.0.0.0.beta2

* Tue Feb 06 2024 František Zatloukal <fzatlouk@redhat.com> - 20.0.0.0-0.4
- Rebuilt for turbojpeg 3.0.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 28 2023 Vasiliy Glazov <vascom2@gmail.com> - 20.0.0.0-0.1
- Update to 20.0.0.0.beta1

* Tue Oct 24 2023 Vasiliy Glazov <vascom2@gmail.com> - 19.0.0.0-6
- Rebuild for new Qt6

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Vasiliy Glazov <vascom2@gmail.com> - 19.0.0.0-4
- Rebuild for Qt6 private api name change

* Wed Jul 05 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 19.0.0.0-3
- Rebuild for flatbuffers-23.5.26

* Thu Mar 02 2023 Vasiliy Glazov <vascom2@gmail.com> - 19.0.0.0-2
- Drop i686 builds
- Add bundled provides

* Tue Feb 28 2023 Vasiliy Glazov <vascom2@gmail.com> - 19.0.0.0-1
- Initial packaging for Fedora
