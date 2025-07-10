# The new wow64 mode is disabled by default
# https://gitlab.winehq.org/wine/wine/-/releases/wine-9.0#wow64
%bcond new_wow64 1

# Compiling the preloader fails with hardening enabled
%undefine _hardened_build

%global no64bit   0
%global winegecko 2.47.4
%global winemono  9.4.0
%if 0%{?fedora}
%global opencl    1
%endif
#global _default_patch_fuzz 2
%ifarch %{ix86}
%global winepedir i386-windows
%global winepedirs %{winepedir}
%global winesodir i386-unix
%endif
%ifarch x86_64
%global winepedir x86_64-windows
%if %{with new_wow64}
%global winepedirs %["{i386-windows,%{winepedir}}"]
%else
%global winepedirs %{winepedir}
%endif
%global winesodir x86_64-unix
%endif
%ifarch aarch64
%global winepedir aarch64-windows
%global winepedirs %{winepedir}
%global winesodir aarch64-unix
%global __brp_llvm_compile_lto_elf %nil
%global __brp_strip_lto %nil
%global __brp_strip_static_archive %nil
%endif

# build with wine-staging patches, see:  https://github.com/wine-staging/wine-staging
%if 0%{?fedora} || 0%{?rhel}
%global wine_staging 1
%endif
# 0%%{?fedora}

Name:           wine
Version:        10.4
Release:        6%{?dist}
Summary:        A compatibility layer for windows applications

License:        LGPL-2.1-or-later
URL:            https://www.winehq.org/
Source0:        https://dl.winehq.org/wine/source/10.x/wine-%{version}.tar.xz
Source10:       https://dl.winehq.org/wine/source/10.x/wine-%{version}.tar.xz.sign

Source1:        wine.systemd
Source2:        wine-README-Fedora

# desktop files
Source100:      wine-notepad.desktop
Source101:      wine-regedit.desktop
Source102:      wine-uninstaller.desktop
Source103:      wine-winecfg.desktop
Source104:      wine-winefile.desktop
Source105:      wine-winemine.desktop
Source106:      wine-winhelp.desktop
Source107:      wine-wineboot.desktop
Source108:      wine-wordpad.desktop
Source109:      wine-oleview.desktop

# AppData files
Source150:      wine.appdata.xml

# wine bugs

# desktop dir
Source200:      wine.menu
Source201:      wine.directory

# mime types
Source300:      wine-mime-msi.desktop

# smooth tahoma (#693180)
# disable embedded bitmaps
Source501:      wine-tahoma.conf
# and provide a readme
Source502:      wine-README-tahoma

Patch511:       wine-cjk.patch

%if 0%{?wine_staging}
# wine-staging patches
# pulseaudio-patch is covered by that patch-set, too.
Source900: https://github.com/wine-staging/wine-staging/archive/v%{version}.tar.gz#/wine-staging-%{version}.tar.gz
%endif

%if !%{?no64bit}
# Fedora 36 Clang doesn't build PE binaries on ARM at the moment
# Wine 9.15 and higher requires ARM MinGW binaries (dlltool)
ExclusiveArch:  %{ix86} x86_64
%else
ExclusiveArch:  %{ix86}
%endif

BuildRequires:  bison
BuildRequires:  flex
%ifarch aarch64
BuildRequires:  clang >= 5.0
BuildRequires:  lld
%else
BuildRequires:  gcc
%endif
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel
BuildRequires:  freeglut-devel
BuildRequires:  libieee1284-devel

BuildRequires:  librsvg2
BuildRequires:  librsvg2-devel
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(libusb-1.0)
%if 0%{?opencl}
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
%endif
BuildRequires:  openldap-devel
BuildRequires:  perl-generators
BuildRequires:  unixODBC-devel
BuildRequires:  sane-backends-devel
BuildRequires:  systemd-devel
BuildRequires:  fontforge freetype-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libpcap-devel
# modular x
BuildRequires:  libX11-devel
BuildRequires:  mesa-libGL-devel mesa-libGLU-devel
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
BuildRequires:  mesa-compat-libOSMesa-devel
%else
BuildRequires:  mesa-libOSMesa-devel
%endif
BuildRequires:  libXxf86dga-devel libXxf86vm-devel
BuildRequires:  libXrandr-devel libXrender-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  fontconfig-devel
BuildRequires:  giflib-devel
BuildRequires:  cups-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
BuildRequires:  libXcursor-devel
BuildRequires:  dbus-devel
BuildRequires:  gnutls-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  gsm-devel
BuildRequires:  libv4l-devel
BuildRequires:  fontpackages-devel
BuildRequires:  gettext-devel
BuildRequires:  chrpath
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  mpg123-devel
%endif
BuildRequires:  SDL2-devel
BuildRequires:  vulkan-devel
BuildRequires:  libappstream-glib
BuildRequires:  pcsc-lite-devel

# Silverlight DRM-stuff needs XATTR enabled.
%if 0%{?wine_staging}
BuildRequires:  gtk3-devel
BuildRequires:  libattr-devel
BuildRequires:  libva-devel
%endif
# 0%%{?wine_staging}

BuildRequires:  icoutils

%ifarch %{ix86} x86_64
BuildRequires:  mingw32-FAudio
BuildRequires:  mingw64-FAudio
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-libxslt
BuildRequires:  mingw64-libxslt
BuildRequires:  mingw32-vkd3d >= 1.14
BuildRequires:  mingw64-vkd3d >= 1.14
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
%endif

Requires:       wine-common = %{version}-%{release}
Requires:       wine-desktop = %{version}-%{release}
Requires:       wine-fonts = %{version}-%{release}

# x86-32 parts
%ifarch %{ix86} x86_64
%if 0%{?fedora}
%if %[ !( "x86_64" == "%{_target_cpu}" && %{with new_wow64} ) ]
Requires:       wine-core(x86-32) = %{version}-%{release}
Requires:       wine-cms(x86-32) = %{version}-%{release}
Requires:       wine-ldap(x86-32) = %{version}-%{release}
Requires:       wine-smartcard(x86-32) = %{version}-%{release}
Requires:       wine-twain(x86-32) = %{version}-%{release}
Requires:       wine-pulseaudio(x86-32) = %{version}-%{release}
Requires:       wine-opencl(x86-32) = %{version}-%{release}
Requires:       mesa-dri-drivers(x86-32)
Recommends:     wine-dxvk(x86-32)
Recommends:     gstreamer1-plugins-good(x86-32)
%endif
Requires:       mingw32-wine-gecko = %winegecko
Requires:       wine-mono = %winemono
#  wait for rhbz#968860 to require arch-specific samba-winbind-clients
Requires:       /usr/bin/ntlm_auth
Recommends:     dosbox-staging
%endif
%endif

# x86-64 parts
%ifarch x86_64
Requires:       wine-core(x86-64) = %{version}-%{release}
Requires:       wine-cms(x86-64) = %{version}-%{release}
Requires:       wine-ldap(x86-64) = %{version}-%{release}
Requires:       wine-smartcard(x86-64) = %{version}-%{release}
Requires:       wine-twain(x86-64) = %{version}-%{release}
Requires:       wine-pulseaudio(x86-64) = %{version}-%{release}
%if 0%{?fedora}
Requires:       wine-opencl(x86-64) = %{version}-%{release}
Requires:       mingw64-wine-gecko = %winegecko
Requires:       wine-mono = %winemono
Recommends:     wine-dxvk(x86-64)
Recommends:     dosbox-staging
%endif
Requires:       mesa-dri-drivers(x86-64)
Recommends:     gstreamer1-plugins-good(x86-64)
%endif

# aarch64 parts
%ifarch aarch64
Requires:       wine-core(aarch-64) = %{version}-%{release}
Requires:       wine-cms(aarch-64) = %{version}-%{release}
Requires:       wine-ldap(aarch-64) = %{version}-%{release}
Requires:       wine-smartcard(aarch-64) = %{version}-%{release}
Requires:       wine-twain(aarch-64) = %{version}-%{release}
Requires:       wine-pulseaudio(aarch-64) = %{version}-%{release}
Requires:       wine-opencl(aarch-64) = %{version}-%{release}
Requires:       mingw64-wine-gecko = %winegecko
Requires:       mesa-dri-drivers(aarch-64)
%endif

%description
Wine as a compatibility layer for UNIX to run Windows applications. This
package includes a program loader, which allows unmodified Windows
3.x/9x/NT binaries to run on x86 and x86_64 Unixes. Wine can use native system
.dll files if they are available.

In Fedora wine is a meta-package which will install everything needed for wine
to work smoothly. Smaller setups can be achieved by installing some of the
wine-* sub packages.

%package core
Summary:        Wine core package
Requires(postun): /sbin/ldconfig
Requires(posttrans):   %{_sbindir}/alternatives
Requires(preun):       %{_sbindir}/alternatives

# require -filesystem
Requires:       wine-filesystem = %{version}-%{release}

%ifarch %{ix86}
# CUPS support uses dlopen - rhbz#1367537
Requires:       cups-libs(x86-32)
Requires:       freetype(x86-32)
Requires:       (nss-mdns(x86-32) if nss-mdns(x86-64))
Requires:       gnutls(x86-32)
Requires:       libXcomposite(x86-32)
Requires:       libXcursor(x86-32)
Requires:       libXinerama(x86-32)
Requires:       libXrandr(x86-32)
Requires:       libXrender(x86-32)
#dlopen in windowscodesc (fixes rhbz#1085075)
Requires:       libpng(x86-32)
Requires:       libpcap(x86-32)
%if 0%{?fedora} >= 42
Requires:       mesa-compat-libOSMesa(x86-32)
%else
Requires:       mesa-libOSMesa(x86-32)
%endif
Requires:       libv4l(x86-32)
Requires:       unixODBC(x86-32)
Requires:       SDL2(x86-32)
Requires:       vulkan-loader(x86-32)
%if 0%{?wine_staging}
Requires:       libva(x86-32)
%endif
Requires:  mingw32-FAudio
Requires:  mingw32-lcms2
Requires:  mingw32-libjpeg-turbo
Requires:  mingw32-libpng
Requires:  mingw32-libtiff
Requires:  mingw32-libxml2
Requires:  mingw32-libxslt
Requires:  mingw32-vkd3d >= 1.14
Requires:  mingw32-win-iconv
Requires:  mingw32-zlib
Provides:  wine-wow32 = %{version}-%{release}
Obsoletes: wine-wow32 < 10.4-6
%endif

%ifarch x86_64
# CUPS support uses dlopen - rhbz#1367537
Requires:       cups-libs(x86-64)
Requires:       freetype(x86-64)
Requires:       (nss-mdns(x86-64) if nss-mdns(x86-32))
Requires:       gnutls(x86-64)
Requires:       libXcomposite(x86-64)
Requires:       libXcursor(x86-64)
Requires:       libXinerama(x86-64)
Requires:       libXrandr(x86-64)
Requires:       libXrender(x86-64)
#dlopen in windowscodesc (fixes rhbz#1085075)
Requires:       libpng(x86-64)
Requires:       libpcap(x86-64)
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
Requires:       mesa-compat-libOSMesa(x86-64)
%else
Requires:       mesa-libOSMesa(x86-64)
%endif
Requires:       libv4l(x86-64)
Requires:       unixODBC(x86-64)
Requires:       SDL2(x86-64)
Requires:       vulkan-loader(x86-64)
%if 0%{?wine_staging}
Requires:       libva(x86-64)
%endif
Requires:  mingw64-FAudio
Requires:  mingw64-lcms2
Requires:  mingw64-libjpeg-turbo
Requires:  mingw64-libpng
Requires:  mingw64-libtiff
Requires:  mingw64-libxml2
Requires:  mingw64-libxslt
Requires:  mingw64-vkd3d >= 1.14
Requires:  mingw64-win-iconv
Requires:  mingw64-zlib
Provides:  wine-wow64 = %{version}-%{release}
Obsoletes: wine-wow64 < 10.4-6
%endif

%ifarch aarch64
# CUPS support uses dlopen - rhbz#1367537
Requires:       cups-libs
Requires:       freetype
Requires:       nss-mdns
Requires:       gnutls
Requires:       libXrender
Requires:       libXcursor
#dlopen in windowscodesc (fixes rhbz#1085075)
Requires:       libpng
Requires:       libpcap
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
Requires:       mesa-compat-libOSMesa
%else
Requires:       mesa-libOSMesa
%endif
Requires:       libv4l
Requires:       unixODBC
Requires:       SDL2
Requires:       vulkan-loader
%if 0%{?wine_staging}
Requires:       libva
%endif
%endif

Provides:       bundled(libjpeg) = 9f
Provides:       bundled(mpg123-libs) = 1.32.9

# removed as of 7.21
Obsoletes:      wine-openal < 7.21
Provides:       wine-openal = %{version}-%{release}

%description core
Wine core package includes the basic wine stuff needed by all other packages.

%package systemd
Summary:        Systemd config for the wine binfmt handler
Requires:       systemd >= 23
BuildArch:      noarch
Requires(post):  systemd
Requires(postun): systemd
Obsoletes:      wine-sysvinit < %{version}-%{release}

%description systemd
Register the wine binary handler for windows executables via systemd binfmt
handling. See man binfmt.d for further information.

%package filesystem
Summary:        Filesystem directories for wine
BuildArch:      noarch

%description filesystem
Filesystem directories and basic configuration for wine.

%package common
Summary:        Common files
Requires:       wine-core = %{version}-%{release}
BuildArch:      noarch

%description common
Common wine files and scripts.

%package desktop
Summary:        Desktop integration features for wine
Requires(post): desktop-file-utils >= 0.8
Requires(postun): desktop-file-utils >= 0.8
Requires:       wine-core = %{version}-%{release}
Requires:       wine-common = %{version}-%{release}
Requires:       wine-systemd = %{version}-%{release}
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description desktop
Desktop integration features for wine, including mime-types and a binary format
handler service.

%package fonts
Summary:       Wine font files
BuildArch:     noarch
# arial-fonts are available with wine-staging patchset, only.
%if 0%{?wine_staging}
Requires:      wine-arial-fonts = %{version}-%{release}
%else
# 0%%{?wine_staging}
Obsoletes:     wine-arial-fonts <= %{version}-%{release}
%endif
# 0%%{?wine_staging}
Requires:      wine-courier-fonts = %{version}-%{release}
Requires:      wine-fixedsys-fonts = %{version}-%{release}
Requires:      wine-small-fonts = %{version}-%{release}
Requires:      wine-system-fonts = %{version}-%{release}
Requires:      wine-marlett-fonts = %{version}-%{release}
Requires:      wine-ms-sans-serif-fonts = %{version}-%{release}
Requires:      wine-tahoma-fonts = %{version}-%{release}
# times-new-roman-fonts are available with wine_staging-patchset, only.
%if 0%{?wine_staging}
Requires:      wine-times-new-roman-fonts = %{version}-%{release}
%else
# 0%%{?wine_staging}
Obsoletes:     wine-times-new-roman-fonts <= %{version}-%{release}
Obsoletes:     wine-times-new-roman-fonts-system <= %{version}-%{release}
%endif
# 0%%{?wine_staging}
Requires:      wine-symbol-fonts = %{version}-%{release}
Requires:      wine-webdings-fonts = %{version}-%{release}
Requires:      wine-wingdings-fonts = %{version}-%{release}
# intermediate fix for #593140
Requires:      liberation-sans-fonts liberation-serif-fonts liberation-mono-fonts
Requires:      liberation-narrow-fonts

%description fonts
%{summary}

%if 0%{?wine_staging}
%package arial-fonts
Summary:       Wine Arial font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description arial-fonts
%{summary}
%endif
# 0%%{?wine_staging}

%package courier-fonts
Summary:       Wine Courier font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description courier-fonts
%{summary}

%package fixedsys-fonts
Summary:       Wine Fixedsys font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description fixedsys-fonts
%{summary}

%package small-fonts
Summary:       Wine Small font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description small-fonts
%{summary}

%package system-fonts
Summary:       Wine System font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description system-fonts
%{summary}


%package marlett-fonts
Summary:       Wine Marlett font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description marlett-fonts
%{summary}


%package ms-sans-serif-fonts
Summary:       Wine MS Sans Serif font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description ms-sans-serif-fonts
%{summary}

# rhbz#693180
# http://lists.fedoraproject.org/pipermail/devel/2012-June/168153.html
%package tahoma-fonts
Summary:       Wine Tahoma font family
BuildArch:     noarch
Requires:      wine-filesystem = %{version}-%{release}

%description tahoma-fonts
%{summary}
Please note: If you want system integration for wine tahoma fonts install the
wine-tahoma-fonts-system package.

%package tahoma-fonts-system
Summary:       Wine Tahoma font family system integration
BuildArch:     noarch
Requires:      fontpackages-filesystem
Requires:      wine-tahoma-fonts = %{version}-%{release}

%description tahoma-fonts-system
%{summary}

%if 0%{?wine_staging}
%package times-new-roman-fonts
Summary:       Wine Times New Roman font family
BuildArch:     noarch
Requires:      wine-filesystem = %{version}-%{release}

%description times-new-roman-fonts
%{summary}
Please note: If you want system integration for wine times new roman fonts install the
wine-times-new-roman-fonts-system package.

%package times-new-roman-fonts-system
Summary:       Wine Times New Roman font family system integration
BuildArch:     noarch
Requires:      fontpackages-filesystem
Requires:      wine-times-new-roman-fonts = %{version}-%{release}

%description times-new-roman-fonts-system
%{summary}
%endif

%package symbol-fonts
Summary:       Wine Symbol font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description symbol-fonts
%{summary}

%package webdings-fonts
Summary:       Wine Webdings font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description webdings-fonts
%{summary}

%package wingdings-fonts
Summary:       Wine Wingdings font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description wingdings-fonts
%{summary}
Please note: If you want system integration for wine wingdings fonts install the
wine-wingdings-fonts-system package.

%package wingdings-fonts-system
Summary:       Wine Wingdings font family system integration
BuildArch:     noarch
Requires:      fontpackages-filesystem
Requires:      wine-wingdings-fonts = %{version}-%{release}

%description wingdings-fonts-system
%{summary}


%package ldap
Summary: LDAP support for wine
Requires: wine-core = %{version}-%{release}

%description ldap
LDAP support for wine

%package cms
Summary: Color Management for wine
Requires: wine-core = %{version}-%{release}

%description cms
Color Management for wine

%package smartcard
Summary: Smart card support for wine
Requires: wine-core = %{version}-%{release}

%description smartcard
Smart card support for wine

%package twain
Summary: Twain support for wine
Requires: wine-core = %{version}-%{release}
%ifarch %{ix86}
Requires: sane-backends-libs(x86-32)
%endif
%ifarch x86_64
Requires: sane-backends-libs(x86-64)
%endif
%ifarch aarch64
Requires: sane-backends-libs
%endif

%description twain
Twain support for wine

%package devel
Summary: Wine development environment
Requires: wine-core = %{version}-%{release}

%description devel
Header, include files and library definition files for developing applications
with the Wine Windows(TM) emulation libraries.

%package pulseaudio
Summary: Pulseaudio support for wine
Requires: wine-core = %{version}-%{release}
# midi output
Requires: wine-alsa%{?_isa} = %{version}-%{release}

%description pulseaudio
This package adds a pulseaudio driver for wine.

%package alsa
Summary: Alsa support for wine
Requires: wine-core = %{version}-%{release}

%description alsa
This package adds an alsa driver for wine.

%if 0%{?opencl}
%package opencl
Summary: OpenCL support for wine
Requires: wine-core = %{version}-%{release}

%description opencl
This package adds the opencl driver for wine.
%endif

%prep
%setup -qn wine-%{version}
%patch -P 511 -p1 -b.cjk

%if 0%{?wine_staging}
# setup and apply wine-staging patches
gzip -dc %{SOURCE900} | tar -xf - --strip-components=1

staging/patchinstall.py DESTDIR="`pwd`" --all -W server-Stored_ACLs

%endif
# 0%%{?wine_staging}

%build
# This package uses top level ASM constructs which are incompatible with LTO.
# Top level ASMs are often used to implement symbol versioning.  gcc-10
# introduces a new mechanism for symbol versioning which works with LTO.
# Converting packages to use that mechanism instead of toplevel ASMs is
# recommended.
# Disable LTO
%define _lto_cflags %{nil}

# disable fortify as it breaks wine
# http://bugs.winehq.org/show_bug.cgi?id=24606
# http://bugs.winehq.org/show_bug.cgi?id=25073
%undefine _fortify_level
# Disable Red Hat specs for package notes (Fedora 38+) and annobin.
# MinGW GCC does not support these options.
export LDFLAGS="$(echo "%{build_ldflags}" | sed -e 's/-Wl,-z,relro//' -e 's/-Wl,--build-id=sha1//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-package-notes//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//')"
%ifarch x86_64
export CFLAGS="$(echo "%{optflags}" | sed -e 's/-O2//' -e 's/-fcf-protection//' -e 's/-fstack-protector-strong//' -e 's/-fstack-clash-protection//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//') -O2"
%else
export CFLAGS="$(echo "%{optflags}" | sed -e 's/-fcf-protection//' -e 's/-fstack-protector-strong//' -e 's/-fstack-clash-protection//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//')"
%endif

%ifarch  aarch64
# Wine enabled -Wl,-WX that turns linker warnings into errors
# Fedora passes '--as-needed' for all binaries and this is a warning from the linker, now an error, so disable flag for now
sed -i 's/-Wl,-WX//g' configure
%global toolchain clang
%endif

# required so that both Linux and Windows development files can be found
unset PKG_CONFIG_PATH

%configure \
 --sysconfdir=%{_sysconfdir}/wine \
 --x-includes=%{_includedir} --x-libraries=%{_libdir} \
 --with-dbus \
 --with-x \
%ifarch x86_64 aarch64
 --enable-win64 \
%ifarch x86_64
%if %{with new_wow64}
 --enable-archs=i386,x86_64 \
%else
 --with-system-dllpath=%{mingw64_bindir} \
%endif
%endif
%endif
%ifarch %{ix86}
 --with-system-dllpath=%{mingw32_bindir} \
%endif
%{?wine_staging: --with-xattr} \
 --disable-tests

%make_build TARGETFLAGS=""

%install

%make_install \
        LDCONFIG=/bin/true \
        UPDATE_DESKTOP_DATABASE=/bin/true

# setup for alternatives usage
%ifarch x86_64 aarch64
mv %{buildroot}%{_bindir}/wine %{buildroot}%{_bindir}/wine64
mv %{buildroot}%{_bindir}/wineserver %{buildroot}%{_bindir}/wineserver64
%endif
%ifarch %{ix86}
mv %{buildroot}%{_bindir}/wine %{buildroot}%{_bindir}/wine32
mv %{buildroot}%{_bindir}/wineserver %{buildroot}%{_bindir}/wineserver32
%endif
touch %{buildroot}%{_bindir}/wine
touch %{buildroot}%{_bindir}/wineserver
mv %{buildroot}%{_libdir}/wine/%{winepedir}/dxgi.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-dxgi.dll
mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d8.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d8.dll
mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d9.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d9.dll
mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d10.dll
mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10_1.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d10_1.dll
mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10core.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d10core.dll
mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d11.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d11.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/dxgi.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d8.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d9.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10_1.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10core.dll
touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d11.dll
%if %[ "x86_64" == "%{_target_cpu}" && %{with new_wow64} ]
mv %{buildroot}%{_libdir}/wine/i386-windows/dxgi.dll %{buildroot}%{_libdir}/wine/i386-windows/wine-dxgi.dll
mv %{buildroot}%{_libdir}/wine/i386-windows/d3d9.dll %{buildroot}%{_libdir}/wine/i386-windows/wine-d3d9.dll
mv %{buildroot}%{_libdir}/wine/i386-windows/d3d10.dll %{buildroot}%{_libdir}/wine/i386-windows/wine-d3d10.dll
mv %{buildroot}%{_libdir}/wine/i386-windows/d3d10_1.dll %{buildroot}%{_libdir}/wine/i386-windows/wine-d3d10_1.dll
mv %{buildroot}%{_libdir}/wine/i386-windows/d3d10core.dll %{buildroot}%{_libdir}/wine/i386-windows/wine-d3d10core.dll
mv %{buildroot}%{_libdir}/wine/i386-windows/d3d11.dll %{buildroot}%{_libdir}/wine/i386-windows/wine-d3d11.dll
touch %{buildroot}%{_libdir}/wine/i386-windows/dxgi.dll
touch %{buildroot}%{_libdir}/wine/i386-windows/d3d9.dll
touch %{buildroot}%{_libdir}/wine/i386-windows/d3d10.dll
touch %{buildroot}%{_libdir}/wine/i386-windows/d3d10_1.dll
touch %{buildroot}%{_libdir}/wine/i386-windows/d3d10core.dll
touch %{buildroot}%{_libdir}/wine/i386-windows/d3d11.dll
%endif

# setup new wow64
%ifarch x86_64
ln -sf /usr/lib/wine/i386-unix %{buildroot}%{_libdir}/wine/i386-unix
ln -sf /usr/lib/wine/i386-windows %{buildroot}%{_libdir}/wine/i386-windows
%endif
%ifarch %{ix86}
ln -sf /usr/lib64/wine/x86_64-unix %{buildroot}%{_libdir}/wine/x86_64-unix
ln -sf /usr/lib64/wine/x86_64-windows %{buildroot}%{_libdir}/wine/x86_64-windows
%endif

# remove rpath
chrpath --delete %{buildroot}%{_bindir}/wmc
chrpath --delete %{buildroot}%{_bindir}/wrc
%ifarch x86_64 aarch64
chrpath --delete %{buildroot}%{_bindir}/wine64
chrpath --delete %{buildroot}%{_bindir}/wineserver64
%else
chrpath --delete %{buildroot}%{_bindir}/wine32
chrpath --delete %{buildroot}%{_bindir}/wineserver32
%endif

mkdir -p %{buildroot}%{_sysconfdir}/wine

# Allow users to launch Windows programs by just clicking on the .exe file...
mkdir -p %{buildroot}%{_binfmtdir}
install -p -c -m 644 %{SOURCE1} %{buildroot}%{_binfmtdir}/wine.conf

# add wine dir to desktop
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
install -p -m 644 %{SOURCE200} \
%{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/wine.menu
mkdir -p %{buildroot}%{_datadir}/desktop-directories
install -p -m 644 %{SOURCE201} \
%{buildroot}%{_datadir}/desktop-directories/Wine.directory

# add gecko dir
mkdir -p %{buildroot}%{_datadir}/wine/gecko

# add mono dir
mkdir -p %{buildroot}%{_datadir}/wine/mono

# extract and install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# This replacement masks a composite program icon .SVG down
# so that only its full-size scalable icon is visible
PROGRAM_ICONFIX='s/height="272"/height="256"/;'\
's/width="632"/width="256"\n'\
'   x="368"\n'\
'   y="8"\n'\
'   viewBox="368, 8, 256, 256"/;'
MAIN_ICONFIX='s/height="272"/height="256"/;'\
's/width="632"/width="256"\n'\
'   x="8"\n'\
'   y="8"\n'\
'   viewBox="8, 8, 256, 256"/;'

# This icon file is still in the legacy format
install -p -m 644 dlls/user32/resources/oic_winlogo.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wine.svg
sed -i -e "$MAIN_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wine.svg

# The rest come from programs/, and contain larger scalable icons
# with a new layout that requires the PROGRAM_ICONFIX sed adjustment
install -p -m 644 programs/notepad/notepad.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/notepad.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/notepad.svg

install -p -m 644 programs/regedit/regedit.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/regedit.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/regedit.svg

install -p -m 644 programs/msiexec/msiexec.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/msiexec.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/msiexec.svg

install -p -m 644 programs/winecfg/winecfg.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winecfg.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winecfg.svg

install -p -m 644 programs/winefile/winefile.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winefile.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winefile.svg

install -p -m 644 programs/winemine/winemine.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winemine.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winemine.svg

install -p -m 644 programs/winhlp32/winhelp.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winhelp.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winhelp.svg

install -p -m 644 programs/wordpad/wordpad.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wordpad.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wordpad.svg

# install desktop files
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE100}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE101}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE102}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE103}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE104}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE105}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE106}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE107}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE108}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE109}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/wine.desktop

#mime-types
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE300}

cp -p %{SOURCE2} README-FEDORA

cp -p %{SOURCE502} README-tahoma

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/


# install Tahoma font for system package
install -p -m 0755 -d %{buildroot}/%{_datadir}/fonts/wine-tahoma-fonts
pushd %{buildroot}/%{_datadir}/fonts/wine-tahoma-fonts
ln -s ../../wine/fonts/tahoma.ttf tahoma.ttf
ln -s ../../wine/fonts/tahomabd.ttf tahomabd.ttf
popd

# add config and readme for tahoma
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -p -m 0644 %{SOURCE501} %{buildroot}%{_fontconfig_templatedir}/20-wine-tahoma-nobitmaps.conf

ln -s %{_fontconfig_templatedir}/20-wine-tahoma-nobitmaps.conf \
      %{buildroot}%{_fontconfig_confdir}/20-wine-tahoma-nobitmaps.conf

%if 0%{?wine_staging}
# install Times New Roman font for system package
install -p -m 0755 -d %{buildroot}/%{_datadir}/fonts/wine-times-new-roman-fonts
pushd %{buildroot}/%{_datadir}/fonts/wine-times-new-roman-fonts
ln -s ../../wine/fonts/times.ttf times.ttf
popd
%endif

# install Wingdings font for system package
install -p -m 0755 -d %{buildroot}/%{_datadir}/fonts/wine-wingdings-fonts
pushd %{buildroot}/%{_datadir}/fonts/wine-wingdings-fonts
ln -s ../../wine/fonts/wingding.ttf wingding.ttf
popd

# clean readme files
pushd documentation
for lang in de es fi fr hu it ja ko nl no pt_br pt ru sv tr uk zh_cn;
do iconv -f iso8859-1 -t utf-8 README-$lang.md > \
 README-$lang.md.conv && mv -f README-$lang.md.conv README-$lang.md
done;
popd

rm -f %{buildroot}%{_initrddir}/wine

# install and validate AppData file
mkdir -p %{buildroot}/%{_metainfodir}/
install -p -m 0644 %{SOURCE150} %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%post systemd
%binfmt_apply wine.conf

%postun systemd
if [ $1 -eq 0 ]; then
/bin/systemctl try-restart systemd-binfmt.service
fi

%ldconfig_post core

%posttrans core
# handle upgrades for a few package updates
rm -f %{_libdir}/wine/%{winepedirs}/d3d8.dll
rm -f %{_bindir}/wine-preloader
%ifarch x86_64 aarch64
%{_sbindir}/alternatives --remove wine %{_bindir}/wine64
%{_sbindir}/alternatives --install %{_bindir}/wine \
  wine %{_bindir}/wine64 20
%{_sbindir}/alternatives --install %{_bindir}/wineserver \
  wineserver %{_bindir}/wineserver64 20
%else
%{_sbindir}/alternatives --remove wine %{_bindir}/wine32
%{_sbindir}/alternatives --install %{_bindir}/wine \
  wine %{_bindir}/wine32 10
%{_sbindir}/alternatives --install %{_bindir}/wineserver \
  wineserver %{_bindir}/wineserver32 10
%endif
%{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedirs}/dxgi.dll \
  'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-dxgi.dll 10
%{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedirs}/d3d8.dll \
  'wine-d3d8%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d8.dll 10
%{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedirs}/d3d9.dll \
  'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d9.dll 10
%{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedirs}/d3d10core.dll \
  'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d10core.dll 10
%{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedirs}/d3d10.dll \
  'wine-d3d10%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d10.dll 10 \
  --slave  %{_libdir}/wine/%{winepedirs}/d3d10_1.dll 'wine-d3d10_1%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d10_1.dll
%{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedirs}/d3d11.dll \
  'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d11.dll 10
%if %[ "x86_64" == "%{_target_cpu}" && %{with new_wow64} ]
%{_sbindir}/alternatives --install %{_libdir}/wine/i386-windows/dxgi.dll \
  'wine-dxgi(x86-32)' %{_libdir}/wine/i386-windows/wine-dxgi.dll 10
%{_sbindir}/alternatives --install %{_libdir}/wine/i386-windows/d3d9.dll \
  'wine-d3d9(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d9.dll 10
%{_sbindir}/alternatives --install %{_libdir}/wine/i386-windows/d3d10.dll \
  'wine-d3d10(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d10.dll 10 \
  --slave  %{_libdir}/wine/i386-windows/d3d10_1.dll 'wine-d3d10_1(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d10_1.dll \
  --slave  %{_libdir}/wine/i386-windows/d3d10core.dll 'wine-d3d10core(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d10core.dll
%{_sbindir}/alternatives --install %{_libdir}/wine/i386-windows/d3d11.dll \
  'wine-d3d11(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d11.dll 10
%endif

%postun core
%{?ldconfig}
if [ $1 -eq 0 ] ; then
%ifarch x86_64 aarch64
  %{_sbindir}/alternatives --remove wine %{_bindir}/wine64
  %{_sbindir}/alternatives --remove wineserver %{_bindir}/wineserver64
%else
  %{_sbindir}/alternatives --remove wine %{_bindir}/wine32
  %{_sbindir}/alternatives --remove wineserver %{_bindir}/wineserver32
%endif
  %{_sbindir}/alternatives --remove 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-dxgi.dll
  %{_sbindir}/alternatives --remove 'wine-d3d8%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d8.dll
  %{_sbindir}/alternatives --remove 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d9.dll
  %{_sbindir}/alternatives --remove 'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d10core.dll
  %{_sbindir}/alternatives --remove 'wine-d3d10%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d10.dll
  %{_sbindir}/alternatives --remove 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedirs}/wine-d3d11.dll
%if %[ "x86_64" == "%{_target_cpu}" && %{with new_wow64} ]
  %{_sbindir}/alternatives --remove 'wine-dxgi(x86-32)' %{_libdir}/wine/i386-windows/wine-dxgi.dll
  %{_sbindir}/alternatives --remove 'wine-d3d9(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d9.dll
  %{_sbindir}/alternatives --remove 'wine-d3d10(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d10.dll
  %{_sbindir}/alternatives --remove 'wine-d3d11(x86-32)' %{_libdir}/wine/i386-windows/wine-d3d11.dll
%endif
fi

%ldconfig_scriptlets ldap

%ldconfig_scriptlets cms

%ldconfig_scriptlets twain

%ldconfig_scriptlets alsa

%files
# meta package

%files core
%license LICENSE
%license LICENSE.OLD
%license COPYING.LIB
%doc ANNOUNCE.md
%doc AUTHORS
%doc README-FEDORA
%doc README.md
%doc VERSION
# do not include huge changelogs .OLD .ALPHA .BETA (#204302)
%doc documentation/README-*
%{_bindir}/msidb
%{_bindir}/winedump
%{_libdir}/wine/%{winepedirs}/explorer.exe
%{_libdir}/wine/%{winepedirs}/cabarc.exe
%{_libdir}/wine/%{winepedirs}/control.exe
%{_libdir}/wine/%{winepedirs}/cmd.exe
%{_libdir}/wine/%{winepedirs}/dxdiag.exe
%{_libdir}/wine/%{winepedirs}/notepad.exe
%{_libdir}/wine/%{winepedirs}/plugplay.exe
%{_libdir}/wine/%{winepedirs}/progman.exe
%{_libdir}/wine/%{winepedirs}/taskmgr.exe
%{_libdir}/wine/%{winepedirs}/winedbg.exe
%{_libdir}/wine/%{winepedirs}/winefile.exe
%{_libdir}/wine/%{winepedirs}/winemine.exe
%{_libdir}/wine/%{winepedirs}/winemsibuilder.exe
%{_libdir}/wine/%{winepedirs}/winepath.exe
%{_libdir}/wine/%{winepedirs}/winmgmt.exe
%{_libdir}/wine/%{winepedirs}/winver.exe
%{_libdir}/wine/%{winepedirs}/wordpad.exe
%{_libdir}/wine/%{winepedirs}/write.exe
%{_libdir}/wine/%{winepedirs}/wusa.exe

%ifarch %{ix86}
%{_bindir}/wine32
%{_bindir}/wineserver32
%endif

%ifarch x86_64 aarch64
%{_bindir}/wine64
%{_bindir}/wineserver64
%endif

%ghost %{_bindir}/wine
%ghost %{_bindir}/wineserver

%dir %{_libdir}/wine

%{_libdir}/wine/%{winepedirs}/attrib.exe
%{_libdir}/wine/%{winepedirs}/arp.exe
%{_libdir}/wine/%{winepedirs}/aspnet_regiis.exe
%{_libdir}/wine/%{winepedirs}/cacls.exe
%{_libdir}/wine/%{winepedirs}/certutil.exe
%{_libdir}/wine/%{winepedirs}/conhost.exe
%{_libdir}/wine/%{winepedirs}/cscript.exe
%{_libdir}/wine/%{winepedirs}/dism.exe
%{_libdir}/wine/%{winepedirs}/dllhost.exe
%{_libdir}/wine/%{winepedirs}/dplaysvr.exe
%ifarch %{ix86} x86_64
%{_libdir}/wine/%{winepedirs}/dpnsvr.exe
%endif
%{_libdir}/wine/%{winepedirs}/dpvsetup.exe
%{_libdir}/wine/%{winepedirs}/eject.exe
%{_libdir}/wine/%{winepedirs}/expand.exe
%{_libdir}/wine/%{winepedirs}/extrac32.exe
%{_libdir}/wine/%{winepedirs}/fc.exe
%{_libdir}/wine/%{winepedirs}/find.exe
%{_libdir}/wine/%{winepedirs}/findstr.exe
%{_libdir}/wine/%{winepedirs}/fsutil.exe
%{_libdir}/wine/%{winepedirs}/hostname.exe
%{_libdir}/wine/%{winepedirs}/ipconfig.exe
%{_libdir}/wine/%{winepedirs}/klist.exe
%{_libdir}/wine/%{winepedirs}/makecab.exe
%{_libdir}/wine/%{winepedirs}/mshta.exe
%{_libdir}/wine/%{winepedirs}/msidb.exe
%{_libdir}/wine/%{winepedirs}/msiexec.exe
%{_libdir}/wine/%{winepedirs}/net.exe
%{_libdir}/wine/%{winepedirs}/netstat.exe
%{_libdir}/wine/%{winepedirs}/ngen.exe
%{_libdir}/wine/%{winepedirs}/ntoskrnl.exe
%{_libdir}/wine/%{winepedirs}/oleview.exe
%{_libdir}/wine/%{winepedirs}/ping.exe
%{_libdir}/wine/%{winepedirs}/pnputil.exe
%{_libdir}/wine/%{winepedirs}/powershell.exe
%{_libdir}/wine/%{winepedirs}/reg.exe
%{_libdir}/wine/%{winepedirs}/regasm.exe
%{_libdir}/wine/%{winepedirs}/regedit.exe
%{_libdir}/wine/%{winepedirs}/regsvcs.exe
%{_libdir}/wine/%{winepedirs}/regsvr32.exe
%{_libdir}/wine/%{winepedirs}/rpcss.exe
%{_libdir}/wine/%{winepedirs}/rundll32.exe
%{_libdir}/wine/%{winepedirs}/schtasks.exe
%{_libdir}/wine/%{winepedirs}/sdbinst.exe
%{_libdir}/wine/%{winepedirs}/secedit.exe
%{_libdir}/wine/%{winepedirs}/servicemodelreg.exe
%{_libdir}/wine/%{winepedirs}/services.exe
%{_libdir}/wine/%{winepedirs}/setx.exe
%{_libdir}/wine/%{winepedirs}/start.exe
%{_libdir}/wine/%{winepedirs}/tasklist.exe
%{_libdir}/wine/%{winepedirs}/termsv.exe
%{_libdir}/wine/%{winepedirs}/timeout.exe
%{_libdir}/wine/%{winepedirs}/view.exe
%{_libdir}/wine/%{winepedirs}/wevtutil.exe
%{_libdir}/wine/%{winepedirs}/where.exe
%{_libdir}/wine/%{winepedirs}/whoami.exe
%{_libdir}/wine/%{winepedirs}/wineboot.exe
%{_libdir}/wine/%{winepedirs}/winebrowser.exe
%{_libdir}/wine/%{winepedirs}/wineconsole.exe
%{_libdir}/wine/%{winepedirs}/winemenubuilder.exe
%{_libdir}/wine/%{winepedirs}/winecfg.exe
%{_libdir}/wine/%{winepedirs}/winedevice.exe
%{_libdir}/wine/%{winepedirs}/winhlp32.exe
%{_libdir}/wine/%{winepedirs}/wmplayer.exe
%{_libdir}/wine/%{winepedirs}/wscript.exe
%{_libdir}/wine/%{winepedirs}/uninstaller.exe

%ifarch %{ix86}
%{_libdir}/wine/x86_64-unix
%{_libdir}/wine/x86_64-windows
%endif
%ifarch x86_64
%{_libdir}/wine/i386-unix
%{_libdir}/wine/i386-windows
%endif

%{_libdir}/wine/%{winepedirs}/acledit.dll
%{_libdir}/wine/%{winepedirs}/aclui.dll
%{_libdir}/wine/%{winepedirs}/activeds.dll
%{_libdir}/wine/%{winepedirs}/activeds.tlb
%{_libdir}/wine/%{winepedirs}/actxprxy.dll
%{_libdir}/wine/%{winepedirs}/adsldp.dll
%{_libdir}/wine/%{winepedirs}/adsldpc.dll
%{_libdir}/wine/%{winepedirs}/advapi32.dll
%{_libdir}/wine/%{winepedirs}/advpack.dll
%{_libdir}/wine/%{winepedirs}/amsi.dll
%{_libdir}/wine/%{winepedirs}/amstream.dll
%{_libdir}/wine/%{winepedirs}/apisetschema.dll
%{_libdir}/wine/%{winepedirs}/apphelp.dll
%{_libdir}/wine/%{winepedirs}/appwiz.cpl
%{_libdir}/wine/%{winepedirs}/appxdeploymentclient.dll
%{_libdir}/wine/%{winepedirs}/atl.dll
%{_libdir}/wine/%{winepedirs}/atl80.dll
%{_libdir}/wine/%{winepedirs}/atl90.dll
%{_libdir}/wine/%{winepedirs}/atl100.dll
%{_libdir}/wine/%{winepedirs}/atl110.dll
%{_libdir}/wine/%{winepedirs}/atlthunk.dll
%{_libdir}/wine/%{winepedirs}/atmlib.dll
%{_libdir}/wine/%{winepedirs}/authz.dll
%{_libdir}/wine/%{winepedirs}/avicap32.dll
%{_libdir}/wine/%{winesodir}/avicap32.so
%{_libdir}/wine/%{winepedirs}/avifil32.dll
%{_libdir}/wine/%{winepedirs}/avrt.dll
%{_libdir}/wine/%{winepedirs}/bcp47langs.dll
%{_libdir}/wine/%{winesodir}/bcrypt.so
%{_libdir}/wine/%{winepedirs}/bcrypt.dll
%{_libdir}/wine/%{winepedirs}/bcryptprimitives.dll
%{_libdir}/wine/%{winepedirs}/bluetoothapis.dll
%{_libdir}/wine/%{winepedirs}/browseui.dll
%{_libdir}/wine/%{winepedirs}/bthprops.cpl
%{_libdir}/wine/%{winepedirs}/cabinet.dll
%{_libdir}/wine/%{winepedirs}/cards.dll
%{_libdir}/wine/%{winepedirs}/cdosys.dll
%{_libdir}/wine/%{winepedirs}/cfgmgr32.dll
%{_libdir}/wine/%{winepedirs}/chcp.com
%{_libdir}/wine/%{winepedirs}/clock.exe
%{_libdir}/wine/%{winepedirs}/clusapi.dll
%{_libdir}/wine/%{winepedirs}/cng.sys
%{_libdir}/wine/%{winepedirs}/colorcnv.dll
%{_libdir}/wine/%{winepedirs}/combase.dll
%{_libdir}/wine/%{winepedirs}/comcat.dll
%{_libdir}/wine/%{winepedirs}/comctl32.dll
%{_libdir}/wine/%{winepedirs}/comdlg32.dll
%{_libdir}/wine/%{winepedirs}/coml2.dll
%{_libdir}/wine/%{winepedirs}/compstui.dll
%{_libdir}/wine/%{winepedirs}/comsvcs.dll
%{_libdir}/wine/%{winepedirs}/concrt140.dll
%{_libdir}/wine/%{winepedirs}/connect.dll
%{_libdir}/wine/%{winepedirs}/coremessaging.dll
%{_libdir}/wine/%{winepedirs}/credui.dll
%{_libdir}/wine/%{winepedirs}/crtdll.dll
%{_libdir}/wine/%{winesodir}/crypt32.so
%{_libdir}/wine/%{winepedirs}/crypt32.dll
%{_libdir}/wine/%{winepedirs}/cryptbase.dll
%{_libdir}/wine/%{winepedirs}/cryptdlg.dll
%{_libdir}/wine/%{winepedirs}/cryptdll.dll
%{_libdir}/wine/%{winepedirs}/cryptext.dll
%{_libdir}/wine/%{winepedirs}/cryptnet.dll
%{_libdir}/wine/%{winepedirs}/cryptowinrt.dll
%{_libdir}/wine/%{winepedirs}/cryptsp.dll
%{_libdir}/wine/%{winepedirs}/cryptui.dll
%{_libdir}/wine/%{winepedirs}/ctapi32.dll
%{_libdir}/wine/%{winesodir}/ctapi32.so
%{_libdir}/wine/%{winepedirs}/ctl3d32.dll
%{_libdir}/wine/%{winepedirs}/d2d1.dll
%ghost %{_libdir}/wine/%{winepedirs}/d3d10.dll
%ghost %{_libdir}/wine/%{winepedirs}/d3d10_1.dll
%ghost %{_libdir}/wine/%{winepedirs}/d3d10core.dll
%{_libdir}/wine/%{winepedirs}/wine-d3d10.dll
%{_libdir}/wine/%{winepedirs}/wine-d3d10_1.dll
%{_libdir}/wine/%{winepedirs}/wine-d3d10core.dll
%ghost %{_libdir}/wine/%{winepedirs}/d3d11.dll
%{_libdir}/wine/%{winepedirs}/wine-d3d11.dll
%{_libdir}/wine/%{winepedirs}/d3d12.dll
%{_libdir}/wine/%{winepedirs}/d3d12core.dll
%{_libdir}/wine/%{winepedirs}/d3dcompiler_*.dll
%{_libdir}/wine/%{winepedirs}/d3dim.dll
%{_libdir}/wine/%{winepedirs}/d3dim700.dll
%{_libdir}/wine/%{winepedirs}/d3drm.dll
%{_libdir}/wine/%{winepedirs}/d3dx9_*.dll
%{_libdir}/wine/%{winepedirs}/d3dx10_*.dll
%{_libdir}/wine/%{winepedirs}/d3dx11_42.dll
%{_libdir}/wine/%{winepedirs}/d3dx11_43.dll
%{_libdir}/wine/%{winepedirs}/d3dxof.dll
%{_libdir}/wine/%{winepedirs}/dataexchange.dll
%{_libdir}/wine/%{winepedirs}/davclnt.dll
%{_libdir}/wine/%{winepedirs}/dbgeng.dll
%{_libdir}/wine/%{winepedirs}/dbghelp.dll
%{_libdir}/wine/%{winepedirs}/dciman32.dll
%{_libdir}/wine/%{winepedirs}/dcomp.dll
%{_libdir}/wine/%{winepedirs}/ddraw.dll
%{_libdir}/wine/%{winepedirs}/ddrawex.dll
%{_libdir}/wine/%{winepedirs}/desk.cpl
%{_libdir}/wine/%{winepedirs}/devenum.dll
%{_libdir}/wine/%{winepedirs}/dhcpcsvc.dll
%{_libdir}/wine/%{winepedirs}/dhcpcsvc6.dll
%{_libdir}/wine/%{winepedirs}/dhtmled.ocx
%{_libdir}/wine/%{winepedirs}/diasymreader.dll
%{_libdir}/wine/%{winepedirs}/difxapi.dll
%{_libdir}/wine/%{winepedirs}/dinput.dll
%{_libdir}/wine/%{winepedirs}/dinput8.dll
%{_libdir}/wine/%{winepedirs}/directmanipulation.dll
%{_libdir}/wine/%{winepedirs}/dispex.dll
%{_libdir}/wine/%{winepedirs}/dmband.dll
%{_libdir}/wine/%{winepedirs}/dmcompos.dll
%{_libdir}/wine/%{winepedirs}/dmime.dll
%{_libdir}/wine/%{winepedirs}/dmloader.dll
%{_libdir}/wine/%{winepedirs}/dmscript.dll
%{_libdir}/wine/%{winepedirs}/dmstyle.dll
%{_libdir}/wine/%{winepedirs}/dmsynth.dll
%{_libdir}/wine/%{winepedirs}/dmusic.dll
%{_libdir}/wine/%{winepedirs}/dmusic32.dll
%{_libdir}/wine/%{winepedirs}/dplay.dll
%{_libdir}/wine/%{winepedirs}/dplayx.dll
%{_libdir}/wine/%{winepedirs}/dpnaddr.dll
%{_libdir}/wine/%{winepedirs}/dpnet.dll
%{_libdir}/wine/%{winepedirs}/dpnhpast.dll
%{_libdir}/wine/%{winepedirs}/dpnhupnp.dll
%{_libdir}/wine/%{winepedirs}/dpnlobby.dll
%{_libdir}/wine/%{winepedirs}/dpvoice.dll
%{_libdir}/wine/%{winepedirs}/dpwsockx.dll
%{_libdir}/wine/%{winepedirs}/drmclien.dll
%{_libdir}/wine/%{winepedirs}/dsound.dll
%{_libdir}/wine/%{winepedirs}/dsdmo.dll
%{_libdir}/wine/%{winepedirs}/dsquery.dll
%{_libdir}/wine/%{winepedirs}/dssenh.dll
%{_libdir}/wine/%{winepedirs}/dsuiext.dll
%{_libdir}/wine/%{winepedirs}/dswave.dll
%{_libdir}/wine/%{winepedirs}/dwmapi.dll
%{_libdir}/wine/%{winepedirs}/dwrite.dll
%{_libdir}/wine/%{winesodir}/dwrite.so
%{_libdir}/wine/%{winepedirs}/dx8vb.dll
%{_libdir}/wine/%{winepedirs}/dxcore.dll
%{_libdir}/wine/%{winepedirs}/dxdiagn.dll
%ghost %{_libdir}/wine/%{winepedirs}/dxgi.dll
%{_libdir}/wine/%{winepedirs}/wine-dxgi.dll
%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedirs}/dxgkrnl.sys
%{_libdir}/wine/%{winepedirs}/dxgmms1.sys
%endif
%{_libdir}/wine/%{winepedirs}/dxtrans.dll
%{_libdir}/wine/%{winepedirs}/dxva2.dll
%{_libdir}/wine/%{winepedirs}/esent.dll
%{_libdir}/wine/%{winepedirs}/evr.dll
%{_libdir}/wine/%{winepedirs}/explorerframe.dll
%{_libdir}/wine/%{winepedirs}/faultrep.dll
%{_libdir}/wine/%{winepedirs}/feclient.dll
%{_libdir}/wine/%{winepedirs}/fltlib.dll
%{_libdir}/wine/%{winepedirs}/fltmgr.sys
%{_libdir}/wine/%{winepedirs}/fntcache.dll
%{_libdir}/wine/%{winepedirs}/fontsub.dll
%{_libdir}/wine/%{winepedirs}/fusion.dll
%{_libdir}/wine/%{winepedirs}/fwpuclnt.dll
%{_libdir}/wine/%{winepedirs}/gameux.dll
%{_libdir}/wine/%{winepedirs}/gamingtcui.dll
%{_libdir}/wine/%{winepedirs}/gdi32.dll
%{_libdir}/wine/%{winepedirs}/gdiplus.dll
%{_libdir}/wine/%{winepedirs}/geolocation.dll
%{_libdir}/wine/%{winepedirs}/glu32.dll
%{_libdir}/wine/%{winepedirs}/gphoto2.ds
%{_libdir}/wine/%{winesodir}/gphoto2.so
%{_libdir}/wine/%{winepedirs}/gpkcsp.dll
%{_libdir}/wine/%{winepedirs}/graphicscapture.dll
%{_libdir}/wine/%{winepedirs}/hal.dll
%{_libdir}/wine/%{winepedirs}/hh.exe
%{_libdir}/wine/%{winepedirs}/hhctrl.ocx
%{_libdir}/wine/%{winepedirs}/hid.dll
%{_libdir}/wine/%{winepedirs}/hidclass.sys
%{_libdir}/wine/%{winepedirs}/hidparse.sys
%{_libdir}/wine/%{winepedirs}/hlink.dll
%{_libdir}/wine/%{winepedirs}/hnetcfg.dll
%{_libdir}/wine/%{winepedirs}/hrtfapo.dll
%{_libdir}/wine/%{winepedirs}/http.sys
%{_libdir}/wine/%{winepedirs}/httpapi.dll
%{_libdir}/wine/%{winepedirs}/hvsimanagementapi.dll
%{_libdir}/wine/%{winepedirs}/ia2comproxy.dll
%{_libdir}/wine/%{winepedirs}/icacls.exe
%{_libdir}/wine/%{winepedirs}/iccvid.dll
%{_libdir}/wine/%{winepedirs}/icinfo.exe
%{_libdir}/wine/%{winepedirs}/icmp.dll
%{_libdir}/wine/%{winepedirs}/icmui.dll
%{_libdir}/wine/%{winepedirs}/ieframe.dll
%{_libdir}/wine/%{winepedirs}/ieproxy.dll
%{_libdir}/wine/%{winepedirs}/iertutil.dll
%{_libdir}/wine/%{winepedirs}/imaadp32.acm
%{_libdir}/wine/%{winepedirs}/imagehlp.dll
%{_libdir}/wine/%{winepedirs}/imm32.dll
%{_libdir}/wine/%{winepedirs}/inetcomm.dll
%{_libdir}/wine/%{winepedirs}/inetcpl.cpl
%{_libdir}/wine/%{winepedirs}/inetmib1.dll
%{_libdir}/wine/%{winepedirs}/infosoft.dll
%{_libdir}/wine/%{winepedirs}/initpki.dll
%{_libdir}/wine/%{winepedirs}/inkobj.dll
%{_libdir}/wine/%{winepedirs}/inseng.dll
%{_libdir}/wine/%{winepedirs}/iphlpapi.dll
%{_libdir}/wine/%{winepedirs}/iprop.dll
%{_libdir}/wine/%{winepedirs}/irprops.cpl
%{_libdir}/wine/%{winepedirs}/ir50_32.dll
%{_libdir}/wine/%{winepedirs}/itircl.dll
%{_libdir}/wine/%{winepedirs}/itss.dll
%{_libdir}/wine/%{winepedirs}/joy.cpl
%{_libdir}/wine/%{winepedirs}/jscript.dll
%{_libdir}/wine/%{winepedirs}/jsproxy.dll
%{_libdir}/wine/%{winesodir}/kerberos.so
%{_libdir}/wine/%{winepedirs}/kerberos.dll
%{_libdir}/wine/%{winepedirs}/kernel32.dll
%{_libdir}/wine/%{winepedirs}/kernelbase.dll
%{_libdir}/wine/%{winepedirs}/ksecdd.sys
%{_libdir}/wine/%{winepedirs}/ksproxy.ax
%{_libdir}/wine/%{winepedirs}/ksuser.dll
%{_libdir}/wine/%{winepedirs}/ktmw32.dll
%{_libdir}/wine/%{winepedirs}/l3codeca.acm
%{_libdir}/wine/%{winepedirs}/l3codecx.ax
%{_libdir}/wine/%{winepedirs}/light.msstyles
%{_libdir}/wine/%{winepedirs}/loadperf.dll
%{_libdir}/wine/%{winesodir}/localspl.so
%{_libdir}/wine/%{winepedirs}/localspl.dll
%{_libdir}/wine/%{winepedirs}/localui.dll
%{_libdir}/wine/%{winepedirs}/lodctr.exe
%{_libdir}/wine/%{winepedirs}/lz32.dll
%{_libdir}/wine/%{winepedirs}/magnification.dll
%{_libdir}/wine/%{winepedirs}/mapi32.dll
%{_libdir}/wine/%{winepedirs}/mapistub.dll
%{_libdir}/wine/%{winepedirs}/mciavi32.dll
%{_libdir}/wine/%{winepedirs}/mcicda.dll
%{_libdir}/wine/%{winepedirs}/mciqtz32.dll
%{_libdir}/wine/%{winepedirs}/mciseq.dll
%{_libdir}/wine/%{winepedirs}/mciwave.dll
%{_libdir}/wine/%{winepedirs}/mf.dll
%{_libdir}/wine/%{winepedirs}/mf3216.dll
%{_libdir}/wine/%{winepedirs}/mfasfsrcsnk.dll
%{_libdir}/wine/%{winepedirs}/mferror.dll
%{_libdir}/wine/%{winepedirs}/mfh264enc.dll
%{_libdir}/wine/%{winepedirs}/mfmediaengine.dll
%{_libdir}/wine/%{winepedirs}/mfmp4srcsnk.dll
%{_libdir}/wine/%{winepedirs}/mfplat.dll
%{_libdir}/wine/%{winepedirs}/mfplay.dll
%{_libdir}/wine/%{winepedirs}/mfreadwrite.dll
%{_libdir}/wine/%{winepedirs}/mfsrcsnk.dll
%{_libdir}/wine/%{winepedirs}/mgmtapi.dll
%{_libdir}/wine/%{winepedirs}/midimap.dll
%{_libdir}/wine/%{winepedirs}/mlang.dll
%{_libdir}/wine/%{winepedirs}/mmcndmgr.dll
%{_libdir}/wine/%{winepedirs}/mmdevapi.dll
%{_libdir}/wine/%{winepedirs}/mofcomp.exe
%{_libdir}/wine/%{winepedirs}/mouhid.sys
%{_libdir}/wine/%{winesodir}/mountmgr.so
%{_libdir}/wine/%{winepedirs}/mountmgr.sys
%{_libdir}/wine/%{winepedirs}/mp3dmod.dll
%{_libdir}/wine/%{winepedirs}/mpr.dll
%{_libdir}/wine/%{winepedirs}/mprapi.dll
%{_libdir}/wine/%{winepedirs}/msacm32.dll
%{_libdir}/wine/%{winepedirs}/msacm32.drv
%{_libdir}/wine/%{winepedirs}/msado15.dll
%{_libdir}/wine/%{winepedirs}/msadp32.acm
%{_libdir}/wine/%{winepedirs}/msasn1.dll
%{_libdir}/wine/%{winepedirs}/msauddecmft.dll
%{_libdir}/wine/%{winepedirs}/mscat32.dll
%{_libdir}/wine/%{winepedirs}/mscoree.dll
%{_libdir}/wine/%{winepedirs}/mscorwks.dll
%{_libdir}/wine/%{winepedirs}/msctf.dll
%{_libdir}/wine/%{winepedirs}/msctfmonitor.dll
%{_libdir}/wine/%{winepedirs}/msctfp.dll
%{_libdir}/wine/%{winepedirs}/msdaps.dll
%{_libdir}/wine/%{winepedirs}/msdasql.dll
%{_libdir}/wine/%{winepedirs}/msdelta.dll
%{_libdir}/wine/%{winepedirs}/msdmo.dll
%{_libdir}/wine/%{winepedirs}/msdrm.dll
%{_libdir}/wine/%{winepedirs}/msftedit.dll
%{_libdir}/wine/%{winepedirs}/msg711.acm
%{_libdir}/wine/%{winepedirs}/msgsm32.acm
%{_libdir}/wine/%{winepedirs}/mshtml.dll
%{_libdir}/wine/%{winepedirs}/mshtml.tlb
%{_libdir}/wine/%{winepedirs}/msi.dll
%{_libdir}/wine/%{winepedirs}/msident.dll
%{_libdir}/wine/%{winepedirs}/msimtf.dll
%{_libdir}/wine/%{winepedirs}/msimg32.dll
%{_libdir}/wine/%{winepedirs}/msimsg.dll
%{_libdir}/wine/%{winepedirs}/msinfo32.exe
%{_libdir}/wine/%{winepedirs}/msisip.dll
%{_libdir}/wine/%{winepedirs}/msisys.ocx
%{_libdir}/wine/%{winepedirs}/msls31.dll
%{_libdir}/wine/%{winepedirs}/msmpeg2vdec.dll
%{_libdir}/wine/%{winepedirs}/msnet32.dll
%{_libdir}/wine/%{winepedirs}/mspatcha.dll
%{_libdir}/wine/%{winepedirs}/msports.dll
%{_libdir}/wine/%{winepedirs}/msscript.ocx
%{_libdir}/wine/%{winepedirs}/mssign32.dll
%{_libdir}/wine/%{winepedirs}/mssip32.dll
%{_libdir}/wine/%{winepedirs}/msrle32.dll
%{_libdir}/wine/%{winepedirs}/mstask.dll
%{_libdir}/wine/%{winepedirs}/msttsengine.dll
%{_libdir}/wine/%{winepedirs}/msv1_0.dll
%{_libdir}/wine/%{winesodir}/msv1_0.so
%{_libdir}/wine/%{winepedirs}/msvcirt.dll
%{_libdir}/wine/%{winepedirs}/msvcm80.dll
%{_libdir}/wine/%{winepedirs}/msvcm90.dll
%{_libdir}/wine/%{winepedirs}/msvcp_win.dll
%{_libdir}/wine/%{winepedirs}/msvcp60.dll
%{_libdir}/wine/%{winepedirs}/msvcp70.dll
%{_libdir}/wine/%{winepedirs}/msvcp71.dll
%{_libdir}/wine/%{winepedirs}/msvcp80.dll
%{_libdir}/wine/%{winepedirs}/msvcp90.dll
%{_libdir}/wine/%{winepedirs}/msvcp100.dll
%{_libdir}/wine/%{winepedirs}/msvcp110.dll
%{_libdir}/wine/%{winepedirs}/msvcp120.dll
%{_libdir}/wine/%{winepedirs}/msvcp120_app.dll
%{_libdir}/wine/%{winepedirs}/msvcp140.dll
%{_libdir}/wine/%{winepedirs}/msvcp140_1.dll
%{_libdir}/wine/%{winepedirs}/msvcp140_2.dll
%{_libdir}/wine/%{winepedirs}/msvcp140_atomic_wait.dll
%{_libdir}/wine/%{winepedirs}/msvcp140_codecvt_ids.dll
%{_libdir}/wine/%{winepedirs}/msvcr70.dll
%{_libdir}/wine/%{winepedirs}/msvcr71.dll
%{_libdir}/wine/%{winepedirs}/msvcr80.dll
%{_libdir}/wine/%{winepedirs}/msvcr90.dll
%{_libdir}/wine/%{winepedirs}/msvcr100.dll
%{_libdir}/wine/%{winepedirs}/msvcr110.dll
%{_libdir}/wine/%{winepedirs}/msvcr120.dll
%{_libdir}/wine/%{winepedirs}/msvcr120_app.dll
%{_libdir}/wine/%{winepedirs}/msvcrt.dll
%{_libdir}/wine/%{winepedirs}/msvcrt20.dll
%{_libdir}/wine/%{winepedirs}/msvcrt40.dll
%{_libdir}/wine/%{winepedirs}/msvcrtd.dll
%{_libdir}/wine/%{winepedirs}/msvfw32.dll
%{_libdir}/wine/%{winepedirs}/msvidc32.dll
%{_libdir}/wine/%{winepedirs}/msvproc.dll
%{_libdir}/wine/%{winepedirs}/mswsock.dll
%{_libdir}/wine/%{winepedirs}/msxml.dll
%{_libdir}/wine/%{winepedirs}/msxml2.dll
%{_libdir}/wine/%{winepedirs}/msxml3.dll
%{_libdir}/wine/%{winepedirs}/msxml4.dll
%{_libdir}/wine/%{winepedirs}/msxml6.dll
%{_libdir}/wine/%{winepedirs}/mtxdm.dll
%{_libdir}/wine/%{winepedirs}/nddeapi.dll
%{_libdir}/wine/%{winepedirs}/ncrypt.dll
%{_libdir}/wine/%{winepedirs}/ndis.sys
%{_libdir}/wine/%{winesodir}/netapi32.so
%{_libdir}/wine/%{winepedirs}/netapi32.dll
%{_libdir}/wine/%{winepedirs}/netcfgx.dll
%{_libdir}/wine/%{winepedirs}/netio.sys
%{_libdir}/wine/%{winepedirs}/netprofm.dll
%{_libdir}/wine/%{winepedirs}/netsh.exe
%{_libdir}/wine/%{winepedirs}/netutils.dll
%{_libdir}/wine/%{winepedirs}/newdev.dll
%{_libdir}/wine/%{winepedirs}/ninput.dll
%{_libdir}/wine/%{winepedirs}/normaliz.dll
%{_libdir}/wine/%{winepedirs}/npmshtml.dll
%{_libdir}/wine/%{winepedirs}/npptools.dll
%{_libdir}/wine/%{winepedirs}/nsi.dll
%{_libdir}/wine/%{winesodir}/nsiproxy.so
%{_libdir}/wine/%{winepedirs}/nsiproxy.sys
%{_libdir}/wine/%{winesodir}/ntdll.so
%{_libdir}/wine/%{winepedirs}/ntdll.dll
%{_libdir}/wine/%{winepedirs}/ntdsapi.dll
%{_libdir}/wine/%{winepedirs}/ntprint.dll
%if 0%{?wine_staging}
#%%{_libdir}/wine/%%{winepedirs}/nvcuda.dll
#%%{_libdir}/wine/%%{winesodir}/nvcuda.dll.so
#%%{_libdir}/wine/%%{winepedirs}/nvcuvid.dll
#%%{_libdir}/wine/%%{winesodir}/nvcuvid.dll.so
%endif
%{_libdir}/wine/%{winepedirs}/objsel.dll
%{_libdir}/wine/%{winesodir}/odbc32.so
%{_libdir}/wine/%{winepedirs}/odbc32.dll
%{_libdir}/wine/%{winepedirs}/odbcbcp.dll
%{_libdir}/wine/%{winepedirs}/odbccp32.dll
%{_libdir}/wine/%{winepedirs}/odbccu32.dll
%{_libdir}/wine/%{winepedirs}/ole32.dll
%{_libdir}/wine/%{winepedirs}/oleacc.dll
%{_libdir}/wine/%{winepedirs}/oleaut32.dll
%{_libdir}/wine/%{winepedirs}/olecli32.dll
%{_libdir}/wine/%{winepedirs}/oledb32.dll
%{_libdir}/wine/%{winepedirs}/oledlg.dll
%{_libdir}/wine/%{winepedirs}/olepro32.dll
%{_libdir}/wine/%{winepedirs}/olesvr32.dll
%{_libdir}/wine/%{winepedirs}/olethk32.dll
%{_libdir}/wine/%{winepedirs}/opcservices.dll
%{_libdir}/wine/%{winepedirs}/packager.dll
%{_libdir}/wine/%{winepedirs}/pdh.dll
%{_libdir}/wine/%{winepedirs}/photometadatahandler.dll
%{_libdir}/wine/%{winepedirs}/pidgen.dll
%{_libdir}/wine/%{winepedirs}/powrprof.dll
%{_libdir}/wine/%{winepedirs}/presentationfontcache.exe
%{_libdir}/wine/%{winepedirs}/printui.dll
%{_libdir}/wine/%{winepedirs}/prntvpt.dll
%{_libdir}/wine/%{winepedirs}/profapi.dll
%{_libdir}/wine/%{winepedirs}/propsys.dll
%{_libdir}/wine/%{winepedirs}/psapi.dll
%{_libdir}/wine/%{winepedirs}/pstorec.dll
%{_libdir}/wine/%{winepedirs}/pwrshplugin.dll
%{_libdir}/wine/%{winepedirs}/qasf.dll
%{_libdir}/wine/%{winepedirs}/qcap.dll
%{_libdir}/wine/%{winesodir}/qcap.so
%{_libdir}/wine/%{winepedirs}/qdvd.dll
%{_libdir}/wine/%{winepedirs}/qedit.dll
%{_libdir}/wine/%{winepedirs}/qmgr.dll
%{_libdir}/wine/%{winepedirs}/qmgrprxy.dll
%{_libdir}/wine/%{winepedirs}/quartz.dll
%{_libdir}/wine/%{winepedirs}/query.dll
%{_libdir}/wine/%{winepedirs}/qwave.dll
%{_libdir}/wine/%{winepedirs}/rasapi32.dll
%{_libdir}/wine/%{winepedirs}/rasdlg.dll
%{_libdir}/wine/%{winepedirs}/regapi.dll
%{_libdir}/wine/%{winepedirs}/regini.exe
%{_libdir}/wine/%{winepedirs}/resampledmo.dll
%{_libdir}/wine/%{winepedirs}/resutils.dll
%{_libdir}/wine/%{winepedirs}/riched20.dll
%{_libdir}/wine/%{winepedirs}/riched32.dll
%{_libdir}/wine/%{winepedirs}/robocopy.exe
%{_libdir}/wine/%{winepedirs}/rometadata.dll
%{_libdir}/wine/%{winepedirs}/rpcrt4.dll
%{_libdir}/wine/%{winepedirs}/rsabase.dll
%{_libdir}/wine/%{winepedirs}/rsaenh.dll
%{_libdir}/wine/%{winepedirs}/rstrtmgr.dll
%{_libdir}/wine/%{winepedirs}/rtutils.dll
%{_libdir}/wine/%{winepedirs}/rtworkq.dll
%{_libdir}/wine/%{winepedirs}/samlib.dll
%{_libdir}/wine/%{winepedirs}/sapi.dll
%{_libdir}/wine/%{winepedirs}/sas.dll
%{_libdir}/wine/%{winepedirs}/sc.exe
%{_libdir}/wine/%{winepedirs}/scarddlg.dll
%{_libdir}/wine/%{winepedirs}/scardsvr.dll
%{_libdir}/wine/%{winepedirs}/sccbase.dll
%{_libdir}/wine/%{winepedirs}/schannel.dll
%{_libdir}/wine/%{winepedirs}/scrobj.dll
%{_libdir}/wine/%{winepedirs}/scrrun.dll
%{_libdir}/wine/%{winepedirs}/scsiport.sys
%{_libdir}/wine/%{winepedirs}/sechost.dll
%{_libdir}/wine/%{winepedirs}/secur32.dll
%{_libdir}/wine/%{winesodir}/secur32.so
%{_libdir}/wine/%{winepedirs}/sensapi.dll
%{_libdir}/wine/%{winepedirs}/serialui.dll
%{_libdir}/wine/%{winepedirs}/setupapi.dll
%{_libdir}/wine/%{winepedirs}/sfc_os.dll
%{_libdir}/wine/%{winepedirs}/shcore.dll
%{_libdir}/wine/%{winepedirs}/shdoclc.dll
%{_libdir}/wine/%{winepedirs}/shdocvw.dll
%{_libdir}/wine/%{winepedirs}/schedsvc.dll
%{_libdir}/wine/%{winepedirs}/shell32.dll
%{_libdir}/wine/%{winepedirs}/shfolder.dll
%{_libdir}/wine/%{winepedirs}/shlwapi.dll
%{_libdir}/wine/%{winepedirs}/shutdown.exe
%{_libdir}/wine/%{winepedirs}/slbcsp.dll
%{_libdir}/wine/%{winepedirs}/slc.dll
%{_libdir}/wine/%{winepedirs}/snmpapi.dll
%{_libdir}/wine/%{winepedirs}/softpub.dll
%{_libdir}/wine/%{winepedirs}/sort.exe
%{_libdir}/wine/%{winepedirs}/spoolsv.exe
%{_libdir}/wine/%{winepedirs}/sppc.dll
%{_libdir}/wine/%{winepedirs}/srclient.dll
%{_libdir}/wine/%{winepedirs}/srvcli.dll
%{_libdir}/wine/%{winepedirs}/srvsvc.dll
%{_libdir}/wine/%{winepedirs}/sspicli.dll
%{_libdir}/wine/%{winepedirs}/stdole2.tlb
%{_libdir}/wine/%{winepedirs}/stdole32.tlb
%{_libdir}/wine/%{winepedirs}/sti.dll
%{_libdir}/wine/%{winepedirs}/strmdll.dll
%{_libdir}/wine/%{winepedirs}/subst.exe
%{_libdir}/wine/%{winepedirs}/svchost.exe
%{_libdir}/wine/%{winepedirs}/svrapi.dll
%{_libdir}/wine/%{winepedirs}/sxs.dll
%{_libdir}/wine/%{winepedirs}/systeminfo.exe
%{_libdir}/wine/%{winepedirs}/t2embed.dll
%{_libdir}/wine/%{winepedirs}/tapi32.dll
%{_libdir}/wine/%{winepedirs}/taskkill.exe
%{_libdir}/wine/%{winepedirs}/taskschd.dll
%{_libdir}/wine/%{winepedirs}/tbs.dll
%{_libdir}/wine/%{winepedirs}/tdh.dll
%{_libdir}/wine/%{winepedirs}/tdi.sys
%{_libdir}/wine/%{winepedirs}/threadpoolwinrt.dll
%{_libdir}/wine/%{winepedirs}/traffic.dll
%{_libdir}/wine/%{winepedirs}/twinapi.appcore.dll
%{_libdir}/wine/%{winepedirs}/tzres.dll
%{_libdir}/wine/%{winepedirs}/ucrtbase.dll
%{_libdir}/wine/%{winepedirs}/uianimation.dll
%{_libdir}/wine/%{winepedirs}/uiautomationcore.dll
%{_libdir}/wine/%{winepedirs}/uiribbon.dll
%{_libdir}/wine/%{winepedirs}/unicows.dll
%{_libdir}/wine/%{winepedirs}/unlodctr.exe
%{_libdir}/wine/%{winepedirs}/updspapi.dll
%{_libdir}/wine/%{winepedirs}/url.dll
%{_libdir}/wine/%{winepedirs}/urlmon.dll
%{_libdir}/wine/%{winepedirs}/usbd.sys
%{_libdir}/wine/%{winepedirs}/user32.dll
%{_libdir}/wine/%{winepedirs}/usp10.dll
%{_libdir}/wine/%{winepedirs}/utildll.dll
%{_libdir}/wine/%{winepedirs}/uxtheme.dll
%{_libdir}/wine/%{winepedirs}/userenv.dll
%{_libdir}/wine/%{winepedirs}/vbscript.dll
%{_libdir}/wine/%{winepedirs}/vcomp.dll
%{_libdir}/wine/%{winepedirs}/vcomp90.dll
%{_libdir}/wine/%{winepedirs}/vcomp100.dll
%{_libdir}/wine/%{winepedirs}/vcomp110.dll
%{_libdir}/wine/%{winepedirs}/vcomp120.dll
%{_libdir}/wine/%{winepedirs}/vcomp140.dll
%{_libdir}/wine/%{winepedirs}/vcruntime140.dll
%ifarch x86_64
%{_libdir}/wine/%{winepedirs}/vcruntime140_1.dll
%endif
%{_libdir}/wine/%{winepedirs}/vdmdbg.dll
%{_libdir}/wine/%{winepedirs}/version.dll
%{_libdir}/wine/%{winepedirs}/vga.dll
%{_libdir}/wine/%{winepedirs}/virtdisk.dll
%{_libdir}/wine/%{winepedirs}/vssapi.dll
%{_libdir}/wine/%{winepedirs}/vulkan-1.dll
%{_libdir}/wine/%{winepedirs}/wbemdisp.dll
%{_libdir}/wine/%{winepedirs}/wbemprox.dll
%{_libdir}/wine/%{winepedirs}/wdscore.dll
%{_libdir}/wine/%{winepedirs}/webservices.dll
%{_libdir}/wine/%{winepedirs}/websocket.dll
%{_libdir}/wine/%{winepedirs}/wer.dll
%{_libdir}/wine/%{winepedirs}/wevtapi.dll
%{_libdir}/wine/%{winepedirs}/wevtsvc.dll
%{_libdir}/wine/%{winepedirs}/wiaservc.dll
%{_libdir}/wine/%{winepedirs}/wimgapi.dll
%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedirs}/win32k.sys
%endif
%{_libdir}/wine/%{winepedirs}/win32u.dll
%{_libdir}/wine/%{winepedirs}/windows.applicationmodel.dll
%{_libdir}/wine/%{winepedirs}/windows.devices.bluetooth.dll
%{_libdir}/wine/%{winepedirs}/windows.devices.enumeration.dll
%{_libdir}/wine/%{winepedirs}/windows.devices.usb.dll
%{_libdir}/wine/%{winepedirs}/windows.gaming.ui.gamebar.dll
%{_libdir}/wine/%{winepedirs}/windows.gaming.input.dll
%{_libdir}/wine/%{winepedirs}/windows.globalization.dll
%{_libdir}/wine/%{winepedirs}/windows.media.dll
%{_libdir}/wine/%{winepedirs}/windows.media.devices.dll
%{_libdir}/wine/%{winepedirs}/windows.media.mediacontrol.dll
%{_libdir}/wine/%{winepedirs}/windows.media.speech.dll
%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedirs}/windows.networking.connectivity.dll
%endif
%{_libdir}/wine/%{winepedirs}/windows.networking.dll
%{_libdir}/wine/%{winepedirs}/windows.networking.hostname.dll
%{_libdir}/wine/%{winepedirs}/windows.perception.stub.dll
%{_libdir}/wine/%{winepedirs}/windows.security.authentication.onlineid.dll
%{_libdir}/wine/%{winepedirs}/windows.security.credentials.ui.userconsentverifier.dll
%{_libdir}/wine/%{winepedirs}/windows.storage.dll
%{_libdir}/wine/%{winepedirs}/windows.storage.applicationdata.dll
%{_libdir}/wine/%{winepedirs}/windows.system.profile.systemid.dll
%{_libdir}/wine/%{winepedirs}/windows.system.profile.systemmanufacturers.dll
%{_libdir}/wine/%{winepedirs}/windows.ui.dll
%{_libdir}/wine/%{winepedirs}/windows.ui.xaml.dll
%{_libdir}/wine/%{winepedirs}/windows.web.dll
%{_libdir}/wine/%{winepedirs}/windowscodecs.dll
%{_libdir}/wine/%{winepedirs}/windowscodecsext.dll
%{_libdir}/wine/%{winesodir}/wine
%{_libdir}/wine/%{winesodir}/wine-preloader
%{_libdir}/wine/%{winesodir}/winebth.so
%{_libdir}/wine/%{winepedirs}/winebth.sys
%{_libdir}/wine/%{winepedirs}/winebus.sys
%{_libdir}/wine/%{winepedirs}/winedmo.dll
%{_libdir}/wine/%{winesodir}/winedmo.so
%{_libdir}/wine/%{winesodir}/winegstreamer.so
%{_libdir}/wine/%{winepedirs}/winegstreamer.dll
%{_libdir}/wine/%{winepedirs}/winehid.sys
%{_libdir}/wine/%{winepedirs}/winemapi.dll
%{_libdir}/wine/%{winepedirs}/wineusb.sys
%{_libdir}/wine/%{winesodir}/wineusb.so
%{_libdir}/wine/%{winesodir}/winevulkan.so
%{_libdir}/wine/%{winepedirs}/winevulkan.dll
%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedirs}/winewayland.drv
%{_libdir}/wine/%{winesodir}/winewayland.so
%endif
%{_libdir}/wine/%{winepedirs}/winex11.drv
%{_libdir}/wine/%{winesodir}/winex11.so
%{_libdir}/wine/%{winepedirs}/wing32.dll
%{_libdir}/wine/%{winepedirs}/winhttp.dll
%{_libdir}/wine/%{winepedirs}/wininet.dll
%{_libdir}/wine/%{winepedirs}/winmm.dll
%{_libdir}/wine/%{winepedirs}/winnls32.dll
%{_libdir}/wine/%{winepedirs}/winprint.dll
%{_libdir}/wine/%{winepedirs}/winspool.drv
%{_libdir}/wine/%{winesodir}/winspool.so
%{_libdir}/wine/%{winepedirs}/winsta.dll
%{_libdir}/wine/%{winepedirs}/wintypes.dll
%{_libdir}/wine/%{winepedirs}/wldp.dll
%{_libdir}/wine/%{winepedirs}/wmadmod.dll
%{_libdir}/wine/%{winepedirs}/wmasf.dll
%{_libdir}/wine/%{winepedirs}/wmi.dll
%{_libdir}/wine/%{winepedirs}/wmic.exe
%{_libdir}/wine/%{winepedirs}/wmilib.sys
%{_libdir}/wine/%{winepedirs}/wmiutils.dll
%{_libdir}/wine/%{winepedirs}/wmp.dll
%{_libdir}/wine/%{winepedirs}/wmvcore.dll
%{_libdir}/wine/%{winepedirs}/wmvdecod.dll
%{_libdir}/wine/%{winepedirs}/spoolss.dll
%{_libdir}/wine/%{winesodir}/win32u.so
%{_libdir}/wine/%{winesodir}/winebus.so
%{_libdir}/wine/%{winepedirs}/winexinput.sys
%{_libdir}/wine/%{winepedirs}/wintab32.dll
%{_libdir}/wine/%{winepedirs}/wintrust.dll
%{_libdir}/wine/%{winepedirs}/winusb.dll
%{_libdir}/wine/%{winepedirs}/wlanapi.dll
%{_libdir}/wine/%{winepedirs}/wlanui.dll
%{_libdir}/wine/%{winepedirs}/wmphoto.dll
%{_libdir}/wine/%{winepedirs}/wnaspi32.dll
%{_libdir}/wine/%{winepedirs}/wofutil.dll
%ifarch x86_64 aarch64
%{_libdir}/wine/%{winepedirs}/wow64.dll
%{_libdir}/wine/%{winepedirs}/wow64win.dll
%endif
%ifarch x86_64
%{_libdir}/wine/%{winepedirs}/wow64cpu.dll
%endif
%{_libdir}/wine/%{winepedirs}/wpc.dll
%{_libdir}/wine/%{winepedirs}/wpcap.dll
%{_libdir}/wine/%{winesodir}/wpcap.so
%{_libdir}/wine/%{winepedirs}/ws2_32.dll
%{_libdir}/wine/%{winesodir}/ws2_32.so
%{_libdir}/wine/%{winepedirs}/wsdapi.dll
%{_libdir}/wine/%{winepedirs}/wshom.ocx
%{_libdir}/wine/%{winepedirs}/wsnmp32.dll
%{_libdir}/wine/%{winepedirs}/wsock32.dll
%{_libdir}/wine/%{winepedirs}/wtsapi32.dll
%{_libdir}/wine/%{winepedirs}/wuapi.dll
%{_libdir}/wine/%{winepedirs}/wuaueng.dll
%{_libdir}/wine/%{winepedirs}/wuauserv.exe
%{_libdir}/wine/%{winepedirs}/security.dll
%{_libdir}/wine/%{winepedirs}/sfc.dll
%{_libdir}/wine/%{winepedirs}/wineps.drv
%{_libdir}/wine/%{winesodir}/wineps.so
%ghost %{_libdir}/wine/%{winepedirs}/d3d8.dll
%{_libdir}/wine/%{winepedirs}/wine-d3d8.dll
%{_libdir}/wine/%{winepedirs}/d3d8thk.dll
%ghost %{_libdir}/wine/%{winepedirs}/d3d9.dll
%{_libdir}/wine/%{winepedirs}/wine-d3d9.dll
%{_libdir}/wine/%{winesodir}/opengl32.so
%{_libdir}/wine/%{winepedirs}/opengl32.dll
%{_libdir}/wine/%{winepedirs}/wined3d.dll
%{_libdir}/wine/%{winepedirs}/dnsapi.dll
%{_libdir}/wine/%{winesodir}/dnsapi.so
%{_libdir}/wine/%{winepedirs}/iexplore.exe
%{_libdir}/wine/%{winepedirs}/x3daudio1_0.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_1.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_2.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_3.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_4.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_5.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_6.dll
%{_libdir}/wine/%{winepedirs}/x3daudio1_7.dll
%{_libdir}/wine/%{winepedirs}/xactengine2_0.dll
%{_libdir}/wine/%{winepedirs}/xactengine2_4.dll
%{_libdir}/wine/%{winepedirs}/xactengine2_7.dll
%{_libdir}/wine/%{winepedirs}/xactengine2_9.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_0.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_1.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_2.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_3.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_4.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_5.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_6.dll
%{_libdir}/wine/%{winepedirs}/xactengine3_7.dll
%{_libdir}/wine/%{winepedirs}/xapofx1_1.dll
%{_libdir}/wine/%{winepedirs}/xapofx1_2.dll
%{_libdir}/wine/%{winepedirs}/xapofx1_3.dll
%{_libdir}/wine/%{winepedirs}/xapofx1_4.dll
%{_libdir}/wine/%{winepedirs}/xapofx1_5.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_0.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_1.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_2.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_3.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_4.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_5.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_6.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_7.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_8.dll
%{_libdir}/wine/%{winepedirs}/xaudio2_9.dll
%{_libdir}/wine/%{winepedirs}/xcopy.exe
%{_libdir}/wine/%{winepedirs}/xinput1_1.dll
%{_libdir}/wine/%{winepedirs}/xinput1_2.dll
%{_libdir}/wine/%{winepedirs}/xinput1_3.dll
%{_libdir}/wine/%{winepedirs}/xinput1_4.dll
%{_libdir}/wine/%{winepedirs}/xinput9_1_0.dll
%{_libdir}/wine/%{winepedirs}/xinputuap.dll
%{_libdir}/wine/%{winepedirs}/xmllite.dll
%{_libdir}/wine/%{winepedirs}/xolehlp.dll
%{_libdir}/wine/%{winepedirs}/xpsprint.dll
%{_libdir}/wine/%{winepedirs}/xpssvcs.dll

%if 0%{?wine_staging}
%ifarch x86_64 aarch64
#%%{_libdir}/wine/%%{winepedirs}/nvapi64.dll
#%%{_libdir}/wine/%%{winepedirs}/nvencodeapi64.dll
#%%{_libdir}/wine/%%{winesodir}/nvencodeapi64.dll.so
%else
#%%{_libdir}/wine/%%{winepedirs}/nvapi.dll
#%%{_libdir}/wine/%%{winepedirs}/nvencodeapi.dll
#%%{_libdir}/wine/%%{winesodir}/nvencodeapi.dll.so
%endif
%endif

# 16 bit and other non 64bit stuff
%ifnarch x86_64 aarch64
%{_libdir}/wine/%{winepedirs}/winevdm.exe
%{_libdir}/wine/%{winepedirs}/ifsmgr.vxd
%{_libdir}/wine/%{winepedirs}/mmdevldr.vxd
%{_libdir}/wine/%{winepedirs}/monodebg.vxd
%{_libdir}/wine/%{winepedirs}/rundll.exe16
%{_libdir}/wine/%{winepedirs}/vdhcp.vxd
%{_libdir}/wine/%{winepedirs}/user.exe16
%{_libdir}/wine/%{winepedirs}/vmm.vxd
%{_libdir}/wine/%{winepedirs}/vnbt.vxd
%{_libdir}/wine/%{winepedirs}/vnetbios.vxd
%{_libdir}/wine/%{winepedirs}/vtdapi.vxd
%{_libdir}/wine/%{winepedirs}/vwin32.vxd
%{_libdir}/wine/%{winepedirs}/w32skrnl.dll
%{_libdir}/wine/%{winepedirs}/avifile.dll16
%{_libdir}/wine/%{winepedirs}/comm.drv16
%{_libdir}/wine/%{winepedirs}/commdlg.dll16
%{_libdir}/wine/%{winepedirs}/compobj.dll16
%{_libdir}/wine/%{winepedirs}/ctl3d.dll16
%{_libdir}/wine/%{winepedirs}/ctl3dv2.dll16
%{_libdir}/wine/%{winepedirs}/ddeml.dll16
%{_libdir}/wine/%{winepedirs}/dispdib.dll16
%{_libdir}/wine/%{winepedirs}/display.drv16
%{_libdir}/wine/%{winepedirs}/gdi.exe16
%{_libdir}/wine/%{winepedirs}/imm.dll16
%{_libdir}/wine/%{winepedirs}/krnl386.exe16
%{_libdir}/wine/%{winepedirs}/keyboard.drv16
%{_libdir}/wine/%{winepedirs}/lzexpand.dll16
%{_libdir}/wine/%{winepedirs}/mmsystem.dll16
%{_libdir}/wine/%{winepedirs}/mouse.drv16
%{_libdir}/wine/%{winepedirs}/msacm.dll16
%{_libdir}/wine/%{winepedirs}/msvideo.dll16
%{_libdir}/wine/%{winepedirs}/ole2.dll16
%{_libdir}/wine/%{winepedirs}/ole2conv.dll16
%{_libdir}/wine/%{winepedirs}/ole2disp.dll16
%{_libdir}/wine/%{winepedirs}/ole2nls.dll16
%{_libdir}/wine/%{winepedirs}/ole2prox.dll16
%{_libdir}/wine/%{winepedirs}/ole2thk.dll16
%{_libdir}/wine/%{winepedirs}/olecli.dll16
%{_libdir}/wine/%{winepedirs}/olesvr.dll16
%{_libdir}/wine/%{winepedirs}/rasapi16.dll16
%{_libdir}/wine/%{winepedirs}/setupx.dll16
%{_libdir}/wine/%{winepedirs}/shell.dll16
%{_libdir}/wine/%{winepedirs}/sound.drv16
%{_libdir}/wine/%{winepedirs}/storage.dll16
%{_libdir}/wine/%{winepedirs}/stress.dll16
%{_libdir}/wine/%{winepedirs}/system.drv16
%{_libdir}/wine/%{winepedirs}/toolhelp.dll16
%{_libdir}/wine/%{winepedirs}/twain.dll16
%{_libdir}/wine/%{winepedirs}/typelib.dll16
%{_libdir}/wine/%{winepedirs}/ver.dll16
%{_libdir}/wine/%{winepedirs}/w32sys.dll16
%{_libdir}/wine/%{winepedirs}/win32s16.dll16
%{_libdir}/wine/%{winepedirs}/win87em.dll16
%{_libdir}/wine/%{winepedirs}/winaspi.dll16
%{_libdir}/wine/%{winepedirs}/windebug.dll16
%{_libdir}/wine/%{winepedirs}/wineps16.drv16
%{_libdir}/wine/%{winepedirs}/wing.dll16
%{_libdir}/wine/%{winepedirs}/winhelp.exe16
%{_libdir}/wine/%{winepedirs}/winnls.dll16
%{_libdir}/wine/%{winepedirs}/winoldap.mod16
%{_libdir}/wine/%{winepedirs}/winsock.dll16
%{_libdir}/wine/%{winepedirs}/wintab.dll16
%{_libdir}/wine/%{winepedirs}/wow32.dll
%endif
%if %[ "x86_64" == "%{_target_cpu}" && %{with new_wow64} ]
%{_libdir}/wine/i386-windows/winevdm.exe
%{_libdir}/wine/i386-windows/ifsmgr.vxd
%{_libdir}/wine/i386-windows/mmdevldr.vxd
%{_libdir}/wine/i386-windows/monodebg.vxd
%{_libdir}/wine/i386-windows/rundll.exe16
%{_libdir}/wine/i386-windows/vdhcp.vxd
%{_libdir}/wine/i386-windows/user.exe16
%{_libdir}/wine/i386-windows/vmm.vxd
%{_libdir}/wine/i386-windows/vnbt.vxd
%{_libdir}/wine/i386-windows/vnetbios.vxd
%{_libdir}/wine/i386-windows/vtdapi.vxd
%{_libdir}/wine/i386-windows/vwin32.vxd
%{_libdir}/wine/i386-windows/w32skrnl.dll
%{_libdir}/wine/i386-windows/avifile.dll16
%{_libdir}/wine/i386-windows/comm.drv16
%{_libdir}/wine/i386-windows/commdlg.dll16
%{_libdir}/wine/i386-windows/compobj.dll16
%{_libdir}/wine/i386-windows/ctl3d.dll16
%{_libdir}/wine/i386-windows/ctl3dv2.dll16
%{_libdir}/wine/i386-windows/ddeml.dll16
%{_libdir}/wine/i386-windows/dispdib.dll16
%{_libdir}/wine/i386-windows/display.drv16
%{_libdir}/wine/i386-windows/gdi.exe16
%{_libdir}/wine/i386-windows/imm.dll16
%{_libdir}/wine/i386-windows/krnl386.exe16
%{_libdir}/wine/i386-windows/keyboard.drv16
%{_libdir}/wine/i386-windows/lzexpand.dll16
%{_libdir}/wine/i386-windows/mmsystem.dll16
%{_libdir}/wine/i386-windows/mouse.drv16
%{_libdir}/wine/i386-windows/msacm.dll16
%{_libdir}/wine/i386-windows/msvideo.dll16
%{_libdir}/wine/i386-windows/ole2.dll16
%{_libdir}/wine/i386-windows/ole2conv.dll16
%{_libdir}/wine/i386-windows/ole2disp.dll16
%{_libdir}/wine/i386-windows/ole2nls.dll16
%{_libdir}/wine/i386-windows/ole2prox.dll16
%{_libdir}/wine/i386-windows/ole2thk.dll16
%{_libdir}/wine/i386-windows/olecli.dll16
%{_libdir}/wine/i386-windows/olesvr.dll16
%{_libdir}/wine/i386-windows/rasapi16.dll16
%{_libdir}/wine/i386-windows/setupx.dll16
%{_libdir}/wine/i386-windows/shell.dll16
%{_libdir}/wine/i386-windows/sound.drv16
%{_libdir}/wine/i386-windows/storage.dll16
%{_libdir}/wine/i386-windows/stress.dll16
%{_libdir}/wine/i386-windows/system.drv16
%{_libdir}/wine/i386-windows/toolhelp.dll16
%{_libdir}/wine/i386-windows/twain.dll16
%{_libdir}/wine/i386-windows/typelib.dll16
%{_libdir}/wine/i386-windows/ver.dll16
%{_libdir}/wine/i386-windows/w32sys.dll16
%{_libdir}/wine/i386-windows/win32s16.dll16
%{_libdir}/wine/i386-windows/win87em.dll16
%{_libdir}/wine/i386-windows/winaspi.dll16
%{_libdir}/wine/i386-windows/windebug.dll16
%{_libdir}/wine/i386-windows/wineps16.drv16
%{_libdir}/wine/i386-windows/wing.dll16
%{_libdir}/wine/i386-windows/winhelp.exe16
%{_libdir}/wine/i386-windows/winnls.dll16
%{_libdir}/wine/i386-windows/winoldap.mod16
%{_libdir}/wine/i386-windows/winsock.dll16
%{_libdir}/wine/i386-windows/wintab.dll16
%{_libdir}/wine/i386-windows/wow32.dll
%endif

%files filesystem
%license COPYING.LIB
%dir %{_datadir}/wine
%dir %{_datadir}/wine/gecko
%dir %{_datadir}/wine/mono
%dir %{_datadir}/wine/fonts
%{_datadir}/wine/wine.inf
%{_datadir}/wine/nls/

%files common
%{_bindir}/notepad
%{_bindir}/winedbg
%{_bindir}/winefile
%{_bindir}/winemine
%{_bindir}/winemaker
%{_bindir}/winepath
%{_bindir}/msiexec
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wineboot
%{_bindir}/wineconsole
%{_bindir}/winecfg
%{_mandir}/man1/wine.1*
%{_mandir}/man1/wineserver.1*
%{_mandir}/man1/msiexec.1*
%{_mandir}/man1/notepad.1*
%{_mandir}/man1/regedit.1*
%{_mandir}/man1/regsvr32.1*
%{_mandir}/man1/wineboot.1*
%{_mandir}/man1/winecfg.1*
%{_mandir}/man1/wineconsole.1*
%{_mandir}/man1/winefile.1*
%{_mandir}/man1/winemine.1*
%{_mandir}/man1/winepath.1*
%lang(de) %{_mandir}/de.UTF-8/man1/wine.1*
%lang(de) %{_mandir}/de.UTF-8/man1/wineserver.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/wine.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/wineserver.1*
%lang(pl) %{_mandir}/pl.UTF-8/man1/wine.1*

%files fonts
# meta package

%if 0%{?wine_staging}
%files arial-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/arial*
%endif
#0%%{?wine_staging}

%files courier-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/cou*

%files fixedsys-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/*vgafix.fon

%files system-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/cvgasys.fon
%{_datadir}/wine/fonts/hvgasys.fon
%{_datadir}/wine/fonts/jvgasys.fon
%{_datadir}/wine/fonts/svgasys.fon
%{_datadir}/wine/fonts/vgas1255.fon
%{_datadir}/wine/fonts/vgas1256.fon
%{_datadir}/wine/fonts/vgas1257.fon
%{_datadir}/wine/fonts/vgas874.fon
%{_datadir}/wine/fonts/vgasys.fon
%{_datadir}/wine/fonts/vgasyse.fon
%{_datadir}/wine/fonts/vgasysg.fon
%{_datadir}/wine/fonts/vgasysr.fon
%{_datadir}/wine/fonts/vgasyst.fon

%files small-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/sma*
%{_datadir}/wine/fonts/jsma*

%files marlett-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/marlett.ttf

%files ms-sans-serif-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/sse*
%if 0%{?wine_staging}
%{_datadir}/wine/fonts/msyh.ttf
%endif

%files tahoma-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/tahoma*ttf

%files tahoma-fonts-system
%doc README-tahoma
%{_datadir}/fonts/wine-tahoma-fonts
%{_fontconfig_confdir}/20-wine-tahoma*conf
%{_fontconfig_templatedir}/20-wine-tahoma*conf

%if 0%{?wine_staging}
%files times-new-roman-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/times.ttf

%files times-new-roman-fonts-system
%{_datadir}/fonts/wine-times-new-roman-fonts
%endif

%files symbol-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/symbol.ttf

%files webdings-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/webdings.ttf

%files wingdings-fonts
%license COPYING.LIB
%{_datadir}/wine/fonts/wingding.ttf

%files wingdings-fonts-system
%{_datadir}/fonts/wine-wingdings-fonts

%files desktop
%{_datadir}/applications/wine-notepad.desktop
%{_datadir}/applications/wine-winefile.desktop
%{_datadir}/applications/wine-winemine.desktop
%{_datadir}/applications/wine-mime-msi.desktop
%{_datadir}/applications/wine.desktop
%{_datadir}/applications/wine-regedit.desktop
%{_datadir}/applications/wine-uninstaller.desktop
%{_datadir}/applications/wine-winecfg.desktop
%{_datadir}/applications/wine-wineboot.desktop
%{_datadir}/applications/wine-winhelp.desktop
%{_datadir}/applications/wine-wordpad.desktop
%{_datadir}/applications/wine-oleview.desktop
%{_datadir}/desktop-directories/Wine.directory
%config %{_sysconfdir}/xdg/menus/applications-merged/wine.menu
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/*svg

%files systemd
%config %{_binfmtdir}/wine.conf

# ldap subpackage
%files ldap
%{_libdir}/wine/%{winepedirs}/wldap32.dll

# cms subpackage
%files cms
%{_libdir}/wine/%{winepedirs}/mscms.dll

# smartcard subpackage
%files smartcard
%{_libdir}/wine/%{winesodir}/winscard.so
%{_libdir}/wine/%{winepedirs}/winscard.dll

# twain subpackage
%files twain
%{_libdir}/wine/%{winepedirs}/twain_32.dll
%{_libdir}/wine/%{winepedirs}/sane.ds
%{_libdir}/wine/%{winesodir}/sane.so

%files devel
%{_bindir}/function_grep.pl
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/winedump
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
%{_mandir}/man1/widl.1*
%{_mandir}/man1/winebuild.1*
%{_mandir}/man1/winecpp.1*
%{_mandir}/man1/winedump.1*
%{_mandir}/man1/winegcc.1*
%{_mandir}/man1/winemaker.1*
%{_mandir}/man1/wmc.1*
%{_mandir}/man1/wrc.1*
%{_mandir}/man1/winedbg.1*
%{_mandir}/man1/wineg++.1*
%lang(de) %{_mandir}/de.UTF-8/man1/winemaker.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/winemaker.1*
%attr(0755, root, root) %dir %{_includedir}/wine
%{_includedir}/wine/*
%ifarch %{ix86} x86_64 aarch64
%{_libdir}/wine/%{winepedirs}/*.a
%endif
%ifarch %{ix86} x86_64
%{_libdir}/wine/%{winesodir}/*.a
%endif


%files pulseaudio
%{_libdir}/wine/%{winepedirs}/winepulse.drv
%{_libdir}/wine/%{winesodir}/winepulse.so

%files alsa
%{_libdir}/wine/%{winepedirs}/winealsa.drv
%{_libdir}/wine/%{winesodir}/winealsa.so

%if 0%{?opencl}
%files opencl
%{_libdir}/wine/%{winepedirs}/opencl.dll
%{_libdir}/wine/%{winesodir}/opencl.so
%endif

%changelog
* Mon Jul 07 2025 Michael Cronenworth <mike@cchtml.com> - 10.4-6
- Deprecate legacy wow32 and wow64 packages

* Wed Jun 25 2025 Teoh Han Hui <teohhanhui@gmail.com> - 10.4-5
- Add conditional build for new wow64 mode

* Tue Jun 24 2025 José Expósito <jexposit@redhat.com> - 10.4-4
- Use mesa-compat-libOSMesa on Fedora 42 and later

* Fri Apr 25 2025 Björn Esser <besser82@fedoraproject.org> - 10.4-3
- Use mesa-compat-libOSMesa on Fedora 43 and later
  Fixes: rhbz#2362160

* Tue Apr 01 2025 Michael Cronenworth <mike@cchtml.com> - 10.4-2
- Initial support for new Wow64 mode

* Sat Mar 22 2025 Michael Cronenworth <mike@cchtml.com> - 10.4-1
- version update

* Sat Mar 01 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 10.2-3
- Spec cleanups: drop EOL RHEL releases, arm32 support
- Use %%license fields, updates for some conditionals (mpg123, OpenCL)
- Force alternatives removal

* Tue Feb 25 2025 Michael Cronenworth <mike@cchtml.com> - 10.2-2
- Change x86_64 default alternatives from wine32 to wine64

* Mon Feb 24 2025 Michael Cronenworth <mike@cchtml.com> - 10.2-1
- version update

* Sun Feb 09 2025 Michael Cronenworth <mike@cchtml.com> - 10.1-1
- version update

* Wed Jan 22 2025 Michael Cronenworth <mike@cchtml.com> - 10.0-1
- version update

* Sun Jan 19 2025 Michael Cronenworth <mike@cchtml.com> - 10.0-0.8rc6
- version update

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-0.8rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Michael Cronenworth <mike@cchtml.com> - 10.0-0.7rc4
- version update

* Fri Dec 27 2024 Zephyr Lykos <fedora@mochaa.ws> - 10.0-0.6rc3
- Fix wine-mono not loading iconv.dll from mingw bindir

* Thu Dec 26 2024 Michael Cronenworth <mike@cchtml.com> - 10.0-0.5rc3
- version update

* Mon Dec 16 2024 Michael Cronenworth <mike@cchtml.com> - 10.0-0.4rc2
- version update

* Tue Dec 10 2024 Michael Cronenworth <mike@cchtml.com> - 10.0-0.3rc1
- Handle upgrades to convert d3d8.dll to alternatives take 2

* Sun Dec 08 2024 Michael Cronenworth <mike@cchtml.com> - 10.0-0.2rc1
- Handle upgrades to convert d3d8.dll to alternatives

* Fri Dec 06 2024 Michael Cronenworth <mike@cchtml.com> - 10.0-0.1rc1
- version update

* Mon Nov 25 2024 Zephyr Lykos <fedora@mochaa.ws> - 9.22-1
- new version

* Tue Nov 12 2024 Zephyr Lykos <fedora@mochaa.ws> - 9.21-1
- version update

* Fri Sep 27 2024 Zephyr Lykos <fedora@mochaa.ws> - 9.18-2
- Pick https://gitlab.winehq.org/wine/wine/-/merge_requests/6547

* Sun Sep 22 2024 Zephyr Lykos <fedora@mochaa.ws> - 9.18-1
- version update

* Sat Sep 07 2024 Zephyr Lykos <fedora@mochaa.ws> - 9.15-2
- Adapt alternatives setup to DXVK 2.0

* Tue Aug 13 2024 Michael Cronenworth <mike@cchtml.com> - 9.15-1
- version update

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Michael Cronenworth <mike@cchtml.com> - 9.5-1
- version update

* Mon Jan 29 2024 Michael Cronenworth <mike@cchtml.com> - 9.1-1
- version update

* Thu Jan 25 2024 Michael Cronenworth <mike@cchtml.com> - 9.0-3
- Revert smartcard subpackage (RHBZ#2259936)

* Fri Jan 19 2024 Michael Cronenworth <mike@cchtml.com> - 9.0-2
- Add smartcard subpackage (RHBZ#2259198)

* Tue Jan 16 2024 Michael Cronenworth <mike@cchtml.com> - 9.0-1
- version update

* Mon Oct 30 2023 Michael Cronenworth <mike@cchtml.com> - 8.19-1
- version update

* Sun Oct 15 2023 Michael Cronenworth <mike@cchtml.com> - 8.18-1
- version update

* Sun Oct 01 2023 Michael Cronenworth <mike@cchtml.com> - 8.17-1
- version update

* Tue Aug 22 2023 Michael Cronenworth <mike@cchtml.com> - 8.14-1
- version update

* Thu Aug 17 2023 Michael Cronenworth <mike@cchtml.com> - 8.13-1
- version update

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Michael Cronenworth <mike@cchtml.com> - 8.12-1
- version update

* Sun Jun 25 2023 Michael Cronenworth <mike@cchtml.com> - 8.11-1
- version update

* Wed Apr 19 2023 Michael Cronenworth <mike@cchtml.com> - 8.6-1
- version update

* Sat Apr 01 2023 Michael Cronenworth <mike@cchtml.com> - 8.5-1
- version update

* Tue Mar 21 2023 Michael Cronenworth <mike@cchtml.com> - 8.4-1
- version update

* Wed Feb 22 2023 Michael Cronenworth <mike@cchtml.com> - 8.2-3
- fix missing requires for win-iconv

* Tue Feb 21 2023 Michael Cronenworth <mike@cchtml.com> - 8.2-2
- fix missing requires for libjpeg and libtiff

* Mon Feb 20 2023 Michael Cronenworth <mike@cchtml.com> - 8.2-1
- version update

* Mon Feb 06 2023 Michael Cronenworth <mike@cchtml.com> - 8.1-1
- version update

* Tue Jan 24 2023 Michael Cronenworth <mike@cchtml.com> - 8.0-1
- version update

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-0.rc4.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Michael Cronenworth <mike@cchtml.com> - 8.0-0.rc4.1
- version update

* Mon Nov 28 2022 Michael Cronenworth <mike@cchtml.com> - 7.22-2
- fix typo in openal obsoletes

* Sun Nov 27 2022 Michael Cronenworth <mike@cchtml.com> - 7.22-1
- version update
- drop openal package

* Mon Oct 31 2022 Michael Cronenworth <mike@cchtml.com> - 7.20-1
- version update

* Mon Oct 24 2022 Michael Cronenworth <mike@cchtml.com> - 7.19-1
- version update

* Thu Oct 13 2022 Michael Cronenworth <mike@cchtml.com> - 7.18-2
- Require MinGW FAudio

* Tue Oct 11 2022 Michael Cronenworth <mike@cchtml.com> - 7.18-1
- version update
- Drop isdn4k-utils from Recommends

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Michael Cronenworth <mike@cchtml.com> - 7.12-2
- Requires on vkd3d

* Tue Jul 05 2022 Michael Cronenworth <mike@cchtml.com> - 7.12-1
- versuon update
- Unbundle vkd3d

* Wed Jun 22 2022 Michael Cronenworth <mike@cchtml.com> - 7.11-1
- version update

* Mon Jun 06 2022 Michael Cronenworth <mike@cchtml.com> - 7.10-2
- Require new Mono

* Mon Jun 06 2022 Michael Cronenworth <mike@cchtml.com> - 7.10-1
- version update

* Mon May 23 2022 Michael Cronenworth <mike@cchtml.com> - 7.9-1
- version update

* Tue Mar 29 2022 Michael Cronenworth <mike@cchtml.com> - 7.5-1
- version update
- drop 32-bit ARM
- require on Fedora MinGW dependencies

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 7.3-2
- Rebuild with mingw-gcc-12

* Fri Mar 11 2022 Michael Cronenworth <mike@cchtml.com> - 7.3-1
- version update

* Sun Feb 13 2022 Björn Esser <besser82@fedoraproject.org> - 7.2-1
- version update

* Mon Jan 31 2022 Björn Esser <besser82@fedoraproject.org> - 7.1-2
- Revert to wine-mono 7.0.0

* Sat Jan 29 2022 Björn Esser <besser82@fedoraproject.org> - 7.1-1
- version update

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Björn Esser <besser82@fedoraproject.org> - 7.0-1
- version update

* Sat Jan 15 2022 Björn Esser <besser82@fedoraproject.org> - 7.0-0.6rc6
- version update

* Sun Jan 09 2022 Björn Esser <besser82@fedoraproject.org> - 7.0-0.5rc5
- version update

* Mon Jan 03 2022 Michael Cronenworth <mike@cchtml.com> 7.0-0.4rc4
- version update

* Mon Jan 03 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> 7.0-0.3rc3
- Silence messages from expected failures during rpm scriptlets

* Mon Dec 27 2021 Björn Esser <besser82@fedoraproject.org> - 7.0-0.2rc3
- version update

* Mon Dec 20 2021 Michael Cronenworth <mike@cchtml.com> 7.0-0.1rc2
- version update

* Wed Nov 10 2021 Michael Cronenworth <mike@cchtml.com> 6.21-1
- version update

* Mon Oct 04 2021 Michael Cronenworth <mike@cchtml.com> 6.18-1
- version update

* Mon Aug 30 2021 Michael Cronenworth <mike@cchtml.com> 6.16-1
- version update

* Wed Jul 07 2021 Michael Cronenworth <mike@cchtml.com> 6.12-1
- version update

* Sat Jun 19 2021 Michael Cronenworth <mike@cchtml.com> 6.11-1
- version update

* Mon Jun 07 2021 Michael Cronenworth <mike@cchtml.com> 6.10-1
- version update

* Mon May 24 2021 Michael Cronenworth <mike@cchtml.com> 6.9-1
- version update

* Sat May 08 2021 Michael Cronenworth <mike@cchtml.com> 6.8-1
- version update

* Sat Apr 24 2021 Michael Cronenworth <mike@cchtml.com> 6.7-1
- version update

* Sun Apr 11 2021 Michael Cronenworth <mike@cchtml.com> 6.6-1
- version update

* Mon Mar 15 2021 Michael Cronenworth <mike@cchtml.com> 6.4-1
- version update

* Sat Feb 27 2021 Michael Cronenworth <mike@cchtml.com> 6.3-1
- version update

* Sat Feb 13 2021 Michael Cronenworth <mike@cchtml.com> 6.2-1
- version update

* Mon Feb 01 2021 Michael Cronenworth <mike@cchtml.com> 6.1-1
- version update

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Michael Cronenworth <mike@cchtml.com> 6.0-1
- version update

* Sun Jan 10 2021 Michael Cronenworth <mike@cchtml.com> 6.0-0.6rc6
- version update

* Thu Jan 07 2021 Michael Cronenworth <mike@cchtml.com> 6.0-0.5rc5
- version update

* Sat Dec 26 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.4rc4
- version update

* Sat Dec 19 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.3rc3
- version update

* Sat Dec 12 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.2rc2
- version update

* Tue Dec 08 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.1rc1
- version update

