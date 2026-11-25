Summary:        Utility to capture video from a DV camera
Name:           dvgrab
Version:        3.5.2
Release:        %{autorelease}
License:        GPL-2.0-or-later
URL:            https://github.com/ddennedy/dvgrab
Source:         https://github.com/ddennedy/dvgrab/archive/%{commit}/dvgrab-%{version}.tar.gz
BuildRequires:  libraw1394-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libdv-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libjpeg-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

ExcludeArch:    s390 s390x

%description
The dvgrab utility will capture digital video from a DV source on the firewire
(IEEE-1394) bus.

%prep
%autosetup -n dvgrab-%{version}
autoreconf -ivf

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README ChangeLog NEWS
%{_bindir}/dvgrab
%{_mandir}/man1/dvgrab.1*

%changelog
%autochangelog
