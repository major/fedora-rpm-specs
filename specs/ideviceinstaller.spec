%global forgeurl https://github.com/libimobiledevice/ideviceinstaller

Name:           ideviceinstaller
Version:        1.2.0
Release:        %autorelease
Summary:        Manage apps of iOS devices

License:        GPL-2.0-or-later
URL:            https://www.libimobiledevice.org/
Source:         %{forgeurl}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  libzip-devel

%description
The ideviceinstaller application allows interacting with the app installation
service of an iOS device.

%prep
%autosetup -p1 -n %{name}-%{version}

%if %{defined commit}
echo %{version} > .tarball-version
%endif

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/ideviceinstaller
%{_mandir}/man1/ideviceinstaller.1*

%changelog
%autochangelog
