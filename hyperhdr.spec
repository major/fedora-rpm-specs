Name:           hyperhdr
Version:        19.0.0.0
Release:        2%{?dist}
Summary:        Ambient lighting

License:        MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/awawa-dev/HyperHDR
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
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
BuildArch:      noarch

%description    common
The %{name}-common package contains LUT files for
%{name}.

%prep
%autosetup -p1 -n HyperHDR-%{version}

mkdir dependencies/bonjour
ln -svf %{_includedir}/mdns.h ./dependencies/bonjour/mdns.h
sed -i  -e 's|file(DOWNLOAD "https://raw.githubusercontent.com/mjansson/mdns/${MJANSSON_MDNS_VERSION}/mdns.h"||' \
        -e 's|"${CMAKE_SOURCE_DIR}/dependencies/bonjour/mdns.h"||' \
        -e 's|STATUS MJANSSON_MDNS_STATUS_H)||' CMakeLists.txt

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
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

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
* Thu Mar 02 2023 Vasiliy Glazov <vascom2@gmail.com> - 19.0.0.0-2
- Drop i686 builds
- Add bundled provides

* Tue Feb 28 2023 Vasiliy Glazov <vascom2@gmail.com> - 19.0.0.0-1
- Initial packaging for Fedora
