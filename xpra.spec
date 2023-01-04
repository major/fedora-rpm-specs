%bcond_with enc_x264
%bcond_with enc_x265
%bcond_with dec_avcodec2
%bcond_with csc_swscale

# For debugging only
%bcond_with debug
%if %{with debug}
%global _with_debug --with-debug
%endif
#

%global __js_jquery_latest %{_datadir}/javascript/jquery/latest/

# These are nececessary as the _with_foo is *not* defined if the
# --with flag isn't specifed, and we need to have the --without
# specified option in that case.
%if %{without enc_x264}
%global _with_enc_x264 --without-enc_x264
%endif

%if %{with enc_x265}
%global _with_enc_x265 --with-enc_x265
%endif

%if %{without dec_avcodec2}
%global _with_dec_avcodec2 --without-dec_avcodec2
%endif

%if %{without csc_swscale}
%global _with_csc_swscale --without-csc_swscale
%endif

# Remove private provides from .so files in the python3_sitearch directory
%global __provides_exclude_from ^%{python3_sitearch}/.*\\.so$

# Note: cups-config not in buildroot during srpm build, so we use the
# conditional execution to silence erros during srpm build.
%if 0%{?_cups_serverbin:1}
%global cupslibdir %_cups_serverbin
%else
%global cupslibdir %(cups-config --serverbin 2> /dev/null || echo "/usr/lib/cups")
%endif

Name:           xpra
Version:        4.4.3
Release:        1%{?dist}
Summary:        Remote display server for applications and desktops
License:        GPLv2+ and BSD and LGPLv3+ and MIT
URL:            https://www.xpra.org/
Source0:        https://github.com/Xpra-org/xpra/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

# Appdata file for Fedora
Source1:        %{name}.appdata.xml

# Horrible fix to find py3cairo.h in python3-cairo-1.16.3
Patch0:         %{name}-find_py3cairo.patch

# Install into /usr/libexec always
Patch1:         %{name}-force_always_libexec.patch

Patch2:         %{name}-bug3693.patch

BuildRequires:  python3-devel
BuildRequires:  gtk3-devel
BuildRequires:  libXtst-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  python3-Cython
BuildRequires:  ack
BuildRequires:  desktop-file-utils
BuildRequires:  libvpx-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXres-devel
BuildRequires:  lz4-devel
BuildRequires:  cups-devel, cups
BuildRequires:  redhat-rpm-config
BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  pandoc
%if 0%{?el8}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  python3-cairo
BuildRequires:  cairo-devel
BuildRequires:  pygobject3-devel
%else
BuildRequires:  python3-gobject-devel
BuildRequires:  libappstream-glib
BuildRequires:  python3-cairo-devel
BuildRequires:  xorg-x11-server-Xorg
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  xorg-x11-xauth
BuildRequires:  xkbcomp
BuildRequires:  setxkbmap
%endif
%if %{with debug}
BuildRequires: libasan
%endif

%if %{with enc_x264}
BuildRequires:  x264-devel
%endif
%if %{with dec_avcodec2} || %{with csc_swscale}
BuildRequires:  ffmpeg-devel
%endif

Requires: python3-pillow
Requires: python3-cups
Requires: python3-pyopengl
Requires: python3-gobject
Requires: python3-inotify
Requires: python3-lz4
Requires: python3-ldap3
Requires: python3-rencode
Requires: python3-netifaces
Requires: python3-dbus
Requires: dbus-x11
Requires: xmodmap
Requires: xrandr
Requires: xorg-x11-drv-dummy%{?_isa}
Requires: xorg-x11-xauth%{?_isa}
Requires: xorg-x11-server-Xorg%{?_isa}
Requires: python3-numpy
Requires: gstreamer1%{?_isa}
Requires: gstreamer1-plugins-base%{?_isa}
Requires: gstreamer1-plugins-good%{?_isa}
%if 0%{?fedora}
Requires: pipewire%{?_isa}
Requires: pipewire-utils%{?_isa}
Requires: pipewire-pulseaudio%{?_isa}
%else
Requires: pulseaudio%{?_isa}
Requires: pulseaudio-utils%{?_isa}
%endif
Requires: cups-filesystem
Requires: shared-mime-info%{?_isa}
Requires: js-jquery

# python3-opencv is required for webcam forwarding support, client-side only.
# Available on Fedora only.
%{?fedora:Requires: python3-opencv}

# Needed to create the xpra group
Requires(pre):  shadow-utils

# xpra-html5 is now separately provided 
Obsoletes: xpra-html5 < 0:4.1-1

%description
Xpra is "screen for X": it allows you to run X programs, usually on a remote
host, direct their display to your local machine, and then to disconnect from
these programs and reconnect from the same or another machine, without losing
any state. It gives you remote access to individual applications.

Xpra is "rootless" or "seamless": programs you run under it show up on your
desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing
network bandwidth constraints.

%package udev
Summary:  xpra udev files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd-udev%{?_isa}

%description udev
Udev rules of xpra.

%prep
%autosetup -n %{name}-%{version} -N

%if 0%{?el8}
%patch0 -p1 -b .backup
%patch1 -p1 -b .backup
sed -i 's|@@python3_sitearch@@|%{python3_sitearch}|' setup.py
%endif
%patch2 -p1 -R -b .backup

# cc1: error: unrecognized compiler option ‘-mfpmath=387’
%ifarch %{arm}
sed -i 's|-mfpmath=387|-mfloat-abi=hard|' setup.py
%endif

%build
%set_build_flags
%if 0%{?el8}
export CFLAGS="%{build_cflags} -I%{_includedir}/cairo"
%endif
%{__python3} setup.py build --executable="%{__python3} -s" \
    --with-verbose \
    --with-vpx \
    %{?_with_enc_x264} \
    %{?_with_enc_x265} \
    %{?_with_dec_avcodec2} \
    %{?_with_csc_swscale} \
    %{?_with_debug} \
    --with-Xdummy \
    --with-Xdummy_wrapper \
    --without-strict \
    --without-enc_ffmpeg

%install
%py3_install

# Installation of these service files is not permitted on Fedora
# See https://pagure.io/fesco/issue/1759
rm -f %{buildroot}/lib/systemd/system/xpra.service
rm -f %{buildroot}/lib/systemd/system/xpra.socket

#move icon to proper directory
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

mv %{buildroot}%{_datadir}/icons/xpra.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

rm -f %{buildroot}%{_datadir}/icons/xpra-mdns.png
install -pm 644 fs/share/icons/xpra-mdns.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

rm -f %{buildroot}%{_datadir}/icons/xpra-shadow.png
install -pm 644 fs/share/icons/xpra-shadow.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

#replace old file with horrible WindowsXP old image
rm -rf %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/

#Install nvenc.keys file
mkdir -p %{buildroot}%{_sysconfdir}/xpra
install -pm 644 fs/etc/xpra/nvenc.keys %{buildroot}%{_sysconfdir}/xpra

#remove doc stuff from /usr/share
rm -f \
    %{buildroot}%{_datadir}/xpra/README \
    %{buildroot}%{_datadir}/xpra/COPYING

#fix shebangs from python3_sitearch
find %{buildroot}%{python3_sitearch}/xpra -name '*.py' | xargs %{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}"
find %{buildroot}%{python3_sitearch}/xpra -name '*.py' | xargs chmod 0755
for i in `ack -rl '^#!/.*python' %{buildroot}%{python3_sitearch}/xpra`; do
    chmod 0755 $i
done

#fix permissions on shared objects
pushd %{buildroot}%{python3_sitearch}/xpra
find . -name '*.so' \
    -exec chmod 0755 {} \;
popd

# delete any bundled SWFs - binary content forbidden by packaging
# guidelines
find %{buildroot}%{_datadir}/xpra -name '*.swf' -exec rm {} \;

# Create this directory for sharing sockets
mkdir -p %{buildroot}%{_rundir}/xpra

# Remove use of /usr/bin/enx on scripts
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{cupslibdir}/backend/xpraforwarder
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{_libexecdir}/xpra/auth_dialog
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{_libexecdir}/xpra/xdg-open

for i in `find %{buildroot}%{_bindir} -perm /644 -type f \( -name "*" \)`; do
    chmod 0755 $i
done

# Remove Build documentation
rm -rf %{buildroot}%{_docdir}/xpra/Build

install -pm 644 README.md %{buildroot}%{_docdir}/xpra/

%check
%{?fedora:appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/xpra.appdata.xml}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%pre
getent group xpra >/dev/null || groupadd -r xpra

%files
%license COPYING
%dir %{_sysconfdir}/xpra
%dir %{_sysconfdir}/xpra/conf.d
%config(noreplace) %{_sysconfdir}/xpra/*.conf
%config(noreplace) %{_sysconfdir}/xpra/nvenc.keys
%config(noreplace) %{_sysconfdir}/xpra/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/90-xpra-virtual.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/xpra.conf
%config(noreplace) %{_sysconfdir}/sysconfig/xpra
%config(noreplace) %{_sysconfdir}/pam.d/xpra
%config(noreplace) %{_sysconfdir}/xpra/content-categories/10_default.conf
%config(noreplace) %{_sysconfdir}/xpra/content-parent/10_default.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/10_role.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/30_title.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/50_class.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/70_commands.conf
%config(noreplace) %{_sysconfdir}/xpra/http-headers/00_nocache.txt
%config(noreplace) %{_sysconfdir}/xpra/http-headers/10_content_security_policy.txt
%{_libexecdir}/xpra/
%{_bindir}/xpra
%{_bindir}/xpra_launcher
%{_bindir}/run_scaled
%{_sysusersdir}/*.conf
%{python3_sitearch}/xpra/
%{python3_sitearch}/*.egg-info
%{_datadir}/applications/xpra*.desktop
%{_datadir}/icons/hicolor/48x48/apps/xpra-mdns.png
%{_datadir}/icons/hicolor/48x48/apps/xpra-shadow.png
%{_datadir}/icons/hicolor/64x64/apps/xpra.png
%{_mandir}/man1/xpra.1.*
%{_mandir}/man1/xpra_*.1.*
%{_mandir}/man1/run_scaled.1.*
%{_metainfodir}/xpra.appdata.xml
%{_datadir}/mime/packages/application-x-xpraconfig.xml
%{_datadir}/xpra/
%{cupslibdir}/backend/xpraforwarder
%{_tmpfilesdir}/xpra.conf
%dir %{_rundir}/xpra
%{_pkgdocdir}/

%files udev
%{_udevrulesdir}/71-xpra-virtual-pointer.rules

%changelog
* Thu Dec 08 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.4.3-1
- Release 4.4.3
- Disable CUDA rebuilds

* Sun Nov 13 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.4.2-1
- Release 4.4.2

* Mon Oct 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.4.1-1
- Release 4.4.1

* Sat Oct 01 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.4-1
- Release 4.4

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.3.4-1
- Release 4.3.4

* Fri Apr 29 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.3.3-1
- Release 4.3.3

* Wed Feb 16 2022 Sérgio Basto <sergio@serjux.com> - 4.3.2-1
- Update xpra to 4.3.2

* Thu Jan 27 2022 Tom Callaway <spot@fedoraproject.org> - 4.3.1-3
- rebuild for libvpx

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.3.1-1
- Release 4.3.1

* Fri Dec 17 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.3.0-1
- Release 4.3

* Wed Oct 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.2.3-1
- Release 4.2.3

* Thu Aug 12 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.2.2-1
- Release 4.2.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.2.1-1
- Release 4.2.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.2-1
- Release 4.2

* Sun May 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.1.3-2
- Switch from pulseaudio to pipewire (rhbz#1960903)

* Wed Apr 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.1.3-1
- Release 4.1.3

* Tue Apr 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.1.2-1
- Release 4.1.2

* Sun Mar 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.1.1-1
- Release 4.1.1

* Wed Mar 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.1-2
- Fix epel8 builds

* Mon Mar 01 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.1-1
- Release 4.1

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.0.6-2
- Fix rhbz#1916026

* Thu Dec 31 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.6-1
- Release 4.0.6

* Wed Nov 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.5-2
- Fix BR packages for epel8

* Wed Nov 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.5-1
- Release 4.0.5

* Mon Sep 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.4-1
- Release 4.0.4

* Sat Aug 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.3-1
- Release 4.0.3

* Wed Aug 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.2-4
- Requires xmodmap xrandr without %%?_isa wrapper (rhbz#1864529)

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 4.0.2-3
- Requires xmodmap xrandr, not xorg-x11-server-utils

* Thu Jul 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.2-2
- Built on EPEL8
- Drop (obsolete) python-websockify dependency
- Add MPLv2.0 LICENSE file for HTML5 version

* Fri Jun 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.2-1
- Release 4.0.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0.1-1
- Release 4.0.1

* Fri May 15 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0-2
- Remove uglify-js

* Sun May 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.0-1
- Release 4.0

* Tue Apr 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.9-1
- Release 3.0.9

* Thu Apr 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.8-1
- Release 3.0.8

* Sat Mar 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.7-2
- Add PAM support (rhbz#1812903)

* Sat Mar 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.7-1
- Release 3.0.7

* Wed Feb 12 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.6-2
- Fix symlinks to js-jquery (rhbz#1801878)

* Sat Feb 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.6-1
- Release 3.0.6

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.5-1
- Release 3.0.5

* Thu Dec 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.3-1
- Release 3.0.3

* Tue Nov 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-1
- Release 3.0.2

* Sat Nov 02 2019 Sérgio Basto <sergio@serjux.com> - 3.0.1-3
- Use %%{_sysusersdir} to fix rpmlint E: hardcoded-library-path

* Fri Nov 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-2
- Create /run/xpra (rhbz#1381005)

* Mon Oct 28 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-1
- Release 3.0.1

* Wed Oct 02 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0-1
- Release 3.0

* Tue Sep 24 2019 Sérgio Basto <sergio@serjux.com> - 2.5.3-4
- BR: the new python3-gobject-devel instead pygobject3-devel (#1749589)

* Thu Sep 05 2019 Sérgio Basto <sergio@serjux.com> - 2.5.3-3
- Remove BR: pygtk2-devel and Requires: pygtkglext (#1738465)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.3-2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.3-1
- Release to 2.5.3
- Switch to Python3 definitively

* Sat Jun 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.2-1
- Release to 2.5.2

* Thu Apr 18 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-1
- Release to 2.5.1

* Wed Mar 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-1
- Release to 2.5.0
- Switch to Python3 on Fedora 29+

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.4.3-3
- Rebuilt (libvpx)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Mon Nov 26 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-2
- Add inotify dependency (rhbz#1653096)

* Fri Nov 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Wed Oct 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1
- Add Python Cairo library BR

* Mon Oct 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-1
- Update to 2.4

* Sun Sep 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Sun Aug 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.2-3
- SPEC file modified for EPEL7

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.7

* Wed Jun 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Sun Jun 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.1-3
- Define build conditions for debugging
- Switch back to Python2 (see xpra.org/trac/ticket/1885) (bz#1583319)

* Sat Jun 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.1-2
- Rebuilt for Python 3.7
- Use --without-strict option

* Wed May 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Thu May 10 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3-1
- Update to 2.3
- Switch to Python3

* Tue Apr 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.6-1
- Update to 2.2.6

* Wed Mar 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.5-1
- Update to 2.2.5

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.4-2
- Add gcc BR

* Fri Feb 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.4-1
- Update to 2.2.4

* Sun Jan 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.3-5
- Rebuild for libvpx again

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> - 2.2.3-4
- rebuild for new libvpx

* Thu Jan 25 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.3-3
- Still require python-gobject on fedora < 27

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.3-2
- Remove obsolete scriptlets

* Thu Jan 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3

* Wed Jan 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.2-2
- Fix python2-gobject as Requires package

* Wed Jan 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-2
- Remove unused directory

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- Appdata file moved into metainfo data directory

* Wed Dec 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2-2
- Fix dependency

* Tue Dec 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2-1
- Update to 2.2
- Split off udev files

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Mon Sep 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Fri Aug 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-2
- Fix Requires

* Fri Aug 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- Replace appdata file with horrible WindowsXP image

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1-2
- Fix Python2 shebang

* Wed Jul 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1-1
- Update to 2.1 (bz#1475316)
- Drop old Werror patch
- Fix systemd files management

* Tue Jul 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Tue May 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- webp option deprecated

* Mon Feb  6 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-1
- Update to 1.0.2
- Drop webp import patch applied upstream

* Sat Dec 10 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0-2
- Disable webp by default, consistent with upstream
  https://www.xpra.org/trac/ticket/1379

* Sat Dec 10 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0-1
- Update to version 1.0
- No longer unbundle javascript libs - shipped versions in html4 client newer than packaged
- Enumerate all bundled js Provides properly
- Improve commentary of Werror patch
- Include all new conf files in pakcage
- Include systemd serice and add BR for systemd

* Tue Nov  8 2016 Orion Poplawski <orion@cora.nwra.com> - 0.17.6-1
- Update to 0.17.6
- Fix build on EPEL7
- Use %%license

* Sat Oct  1 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.17.5-2
- Clean up some rpmlint errors
- Use %%_cups_serverbin if defined
- Use %%{_tmpfilesdir}

* Sun Sep 11 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.17.5-1
- Update to 0.17.5

* Sun Jul 31 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.17.4-1
- Update to 0.17.4

* Fri Jul 22 2016 Tom Callaway <spot@fedoraproject.org> - 0.16.3-5
- rebuild for libvpx 1.6.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 14 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.3-3
- Fix deps for F22

* Thu Apr 14 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.3-2
- Correctly enable use of shared sockets with the xpra group
- Require(pre) for shadow-utils
- Create xpra group during %%pre
- Create and ghost own %%{_localstatedir}/run/lightdm/

* Thu Mar 24 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.3-1
- Update to 0.16.3

* Mon Feb 29 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-8
- Properly enable opencl support on Fedora 23
- Change PyOpenGL requires to python2-opengl on f24 and higher

* Sun Feb 28 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-7
- Change python-imaging dep to python[2]-pillow
- Change python-cups to python2-cups of F24 and higher

* Sun Feb 28 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-6
- Remove python-numeric Requires
- Change python-rencode dep to python2-rencode
- Change python-lz4 dep to python2-lz4

* Mon Feb 22 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-5
- Fix cupslibdir macro to not spew errors during SRPM build

* Fri Feb 19 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-4
- Move icon files back into main package

* Fri Feb 19 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-3
- Drop xpra-0.16.2-move-to-var-run.patch - broken

* Fri Feb 19 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-2
- Add pyopencl Suggests for F23
- No longer move the run script to /var/run - breaks other clients
- Use XDG_RUNTIME_DIR for socket and logs (BZ 1309872)

* Fri Feb 19 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.2-1
- Uodate to 0.16.2 (BZ 1301357)
- Replace gstreamer Requires with gstreamer1 Requires (BZ 1309811)
- Require python-gobject (BZ 1309811)
- No longer Require gstreamer-python (BZ 1309811)
- Require xorg-x11-xauth (BZ 1309804)
- Require dbus-x11 (BZ 1309827)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.1-2
- Split html5 support out into subpackage

* Tue Jan 26 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.1-1
- Update to 0.16.1

* Thu Jan  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.0-3
- Re-add ~/.xpra to socket-dirs for backwards compatibility as second
  in search order

* Thu Jan  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.0-2
- Add patch to Move sockets, log files, script files from ~/.xpra to
  /var/run/user/$UID/xpra

* Thu Jan  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Tue Dec 29 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.10-2
- Rebuild for libwebp 0.5.0

* Sat Dec 19 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.10-1
- Update to 0.15.10

* Wed Dec  2 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.9-1
- Update to 0.15.9

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 0.15.8-3
- rebuild for libvpx 1.5.0

* Mon Nov 30 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.8-2
- Use same options for build and install
- Add csc_opencl support for Fedora 24 and later

* Sat Nov 14 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.8-1
- Update to 0.15.8
- Fix typo in spec file

* Wed Sep 16 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.7-1
- Update to 0.15.7
- Fix typo in spec changelog

* Wed Sep 16 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.6-1
- Update to 0.15.6

* Wed Sep  2 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.15.5-1
- Update to 0.15.5
- Drop patches related to color encoding

* Fri Aug 21 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.4-4
- Remove xpra-r10393.patch and add xpra-r10396.patch and xpra-r10399.patch
  as second attempt to fix the color encoding issues

* Fri Aug 21 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.4-3
- No longer revert r9983, but include xpra-r10393.patch to fix the
  color encoding

* Wed Aug  5 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.4-2
- Add patch to revert upstream commit r9983 which breaks color encodding

* Tue Aug  4 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.4-1
- Update to 0.15.4
- Add missing release tag to previous rpm changelog entry

* Tue Jul 14 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.3-1
- Update to 0.15.3
- Remove xpra-0.15.2-9768.patch
- Add BuildRequires for redhat-lsb-core to make lsb_release available
  at build time (used to detect system type)
- Add --with-Xdummy and --with-Xdummy_wrapper to install options to
  ensure Xdummy is used

* Thu Jul  2 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.2-2
- Add small fix from upsteam (rev 9768)

* Thu Jul  2 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.2-1
- Update to 0.15.2
- Add Requires for python-lz4 and python-cups

* Mon Jun 22 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.1-1
- Update to 0.15.1
- Add Requires shared-mime-info for (/usr/share/mime/packages ownership)
- Add /usr/share/mime/packages/application-x-xpraconfig.xml file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun  4 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.0-2
- Remove extraneous second definition of cupslibdir

* Mon Jun  1 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15.0-1
- Update to 0.15.0
- Add BuildRequires for cups-devel and Requires for cups-filesystem
- Replace mention of avcodec with avcodec2
- Drop xpra-unbundle-rencode.patch, and no longer patch to use system
  rencode
- Drop xpra-0.14-stop-using-void-driver.patch
- Drop xpra-0.14.22-fedora22-xorg.patch

* Wed May 27 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.24-1
- Update to 0.14.24
- Remove Requires for xorg-x11-server-Xvfb
- Remove upstreamed appdata patch

* Tue May 26 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.22-5
- Add patch to correctly locate Xorg binary in Fedora 22 onwards (BZ 1224678)

* Tue Apr 28 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.22-4
- Patch appdata file to have more information and proper paragraph
  ending period so validation works

* Mon Apr 27 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.22-3
- Remove Requires for xorg-x11-drv-void

* Mon Apr 27 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.22-2
- Validate and own /usr/share/appdata/xpra.appdata.xml
- Add BuildRequires libappstream-glib

* Mon Apr 27 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.22-1
- Update to 0.14.22

* Mon Apr 27 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.21-5
- Add patch to remove reference to the xorg void driver in xorg.conf (BZ #1215527)

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 0.14.21-4
- rebuild for libvpx 1.4.0

* Tue Mar 24 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.21-3
- Update license tag from GPLv2+ to GPLv2+ and BSD and LGPLv3+ and MIT

* Mon Mar 23 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.21-2
- Add conditionals for building with ffmpeg and x264 support, disabled
  by default
- Remove Provides for bundled(js-web-socket-js)
- Use system js-zlib on Fedora >= 21
- On Fedora < 21 add Provides for bundled(js-zlib)

* Wed Mar 18 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.21-1
- Update to 0.14.21

* Wed Mar 18 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.19-6
- Unbundle js-query even on Fedora 20

* Wed Mar 18 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.19-5
- Unbundle web-socket-js

* Tue Mar  3 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.19-4
- Add --with-Xdummy and --with-Xdummy_wrapper build options since Xorg
  not installed at build time so autodetection fails

* Tue Mar  3 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.19-3
- Use js-jquery package only on F22 or later - not available on
  earlier distros

* Tue Mar  3 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.19-2
- Update Summary to be more descriptive of package
- Use packaged js-jquery
- Add provides for bundled(js-jquery-ui) and bundled(js-web-socket-js)
- Build with vpx and webp support enabled
- Remove any installed SWF files
- Remove executable flag for all .js files
- Remove Requires for python-webm

* Tue Mar  3 2015 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14.19-1
- Update to upstream 0.14.19
- Add BuildRequires for libxkbfile-devel
- No longer need to unbundle webp
- Rework and rename patch for unbundling of rencode

* Fri Oct 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.6-1
- new upstream release 0.10.6
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-October/000726.html

* Tue Oct 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.4-2
- reenable webp support
- fix webm unbundling to support importing all modules in the webm package
- require latest python-webm so it matches what's bundled upstream

* Mon Oct 07 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.4-1
- rebase to 0.10.4
- don't ship webm stuff that doesn't work without ffmpeg anyway

* Thu Aug 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.8-1
- new upstream release 0.9.8
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-July/000615.html
- use HTTPS for URL and Source0

* Wed Jul 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.6-1
- new upstream release 0.9.6
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-June/000552.html

* Thu Jun 27 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-1
- new upstream release 0.9.5
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-June/000549.html

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.4-1
- new upstream release 0.9.4
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-May/000539.html

* Mon May 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.2-1
- new upstream release 0.9.2
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-May/000525.html

* Fri May 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.1-1
- new upstream release 0.9.1
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-May/000522.html

* Tue May 07 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.0-2
- fix rencode __version__ importing

* Thu May 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.0-1
- new upstream release 0.9.0
  http://lists.devloop.org.uk/pipermail/shifter-users/2013-April/000479.html
- delete the bundled code in prep instead of inside the patches
- don't bother including parti; it's going away upstream soon
- merge python-wimpiggy into main xpra package; it won't be seperated upstream soon

* Thu Apr 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.8-4
- unbundle rencode and webm
- fix equality operator in Requires
- drop unnecessary multiple copies of NEWS
- don't remove buildroot

* Thu Apr 11 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.8-3
- drop unmet dependency on gstreamer-plugins-ugly
- fix permissions on shared objects
- add scriptlets necessary for icon/desktop file

* Thu Mar 28 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.8-2
- disable codecs prohibited in Fedora

* Thu Mar 14 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.8-1
- initial package
