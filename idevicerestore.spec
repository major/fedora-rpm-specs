%global commit 609f7f058487596597e8e742088119fdd46729df
%global date 20230523
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           idevicerestore
Version:        1.0.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Restore/upgrade firmware of iOS devices

License:        LGPL-3.0-only
URL:            https://github.com/libimobiledevice/idevicerestore
%if %{defined commit}
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif
# Add support for mac mini m2 pro
Patch:          %{url}/pull/586.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  libcurl-devel
BuildRequires:  libimobiledevice-devel
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libirecovery-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel

%description
idevicerestore is a command-line application to restore firmware files to iOS
devices. In general, upgrades and downgrades are possible, however subject to
availability of SHSH blobs from Apple for signing the firmware files.

%prep
%if %{defined commit}
%autosetup -p1 -n %{name}-%{commit}
echo %{version} > .tarball-version
%else
%autosetup -p1
%endif

%build
NOCONFIGURE=1 ./autogen.sh
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
