Name:           libfprint

Version:        1.94.10
Release:        %autorelease
Summary:        Toolkit for fingerprint scanner

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
# Most of the code is LGPL-2.1-or-later
# libfprint/nbis is NIST-PD
License:        LGPL-2.1-or-later AND NIST-PD
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.gz

# Backport from upstream
Patch00001:     https://gitlab.freedesktop.org/libfprint/libfprint/-/commit/2c7842c905147a2d127c1b168b2e9d43.patch

# the updates for the fpi
Patch10001:     0001-doc-Include-Binary-buffer-I-O-section-for-the-byte-r.patch
Patch10002:     0002-fpi-byte-writer-Add-APIs-to-write-and-get-GBytes.patch
Patch10003:     0003-fpi-byte-reader-Add-support-to-read-and-get-peek-GBy.patch
Patch10004:     0004-fpi-byte-reader-Add-support-to-read-to-a-static-buff.patch
Patch10005:     0005-fpi-usb-transfer-Add-missing-definition-of-set_short.patch
Patch10006:     0006-fpi-usb-transfer-Wrap-g_error_new-arguments.patch
# Add EGIS readers
# https://gitlab.freedesktop.org/libfprint/libfprint/-/merge_requests/561
Patch10007:     egis_reader.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2

%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -S git -n libfprint-v%{version}

%build
# Include the virtual image driver for integration tests
%meson -Ddrivers=all
%meson_build

%install
%meson_install

%ldconfig_scriptlets

# TODO: The test can't run with the recent pygobject3.52.
# So, skip the test until the issue of pygobject is fixed.

%files
%license COPYING
%doc NEWS THANKS AUTHORS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules
%{_datadir}/metainfo/org.freedesktop.libfprint.metainfo.xml

%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-2.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/

%files tests
%{_libexecdir}/installed-tests/libfprint-2/
%{_datadir}/installed-tests/libfprint-2/

%changelog
%autochangelog
