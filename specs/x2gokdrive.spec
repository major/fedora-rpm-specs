Name:           x2gokdrive
Version:        0.0.0.3
Release:        3%{?dist}
Summary:        KDrive graphical server backend for X2GoServer

# Per debian/copyright, only the testscripts folder is GPLv2
License:        GPL-3.0-or-later

URL:            https://www.x2go.org
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
# Upstream copyright file
# https://code.x2go.org/gitweb?p=x2gokdrive.git;a=blob_plain;f=debian/copyright;h=88c3411550b8f79d29f1b9a7a3c20996126375db;hb=HEAD
Source1:        copyright
Source2:        xorg.conf
ExcludeArch:    %{ix86}

# Required specifically for x2gokdrive
BuildRequires:  xorg-x11-server-source
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  libpng-devel
BuildRequires:  quilt

# XCB bits for Xephyr
# Copied/synced with debian/control.
BuildRequires:  pkgconfig(xcb) >= 1
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-xf86dri)

# Dependencies for xorg-x11-server.
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  font-util
BuildRequires:  imake
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xcmiscproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(bigreqsproto)
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pam-devel
# We probably won't need some libudev-devel equivalent because we disable that
# feature anyway.
# Same goes for pkgconfig(libselinux).
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(auparse)
# Same goes for pkgconfig(libdrm).
BuildRequires:  pkgconfig(dri)
%if 0%{?el8}
BuildRequires:  pkgconfig(fontutil)
%endif
BuildRequires:  pkgconfig(gl)
# No libunwind on RHEL8 s390x
%if !(0%{?el8} && "%{_arch}" == "s390x")
BuildRequires:  pkgconfig(libunwind)
%endif
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xinerama)
# RPM-specific... probably?
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xshmfence)
#For tests
BuildRequires:  xauth
BuildRequires:  xkbcomp
BuildRequires:  Xvfb
BuildRequires:  x2gokdriveclient

%description
X2Go is a server based computing environment with
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client-side mass storage mounting support
   - client-side printing support
   - audio support
   - authentication by smartcard and USB stick

X2Go KDrive is a KDrive-based Xserver for X2Go. It provides support for
running modern desktop environments like GNOME, KDE Plasma, Cinnamon, etc.
in X2Go Sessions.

The X2Go KDrive graphical backend is not suitable for low bandwidth WAN
connections between X2Go Client and X2Go Server. It is supposed for X2Go
being used on the local area network.

More information about X.Org can be found at:
<URL:https://www.x.org>

More information about X2Go can be found at:
<URL:https://wiki.x2go.org>


%package -n xorg-x11-server-x2gokdrive
Summary:        KDrive graphical server backend for X2GoServer
Requires:       xorg-x11-server-common >= 1.18.4
%if 0%{?fedora} || 0%{?rhel} > 8
Recommends:     mesa-dri-drivers
Recommends:     x2goserver >= 4.1.0.4
%else
Requires:       mesa-dri-drivers
Requires:       x2goserver >= 4.1.0.4
%endif

%description -n xorg-x11-server-x2gokdrive
X2Go is a server based computing environment with
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client-side mass storage mounting support
   - client-side printing support
   - audio support
   - authentication by smartcard and USB stick

This package is built from the X.org xserver module. X2Go KDrive is a
KDrive-based Xserver for X2Go. It provides support for running modern
desktop environments like GNOME, KDE Plasma, Cinnamon, etc. in X2Go
Sessions.

The X2Go KDrive graphical backend is not suitable for low bandwidth WAN
connections between X2Go Client and X2Go Server. It is supposed for X2Go
being used on the local area network.

More information about X.Org can be found at:
<URL:https://www.x.org>

More information about X2Go can be found at:
<URL:https://wiki.x2go.org>


%prep
%autosetup
cp -a %SOURCE1 .

# prepare xorg-server build tree
mkdir -p 'BUILD'
cp -av '/usr/share/xorg-x11-server-source/'* 'BUILD/'
# Precaution from:
# https://src.fedoraproject.org/rpms/tigervnc/blob/master/f/tigervnc.spec
find 'BUILD/' -type 'f' -perm '-001' -print0 | while read -r -d '' file; do
  chmod -x "${file}"
done
mkdir -p 'BUILD/hw/kdrive/x2gokdrive/'

# inject x2gokdrive into xorg-server build tree
cp 'Makefile.am' *'.c' *'.h' 'BUILD/hw/kdrive/x2gokdrive/'
cp -r 'man/' 'BUILD/hw/kdrive/x2gokdrive/'

# patch xorg-server build tree, so that it will build x2gokdrive
export XORG_UPSTREAM_VERSION="$(grep 'AC_INIT' 'BUILD/configure.ac' | sed -r 's/^AC_INIT[^,]*, ([^,]+),.*/\1/')"
# Just use the latest version present
[ ! -d "patches.xorg/${XORG_UPSTREAM_VERSION}" ] && cp -a patches.xorg/1.20.13 patches.xorg/${XORG_UPSTREAM_VERSION}
pushd 'BUILD'
QUILT_PATCHES="../patches.xorg/${XORG_UPSTREAM_VERSION}/" quilt push -a
if [ -d "../patches.xorg/${XORG_UPSTREAM_VERSION}/missing" ]; then
  # Hack used to install missing files.
  # This is actually working around problems in the upstream
  # xorg-server-source packages, which will have to be reported upstream.
  cp -av "../patches.xorg/${XORG_UPSTREAM_VERSION}/missing/"* 'BUILD/'
fi

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$CFLAGS"

pushd 'BUILD'
# Clean up old configure files that might have had the executable bit set.
# Will be regenerated later on.
rm -f 'configure' 'config.'{sub,guess} 'depcomp' 'install-sh' 'compile' 'ltmain.sh' 'missing' 'ylwrap'
autoreconf -fvi
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
# disable-static is so we don't get libfoo.a for modules.  now if only we could
# kill the .las.
%configure \
        --libexecdir='%{_prefix}/lib/xorg' \
        --with-module-dir='%{_prefix}/lib/xorg/modules' \
        --with-serverconfig-path='%{_libexecdir}' \
        --disable-silent-rules \
        --disable-static \
        --disable-devel-docs \
        --disable-docs \
        --without-dtrace \
        --disable-strict-compilation \
        --disable-debug \
        --with-int10=x86emu \
        --with-vendor-name="Fedora Project" \
        --with-builderstring="%{name} %{version} (https://wiki.x2go.org)" \
        --with-xkb-path=%{_datadir}/X11/xkb \
        --with-xkb-output=%{_localstatedir}/lib/xkb \
        --with-shared-memory-dir=/dev/shm \
        --enable-mitshm \
        --enable-xres \
        --disable-xcsecurity \
        --disable-tslib \
        --enable-dbe \
        --disable-xf86bigfont \
        --enable-dpms \
        --disable-xorg \
        --disable-linux-acpi \
        --disable-linux-apm \
        --disable-xquartz \
        --disable-xwin \
        --disable-xnest \
        --disable-xfake \
        --disable-xfbdev \
        --disable-install-setuid \
        --disable-xshmfence \
        --disable-config-hal \
        --disable-config-udev \
        --with-default-font-path="catalogue:%{_sysconfdir}/X11/fontpath.d,built-ins" \
        --enable-composite \
        --enable-record \
        --enable-xv \
        --disable-xvmc \
        --disable-dga \
        --enable-screensaver \
        --disable-xdmcp \
        --disable-xdm-auth-1 \
        --enable-glx \
        --enable-present \
        --enable-xinerama \
        --enable-xf86vidmode \
        --enable-xace \
        --disable-xfree86-utils \
        --disable-suid-wrapper \
        --disable-dmx \
        --disable-xvfb \
        --enable-kdrive \
        --enable-x2gokdrive \
        --disable-xephyr \
        --disable-xwayland \
        --with-sha1=libgcrypt \
        --enable-xcsecurity \
        --disable-dri3 \
        --disable-xselinux \
        --disable-systemd-logind \
        --without-systemd-daemon \
        --disable-dri \
        --disable-dri2 \
        --disable-glamor \
%if !(0%{?el8} && "%{_arch}" == "s390x")
        --enable-libunwind \
%else
        --disable-libunwind \
%endif
        --disable-libdrm \
        --enable-unit-tests \
        CPPFLAGS="${CPPFLAGS} %{?__global_cppflags} -DPRE_RELEASE=0" \
        LDFLAGS='%{__global_ldflags}'
%make_build
popd


%install
pushd 'BUILD'
%make_install
popd


%check
# This doesn't really seem to work - maybe someday upstream will have a better test
export PATH=%{buildroot}%{_bindir}:$PATH
export QT_DEBUG_PLUGINS=1
xvfb-run -f ~/.Xauthority testscripts/run-x2gokdriveclient-to-x2gokdrive-on-localhost
sleep 5
cat $HOME/.x2go/S-9/session
cat $HOME/.x2go/C-9/session
# kill any remaining processes
for pid in $HOME/.x2go/[CS]-9/pid
do
  [ -f $pid ] && kill $(cat $pid)
done
exit 0


%files -n xorg-x11-server-x2gokdrive
%license copyright
%{_bindir}/x2gokdrive
# Exclude protocol.txt, it's shipped by xorg-x11-server(-common) and we don't
# want to conflict with that package.
%exclude %{_libexecdir}/protocol.txt
%exclude %{_mandir}/man1/Xserver.1.gz
%exclude %{_var}/lib/xkb/
%doc %{_mandir}/man1/x2gokdrive.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Orion Poplawski <orion@nwra.com> - 0.0.0.3-1
- Update to 0.0.0.3

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Orion Poplawski <orion@nwra.com> - 0.0.0.2-2
- Fix License tag and add upstream copyright file
- Add %%check

* Mon Sep 25 2023 Orion Poplawski <orion@nwra.com> - 0.0.0.2-1
- Update to 0.0.0.2

* Thu Jun 15 2023 Orion Poplawski <orion@nwra.com> - 0.0.0.1-1
- Initial Fedora package
