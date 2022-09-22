Name:           idevicerestore
Version:        1.0.0
Release:        %autorelease
Summary:        Restore/upgrade firmware of iOS devices

License:        LGPLv3
URL:            https://github.com/libimobiledevice/idevicerestore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  libcurl-devel
BuildRequires:  libimobiledevice-devel
BuildRequires:  libirecovery-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel

%description
idevicerestore is a command-line application to restore firmware files to iOS
devices. In general, upgrades and downgrades are possible, however subject to
availability of SHSH blobs from Apple for signing the firmware files.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
