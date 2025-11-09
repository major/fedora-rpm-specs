%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global gettext_package         dbus-1

%global libselinux_version      2.0.86

# fedora-release-30-0.2 and generic-release-0.1 added required presets to enable systemd-unit symlinks
%global fedora_release_version  30-0.2
%global generic_release_version 30-0.1

# Allow extra dependencies required for some tests to be disabled.
%bcond_without tests
# Disabled in June 2014: http://lists.freedesktop.org/archives/dbus/2014-June/016223.html
%bcond_with check
# Allow cmake support to be disabled. #1497257
%bcond_without cmake

Name:    dbus
Epoch:   1
Version: 1.16.0
Release: %autorelease
Summary: D-BUS message bus

# The effective license of the majority of the package, including the shared
# library, is "GPL-2+ or AFL-2.1". Certain utilities are "GPL-2+" only.
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:     https://www.freedesktop.org/wiki/Software/dbus/
Source0: https://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1: https://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz.asc
# gpg --keyserver keyring.debian.org --recv-keys DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90
# gpg --export --export-options export-minimal > gpgkey-DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90.gpg
Source2: gpgkey-DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90.gpg
Source3: 00-start-message-bus.sh
Source4: dbus.socket
Source5: dbus-daemon.service
Source6: dbus.user.socket
Source7: dbus-daemon.user.service
Source8: dbus-systemd-sysusers.conf
Patch0: 0001-tools-Use-Python3-for-GetAllMatchRules.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: audit-libs-devel >= 0.9
BuildRequires: gnupg2
BuildRequires: libX11-devel
BuildRequires: libcap-ng-devel
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(libselinux) >= %{libselinux_version}
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(systemd)
BuildRequires: doxygen
# For Ducktype documentation.
BuildRequires: /usr/bin/ducktype
BuildRequires: /usr/bin/yelp-build
# For building XML documentation.
BuildRequires: /usr/bin/xsltproc
BuildRequires: xmlto
%if %{with cmake}
# For AutoReq cmake-filesystem.
BuildRequires: cmake
%endif

#For macroized scriptlets.
BuildRequires:    systemd

# Note: These is only required for --with-tests; when bootstrapping, you can
# pass --without-tests.
%if %{with tests}
BuildRequires: pkgconfig(gio-2.0) >= 2.40.0
BuildRequires: python3-dbus
BuildRequires: python3-gobject
%endif
%if %{with check}
BuildRequires: /usr/bin/Xvfb
%endif

# Since F30 the default implementation is dbus-broker over dbus-daemon
Requires: (dbus-broker >= 16-4 if systemd)

%description
D-BUS is a system for sending messages between applications. It is
used both for the system-wide message bus service, and as a
per-user-login-session messaging facility.

%package common
Summary:        D-BUS message bus configuration
BuildArch:      noarch
Conflicts:      fedora-release < %{fedora_release_version}
Conflicts:      generic-release < %{generic_release_version}

%description common
The %{name}-common package provides the configuration and setup files for D-Bus
implementations to provide a System and User Message Bus.

%package daemon
Summary:        D-BUS message bus
Conflicts:      fedora-release < %{fedora_release_version}
Conflicts:      generic-release < %{generic_release_version}
Requires:       libselinux%{?_isa} >= %{libselinux_version}
Requires:       dbus-common = %{epoch}:%{version}-%{release}
Requires:       dbus-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       dbus-tools = %{epoch}:%{version}-%{release}
%{?sysusers_requires_compat}

%description daemon
D-BUS is a system for sending messages between applications. It is
used both for the system-wide message bus service, and as a
per-user-login-session messaging facility.

%package tools
Summary:        D-BUS Tools and Utilities
Requires:       dbus-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
Tools and utilities to interact with a running D-Bus Message Bus, provided by
the reference implementation.

%package libs
Summary: Libraries for accessing D-BUS

%description libs
This package contains lowlevel libraries for accessing D-BUS.

%package doc
Summary: Developer documentation for D-BUS
Requires: %{name}-daemon = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
This package contains developer documentation for D-Bus along with
other supporting documentation such as the introspect dtd file.

%package devel
Summary: Development files for D-BUS
Requires: dbus-libs%{?_isa} = %{epoch}:%{version}-%{release}
# For xml directory ownership.
Requires: xml-common

%description devel
This package contains libraries and header files needed for
developing software that uses D-BUS.

%package tests
Summary: Tests for the %{name}-daemon package
Requires: %{name}-daemon%{?_isa} = %{epoch}:%{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name}-daemon package.

%package x11
Summary: X11-requiring add-ons for D-BUS
# The server package can be a different architecture.
Requires: %{name}-daemon = %{epoch}:%{version}-%{release}

%description x11
D-BUS contains some tools that require Xlib to be installed, those are
in this separate package so server systems need not install X.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
CONFIG_OPTIONS=(
  -Dlibaudit=enabled
  -Dselinux=enabled
  -Dsystem_socket=/run/dbus/system_bus_socket
  -Ddbus_user=dbus
  -Duser_session=true
  -Dinstalled_tests=true
  --libexecdir=%{_libexecdir}/dbus-1
)

%global _vpath_builddir build
%meson \
  "${CONFIG_OPTIONS[@]}" \
  -Ddoxygen_docs=enabled \
  -Dducktype_docs=enabled \
  -Dxml_docs=enabled \
  -Dasserts=false \
  -Dqt_help=disabled \
  -Dapparmor=disabled \
  -Dkqueue=disabled \
  -Dlaunchd=disabled
%meson_build

%if %{with check}
%global _vpath_builddir build-check
%meson "${CONFIG_OPTIONS[@]}" -Dasserts=true -Dverbose_mode=true
%meson_build
%endif


%install
%global _vpath_builddir build
%meson_install

# Delete python2 code
rm -f %{buildroot}/%{_pkgdocdir}/examples/GetAllMatchRules.py

%if ! %{with cmake}
rm -rf %{buildroot}%{_libdir}/cmake
%endif

# Delete upstream units
rm -f %{buildroot}%{_unitdir}/dbus.{socket,service}
rm -f %{buildroot}%{_unitdir}/sockets.target.wants/dbus.socket
rm -f %{buildroot}%{_unitdir}/multi-user.target.wants/dbus.service
rm -f %{buildroot}%{_userunitdir}/dbus.{socket,service}
rm -f %{buildroot}%{_userunitdir}/sockets.target.wants/dbus.socket
rm -f %{buildroot}%{_sysusersdir}/dbus.conf

# Install downstream units
install -Dp -m755 %{SOURCE3} %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/00-start-message-bus.sh
install -Dp -m644 %{SOURCE4} %{buildroot}%{_unitdir}/dbus.socket
install -Dp -m644 %{SOURCE5} %{buildroot}%{_unitdir}/dbus-daemon.service
install -Dp -m644 %{SOURCE6} %{buildroot}%{_userunitdir}/dbus.socket
install -Dp -m644 %{SOURCE7} %{buildroot}%{_userunitdir}/dbus-daemon.service
install -Dp -m644 %{SOURCE8} %{buildroot}%{_sysusersdir}/dbus.conf

# Obsolete, but still widely used, for drop-in configuration snippets.
install --directory %{buildroot}%{_sysconfdir}/dbus-1/session.d
install --directory %{buildroot}%{_sysconfdir}/dbus-1/system.d

install --directory %{buildroot}%{_datadir}/dbus-1/interfaces

## %%find_lang %%{gettext_package}

install --directory %{buildroot}/var/lib/dbus
install --directory %{buildroot}/run/dbus

install -pm 644 -t %{buildroot}%{_pkgdocdir} \
    doc/introspect.dtd doc/introspect.xsl doc/system-activation.txt

# Make sure that the documentation shows up in Devhelp.
install --directory %{buildroot}%{_datadir}/gtk-doc/html
ln -s %{_pkgdocdir} %{buildroot}%{_datadir}/gtk-doc/html/dbus

# Shell wrapper for installed tests, modified from Debian package.
cat > dbus-run-installed-tests <<EOF
#!/bin/sh
# installed-tests wrapper for dbus. Outputs TAP format because why not

set -e

timeout="timeout 300s"
ret=0
i=0
tmpdir=\$(mktemp --directory --tmpdir dbus-run-installed-tests.XXXXXX)

for t in %{_libexecdir}/dbus-1/installed-tests/dbus/test-*; do
    i=\$(( \$i + 1 ))
    echo "# \$i - \$t ..."
    echo "x" > "\$tmpdir/result"
    ( set +e; \$timeout \$t; echo "\$?" > "\$tmpdir/result" ) 2>&1 | sed 's/^/# /'
    e="\$(cat "\$tmpdir/result")"
    case "\$e" in
        (0)
            echo "ok \$i - \$t"
            ;;
        (77)
            echo "ok \$i # SKIP \$t"
            ;;
        (*)
            echo "not ok \$i - \$t (\$e)"
            ret=1
            ;;
    esac
done

rm -rf tmpdir
echo "1..\$i"
exit \$ret
EOF

install -pm 755 -t %{buildroot}%{_libexecdir}/dbus-1 dbus-run-installed-tests


%if %{with check}
%check
pushd build-check

# TODO: better script for this...
export DISPLAY=42
{ Xvfb :${DISPLAY} -nolisten tcp -auth /dev/null >/dev/null 2>&1 &
  trap "kill -15 $! || true" 0 HUP INT QUIT TRAP TERM; };
%meson_test
popd
%endif


%pre daemon
# Add the "dbus" user and group
%sysusers_create_compat %{SOURCE8}

%post common
%systemd_post dbus.socket
%systemd_user_post dbus.socket

%post daemon
%systemd_post dbus-daemon.service
%systemd_user_post dbus-daemon.service

%preun common
%systemd_preun dbus.socket
%systemd_user_preun dbus.socket

%preun daemon
%systemd_preun dbus-daemon.service
%systemd_user_preun dbus-daemon.service

%postun common
%systemd_postun dbus.socket
%systemd_user_postun dbus.socket

%postun daemon
%systemd_postun dbus-daemon.service
%systemd_user_postun dbus-daemon.service

%triggerpostun common -- dbus-common < 1:1.12.10-4
if [ -x /usr/bin/systemctl ]; then
    systemctl --no-reload preset dbus.socket &>/dev/null || :
    systemctl --no-reload --global preset dbus.socket &>/dev/null || :
fi

%triggerpostun daemon -- dbus-daemon < 1:1.12.10-7
if [ -x /usr/bin/systemctl ]; then
    systemctl --no-reload preset dbus-daemon.service &>/dev/null || :
    systemctl --no-reload --global preset dbus-daemon.service &>/dev/null || :
fi

%files
# The 'dbus' package is only retained for compatibility purposes. It will
# eventually be removed and then replaced by 'Provides: dbus' in the
# dbus-daemon package. It will then exclusively be used for other packages to
# describe their dependency on a system and user bus. It does not pull in any
# particular dbus *implementation*, nor any libraries. These should be pulled
# in, if required, via explicit dependencies.

%files common
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/session.d
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/session.conf
%config %{_sysconfdir}/dbus-1/system.conf
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/session.d
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/session.conf
%{_datadir}/dbus-1/system.conf
%{_datadir}/dbus-1/services
%{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/interfaces
%{_sysusersdir}/dbus.conf
%{_unitdir}/dbus.socket
%{_userunitdir}/dbus.socket

%files daemon
# Strictly speaking, we could remove the COPYING from this subpackage and 
# just have it be in libs, because dbus Requires dbus-libs.
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS CONTRIBUTING.md NEWS README
%exclude %{_pkgdocdir}/api
%exclude %{_pkgdocdir}/diagram.*
%exclude %{_pkgdocdir}/introspect.*
%exclude %{_pkgdocdir}/system-activation.txt
%exclude %{_pkgdocdir}/*.html
%ghost %dir /run/%{name}
%dir %{_localstatedir}/lib/dbus/
%{_bindir}/dbus-daemon
%{_bindir}/dbus-cleanup-sockets
%{_bindir}/dbus-run-session
%{_bindir}/dbus-test-tool
%{_mandir}/man1/dbus-cleanup-sockets.1*
%{_mandir}/man1/dbus-daemon.1*
%{_mandir}/man1/dbus-run-session.1*
%{_mandir}/man1/dbus-test-tool.1*
%dir %{_libexecdir}/dbus-1
# See doc/system-activation.txt in source tarball for the rationale
# behind these permissions
%attr(4750,root,dbus) %{_libexecdir}/dbus-1/dbus-daemon-launch-helper
%exclude %{_libexecdir}/dbus-1/dbus-run-installed-tests
%{_tmpfilesdir}/dbus.conf
%{_unitdir}/dbus-daemon.service
%{_userunitdir}/dbus-daemon.service

%files tools
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/dbus-send
%{_bindir}/dbus-monitor
%{_bindir}/dbus-update-activation-environment
%{_bindir}/dbus-uuidgen
%{_mandir}/man1/dbus-monitor.1*
%{_mandir}/man1/dbus-send.1*
%{_mandir}/man1/dbus-update-activation-environment.1*
%{_mandir}/man1/dbus-uuidgen.1*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*dbus-1*.so.*

%files tests
%{_libexecdir}/dbus-1/installed-tests
%{_libexecdir}/dbus-1/dbus-run-installed-tests
%{_datadir}/installed-tests

%files x11
%{_bindir}/dbus-launch
%{_mandir}/man1/dbus-launch.1*
%{_sysconfdir}/X11/xinit/xinitrc.d/00-start-message-bus.sh

%files doc
%{_pkgdocdir}/*
%{_datadir}/gtk-doc

%files devel
%{_datadir}/xml/dbus-1
%{_libdir}/lib*.so
%dir %{_libdir}/dbus-1.0
%if %{with cmake}
%{_libdir}/cmake/DBus1
%endif
%{_libdir}/dbus-1.0/include/
%{_libdir}/pkgconfig/dbus-1.pc
%{_includedir}/*


%changelog
%autochangelog
