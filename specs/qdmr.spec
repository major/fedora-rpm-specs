# Fedora qdmr spec, heavily inspired by qdmr upstream spec,
# original spec credit/license:
#
# Copyright (c) 2021-2023, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:		qdmr
Version:	0.12.1
Release:	4%{?dist}
Summary:	A GUI application for configuring and programming DMR radios
License:	GPL-3.0-or-later
URL:		https://dm3mat.darc.de/qdmr/
Source0:	https://github.com/hmatuschek/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Workaround for https://gitlab.com/graphviz/graphviz/-/issues/2681
Source1:	dot_autodetect.png
Requires:	hicolor-icon-theme
# for udev rule directory
Requires:	systemd-udev
BuildRequires:	systemd-rpm-macros
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	libusbx-devel
BuildRequires:	doxygen
BuildRequires:	libxslt
BuildRequires:	docbook5-style-xsl
BuildRequires:	yaml-cpp-devel
BuildRequires:	gettext
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Positioning)
BuildRequires:	pkgconfig(Qt5SerialPort)
BuildRequires:	pkgconfig(Qt5Test)
# https://bugzilla.redhat.com/show_bug.cgi?id=2364151
BuildRequires:	pkgconfig(Qt5UiTools)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	desktop-file-utils
# for appdata metainfo validation with appstream-util
BuildRequires:	libappstream-glib
Patch:		qdmr-0.12.1-fix-docbook-xsl-path.patch
# https://github.com/hmatuschek/qdmr/pull/587
Patch:		qdmr-0.12.1-metainfo-fix.patch
# https://github.com/hmatuschek/qdmr/pull/594
Patch:		qdmr-0.12.1-icons-path-fix.patch

%description
A Qt5 application to program DMR radios. DMR is a digital modulation
standard used in amateur and commercial radio. To this end, qdmr is an
alternative codeplug programming software (CPS) that supports several radios
across several manufacturers.

%package -n libdmrconf
Summary:	Library for configuring DMR radios

%description -n libdmrconf
This library is built from the qdmr SRPM.

%package -n libdmrconf-doc
Summary:	Documentation for libdmrconf
Requires:	libdmrconf{?_isa} = %{version}-%{release}
BuildArch:	noarch

%description -n libdmrconf-doc
Documentation for libdmrconf.

%package devel
Summary:	Development files for dmrconf
Requires:	libdmrconf%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications using libdmrconf.

%prep
%autosetup -p1

%build
%cmake \
  -DBUILD_MAN=ON \
  -DBUILD_DOCS=ON \
  -DBUILD_TESTS=ON \
  -DINSTALL_APPSTREAM_DATA=ON \
  -DINSTALL_UDEV_RULES=ON \
  -DINSTALL_UDEV_PATH=%{_udevrulesdir}
%cmake_build

%install
%cmake_install

# move libdmrconf documentation
mv %{buildroot}%{_docdir}/qdmr/libdmrconf %{buildroot}%{_docdir}

# fix png that generates a bit differently on various architectures
# workaround for https://gitlab.com/graphviz/graphviz/-/issues/2681
mv %{SOURCE1} %{buildroot}%{_docdir}/libdmrconf/html/dot_autodetect.png

%find_lang %{name} --with-qt

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%ctest

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/dmrconf
%{_bindir}/qdmr
%{_udevrulesdir}/99-qdmr.rules
%{_datadir}/applications/qdmr.desktop
%{_metainfodir}/de.darc.dm3mat.qdmr.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/qdmr.png
%{_mandir}/man1/dmrconf.1*
%{_mandir}/man1/qdmr.1*

%files -n libdmrconf
%license LICENSE
%exclude %{_docdir}/libdmrconf/html
# workaround to own empty doc directory
%dir %{_docdir}/libdmrconf
%{_libdir}/libdmrconf.so.0*

%files -n libdmrconf-doc
%doc %{_docdir}/libdmrconf/html

%files devel
%{_includedir}/libdmrconf
%{_libdir}/libdmrconf.so

%changelog
* Tue May 20 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 0.12.1-4
- Fixed icons path

* Tue May 13 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 0.12.1-3
- Added appdata metainfo validation according to the review

* Tue May  6 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 0.12.1-2
- Updated according to the review

* Mon May  5 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 0.12.1-1
- Initial version
