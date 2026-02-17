Name:          feather
Version:       2.8.1
Release:       %autorelease
Summary:       Monero desktop wallet

License:       BSD-3-Clause
URL:           https://featherwallet.org/
Source0:       https://featherwallet.org/files/releases/source/%{name}-%{version}.tar.gz
Source1:       https://featherwallet.org/files/releases/source/%{name}-%{version}.tar.gz.asc
# gpg2 --export --export-options export-minimal 8185E158A33330C7FD61BC0D1F76E155CEFBA71C >gpgkey-featherwallet.gpg
Source2:       gpgkey-featherwallet.gpg
Source3:       feather.metainfo.xml

Patch0:        cmath.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gnupg2
BuildRequires: zeromq-devel
BuildRequires: qrencode-devel
BuildRequires: zbar-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qtwebsockets-devel
BuildRequires: qt6-qtmultimedia-devel
BuildRequires: qt6-qtwayland-devel
BuildRequires: libgcrypt-devel
BuildRequires: openssl-devel
BuildRequires: libzip-devel
BuildRequires: boost-devel
BuildRequires: boost-filesystem
BuildRequires: boost-thread
BuildRequires: boost-regex
BuildRequires: boost-chrono
BuildRequires: libsodium-devel
BuildRequires: protobuf-lite-devel
BuildRequires: libusb1-devel
BuildRequires: unbound-devel
BuildRequires: wayland-devel
BuildRequires: zxing-cpp-devel
Requires:      tor

# virtual memory exhausted: Cannot allocate memory
ExcludeArch:   %{arm} %{ix86}

%description
Feather is a wallet for the Monero cryptocurrency.

%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p0

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DARCH=default -DMANUAL_SUBMODULES=ON -DBUILD_SHARED_LIBS=OFF -DTOR_BIN=OFF -DDONATE_BEG=OFF -DWITH_SCANNER=ON -DUSE_DEVICE_TREZOR=ON
%cmake_build

%install
%cmake_install
install -Dpm644 %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE
%{_bindir}/feather
%{_datadir}/applications/feather.desktop
%{_datadir}/icons/hicolor/*/apps/feather.png
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
