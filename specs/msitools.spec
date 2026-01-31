%define _version_suffix -a155

# The mingw* RPMs are noarch, and the wxi data files are
# arch independant, so it is a waste of CPU cycles to run
# validation on all arches. Just run on x86_64 since that
# has the fastest Fedora builders.
%ifarch x86_64
%define with_validate 1
%else
%define with_validate 0
%endif

Name:           msitools
Version:        0.106.58
Release:        %autorelease
Summary:        Windows Installer tools

# LGPL-2.1-or-later: the project as a whole
# blessing:
# - libmsi/tokenize.c (libmsi1)
# - tools/sqldelim.* (not in any binary RPM)
# GPL-2.0-or-later:
# - tools/msidiff.in (main package)
# - tools/msidump.in (main package)
# - tools/msibuild.c (main package)
# - tools/msiinfo.c (main package)
# - data/wxi-validate.pl (not in any binary RPM)
# GPL-3.0-or-later:
# - build-aux/git-version-gen (not in any binary RPM)
# MS-RL:
# - data/ext/ui/* (main package)
# MIT:
# - subprojects/bats-core/* (not in any binary RPM)
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND MS-RL
URL:            http://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}%{?_version_suffix}.tar.xz

Requires:       libgsf >= 1.14.24-2

BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgcab1-devel >= 0.2
BuildRequires:  libgsf-devel
BuildRequires:  vala
BuildRequires:  bison

%if %{with_validate}
BuildRequires:  perl-base
BuildRequires:  perl-XML-XPath
# these are available in the RHEL/ELN buildroot
# srvany is also available but not used by the tests
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libffi
BuildRequires:  mingw64-libffi
BuildRequires:  mingw32-pcre2
BuildRequires:  mingw64-pcre2
BuildRequires:  mingw32-termcap
BuildRequires:  mingw64-termcap
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
%if %{undefined rhel}
BuildRequires:  mingw32-adwaita-icon-theme
BuildRequires:  mingw64-adwaita-icon-theme
BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-brotli
BuildRequires:  mingw64-brotli
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-curl
BuildRequires:  mingw64-curl
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw32-expat
BuildRequires:  mingw64-expat
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw64-freetype
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-glib-networking
BuildRequires:  mingw64-glib-networking
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-gmp
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-gsm
BuildRequires:  mingw64-gsm
BuildRequires:  mingw32-gstreamer1-plugins-bad-free
BuildRequires:  mingw64-gstreamer1-plugins-bad-free
BuildRequires:  mingw32-gstreamer1-plugins-base
BuildRequires:  mingw64-gstreamer1-plugins-base
BuildRequires:  mingw32-gstreamer1-plugins-good
BuildRequires:  mingw64-gstreamer1-plugins-good
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-gtk-vnc2
BuildRequires:  mingw64-gtk-vnc2
BuildRequires:  mingw32-gvnc
BuildRequires:  mingw64-gvnc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw32-hicolor-icon-theme
BuildRequires:  mingw64-hicolor-icon-theme
BuildRequires:  mingw32-icu
BuildRequires:  mingw64-icu
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw32-libcroco
BuildRequires:  mingw64-libcroco
BuildRequires:  mingw32-libdeflate
BuildRequires:  mingw64-libdeflate
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-libgovirt
BuildRequires:  mingw64-libgovirt
BuildRequires:  mingw32-libgpg-error
BuildRequires:  mingw64-libgpg-error
BuildRequires:  mingw32-libidn2
BuildRequires:  mingw64-libidn2
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw32-libogg
BuildRequires:  mingw64-libogg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw32-librsvg2
BuildRequires:  mingw64-librsvg2
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw32-libssh2
BuildRequires:  mingw64-libssh2
BuildRequires:  mingw32-libtasn1
BuildRequires:  mingw64-libtasn1
BuildRequires:  mingw32-libtheora
BuildRequires:  mingw64-libtheora
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw32-libunistring
BuildRequires:  mingw64-libunistring
BuildRequires:  mingw32-libusb1
BuildRequires:  mingw64-libusb1
BuildRequires:  mingw32-libvirt-glib
BuildRequires:  mingw64-libvirt-glib
BuildRequires:  mingw32-libvirt
BuildRequires:  mingw64-libvirt
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-openal-soft
BuildRequires:  mingw64-openal-soft
BuildRequires:  mingw32-openexr
BuildRequires:  mingw64-openexr
BuildRequires:  mingw32-openjpeg
BuildRequires:  mingw64-openjpeg
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-opus
BuildRequires:  mingw64-opus
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-portablexdr
BuildRequires:  mingw64-portablexdr
BuildRequires:  mingw32-readline
BuildRequires:  mingw64-readline
BuildRequires:  mingw32-rest
BuildRequires:  mingw64-rest
BuildRequires:  mingw32-sdl2-compat
BuildRequires:  mingw64-sdl2-compat
BuildRequires:  mingw32-speex
BuildRequires:  mingw64-speex
BuildRequires:  mingw32-spice-glib
BuildRequires:  mingw64-spice-glib
BuildRequires:  mingw32-spice-gtk3
BuildRequires:  mingw64-spice-gtk3
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw32-usbredir
BuildRequires:  mingw64-usbredir
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack
%endif
%endif

%description
msitools is a collection of utilities to inspect and create Windows
Installer files.  It is useful in a cross-compilation environment such
as fedora-mingw.

%package -n libmsi1
Summary:        A library to manipulate Windows .MSI files
License:        LGPL-2.1-or-later AND blessing

%description -n libmsi1
libmsi is a GObject library to work with Windows Installer files.  It is
a port from the MSI library of the Wine project.

%package -n libmsi1-devel
Summary:        A library to manipulate Windows .MSI files
License:        LGPL-2.1-or-later
Requires:       libmsi1%{?_isa} = %{version}-%{release}

%description -n libmsi1-devel
The libmsi1-devel package includes the header files for libmsi.

%prep
%autosetup -S git_am -n msitools-%{version}%{?_version_suffix}

%build
%if %{with_validate}
%meson -Dvalidate-wxi=true
%else
%meson
%endif
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%ldconfig_scriptlets -n libmsi1

%files
%doc copyright NEWS README.md TODO
%{_bindir}/msibuild
%{_bindir}/msidiff
%{_bindir}/msidump
%{_bindir}/msiextract
%{_bindir}/msiinfo
%{_bindir}/wixl
%{_bindir}/wixl-heat
%{_datadir}/bash-completion/completions/msitools
%{_datadir}/wixl-%{version}%{?_version_suffix}

%files -n libmsi1 -f %{name}.lang
%{_libdir}/girepository-1.0/Libmsi-1.0.typelib
%{_libdir}/libmsi-1.0.so.0*

%files -n libmsi1-devel
%{_datadir}/gir-1.0/Libmsi-1.0.gir
%{_datadir}/vala/vapi/libmsi-1.0.vapi
%{_datadir}/vala/vapi/libmsi-1.0.deps
%{_includedir}/libmsi-1.0/*
%{_libdir}/libmsi-1.0.so
%{_libdir}/pkgconfig/libmsi-1.0.pc


%changelog
%autochangelog
