%global _hardened_build 1
%ifarch ppc64le
%if 0%{?el7}
# Works around https://bugs.centos.org/view.php?id=13779 / https://bugzilla.redhat.com/show_bug.cgi?id=1489712
# Compilation failure on PPC64LE due to a compiler bug.
# REMEMBER TO REMOVE ONCE DOWNSTREAM FIXES THE ISSUE!
%global __global_cflags %{__global_cflags} -mno-vsx
%global __global_cxxflags %{__global_cxxflags} -mno-vsx
%endif
%endif

Name:           nx-libs
Version:        3.5.99.27
Release:        7%{?dist}
Summary:        NX X11 protocol compression libraries

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/ArcticaProject/nx-libs
Source0:        https://github.com/ArcticaProject/nx-libs/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  expat-devel
BuildRequires:  imake
BuildRequires:  make
BuildRequires:  quilt
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXfixes-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  libXfont2-devel
%else
BuildRequires:  libXfont-devel
%endif
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  pixman-devel
%if 0%{?fedora}
BuildRequires:  xkbcomp-devel
%else
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  xorg-x11-xkb-utils-devel
%endif
%endif
# For imake
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
%else
BuildRequires:  python-rpm-macros
%endif
%if !(0%{?fedora} >= 38 || 0%{?rhel} >= 8)
BuildRequires:  /usr/bin/pathfix.py
%endif

ExcludeArch:    %{ix86}

Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Provides:       nx%{?_isa} = %{version}-%{release}
Obsoletes:      libNX_Xau < 3.5.99.1
Obsoletes:      libNX_Xcomposite < 3.5.99.1
Obsoletes:      libNX_Xdamage < 3.5.99.1
Obsoletes:      libNX_Xdmcp < 3.5.99.1
Obsoletes:      libNX_Xext < 3.5.99.1
Obsoletes:      libNX_Xfixes < 3.5.99.1
Obsoletes:      libNX_Xinerama < 3.5.99.1
Obsoletes:      libNX_Xpm < 3.5.99.1
Obsoletes:      libNX_Xrandr < 3.5.99.1
Obsoletes:      libNX_Xrender < 3.5.99.1
Obsoletes:      libNX_Xtst < 3.5.99.1
Obsoletes:      libXcompext < 3.5.99.3

%description
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.


%package -n libNX_X11
Summary:        Core NX protocol client library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n libNX_X11
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.


%package -n libNX_X11-devel
Summary:        Development files for the Core NX protocol library
Requires:       libNX_X11%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}

%description -n libNX_X11-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

This package contains all necessary include files and libraries
needed to develop applications that require these.


%package -n libXcomp-devel
Summary:        Development files for the NX differential compression library
Requires:       libXcomp%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel = %{version}-%{release}
Obsoletes:      libXcompext-devel < 3.5.99.3

%description -n libXcomp-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX differential compression library's development files.


%package -n libXcomp
Summary:        NX differential compression library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n libXcomp
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains the NX differential compression library for X11.


%package -n libXcompshad-devel
Summary:        Development files for the NX session shadowing library
Requires:       libXcompshad%{?_isa} = %{version}-%{release}
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n libXcompshad-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX session shadowing library's development files.


%package -n libXcompshad
Summary:        NX session shadowing Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n libXcompshad
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package provides the session shadowing library.


%package devel
Summary:        Include files and libraries for NX development
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      libNX_Xau-devel < 3.5.99.1
Obsoletes:      libNX_Xdmcp-devel < 3.5.0.32-2
Obsoletes:      libNX_Xext-devel < 3.5.99.1
Obsoletes:      libNX_Xfixes-devel < 3.5.99.1
Obsoletes:      libNX_Xpm-devel < 3.5.0.32-2
Obsoletes:      libNX_Xrender-devel < 3.5.99.1

%description devel
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains all necessary include files and libraries
needed to develop nx-X11 applications that require these.


%package -n nx-proto-devel
Summary:        Include files for NX development

%description -n nx-proto-devel
This package contains all necessary include files and libraries
for the nx_X11 wire protocol.


%package -n nxagent
Summary:        NX Agent
# For /usr/share/X11/xkb
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     xkeyboard-config
%else
Requires:       xkeyboard-config
%endif
# For /usr/share/X11/fonts
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} <= 8 )
Requires:       xorg-x11-font-utils
%endif
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Provides:       nx%{?_isa} = %{version}-%{release}
Obsoletes:      nxauth < 3.5.99.1

%description -n nxagent
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

nxagent is an agent providing NX transport of X sessions. The
application is based on the well-known Xnest server. nxagent, like
Xnest, is an X server for its own clients, and at the same time, an X
client for a system's local X server.

The main scope of nxagent is to eliminate X round-trips or transform
them into asynchronous replies. nxagent works together with nxproxy.
nxproxy itself does not make any effort to minimize round-trips by
itself, this is demanded of nxagent.

Being an X server, nxagent is able to resolve all the property/atoms
related requests locally, ensuring that the most common source of
round-trips are nearly reduced to zero.


%package -n nxproxy
Summary:        NX Proxy
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Provides:       nx%{?_isa} = %{version}-%{release}

%description -n nxproxy
This package provides the NX proxy (client) binary.


%package -n nxdialog
Summary:        NX Dialog

%description -n nxdialog
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
pplications over a network, especially a slow one.

This package provides the nxdialog helper script.


%prep
%autosetup -p1
# Install into /usr
sed -i -e 's,/usr/local,/usr,' nx-X11/config/cf/site.def
# Fix FSF address
find -name LICENSE | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'
# Fix source permissions
find -type f -name '*.[hc]' | xargs chmod -x

# Bundled nx-X11/extras
# Mesa - Used by the X server
# Xcursor - Other code still references files in it


%build
cat >"my_configure" <<'EOF'
%configure --disable-silent-rules "${@}"
EOF
chmod a+x my_configure;
# _hardened_build not working for EL6, at least define __global_ldflags for now
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro -Wl,-z,now}
export SHLIBGLOBALSFLAGS="%{__global_ldflags}"
export LOCAL_LDFLAGS="%{__global_ldflags}"
export CDEBUGFLAGS="%{optflags}"
IMAKE_DEFINES="-DUseTIRPC=YES"
# parallel make failed
make VERBOSE=1 CONFIGURE="$PWD/my_configure" LIBDIR=%{_libdir} CDEBUGFLAGS="${CDEBUGFLAGS}" LOCAL_LDFLAGS="${LOCAL_LDFLAGS}" SHLIBGLOBALSFLAGS="${SHLIBGLOBALSFLAGS}" IMAKE_DEFINES="${IMAKE_DEFINES}"


%install
%make_install \
        PREFIX=%{_prefix} \
        LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} \
        INSTALL_DIR="install -dm0755" \
        INSTALL_FILE="install -pm0644" \
        INSTALL_PROGRAM="install -pm0755"

ln -s ../X11/fonts %{buildroot}%{_datadir}/nx/fonts

# Remove static libs
rm %{buildroot}%{_libdir}/*.a

# Fix permissions on shared libraries
chmod 755  %{buildroot}%{_libdir}/lib*.so*

# Remove extras, GL, and other unneeded headers
rm -r %{buildroot}%{_includedir}/GL
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XK*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/*Xv*.h
rm -r %{buildroot}%{_includedir}/nx-X11/Xtrans

#Remove our shared libraries' .la files before wrapping up the packages
rm %{buildroot}%{_libdir}/*.la

# Fix python scripts
%if 0%{?fedora} || 0%{?rhel} >= 8
%py3_shebang_fix %{buildroot}%{_bindir}/nxdialog
%else
pathfix.py -pni "%{__python2} %{py2_shbang_opts}" %{buildroot}%{_bindir}/nxdialog
%endif

%ldconfig_scriptlets
%ldconfig_scriptlets -n libNX_X11
%ldconfig_scriptlets -n libXcomp
%ldconfig_scriptlets -n libXcompshad

%files
%license COPYING LICENSE LICENSE.nxcomp
%doc ChangeLog
%dir %{_libdir}/nx
%dir %{_datadir}/nx
%dir %{_datadir}/nx/X11
%{_datadir}/nx/SecurityPolicy
%{_datadir}/nx/X11/XErrorDB
%{_datadir}/nx/X11/Xcms.txt

%files -n libNX_X11
%{_libdir}/libNX_X11.so.6*

%files -n libNX_X11-devel
%{_libdir}/libNX_X11.so
%{_libdir}/pkgconfig/nx-x11.pc
%dir %{_includedir}/nx-X11
%{_includedir}/nx-X11/ImUtil.h
%{_includedir}/nx-X11/Xauth.h
%{_includedir}/nx-X11/XKBlib.h
%{_includedir}/nx-X11/Xcms.h
%{_includedir}/nx-X11/Xlib.h
%{_includedir}/nx-X11/XlibConf.h
%{_includedir}/nx-X11/Xlibint.h
%{_includedir}/nx-X11/Xlocale.h
%{_includedir}/nx-X11/Xregion.h
%{_includedir}/nx-X11/Xresource.h
%{_includedir}/nx-X11/Xutil.h
%{_includedir}/nx-X11/cursorfont.h

%files -n libXcomp-devel
%{_libdir}/libXcomp.so
%{_libdir}/pkgconfig/nxcomp.pc
%dir %{_includedir}/nx
%{_includedir}/nx/MD5.h
%{_includedir}/nx/NX.h
%{_includedir}/nx/NXalert.h
%{_includedir}/nx/NXpack.h
%{_includedir}/nx/NXproto.h
%{_includedir}/nx/NXvars.h

%files -n libXcomp
%license COPYING LICENSE LICENSE.nxcomp
%doc ChangeLog
%_libdir/libXcomp.so.3*

%files -n libXcompshad-devel
%{_libdir}/libXcompshad.so
%{_libdir}/pkgconfig/nxcompshad.pc
%dir %{_includedir}/nx
%{_includedir}/nx/Shadow.h

%files -n libXcompshad
%license COPYING LICENSE LICENSE.nxcomp
%doc ChangeLog
%_libdir/libXcompshad.so.3*

%files devel
%dir %{_includedir}/nx-X11/extensions
%{_includedir}/nx-X11/extensions/panoramiXext.h
%{_includedir}/nx-X11/misc.h
%{_includedir}/nx-X11/os.h

%files -n nx-proto-devel
%dir %{_includedir}/nx-X11
%{_includedir}/nx-X11/DECkeysym.h
%{_includedir}/nx-X11/HPkeysym.h
%{_includedir}/nx-X11/Sunkeysym.h
%{_includedir}/nx-X11/X.h
%{_includedir}/nx-X11/XF86keysym.h
%{_includedir}/nx-X11/Xarch.h
%{_includedir}/nx-X11/Xatom.h
%{_includedir}/nx-X11/Xdefs.h
%{_includedir}/nx-X11/Xfuncproto.h
%{_includedir}/nx-X11/Xfuncs.h
%{_includedir}/nx-X11/Xmd.h
%{_includedir}/nx-X11/Xos.h
%{_includedir}/nx-X11/Xos_r.h
%{_includedir}/nx-X11/Xosdefs.h
%{_includedir}/nx-X11/Xpoll.h
%{_includedir}/nx-X11/Xproto.h
%{_includedir}/nx-X11/Xprotostr.h
%{_includedir}/nx-X11/Xthreads.h
%{_includedir}/nx-X11/keysym.h
%{_includedir}/nx-X11/keysymdef.h
%{_includedir}/nx-X11/extensions/Xdbeproto.h
%{_includedir}/nx-X11/extensions/XI.h
%{_includedir}/nx-X11/extensions/XIproto.h
%{_includedir}/nx-X11/extensions/XResproto.h
%{_includedir}/nx-X11/extensions/bigreqstr.h
%{_includedir}/nx-X11/extensions/composite.h
%{_includedir}/nx-X11/extensions/compositeproto.h
%{_includedir}/nx-X11/extensions/damagewire.h
%{_includedir}/nx-X11/extensions/damageproto.h
%{_includedir}/nx-X11/extensions/dpms.h
%{_includedir}/nx-X11/extensions/dpmsstr.h
%{_includedir}/nx-X11/extensions/panoramiXproto.h
%{_includedir}/nx-X11/extensions/randr.h
%{_includedir}/nx-X11/extensions/randrproto.h
%{_includedir}/nx-X11/extensions/record*.h
%{_includedir}/nx-X11/extensions/render.h
%{_includedir}/nx-X11/extensions/renderproto.h
%{_includedir}/nx-X11/extensions/saver.h
%{_includedir}/nx-X11/extensions/saverproto.h
%{_includedir}/nx-X11/extensions/security.h
%{_includedir}/nx-X11/extensions/securstr.h
%{_includedir}/nx-X11/extensions/shapeconst.h
%{_includedir}/nx-X11/extensions/sync.h
%{_includedir}/nx-X11/extensions/syncstr.h
%{_includedir}/nx-X11/extensions/xcmiscstr.h
%{_includedir}/nx-X11/extensions/xf86bigfont.h
%{_includedir}/nx-X11/extensions/xf86bigfproto.h
%{_includedir}/nx-X11/extensions/xfixesproto.h
%{_includedir}/nx-X11/extensions/xfixeswire.h
%{_includedir}/nx-X11/extensions/xtestconst.h
%{_includedir}/nx-X11/extensions/xteststr.h

%files -n nxagent
%doc doc/nxagent/README.keystrokes
%dir %{_sysconfdir}/nxagent
%config(noreplace) %{_sysconfdir}/nxagent/keystrokes.cfg
%{_bindir}/nxagent
%dir %{_libdir}/nx
%dir %{_libdir}/nx/bin
%{_libdir}/nx/bin/nxagent
%dir %{_libdir}/nx/X11
%{_libdir}/nx/X11/libX11.so.6*
%dir %{_datadir}/nx
%{_datadir}/nx/fonts
%{_datadir}/nx/VERSION.nxagent
%{_mandir}/man1/nxagent.1*

%files -n nxproxy
%{_bindir}/nxproxy
%dir %{_libdir}/nx
%dir %{_libdir}/nx/bin
%dir %{_datadir}/nx
%{_datadir}/nx/VERSION.nxproxy
%{_mandir}/man1/nxproxy.1*

%files -n nxdialog
%doc nxdialog/README.md
%{_bindir}/nxdialog
%{_mandir}/man1/nxdialog.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Orion Poplawski <orion@nwra.com> - 3.5.99.27-6
- Drop i686 builds (FTBFS rhbz#2301004)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.5.99.27-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Orion Poplawski <orion@nwra.com> - 3.5.99.27-1
- Update to 3.5.99.27
- Switch from pathfix.py to %%py3_shebang_fix

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Orion Poplawski <orion@nwra.com> - 3.5.99.26-6
- Drop xorg-x11-font-utils requirement on EL9+ (bz#2104335)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 Orion Poplawski <orion@nwra.com> - 3.5.99.26-3
- Fix obsolete ar option usage (FTBFS bz#1987735)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Orion Poplawski <orion@nwra.com> - 3.5.99.26-1
- Update to 3.5.99.26

* Tue Jan 26 2021 Orion Poplawski <orion@nwra.com> - 3.5.99.25-4
- Add upstream patch to quiet logging

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Orion Poplawski <orion@nwra.com> - 3.5.99.25-2
- Add upstream commit to fix typo/build failure

* Fri Nov 06 2020 Orion Poplawski <orion@nwra.com> - 3.5.99.25-1
- Update to 3.5.99.25
- Split nxdialog into a separate package

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Orion Poplawski <orion@nwra.com> - 3.5.99.24-1
- Update to 3.5.99.24

* Sat Feb 01 2020 Orion Poplawski <orion@nwra.com> - 3.5.99.23-1
- Update to 3.5.99.23

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Orion Poplawski <orion@nwra.com> - 3.5.99.22-1
- Update to 3.5.99.22

* Thu Aug 15 2019 Orion Poplawski <orion@nwra.com> - 3.5.99.21-2
- BR libXfont2 on Fedora and RHEL 8+

* Thu Aug 15 2019 Orion Poplawski <orion@nwra.com> - 3.5.99.21-1
- Update to 3.5.99.21

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Orion Poplawski <orion@nwra.com> - 3.5.99.20-1
- Update to 3.5.99.20

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Orion Poplawski <orion@nwra.com> - 3.5.99.17-1
- Update to 3.5.99.17

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 6 2018 Orion Poplawski <orion@nwra.com> - 3.5.99.16-1
- Update to 3.5.99.16

* Thu Mar 8 2018 Orion Poplawski <orion@nwra.com> - 3.5.99.15-1
- Update to 3.5.99.15

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 3.5.99.14-2
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Mar 2 2018 Orion Poplawski <orion@nwra.com> - 3.5.99.14-1
- Update to 3.5.99.14

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Orion Poplawski <orion@nwra.com> - 3.5.0.33-3
- Remove useless obsoletes on provided name (bug #1537214)
- Use libtripc

* Fri Nov 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.33-2
- Work around compiler bug on epel7 ppc64le
- Improve compiler flag handling

* Wed Nov 8 2017 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.33-1
- Update to 3.5.0.33

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.32-5
- Drop old path from ld.so.conf file (bug #1405818)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.32-3
- Fix libXinerama symlink (bug #1256724)

* Tue Aug 25 2015 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.32-2
- Make libXinerama symlink (bug #1256724)

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.32-1
- Update to 3.5.0.32

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.31-1
- Update to 3.5.0.31
- Own /etc/x2go to ensure proper cleanup

* Fri Mar 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.29-1
- Update to 3.5.0.29

* Thu Nov 13 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.28-1
- Update to 3.5.0.28
- Fix unowned directories
- Minor cleanup

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 7 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.27-1
- Update to 3.5.0.27
- Drop aarch64 patch applied upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 7 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.24-2
- Add patch for aarch64 support attempt

* Wed May 7 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.24-1
- Update to 3.5.0.24
- Drop format patch applied upstream

* Tue May 6 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.23-1
- Update to 3.5.0.23
- Drop ppc64 and imake patches applied upstream

* Fri Jan 24 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.22-3
- Add patch to fix imake build
- Add patch to fix -Werror=format-security build

* Fri Jan 24 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.22-2
- Set compile flags properly on arm and ppc64
- Add patch to fix ppc64 build

* Sun Jan 5 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.22-1
- Update to 3.5.0.22
- Drop bundled patch applied upstream
- Fix Xinerama support

* Fri Jan 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.21-5
- Provide /usr/share/X11/xkb/keymap.dir so nxagent can find keymap dir (bug #1033876)

* Thu Oct 10 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.21-4
- Do not build/ship unneeded xlib18n libs

* Wed Sep 4 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.21-3
- Fix nx obsoletes version

* Tue Sep 3 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.21-2
- Have nxagent and nxproxy also obsolete/provide nx

* Fri Aug 30 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.21-1
- Update to 3.5.0.21
- Many bundled libs removed upstream
- Drop initgroups patch applied upstream
- Fix macro in comments
- Remove execute permissions from source files
- Add %%postun ldconfig scripts
- Rename nx-devel nx-libs-devel

* Thu Aug 29 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-7
- Add patch to call initgroups()

* Thu Jul 11 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-6
- Drop building and/or shipping a bunch of unneeded libraries

* Thu Jun 13 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-5
- Add more explicit verioned requires
- Drop unnecessary directory ownership by sub-packages
- Remove many bundled libraries

* Tue Jun 11 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-4
- Fix 775 library permissions
- Move nx/X11 .so files to -devel
- Fix nx obsoletes
- Mark ld.so.conf.d files config(noreplace)
- Fix requires

* Fri May 31 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-3
- Fix quoting when creating my_configure script

* Thu May 30 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-2
- Use optflags for compiling, __global_ldflags for linking

* Thu Apr 4 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.20-1
- Update to 3.5.0.20

* Mon Mar 25 2013 Orion Poplawski <orion@cora.nwra.com> - 3.5.0.18-1
- Initial package
