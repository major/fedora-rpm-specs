%global srcname Ultimarc-linux

Name:           ultimarc
Version:        1.2.0
Release:        %autorelease
Summary:        Library and command line utility to configure Ultimarc boards

License:        GPLv2
URL:            https://github.com/katie-snow/Ultimarc-linux
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  json-c-devel
BuildRequires:  libusbx-devel
# for libudev specifically
BuildRequires:  systemd-devel

%description
This utility will configure the following Ultimarc boards: ServoStik, PACDrive,
IPAC Ultimate, I-Pac 2, I-Pac 4, Mini-Pac, JPAC, UltraStik 360, PacLED64, U-HID
and U-HID Nano. There is support for the PAC 2015 boards, UltraStik 2015 board
and the previous generation of the PAC boards. It uses JSON configuration files
to configure the different boards. It also supports the ability to change the
device ID of the UltraStik 360 boards, allowing for the configuring of four
different boards at once.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
Libraries to configure Ultimarc boards.

%prep
%autosetup -n %{srcname}-%{version}
# collate JSON config examples
mkdir examples
cp -P src/umtool/*.json examples

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libultimarc.la
# Install udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
cp -P 21-ultimarc.rules %{buildroot}%{_udevrulesdir}

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README.cfg README.fw README.md
%doc examples
%{_bindir}/umtool
%{_udevrulesdir}/21-ultimarc.rules

%files libs
%license LICENSE
%{_libdir}/libultimarc.so.1*

%files devel
%{_includedir}/ultimarc
%{_libdir}/libultimarc.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
