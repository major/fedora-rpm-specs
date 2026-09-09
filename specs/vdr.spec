%global varbase   %{_var}/lib/vdr
%global videodir  %{varbase}/video
%global vardir    %{varbase}/data
%global plugindir %{_libdir}/vdr
%global configdir %{_sysconfdir}/vdr
%global cachedir  %{_var}/cache/vdr
%global rundir    /run/vdr
%global vdr_user  vdr
%global vdr_group video

%bcond_without    docs

%global __provides_exclude_from ^%{plugindir}/.*\\.so.*$

Name:           vdr
Version:        2.8.2
Release:        3%{?dist}
Summary:        Video Disk Recorder

License:        GPL-2.0-or-later
URL:            https://www.tvdr.de/
Source0:        https://git.tvdr.de/?p=vdr.git;a=snapshot;h=refs/tags/%{version};sf=tbz2#/%{name}-%{version}.tar.bz2

# The plugin ABI version, extracted from config.h in the tarball at parse
# time.  Must stay below Source0: the %%() shell runs when %%global is
# defined, so %%{S:0} has to exist already.  Fallback 0 for spec-only tools
# (rpmlint); %%check verifies the packaged value against vdr.pc.
%global apiver %(v=$(tar -xOf %{S:0} %{name}-%{version}/config.h 2>/dev/null | sed -ne '/define APIVERSION/s/^.*"\\(.*\\)".*$/\\1/p' | head -n1); echo ${v:-0})

Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.sudoers
Source4:        %{name}.macros
Source5:        %{name}-reccmds.conf
Source6:        %{name}-commands.conf
Source7:        %{name}-timercmds.conf
Source8:        %{name}-skincurses.conf
Source9:        %{name}-README.package
Source10:       %{name}-runvdr.sh
Source11:       %{name}-config.sh
Source12:       %{name}-shutdown.sh
Source13:       %{name}-moveto.sh
Source14:       %{name}-check-setup.sh
Source15:       %{name}-set-wakeup.sh

# Fedora/FHS integration: export datadir/rundir/vardir/user/group from vdr.pc
Patch:          %{name}-fedora.patch
# MainMenuHooks, reduced to the only hook any shipped plugin implements
# (epgsearch's "Replace original schedule").
Patch:          %{name}-mainmenuhooks.patch
# Sent upstream: replace the FSF's stale postal address in COPYING with the
# license URLs; rpmlint rejects the old address.
Patch:          %{name}-fsf-address.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  libcap-devel
BuildRequires:  libjpeg-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  sudo
BuildRequires:  systemd-rpm-macros
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

# sudo authorizes the shutdown script's privileged commands (sudoers.d/vdr);
# util-linux provides "rtcwake -m no" for timer-driven wakeups
Requires:       sudo
Requires:       util-linux
Requires:       vdrsymbol-fonts
%{?systemd_requires}
Provides:       vdr(abi)%{?_isa} = %{apiver}

%description
VDR implements a complete digital set-top-box and video recorder.
It can work with signals received from satellites (DVB-S) as well as
cable (DVB-C) and terrestrial (DVB-T) signals. At least one DVB card
is required to run VDR.

%package        devel
Summary:        Development files for VDR
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gettext-runtime
Provides:       vdr-devel(api) = %{apiver}

%description    devel
Headers, pkg-config file and RPM macros needed to build VDR plugins.

%package        docs
Summary:        Developer documentation for VDR
BuildArch:      noarch

%description    docs
Developer documentation for the VDR core, generated from its sources.

%package        skincurses
Summary:        Shell window skin plugin for VDR
Requires:       vdr(abi)%{?_isa} = %{apiver}

%description    skincurses
The skincurses plugin implements a VDR skin that works in a shell
window, using only plain text output.


%prep
%autosetup -p1

for f in CONTRIBUTORS HISTORY ; do
    iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f && mv $f.utf8 $f
done

cp -p %{SOURCE5} reccmds.conf
cp -p %{SOURCE6} commands.conf
cp -p %{SOURCE7} timercmds.conf
install -pm 644 %{SOURCE9} README.package

printf '\n' > channels.conf
printf '\n' > remote.conf
printf '\n' > setup.conf
printf '\n' > timers.conf

cat << EOF > %{name}.sysusers
u %{vdr_user} -:%{vdr_group} 'Video Disk Recorder' %{vardir} -
m %{vdr_user} audio
EOF

# Disable some graphs that end up too big to be useful.
for g in COLLABORATION INCLUDE INCLUDED_BY ; do
    sed -i -e 's/^\(\s*'$g'_GRAPH\s*=\s*\).*/\1NO/' Doxyfile
done


%build
cat << EOF > Make.config
CC           = %{__cc}
CXX          = %{__cxx}

CFLAGS       = \$(shell pkg-config vdr --variable=cflags)
CXXFLAGS     = \$(shell pkg-config vdr --variable=cxxflags)
LDFLAGS      = %{build_ldflags}

PREFIX       = %{_prefix}
MANDIR       = \$(shell pkg-config vdr --variable=mandir)
BINDIR       = \$(shell pkg-config vdr --variable=bindir)

LOCDIR       = \$(shell pkg-config vdr --variable=locdir)
PLUGINLIBDIR = \$(shell pkg-config vdr --variable=libdir)
VIDEODIR     = \$(shell pkg-config vdr --variable=videodir)
CONFDIR      = \$(shell pkg-config vdr --variable=configdir)
CACHEDIR     = \$(shell pkg-config vdr --variable=cachedir)
RESDIR       = \$(shell pkg-config vdr --variable=resdir)
INCDIR       = %{_includedir}
LIBDIR       = \$(PLUGINLIBDIR)

PLGCFG       = \$(LIBDIR)/plugins.mk
LIRC_DEVICE  = /run/lirc/lircd
VDR_USER     = \$(shell pkg-config vdr --variable=user)
SDNOTIFY     = 1
EOF

cat << EOF > plugins.mk
LDFLAGS = %{build_ldflags}
EOF

cp plugins.mk bundled-plugins.mk
cat << EOF >> bundled-plugins.mk
CFLAGS += -I$PWD/include
CXXFLAGS += -I$PWD/include
EOF

cflags="%{build_cflags} -fPIC"

make vdr.pc BINDIR=%{_bindir} MANDIR=%{_mandir} CONFDIR=%{configdir} \
    VIDEODIR=%{videodir} CACHEDIR=%{cachedir} RESDIR=%{_datadir}/vdr \
    LIBDIR=%{plugindir} LOCDIR=%{_datadir}/locale RUNDIR=%{rundir} \
    VARDIR=%{vardir} VDR_USER=%{vdr_user} VDR_GROUP=%{vdr_group} \
    LDFLAGS="%{build_ldflags}" CFLAGS="$cflags" \
    CXXFLAGS="$cflags -Werror=overloaded-virtual -Wno-parentheses"

PKG_CONFIG_PATH="$PWD:$PKG_CONFIG_PATH" \
%make_build vdr include-dir i18n

%make_build -C PLUGINS/src/skincurses VDRDIR=$PWD \
    PLGCFG=$PWD/bundled-plugins.mk all

%if %{with docs}
%make_build srcdoc
%endif


%install
# Not using the install-pc target to preserve our already good vdr.pc
install -Dpm 644 vdr.pc %{buildroot}%{_libdir}/pkgconfig/vdr.pc

PKG_CONFIG_PATH="%{buildroot}%{_libdir}/pkgconfig:$PKG_CONFIG_PATH" \
make install-bin install-dirs install-conf install-doc install-i18n \
    install-includes DESTDIR=%{buildroot}

install -pm 755 epg2html %{buildroot}%{_bindir}

install -dm 755 %{buildroot}%{configdir}/plugins
install -dm 755 %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d
install -dm 755 %{buildroot}%{vardir}
install -dm 755 %{buildroot}%{configdir}/themes
install -dm 755 %{buildroot}%{_datadir}/vdr/{logos,plugins}
install -dm 755 %{buildroot}%{plugindir}/bin

touch %{buildroot}%{configdir}/themes/{classic,sttng}-default.theme
touch %{buildroot}%{videodir}/.update
touch %{buildroot}%{cachedir}/epg.data

install -pm 755 %{SOURCE10} %{buildroot}%{_bindir}/runvdr
sed -i \
    -e 's|/usr/sbin/|%{_bindir}/|'                     \
    -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|g' \
    -e 's|/usr/lib/vdr\b|%{plugindir}|'                \
    -e 's|VDR_PLUGIN_VERSION|%{apiver}|'               \
    %{buildroot}%{_bindir}/runvdr

install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/vdr
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|' \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr

install -pm 755 %{SOURCE12} %{buildroot}%{plugindir}/bin/%{name}-shutdown.sh
sed -i \
    -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|' \
    -e 's|/var/run/vdr/|%{rundir}/|'                  \
    -e 's|/usr/lib/vdr/|%{plugindir}/|'               \
    %{buildroot}%{plugindir}/bin/%{name}-shutdown.sh

install -pm 755 %{SOURCE13} %{buildroot}%{plugindir}/bin/%{name}-moveto.sh
sed -i \
    -e 's|/var/lib/vdr/video|%{videodir}|' \
    -e 's|/etc/vdr/|%{configdir}/|'        \
    %{buildroot}%{plugindir}/bin/%{name}-moveto.sh

install -pm 755 %{SOURCE14} %{buildroot}%{plugindir}/bin/%{name}-check-setup
sed -i \
    -e 's|/etc/vdr/|%{configdir}/|' \
    -e 's|VDR_USER|%{vdr_user}|'    \
    -e 's|VDR_GROUP|%{vdr_group}|'  \
    %{buildroot}%{plugindir}/bin/%{name}-check-setup

install -pm 755 %{SOURCE15} %{buildroot}%{plugindir}/bin/%{name}-set-wakeup
sed -i \
    -e 's|/usr/sbin/|%{_bindir}/|'   \
    -e 's|/var/run/vdr/|%{rundir}/|' \
    %{buildroot}%{plugindir}/bin/%{name}-set-wakeup

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|'        \
    -e 's|/usr/sbin/|%{_bindir}/|'             \
    -e 's|/usr/share/doc/vdr/|%{_pkgdocdir}/|' \
    %{buildroot}%{_unitdir}/%{name}.service

install -Dpm 440 %{SOURCE3} %{buildroot}%{_sysconfdir}/sudoers.d/vdr
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|' \
    %{buildroot}%{_sysconfdir}/sudoers.d/vdr
install -Dpm 644 %{name}.sysusers %{buildroot}%{_sysusersdir}/%{name}.conf

install -dm 755 %{buildroot}%{_pkgdocdir}
install -pm 644 CONTRIBUTORS HISTORY* INSTALL MANUAL PLUGINS.html \
    README* %{buildroot}%{_pkgdocdir}
%if %{with docs}
cp -pR srcdoc/html %{buildroot}%{_pkgdocdir}
%endif

# devel

install -pm 755 %{SOURCE11} %{buildroot}%{_bindir}/vdr-config
install -pm 755 newplugin %{buildroot}%{_bindir}/vdr-newplugin
install -pm 644 Make.{config,global} plugins.mk %{buildroot}%{plugindir}
ln -sr %{buildroot}%{_includedir}/vdr/config.h %{buildroot}%{plugindir}
install -Dpm 644 %{SOURCE4} %{buildroot}%{_rpmmacrodir}/macros.vdr

# plugins

%make_install -C PLUGINS/src/skincurses
install -pm 644 %{SOURCE8} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf

%find_lang %{name}
%find_lang %{name}-skincurses


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config vdr --variable=apiversion)" = "%{apiver}"
test "$(pkg-config vdr --modversion)" = "%{version}"
# The Fedora patch must have taken effect
test "$(pkg-config vdr --variable=user)" = "%{vdr_user}"
test "$(pkg-config vdr --variable=vardir)" = "%{vardir}"
# The MainMenuHooks patch must have taken effect
grep -q 'MainMenuHooksPatch-v1.0::osSchedule' vdr
# The FSF address patch must have taken effect (rpmlint rejects the old address)
! grep -qr 'Franklin' COPYING PLUGINS/src/skincurses/COPYING
# vdr resolves VDRPluginCreator after dlopen; a plugin without that export
# is broken even if it links cleanly
nm -D --defined-only %{buildroot}%{plugindir}/libvdr-skincurses.so.%{apiver} | grep -q ' VDRPluginCreator$'
# The sudoers drop-in must parse
visudo -cf %{buildroot}%{_sysconfdir}/sudoers.d/vdr


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files -f %{name}.lang
%license COPYING
%{_pkgdocdir}
%if %{with docs}
%exclude %{_pkgdocdir}/html/
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/vdr
%config %dir %{_sysconfdir}/sysconfig/vdr-plugins.d/
%{_bindir}/epg2html
%{_bindir}/runvdr
%{_bindir}/svdrpsend
%{_bindir}/vdr
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%config(noreplace) %attr(0440,root,root) %{_sysconfdir}/sudoers.d/vdr
%dir %{plugindir}/
%dir %{plugindir}/bin/
%{plugindir}/bin/%{name}-check-setup
%{plugindir}/bin/%{name}-moveto.sh
%{plugindir}/bin/%{name}-set-wakeup
%{plugindir}/bin/%{name}-shutdown.sh
%{_datadir}/vdr/
%{_mandir}/man1/svdrpsend.1*
%{_mandir}/man1/vdr.1*
%{_mandir}/man5/vdr.5*
%dir %{varbase}/
%attr(-,%{vdr_user},%{vdr_group}) %config(noreplace) %{configdir}/*.conf
%dir %attr(-,%{vdr_user},%{vdr_group}) %{videodir}/
%ghost %attr(-,%{vdr_user},%{vdr_group}) %{videodir}/.update
%ghost %attr(-,%{vdr_user},%{vdr_group}) %{configdir}/themes/*.theme
%ghost %attr(-,%{vdr_user},%{vdr_group}) %{cachedir}/epg.data
%dir %attr(-,%{vdr_user},root) %{configdir}/
%dir %attr(-,%{vdr_user},root) %{configdir}/plugins/
%dir %attr(-,%{vdr_user},root) %{vardir}/
%dir %attr(-,%{vdr_user},root) %{configdir}/themes/
%dir %attr(-,%{vdr_user},root) %{cachedir}/

%files devel
%license COPYING
%{_bindir}/vdr-config
%{_bindir}/vdr-newplugin
%{_includedir}/libsi/
%{_includedir}/vdr/
%{_libdir}/pkgconfig/vdr.pc
%{_rpmmacrodir}/macros.vdr
%{plugindir}/Make.config
%{plugindir}/Make.global
%{plugindir}/config.h
%{plugindir}/plugins.mk

%if %{with docs}
%files docs
%license COPYING
%{_pkgdocdir}/html/
%endif

%files skincurses -f %{name}-skincurses.lang
%license PLUGINS/src/skincurses/COPYING
%doc PLUGINS/src/skincurses/HISTORY PLUGINS/src/skincurses/README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
%{plugindir}/libvdr-skincurses.so.%{apiver}


%changelog
* Thu Aug 13 2026 Dirk Nehring  <dnehring@gmx.net> - 2.8.2-3
- Refactor the spec file
- Themes live in /etc/vdr/themes: stock VDR's path, now that the old
  theme-directory rewriting patch is gone
- vdr-devel now requires the base package (fully versioned, arch-specific)

* Fri Jul 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue Jun 23 2026 Martin Gansser <martinkg@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2 API version 13

* Mon Mar 23 2026 Martin Gansser <martinkg@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Mon Feb 09 2026 Martin Gansser <martinkg@fedoraproject.org> - 2.7.9-1
- Update to 2.7.9
- Add vdr-2.7.9-remove-leftover-path.diff
- Add vdr-2.7.9-last-replayed-per-folder-05.diff

* Thu Jan 22 2026 Martin Gansser <martinkg@fedoraproject.org> - 2.7.8-1
- Update to 2.7.8

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Martin Gansser <martinkg@fedoraproject.org> - 2.7.7-1
- Update to 2.7.7

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jun 21 2025 Martin Gansser <martinkg@fedoraproject.org> - 2.7.6-1
- Update to 2.7.6

* Tue May 27 2025 Martin Gansser <martinkg@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5
- Add vdr-2.7.5-override-keyword.patch

* Sun May 11 2025 Peter Bieringer <pb@bieringer.de> - 2.7.4-3
- Re-add MainMenuHooks patch for 2.7.x

* Thu Apr 24 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.7.4-2
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Wed Feb 26 2025 Martin Gansser <martinkg@fedoraproject.org> - 2.7.4-1
- Update to 2.7.4
- Add vdr-2.7.4-fedora-pkgconfig.patch

* Fri Jan 24 2025 Martin Gansser <martinkg@fedoraproject.org> - 2.7.3-3
- Fix FTBFS #2341505

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.7.3-1
- Update to 2.7.3
- Use recent dvbhddevice Source file 3473a7b939d7.zip
- Add %%{name}-2.7.3-remux-radio.patch

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.6.9-1
- Update to 2.6.9

* Sun Jul 14 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.6.8-2
- Add vdr-2.6.8-fix-timeout-open-frontend.diff.txt
- Add vdr-2.6.8-fix-pause-epg-scan.diff.txt

* Tue Jul 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.6.8-1
- Update to 2.6.8
- Add strreplace.patch

* Tue Apr 02 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.6.7-1
- Update to 2.6.7

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.6.6-1
- Update to 2.6.6

* Wed Jan 03 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.6.5-1
- Update to 2.6.5
- vdr-devel does not require any translation management tools (BZ#2119032)
  use RR gettext-runtime

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Martin Gansser <martinkg@fedoraproject.org> - 2.6.4-1
- Update to 2.6.4

* Fri Feb 10 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for rawhide

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3
- Dropped vdr-2.6.2-remux.patch
- Dropped vdr-2.6.2-index-file-regeneration-failed.patch

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.6.2-2
- Add vdr-2.6.2-index-file-regeneration-failed.patch

* Wed Nov 30 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2
- Add vdr-2.6.2-remux.patch

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Sat Jan 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.6.0-4
- Add vdr-2.6.0-fix-dvbplayer.diff
- Add %%undefine _package_note_flags

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.6.0-2
- Reenable mainmenuhooks patch opt-42-x_MainMenuHooks-v1.0.3.patch
- Add vdr-2.6.0-eit.patch to fix epg handling transaction logic

* Wed Dec 29 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Wed Dec 29 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.8-1
- Update to 2.4.8

* Thu Oct 21 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.7-5
- Delete missing kernel header files #Source33 because they are
  available again in kernel-headers-5.14.0-300 package

* Tue Aug 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.7-4
- Add missing kernel-header files audio.h osd.h and video.h via #Source33
- Add missing-kernel-headers.patch fixes (BZ#1989125) (BZ#1988085)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.7-2
- Add vdr-2.4.7_gcc11.patch

* Fri Apr 23 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.7-1
- Update to 2.4.7

* Tue Feb 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.6-7
- Add systemd watchdog support in to unit file vdr.service
- Add systemctl daemon-reload, because after every update of vdr,
  it claims about missing systemd daemon-reload

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.6-5
- Add modified vdr-2.4.4-RecordingInfo.patch for extrecmenung plugin

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.6-4
- Add vdr-2.4.4-RecordingInfo.patch for extrecmenung plugin
- Add mcli to sysconfig's VDR_PLUGIN_ORDER
- Add extrecmenung to sysconfig's VDR_PLUGIN_ORDER

* Thu Jan 07 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.6-3
- Add modified vdr-2.4.6-ClearObsoleteChannels2.diff

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.6-2
- Add vdr-2.4.6-ClearObsoleteChannels.diff

* Mon Dec 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.6-1
- Update to 2.4.6
- Re-add vdr-2.4.6-editrecording.patch.gz
- Drop vdr-2.4.1-mark-obsolete-NidTid.patch
- set execution permission Doxyfile.filter
- Force C++14 as this code is not C++17 ready, needed for gcc11

* Wed Aug 26 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.4-1
- Update to 2.4.4
- Add vdr-2.4.1-mark-obsolete-NidTid.patch
- Dropped vdr-2.4.1-skincurses-log-errors.patch
- Dropped vdr-2.4.1-glibc231.patch
- Dropped vdr-2.4.1-editrecording.patch.gz
- Dropped vdr-2.4.1-lcn-support-v2.patch.gz

* Fri Aug 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-8
- Rebuilt for rawhide

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-6
- Rebuilt for rawhide

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-4
- Modify %%{name}-2.4.1-glibc231.patch

* Sat Dec 14 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-3
- Add %%{name}-2.4.1-glibc231.patch

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.1-1
- Dropped Patch5 vdr-2.4.0-01-fix-svdrp-modt-recflag.diff
- Ccustomized Patch6 vdr-2.4.1-skincurses-log-errors.patch
- Add vdr-2.4.0-lcn-support-v2.patch.gz
- Add vdr-2.4.1-editrecording.patch.gz
- Fix systemd-tmpfiles migration warning, rundir from %%{_var}/run/vdr to /run/vdr

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-5
- Rebuild for tinyxml2 7.x

* Sun Oct 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-4
- Re-add dvbsddevice Plugin
- Re-add rcu Plugin

* Fri Sep 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-3
- Add BR gcc
- Add BR gcc-c++
- Update to dvbhddevice-2ea854ae8c7a
- Add define_AUDIO_GET_PTS.patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-1
- Dropped dvbsddevice and rcu plugins
- SPEC File cleanup
- Dropped patch9  vdr-1.7.29-hlcutter-0.2.3.diff
- Dropped patch14 0001-Fix-build-with-systemd-230.patch
- Dropped patch19 vdr-2.2.0-menuselection.patch
- Dropped Patch20 %%{name}-2.3.2-unsignedtosigned.diff
- Dropped Patch21 %%{name}-gcc7-fix.patch
- Add %%{name}-2.4.0-01-fix-svdrp-modt-recflag.diff
- Add skincurses-log-errors.patch
- Add 12_osdbase-maxitems.patch

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.0-14
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 2.2.0-11
- Add %%{name}-2.3.2-unsignedtosigned.diff
- Add %%{name}-gcc7-fix.patch

* Fri Jun 17 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-10
- Patch to fix build with systemd >= 230 (#1347724)
- Drop %%{_licensedir} conditionals

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-8
- Require vdrsymbol-fonts instead of an arbitrary English font
- Order service after sound.target (in absence of dvb.target)
- Update LCN support patch

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-6
- Drop udev rules (#1226698)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 13 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-4
- Add LCN support patch by Rolf Ahrenberg
- Don't chdir to /tmp in runvdr, no longer necessary with systemd

* Sat Feb 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-3
- Add edit recording patch by Rolf Ahrenberg
- Make use of systemd notification in service

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-2
- Enable systemd notification support
- Refresh some patches

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-1
- Update to 2.2.0

* Wed Jan 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.7-1
- Update to 2.0.7
- Mark license files as %%license where available

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  9 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.6-4
- Disable previous patch, causes crashes

* Wed May  7 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.6-3
- Add epghandler segment transfer patch for epg2vdr.

* Mon Mar 31 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.6-2
- Bring back NALU dump patch

* Sat Mar 22 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.6-1
- Update to 2.0.6
- Drop NALU dump (N/A for 2.0.6 at the moment) and resumereset patches
- Bring back jumpplay patch from yavdr

* Tue Jan  7 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.5-1
- Update to 2.0.5, starting after lirc.service is no longer needed.
- Remove restart logic from runvdr, handle it with systemd instead.
- Drop DVB reloading logic due to the above change.
- Use stdout/err for script log messages and let systemd route them.
- Get locale settings from /etc/locale.conf, not /etc/sysconfig/i18n.
- Use systemd macros in scriptlets (#850358).

* Wed Dec 11 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.4-2
- Use main package's doc dir in -devel and -docs.
- Use upstream copy of NALU dump patch.

* Wed Oct 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.4-1
- Update to 2.0.4.

* Mon Sep  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.3-1
- Update to 2.0.3.

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.0.2-4
- Perl 5.18 rebuild

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-3
- Honor %%{_pkgdocdir} where available.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0.2-2
- Perl 5.18 rebuild

* Mon May 20 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-1
- Update to 2.0.2.

* Sat Apr 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-1
- Update to 2.0.1.

* Sun Apr  7 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-2
- Update vasarajanauloja patch to 2.0.0.
- Apply upstream cDevice::keepTracks init patch.

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-1
- Update to 2.0.0.
- Move pre-1.7 changelog entries to CHANGES.package.old.

* Sat Mar 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.42-2
- Fix API version.

* Sat Mar 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.42-1
- Update to 1.7.42.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.41-1
- Update to 1.7.41.
- Move macros.vdr to %%{_rpmconfigdir}/macros.d where applicable.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.40-1
- Update to 1.7.40.

* Sun Mar  3 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.39-2
- Move tmpfiles.d snippet to %%{_prefix}/lib/tmpfiles.d, make it more friendly
  to plugin specific subdirs.

* Sun Mar  3 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.39-1
- Update to 1.7.39.
- Apply Udo Richter's NALU dump patch.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.38-1
- Update to 1.7.38; hard link cutter and jumpplay are temporarily not included,
  and some variables in *.pc and macros have changed.
- Drop no longer needed sysv-to-systemd migration scriptlets.
- Drop After=syslog.target from systemd unit file.
- Drop deprecated %%{_isa}-less vdr(abi) provision.
- Misc specfile cleanups.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.7.31-4
- rebuild due to "jpeg8-ABI" feature drop

* Sat Dec 22 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.31-3
- Fix build with DVB API 5.8 (upstream).
- Do not mark recordings as new when removing marks at EOF (Rolf Ahrenberg).
- Require font(:lang=en) [#863720].

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.7.31-2
- rebuild against new libjpeg

* Tue Oct  2 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.31-1
- Update to 1.7.31.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.30-1
- Update to 1.7.30.
- Add Documentation entries to systemd service.

* Wed Jul 18 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.29-1
- Update to 1.7.29.

* Wed Jun 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.28-1
- Update to 1.7.28.
- Add softhdddevice to sysconfig's VDR_PLUGIN_ORDER.

* Mon Apr 23 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.27-2
- Build with hardening flags on.
- Update hlcutter patch to 0.2.3.
- Patch to build libhdffcmd with our CFLAGS.
- Sync CXXFLAGS in Make.config with upstream.

* Mon Mar 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.27-1
- Update to 1.7.27, re-enable legacy receiver code for now.

* Sun Mar 18 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.26-2
- Apply Rolf Ahrenberg's subtitles fix.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.26-1
- Update to 1.7.26.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.25-1
- Update to 1.7.25; RCU functionality split into -rcu plugin subpackage.

* Tue Feb 21 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.24-3
- Apply upstream dvbplayer 50fps reload patch.

* Tue Feb 21 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.24-2
- Revert only problematic dvbplayer changes to 1.7.23, thanks to Udo Richter.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.24-1
- Update to 1.7.24 sans dvbplayer changes that broke some output plugins.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.23-1
- Update to 1.7.23.
- Migrate to systemd.
- runvdr cleanups.

* Wed Jan  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.22-2
- Fix build with g++ 4.7.0.
- Turn on teletext subtitles by default for 1.6.x backwards compat.

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.22-1
- Update to 1.7.22.
- Build docs by default.

* Thu Nov 17 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.21-2
- Update liemikuutio patch to 1.33.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.21-1
- Update to 1.7.21.
- Clean up specfile constructs no longer needed with Fedora or EL6+.
