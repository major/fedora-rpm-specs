Name:		libzbd
Version:	2.0.4
Release:	7%{?dist}
Summary:	A library to control zoned block devices

# Automatically converted from old format: LGPLv3+ and GPLv3+ - review is highly recommended.
License:	LGPL-3.0-or-later AND GPL-3.0-or-later
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	gtk3-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc

%description
libzbd is a library providing functions simplifying the management and
use of zoned block devices using the kernel ioctl interface.

# Development headers package
%package devel
Summary: Development header files for libzbd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development header files for libzbd.

# Command line tools package
%package cli-tools
Summary: Command line tools using libzbd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cli-tools
This package provides command line tools using libzbd.

# Graphic tools package
%package gtk-tools
Summary: GTK tools using libzbd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gtk-tools
This package provides GTK-based graphical tools using libzbd.

%prep
%autosetup

%build
sh autogen.sh
%configure --libdir="%{_libdir}" --includedir="%{_includedir}"
%make_build

%install
%make_install PREFIX=%{_prefix}
chmod -x ${RPM_BUILD_ROOT}%{_mandir}/man8/*.8*

find ${RPM_BUILD_ROOT} -name '*.la' -delete

desktop-file-validate %{buildroot}/%{_datadir}/applications/gzbd.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/gzbd-viewer.desktop

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%exclude %{_libdir}/*.a
%exclude %{_libdir}/pkgconfig/*.pc
%license LICENSES/LGPL-3.0-or-later.txt
%doc README.md

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%license LICENSES/LGPL-3.0-or-later.txt

%files cli-tools
%{_bindir}/zbd
%{_mandir}/man8/zbd.8*
%license LICENSES/GPL-3.0-or-later.txt

%files gtk-tools
%{_bindir}/gzbd
%{_datadir}/polkit-1/actions/org.gnome.gzbd.policy
%{_datadir}/applications/gzbd.desktop
%{_datadir}/pixmaps/gzbd.png
%{_bindir}/gzbd-viewer
%{_datadir}/polkit-1/actions/org.gnome.gzbd-viewer.policy
%{_datadir}/applications/gzbd-viewer.desktop
%{_datadir}/pixmaps/gzbd-viewer.png
%{_mandir}/man8/gzbd.8*
%{_mandir}/man8/gzbd-viewer.8*
%license LICENSES/GPL-3.0-or-later.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 7 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.4-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Damien Le Moal <damien.lemoal@wdc.com> 2.0.4
- Update to version 2.0.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Damien Le Moal <damien.lemoal@wdc.com> 2.0.2-1
- Update to version 2.0.2
