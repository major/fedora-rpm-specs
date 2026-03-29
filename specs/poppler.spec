%global test_sha 03a4b9eb854a06a83c465e82de601796c458bbe9
%global test_date 2021-01-11

%bcond qt 1

%if %{with qt}
# Enable qt5 support (or not)
# RHEL 10 drops support for Qt5, adds Qt6
%if %{undefined rhel} || 0%{?rhel} < 10
%global qt5 1
%endif
%if %{undefined rhel} || 0%{?rhel} >= 10
%global qt6 1
%endif
%endif

Summary: PDF rendering library
Name:    poppler
Version: 26.01.0
Release: %autorelease
License: (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:     https://poppler.freedesktop.org/
Source0: https://poppler.freedesktop.org/poppler-%{version}.tar.xz
Source1: https://poppler.freedesktop.org/poppler-%{version}.tar.xz.sig
# https://pgp.surfnet.nl/pks/lookup?op=get&search=0xCA262C6C83DE4D2FB28A332A3A6A4DB839EAA6D7
Source2: armored-keys.asc
# git archive --prefix test/
Source3: %{name}-test-%{test_date}-%{test_sha}.tar.xz

Patch1:  poppler-0.90.0-position-independent-code.patch

Patch2:  poppler-21.01.0-glib-introspection.patch

Patch3:  poppler-26.01.0-climits.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-ft)
BuildRequires: pkgconfig(cairo-pdf)
BuildRequires: pkgconfig(cairo-ps)
BuildRequires: pkgconfig(cairo-svg)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(poppler-data)
BuildRequires: pkgconfig(libcurl)
BuildRequires: cmake(Gpgmepp)
%if 0%{?qt5}
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
%endif
%if 0%{?qt6}
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
%endif
BuildRequires: boost-devel
# for %%gpgverify
BuildRequires: gnupg2

Requires: poppler-data

# Recommend Zapf Dingbats and Symbol fonts
Recommends: font(d050000l)
Recommends: font(standardsymbolsps)

Obsoletes: poppler-glib-demos < 0.60.1-1

%description
%{name} is a PDF rendering library.

%package devel
Summary: Libraries and headers for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
You should install the poppler-devel package if you would like to
compile applications based on poppler.

%package glib
Summary: Glib wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gobject-introspection

%description glib
%{summary}.

%package glib-devel
Summary: Development files for glib wrapper
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Suggests: %{name}-doc = %{version}-%{release}

%description glib-devel
%{summary}.

%package glib-doc
Summary: Documentation for glib wrapper
BuildArch: noarch

%description glib-doc
%{summary}.

%if 0%{?qt5}
%package qt5
Summary: Qt5 wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-qt < 0.90.0-9
%description qt5
%{summary}.

%package qt5-devel
Summary: Development files for Qt5 wrapper
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
Obsoletes: %{name}-qt-devel < 0.90.0-9
%description qt5-devel
%{summary}.
%endif

%if 0%{?qt6}
%package qt6
Summary: Qt6 wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for Qt6 wrapper
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
%description qt6-devel
%{summary}.
%endif

%package cpp
Summary: Pure C++ wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cpp
%{summary}.

%package cpp-devel
Summary: Development files for C++ wrapper
Requires: %{name}-cpp%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description cpp-devel
%{summary}.

%package utils
Summary: Command line utilities for converting PDF files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Command line tools for manipulating PDF files and converting them to
other formats.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -b 3

chmod -x poppler/CairoFontEngine.cc

%build
%cmake \
  -DENABLE_CMS=lcms2 \
  -DENABLE_DCTDECODER=libjpeg \
  -DENABLE_GTK_DOC=ON \
  -DENABLE_LIBOPENJPEG=openjpeg2 \
%if ! 0%{?qt5}
  -DENABLE_QT5=OFF \
%endif
%if ! 0%{?qt6}
  -DENABLE_QT6=OFF \
%endif
  -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
  -DENABLE_ZLIB=OFF \
  ..
%cmake_build

%install
%cmake_install
%find_lang pdfsig

%check
%make_build test

# verify pkg-config sanity/version
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion poppler)" = "%{version}"
test "$(pkg-config --modversion poppler-cpp)" = "%{version}"
test "$(pkg-config --modversion poppler-glib)" = "%{version}"
%if 0%{?qt5}
test "$(pkg-config --modversion poppler-qt5)" = "%{version}"
%endif
%if 0%{?qt6}
test "$(pkg-config --modversion poppler-qt6)" = "%{version}"
%endif

%ldconfig_scriptlets

%ldconfig_scriptlets glib

%if 0%{?qt5}
%ldconfig_scriptlets qt5
%endif

%if 0%{?qt6}
%ldconfig_scriptlets qt6
%endif

%ldconfig_scriptlets cpp

%files
%doc README.md
%license COPYING
%{_libdir}/libpoppler.so.156*

%files devel
%{_libdir}/pkgconfig/poppler.pc
%{_libdir}/libpoppler.so
%dir %{_includedir}/poppler/
# xpdf headers
%{_includedir}/poppler/*.h
%{_includedir}/poppler/fofi/
%{_includedir}/poppler/goo/
%{_includedir}/poppler/splash/

%files glib
%{_libdir}/libpoppler-glib.so.8*
%{_libdir}/girepository-1.0/Poppler-0.18.typelib

%files glib-devel
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/libpoppler-glib.so
%{_datadir}/gir-1.0/Poppler-0.18.gir
%{_includedir}/poppler/glib/

%files glib-doc
%license COPYING
%{_datadir}/gtk-doc/

%if 0%{?qt5}
%files qt5
%{_libdir}/libpoppler-qt5.so.1*

%files qt5-devel
%{_libdir}/libpoppler-qt5.so
%{_libdir}/pkgconfig/poppler-qt5.pc
%{_includedir}/poppler/qt5/
%endif

%if 0%{?qt6}
%files qt6
%{_libdir}/libpoppler-qt6.so.3*

%files qt6-devel
%{_libdir}/libpoppler-qt6.so
%{_libdir}/pkgconfig/poppler-qt6.pc
%{_includedir}/poppler/qt6/
%endif

%files cpp
%{_libdir}/libpoppler-cpp.so.3*

%files cpp-devel
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_libdir}/libpoppler-cpp.so
%{_includedir}/poppler/cpp

%files utils -f pdfsig.lang
%{_bindir}/pdf*
%{_mandir}/man1/*

%changelog
%autochangelog
