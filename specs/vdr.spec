# TODO, maybe some day:
# - livebuffer patch, http://www.vdr-portal.de/board/thread.php?threadid=37309
# - channelfilter patch, http://www.u32.de/vdr.html#patches
# - pause patch (causes OSD placement issues at least with unrebuilt text2skin)
#   http://www.tolleri.net/vdr/vdr/vdr-1.6.0-2-pause-0.0.1.patch

# - The dvbhddevice plugin is no longer part of the VDR source archive.
#  You can get the latest version of this plugin from the author's repository at
#  https://bitbucket.org/powARman/dvbhddevice.
# - The dvbsddevice and rcu plugins are no longer part of the VDR source archive.
#  You can get the latest versions of these plugins from ftp://ftp.tvdr.de/vdr/Plugins.

%undefine _package_note_flags
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global _hardened_build 1
%bcond_without    docs

%global varbase   %{_var}/lib/vdr
%global videodir  %{varbase}/video
%global vardir    %{varbase}/data
%global plugindir %{_libdir}/vdr
%global configdir %{_sysconfdir}/vdr
%global cachedir  %{_var}/cache/vdr
%global rundir    /run/vdr
%global vdr_user  vdr
%global vdr_group video
# From APIVERSION in config.h
%global apiver    5

Name:           vdr
Version:        2.7.3
Release:        3%{?dist}
Summary:        Video Disk Recorder

License:        GPL-2.0-or-later
URL:            http://www.tvdr.de/
# Get vdr source from http://git.tvdr.de/?p=vdr.git;a=snapshot;h=refs/tags/2.7.3;sf=tbz2
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.sudoers
Source5:        %{name}-reccmds.conf
Source6:        %{name}-commands.conf
Source7:        %{name}-runvdr.sh
Source8:        %{name}-dvbsddevice.conf
Source9:        %{name}-config.sh
Source10:       %{name}-README.package
Source11:       %{name}-skincurses.conf
Source12:       %{name}-dvbhddevice.conf
Source13:       %{name}-timercmds.conf
Source14:       %{name}-shutdown.sh
Source15:       %{name}-moveto.sh
Source16:       %{name}-CHANGES.package.old
Source17:       %{name}.macros
Source18:       http://cdn.debian.net/debian/pool/main/v/vdr/vdr_2.2.0-5.debian.tar.bz2
Source19:       %{name}-check-setup.sh
Source20:       %{name}-rcu.conf
Source21:       %{name}-set-wakeup.sh
Source30:       https://bitbucket.org/powARman/dvbhddevice/get/3473a7b939d7.zip
Source31:       ftp://ftp.tvdr.de/vdr/Plugins/vdr-dvbsddevice-2.2.0.tgz
Source32:       ftp://ftp.tvdr.de/vdr/Plugins/vdr-rcu-2.2.0.tgz

Patch0:         define_AUDIO_GET_PTS.patch
Patch1:         http://zap.tartarus.org/~ds/debian/dists/stable/main/source/vdr_1.4.5-2.ds.diff.gz
Patch2:         http://www.saunalahti.fi/~rahrenbe/vdr/patches/vdr-2.4.6-editrecording.patch.gz
# Extracted from http://copperhead.htpc-forum.de/downloads/extensionpatch/extpngvdr1.7.21v1.diff.gz
Patch3:         %{name}-1.7.21-plugin-missing.patch
Patch4:         %{name}-2.4.0-paths.patch
# http://vdrportal.de/board/thread.php?postid=343665#post343665
Patch5:         12_osdbase-maxitems.patch

# https://www.vdr-portal.de/forum/index.php?thread/136501-vdr-2-7-3-bei-radioaufnahmen-werden-viele-fehler-gez%C3%A4hlt/&postID=1375464#post1375464
Patch6:         %{name}-2.7.3-remux-radio.patch

# Sent upstream 2016-06-17
Patch15:        %{name}-1.7.37-fedora-pkgconfig.patch
# https://www.vdr-portal.de/index.php?attachment/44831-vdr-2-4-6-clearobsoletechannels-diff
Patch99:        %{name}-2.4.6-ClearObsoleteChannels2.diff

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig
BuildRequires:  perl(File::Spec)
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gettext
# systemd >= 186 for scriptlet macros
BuildRequires:  systemd >= 186
BuildRequires:  systemd-devel
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
# udev >= 136-1 for the audio, cdrom, dialout, and video groups
Requires:       udev >= 136-1
# sudo for the shutdown script, >= 1.7.2p2-3 for sudoers.d functionality
Requires:       sudo >= 1.7.2p2-3
# util-linux >= 2.15 for "rtcwake -m no" timer driven wakeups
Requires:       util-linux >= 2.15
Requires:       vdrsymbol-fonts
# shadow-utils >= 4.1.1 for useradd -N
Requires(pre):  shadow-utils >= 2:4.1.1
# systemd >= 189 for RestartPreventExitStatus=
Requires(post,preun,postun): systemd >= 189
Provides:       vdr(abi)%{?_isa} = %{apiver}
Obsoletes:      vdr-subtitles <= 0.5.0
Obsoletes:      vdr-sky < 1.7.11

%description
VDR implements a complete digital set-top-box and video recorder.
It can work with signals received from satellites (DVB-S) as well as
cable (DVB-C) and terrestrial (DVB-T) signals.  At least one DVB card
is required to run VDR.

%package        devel
Summary:        Development files for VDR
Requires:       gettext-runtime
Provides:       vdr-devel(api) = %{apiver}

%description    devel
%{summary}.

%package        docs
Summary:        Developer documentation for VDR
BuildArch:      noarch

%description    docs
%{summary}.

%package        dvbhddevice
Summary:        VDR output device plugin for TechnoTrend S2-6400 DVB cards
Requires:       vdr(abi)%{?_isa} = %{apiver}

%description    dvbhddevice
The dvbhddevice plugin implements a VDR output device for the "Full
Featured TechnoTrend S2-6400" DVB cards.

%package        dvbsddevice
Summary:        VDR output device plugin for full featured SD DVB cards
Requires:       vdr(abi)%{?_isa} = %{apiver}
# To get this subpackage pulled in on upgrades
Obsoletes:      vdr < 1.7.11

%description    dvbsddevice
The dvbsddevice plugin implements the output device for the "Full
Featured" DVB cards based on the TechnoTrend/Fujitsu-Siemens design.

%package        rcu
Summary:        VDR remote control unit plugin
Requires:       vdr(abi)%{?_isa} = %{apiver}
# To get this subpackage pulled in on upgrades
Obsoletes:      vdr < 1.7.25

%description    rcu
The rcu plugin implements a remote control unit for VDR.

%package        skincurses
Summary:        Shell window skin plugin for VDR
BuildRequires:  ncurses-devel
Requires:       vdr(abi)%{?_isa} = %{apiver}

%description    skincurses
The skincurses plugin implements a VDR skin that works in a shell
window, using only plain text output.


%prep
%setup -q -a 18
# dvbhddevice
unzip -o %{SOURCE30} -d $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src
mv $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/powARman-dvbhddevice-3473a7b939d7 $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/dvbhddevice
cd PLUGINS/src
%patch 0 -p3
cd ../..
# dvbsddevice
tar -xzf %{SOURCE31} -C $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src
mv $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/dvbsddevice-2.2.0 $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/dvbsddevice
# rcu
tar -xzf %{SOURCE32} -C $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src
mv $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/rcu-2.2.0 $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/rcu

%patch 1 -p1
# sort_options would be nice, but it conflicts with channel+epg which is nicer
#patch -F 0 -i debian/patches/02_sort_options.dpatch
# TODO: does not apply since 1.7.24
#patch -F 0 -i debian/patches/06_recording_scan_speedup.dpatch
patch -F 2 -i debian/patches/07_blockify_define.dpatch
%patch 2 -p1
%patch 3 -p1
sed \
    -e 's|__CACHEDIR__|%{cachedir}|'   \
    -e 's|__CONFIGDIR__|%{configdir}|' \
    -e 's|__PLUGINDIR__|%{plugindir}|' \
    -e 's|__VARDIR__|%{vardir}|'       \
    -e 's|__VIDEODIR__|%{videodir}|'   \
    %{PATCH4} | %{__patch} -p1
%patch 5 -p1
%patch 6 -p0
%patch 15 -p1
%patch 99 -p1

# Patch APIVERSION TO 2.4.8 to match VDRVERSION
# sed -i 's/2\.4\.3/2.4.8/' config.h
# sed -i 's/20406/20407/' config.h

for f in CONTRIBUTORS HISTORY UPDATE-1.4.0 \
    PLUGINS/src/dvbhddevice/HISTORY; do
    iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f && mv $f.utf8 $f
done

cp -p %{SOURCE5} reccmds.conf
cp -p %{SOURCE13} timercmds.conf
cp -p %{SOURCE6} commands.conf
# Unfortunately these can't have comments in them, so ship 'em empty.
cat /dev/null > channels.conf
cat /dev/null > remote.conf
cat /dev/null > setup.conf
cat /dev/null > timers.conf

install -pm 644 %{SOURCE10} README.package
install -pm 644 %{SOURCE16} CHANGES.package.old

# Would like to do "files {channels,setup,timers}.conf" from config dir
# only, but rename() in cSafeFile barks "device or resource busy", cf.
# http://lists.suse.com/archive/suse-programming-e/2003-Mar/0051.html
cat << EOF > %{name}.rwtab
dirs    %{cachedir}
files   %{configdir}
files   %{vardir}
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
LDFLAGS      = $RPM_LD_FLAGS

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
LIRC_DEVICE  = %{_localstatedir}/run/lirc/lircd
# New Bug 1873027 LIRC_DEVICE  = /run/lirc/lircd
VDR_USER     = \$(shell pkg-config vdr --variable=user)
SDNOTIFY     = 1
EOF

cat << EOF > plugins.mk
LDFLAGS = $RPM_LD_FLAGS
EOF

cp plugins.mk bundled-plugins.mk
cat << EOF >> bundled-plugins.mk
CFLAGS += -I$PWD/include
CXXFLAGS += -I$PWD/include
EOF

cflags="${RPM_OPT_FLAGS/-O2/-O3} -fPIC" # see HISTORY for 1.7.17 for -O3

make vdr.pc BINDIR=%{_bindir} MANDIR=%{_mandir} CONFDIR=%{configdir} \
    VIDEODIR=%{videodir} CACHEDIR=%{cachedir} RESDIR=%{_datadir}/vdr \
    LIBDIR=%{plugindir} LOCDIR=%{_datadir}/locale RUNDIR=%{rundir} \
    VARDIR=%{vardir} VDR_USER=%{vdr_user} VDR_GROUP=%{vdr_group} \
    LDFLAGS="$RPM_LD_FLAGS" CFLAGS="$cflags" \
    CXXFLAGS="$cflags -Werror=overloaded-virtual -Wno-parentheses"

PKG_CONFIG_PATH="$PWD:$PKG_CONFIG_PATH" \
%make_build vdr include-dir i18n

for plugin in dvbhddevice dvbsddevice rcu skincurses ; do
    %make_build -C PLUGINS/src/$plugin VDRDIR=$PWD \
        PLGCFG=$PWD/bundled-plugins.mk all
done

%if %{with docs}
%make_build srcdoc
%endif


%install
# Not using the install-pc target to preserve our already good vdr.pc
install -Dpm 644 vdr.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/vdr.pc

PKG_CONFIG_PATH="$RPM_BUILD_ROOT%{_libdir}/pkgconfig:$PKG_CONFIG_PATH" \
make install-bin install-dirs install-conf install-doc install-i18n \
    install-includes DESTDIR=$RPM_BUILD_ROOT

install -pm 755 epg2html $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_sbindir}
#mv $RPM_BUILD_ROOT%{_bindir}/vdr $RPM_BUILD_ROOT%{_sbindir}

# Avoid mv error by checking if source and destination are the same
if [ "$RPM_BUILD_ROOT%{_bindir}/vdr" != "$RPM_BUILD_ROOT%{_sbindir}/vdr" ]; then
    mv $RPM_BUILD_ROOT%{_bindir}/vdr $RPM_BUILD_ROOT%{_sbindir}
fi

install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d

install -dm 755 $RPM_BUILD_ROOT%{vardir}/themes
touch $RPM_BUILD_ROOT%{vardir}/themes/{classic,sttng}-default.theme

install -pm 755 %{SOURCE7} $RPM_BUILD_ROOT%{_sbindir}/runvdr
sed -i \
    -e 's|/usr/sbin/|%{_sbindir}/|'                    \
    -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|g' \
    -e 's|/usr/lib/vdr\b|%{plugindir}|'                \
    -e 's|VDR_PLUGIN_VERSION|%{apiver}|'               \
    $RPM_BUILD_ROOT%{_sbindir}/runvdr

install -Dm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|' \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr

touch $RPM_BUILD_ROOT%{videodir}/.update

install -dm 755 $RPM_BUILD_ROOT%{plugindir}/bin

install -m 755 %{SOURCE14} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-shutdown.sh
sed -i \
    -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|' \
    -e 's|/var/run/vdr/|%{rundir}/|'                  \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-shutdown.sh

install -m 755 %{SOURCE15} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-moveto.sh
sed -i \
    -e 's|/var/lib/vdr/video|%{videodir}|' \
    -e 's|/etc/vdr/|%{configdir}/|'        \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-moveto.sh

install -m 755 %{SOURCE19} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-check-setup
sed -i \
    -e 's|/etc/vdr/|%{configdir}/|' \
    -e 's|VDR_USER|%{vdr_user}|'    \
    -e 's|VDR_GROUP|%{vdr_group}|'  \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-check-setup

install -m 755 %{SOURCE21} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-set-wakeup
sed -i \
    -e 's|/usr/sbin/|%{_sbindir}/|'  \
    -e 's|/var/run/vdr/|%{rundir}/|' \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-set-wakeup

install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|'        \
    -e 's|/usr/sbin/|%{_sbindir}/|'            \
    -e 's|/usr/share/doc/vdr/|%{_pkgdocdir}/|' \
    $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

install -Dpm 440 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sudoers.d/vdr

touch $RPM_BUILD_ROOT%{cachedir}/epg.data
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/vdr/{logos,plugins}
install -dm 755 $RPM_BUILD_ROOT%{rundir}
touch $RPM_BUILD_ROOT%{rundir}/next-timer
install -dm 755 $RPM_BUILD_ROOT%{vardir}

install -Dpm 644 %{name}.rwtab $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/%{name}

install -dm 755 $RPM_BUILD_ROOT%{_pkgdocdir}
install -pm 644 CHANGES.package.old CONTRIBUTORS \
    HISTORY* INSTALL MANUAL PLUGINS.html README* UPDATE-?.?.0 \
    $RPM_BUILD_ROOT%{_pkgdocdir}
%if %{with docs}
cp -pR srcdoc/html $RPM_BUILD_ROOT%{_pkgdocdir}
%endif

# devel

abs2rel() { perl -MFile::Spec -e 'print File::Spec->abs2rel(@ARGV)' "$@" ; }

install -pm 755 %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/vdr-config
install -pm 755 newplugin $RPM_BUILD_ROOT%{_bindir}/vdr-newplugin
install -pm 644 Make.{config,global} plugins.mk $RPM_BUILD_ROOT%{_libdir}/vdr
ln -s $(abs2rel %{_includedir}/vdr/config.h %{_libdir}/vdr) \
    $RPM_BUILD_ROOT%{_libdir}/vdr
macrodir=%{_sysconfdir}/rpm
[ -d %{_rpmconfigdir}/macros.d ] && macrodir=%{_rpmconfigdir}/macros.d
install -Dpm 644 %{SOURCE17} $RPM_BUILD_ROOT$macrodir/macros.vdr
echo $macrodir/macros.vdr > %{name}-devel.files

# i18n

%find_lang %{name}
sed -i -e '1i%%defattr(-,root,root,-)' %{name}.lang

install -dm 755 $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
echo "d %{rundir} 0755 %{vdr_user} root -" \
    > $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/%{name}.conf
echo "%{_prefix}/lib/tmpfiles.d/%{name}.conf" \
    >> %{name}.lang


# plugins

%make_install -C PLUGINS/src/dvbhddevice
install -pm 644 %{SOURCE12} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/dvbhddevice.conf
%find_lang %{name}-dvbhddevice

%make_install -C PLUGINS/src/dvbsddevice
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/dvbsddevice.conf

%make_install -C PLUGINS/src/rcu
install -pm 644 %{SOURCE20} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/rcu.conf

%make_install -C PLUGINS/src/skincurses
install -pm 644 %{SOURCE11} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
%find_lang %{name}-skincurses


%check
export PKG_CONFIG_PATH=$RPM_BUILD_ROOT%{_libdir}/pkgconfig
if [ "$(pkg-config vdr --variable=apiversion)" != "%{apiver}" ] ; then
    echo "ERROR: API version mismatch in vdr.pc / package / config.h" ; exit 1
fi


%pre
# dialout for serial port remote controllers
getent passwd %{vdr_user} >/dev/null || \
useradd -r -g %{vdr_group} -d %{vardir} -s /sbin/nologin -M -N \
    -G audio,cdrom,dialout -c "Video Disk Recorder" %{vdr_user} || :

%post
%systemd_post %{name}.service
systemctl daemon-reload

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{name}.lang
%{_pkgdocdir}
%exclude %{_pkgdocdir}/PLUGINS.html
%if %{with docs}
%exclude %{_pkgdocdir}/html/
%endif
%config(noreplace) %{_sysconfdir}/sudoers.d/vdr
%config(noreplace) %{_sysconfdir}/sysconfig/vdr
%config(noreplace) %{_sysconfdir}/rwtab.d/%{name}
%config %dir %{_sysconfdir}/sysconfig/vdr-plugins.d/
%{_bindir}/epg2html
%{_bindir}/svdrpsend
%{_sbindir}/runvdr
%{_sbindir}/vdr
%{_unitdir}/%{name}.service
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
%defattr(-,%{vdr_user},%{vdr_group},-)
# TODO: tighten ownerships to root:root for some files in %%{configdir}
%config(noreplace) %{configdir}/*.conf
%dir %{videodir}/
%ghost %{videodir}/.update
%ghost %{vardir}/themes/*.theme
%ghost %{cachedir}/epg.data
%defattr(-,%{vdr_user},root,-)
%dir %{configdir}/
%dir %{configdir}/plugins/
%dir %{rundir}/
%ghost %{rundir}/next-timer
%dir %{vardir}/
%dir %{vardir}/themes/
%dir %{cachedir}/

%files devel -f %{name}-devel.files
%{!?_with_docs:%dir %{_pkgdocdir}}
%license COPYING
%if ! %{with docs}
%{_pkgdocdir}/PLUGINS.html
%endif
%{_bindir}/vdr-config
%{_bindir}/vdr-newplugin
%{_includedir}/libsi/
%{_includedir}/vdr/
%{_libdir}/pkgconfig/vdr.pc
%dir %{_libdir}/vdr/
%{_libdir}/vdr/Make.config
%{_libdir}/vdr/Make.global
%{_libdir}/vdr/config.h
%{_libdir}/vdr/plugins.mk

%if %{with docs}
%files docs
%dir %{_pkgdocdir}
%license COPYING
%{_pkgdocdir}/PLUGINS.html
%{_pkgdocdir}/html/
%endif

%files dvbhddevice -f %{name}-dvbhddevice.lang
%license PLUGINS/src/dvbhddevice/COPYING
%doc PLUGINS/src/dvbhddevice/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/dvbhddevice.conf
%{plugindir}/libvdr-dvbhddevice.so.%{apiver}

%files dvbsddevice
%license PLUGINS/src/dvbsddevice/COPYING
%doc PLUGINS/src/dvbsddevice/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/dvbsddevice.conf
%{plugindir}/libvdr-dvbsddevice.so.%{apiver}

%files rcu
%license PLUGINS/src/rcu/COPYING
%doc PLUGINS/src/rcu/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/rcu.conf
%{plugindir}/libvdr-rcu.so.%{apiver}

%files skincurses -f %{name}-skincurses.lang
%license PLUGINS/src/skincurses/COPYING
%doc PLUGINS/src/skincurses/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
%{plugindir}/libvdr-skincurses.so.%{apiver}


%changelog
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
