# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

%global commit ca0118851b2af77d19c59d892a65a65e2db10848
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20261125
%global snapnumber %{commitdate}.1

Name:           mddm
Version:        0.21.0^%{snapnumber}.%{shortcommit}
Release:        1%{?dist}
SourceLicense:  GPL-2.0-or-later and CC-BY-SA-3.0 and CC-BY-4.0 and Apache-2.0 and MIT
License:        GPL-2.0-or-later
Summary:        QML based desktop and login manager

URL:            https://forge.moderndesktop.dev/ModernDesktopInitiative/mddm
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

## upstream patches

## upstreamable patches

## downstream patches
Patch101:       mddm-fedora_config.patch

# mddm.service: +EnvironmentFile=-/etc/sysconfig/mddm
Patch103:       mddm-environment_file.patch

# Workaround for https://pagure.io/fedora-kde/SIG/issue/87
Patch104:       mddm-rpmostree-tmpfiles-hack.patch

# sample mddm.conf generated with mddm --example-config, and entries commented-out
Source13:       mddm.conf
# README.scripts
Source14:       README.scripts
# sysconfig snippet
Source15:       mddm.sysconfig

# sysusers config file. note these are shipped in the upstream tarball
# but we cannot use the files from the tarball for %pre scriptlet
# generation, so we duplicate them as source files for that purpose;
# this is an ugly hack that should be removed if it becomes possible.
# see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/TFDMAU7KLMSQTKPJELHSM6PFVXIZ56GK/
Source17:        mddm-systemd-sysusers.conf


Provides:       service(graphical-login) = mddm

BuildRequires:  cmake >= 3.22
BuildRequires:  extra-cmake-modules
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# X11 Sessions: The helper writes Xauthority cookies with libXau
BuildRequires:  pkgconfig(xau)
# For reading the keyboard state and ensuring the greeter has a visible mouse cursor
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
# sometimes python-docutils, sometimes python2-docutils, sometimes python3-docutils.
# use path then for sanity
BuildRequires:  /usr/bin/rst2man
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6QuickTest)
# verify presence to pull defaults from /etc/login.defs
BuildRequires:  shadow-utils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

%if 0%{?fedora}
# for /usr/share/backgrounds/default.{jxl,png}
BuildRequires: desktop-backgrounds-compat
BuildRequires: ImageMagick
Requires: desktop-backgrounds-compat
# for jxl support
Requires: kf6-kimageformats%{?_isa}
# for /usr/share/pixmaps/system-logo-white.png
Requires: system-logos
%endif
Requires: systemd
%if %{with x11}
Requires: xorg-x11-xinit
%endif
%{?systemd_requires}

Requires(pre): shadow-utils

# Virtual dependency for mddm greeter setup
Requires: mddm-greeter-displayserver
Suggests: mddm-wayland-generic

%description
MDDM is a modern graphical display manager aiming to be fast, simple and
beautiful. It uses modern technologies like QtQuick, which in turn gives the
designer the ability to create smooth, animated user interfaces.

%package wayland-generic
Summary: Generic Wayland MDDM greeter display server configuration
Provides: mddm-greeter-displayserver
Conflicts: mddm-greeter-displayserver
Requires: weston
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description wayland-generic
This package contains configuration and dependencies for MDDM
to use Weston for the greeter display server.

This is the generic default Wayland configuration provided
by MDDM.

%package themes
Summary: MDDM Themes
License: GPL-2.0-or-later and CC-BY-SA-3.0 and CC-BY-4.0 and Apache-2.0 and MIT
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description themes
A collection of mddm themes, including: elarun, maldives, maya

%package compat-sddm-themes
Summary: MDDM compatibility support for SDDM themes
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
# This provides files that are alternatively part of SDDM
Conflicts: sddm
%description compat-sddm-themes
This package provides the compatibility interfaces
and location for SDDM themes to run on MDDM.

%prep
%autosetup -C -p1

%if 0%{?fedora}
bg_file_ext="jxl"
if [ -f "/usr/share/backgrounds/default.png" ]; then
bg_file_ext="png"
fi
#FIXME/TODO: use version on filesystem instead of using a bundled copy
cp -v "/usr/share/backgrounds/default.${bg_file_ext}"  \
      "src/greeter/theme/background.${bg_file_ext}"
ls -sh "src/greeter/theme/background.${bg_file_ext}"
magick mogrify -resize 1920x1200 "src/greeter/theme/background.${bg_file_ext}"
ls -sh "src/greeter/theme/background.${bg_file_ext}"

if [ "$bg_file_ext" != "png" ]; then
sed -e "s/background.png/background.${bg_file_ext}/g" -i src/greeter/theme.qrc src/greeter/theme/{Main.qml,theme.conf}
fi
%endif


%conf
%cmake \
  -DBUILD_MAN_PAGES:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DENABLE_JOURNALD:BOOL=ON \
  -DSESSION_COMMAND:PATH=/etc/X11/xinit/Xsession \
  -DWAYLAND_SESSION_COMMAND:PATH=/etc/mddm/wayland-session


%build
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/mddm.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/mddm/mddm.conf.d
install -Dpm 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/mddm.conf
install -Dpm 644 %{SOURCE14} %{buildroot}%{_datadir}/mddm/scripts/README.scripts
install -Dpm 644 %{SOURCE15} %{buildroot}%{_sysconfdir}/sysconfig/mddm

mkdir -p %{buildroot}/run/mddm
mkdir -p %{buildroot}%{_localstatedir}/lib/mddm
mkdir -p %{buildroot}%{_sysconfdir}/mddm/
cp -a %{buildroot}%{_datadir}/mddm/scripts/* \
      %{buildroot}%{_sysconfdir}/mddm/
# we're using /etc/X11/xinit/Xsession (by default) instead
rm -fv %{buildroot}%{_sysconfdir}/mddm/Xsession

# Create legacy theme directory location for SDDM themes
mkdir -p %{buildroot}%{_datadir}/sddm/themes


%pre
%sysusers_create_compat %{SOURCE17}


%post
%systemd_post mddm.service


%preun
%systemd_preun mddm.service


%postun
%systemd_postun mddm.service


%files
%license LICENSE
%doc README.md CONTRIBUTORS
%dir %{_sysconfdir}/mddm/
%dir %{_sysconfdir}/mddm.conf.d
%dir %{_prefix}/lib/mddm
%dir %{_prefix}/lib/mddm/mddm.conf.d
%config(noreplace)   %{_sysconfdir}/mddm/*
%config(noreplace)   %{_sysconfdir}/mddm.conf
%config(noreplace) %{_sysconfdir}/sysconfig/mddm
%{_prefix}/lib/pam.d/mddm*
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-mddm.conf
%{_bindir}/mddm
%{_bindir}/mddm-greeter*
%{_libexecdir}/mddm-helper
%{_libexecdir}/mddm-helper-start-wayland
%{_libexecdir}/mddm-helper-start-x11user
%{_tmpfilesdir}/mddm.conf
%{_sysusersdir}/mddm.conf
%attr(0711, root, mddm) %dir /run/mddm
%attr(1770, mddm, mddm) %dir %{_localstatedir}/lib/mddm
%{_unitdir}/mddm.service
%dir %{_datadir}/mddm
%{_datadir}/mddm/faces/
%{_datadir}/mddm/flags/
%dir %{_datadir}/mddm/qml
%{_datadir}/mddm/qml/MddmComponents/
%{_datadir}/mddm/scripts/
%dir %{_datadir}/mddm/themes/
# %%lang'ify? they're small, probably not worth it -- rex
%{_datadir}/mddm/translations*/
%{_mandir}/man1/mddm.1*
%{_mandir}/man1/mddm-greeter.1*
%{_mandir}/man5/mddm.conf.5*
%{_mandir}/man5/mddm-state.conf.5*


%files wayland-generic
# No files since default configuration


%files themes
%{_datadir}/mddm/themes/elarun/
%{_datadir}/mddm/themes/maldives/
%{_datadir}/mddm/themes/maya/


%files compat-sddm-themes
%{_datadir}/mddm/qml/SddmComponents/
%{_datadir}/sddm/


%changelog
* Wed Nov 25 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0^20261125.1.ca01188-1
- Initial packaging (rhbz#2582260)

