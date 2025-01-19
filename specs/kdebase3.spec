%global debug_package %{nil}

%define _default_patch_fuzz 2

%define debug 0 
%define final 1 
%define redhatify 1
%define arts 1

%define _with_libutempter 1
%define _with_samba --with-samba

# make -pim-ioslaves subpkg
%define pim 1

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name:    kdebase3
Summary: KDE 3 core files
Version: 3.5.10
Release: 84%{?dist}

# programs: GPLv2, libs: LGPLv2
License: GPL-2.0-only
Url: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebase-%{version}.tar.bz2

Source1: konsole.desktop

Source5: kde-np.pamd
Source6: logrotate-kdm
Source7: mailsettings.cc
Source8: env.sh
Source9: cr16-app-package_games_kids.png
Source10: cr32-app-package_games_kids.png
Source11: cr48-app-package_games_kids.png

Source50:   kde-np-legacy.pamd
Source1001: kde.pamd
Source1002: kde-legacy.pamd

Patch0: kdebase-3.5.5-redhat-pam.patch
Patch1: kdebase-3.5.9-redhat-startkde.patch
Patch2: kdebase-3.3.92-vroot.patch
Patch3: kdebase-3.x-shortcuts.patch
Patch4: kdebase-3.2.0-keymap.patch
Patch5: kdebase-3.1-startpage.patch
Patch6: kdebase-3.1.3-konsole-double-esc.patch
Patch7: kdebase-3.3.92-kpersonalizer.patch
Patch8: kdebase-3.2.92-logo.patch 
Patch10: kdebase-3.4.2-kdesktop-konsole.patch
Patch11: kdebase-3.5.1-xdg.patch
Patch13: kdebase-3.5.5-dbus.patch
Patch14: kdebase-3.5.1-kdm-readme.patch
Patch15: kdebase-3.5.1-konsole-fonts.patch
Patch18: kdebase-3.5.2-kconf_update-klipper.patch
Patch20: kdebase-3.5.5-keyinit.patch
Patch21: kdebase-3.5.3-khelpcenter-sort.patch
Patch22: kdebase-3.5.4-htdig.patch
Patch24: kdebase-3.5.4-tango-icon-theme.patch
Patch25: kdebase-3.5.4-konqueror-shortcut.patch
Patch26: kdebase-3.5.5-suspend.patch
Patch27: kdebase-3.5.8-consolekit-kdm.patch
Patch28: kdebase-3.5.6-kdm-alternatebackground.patch
Patch30: kdebase-3.5.7-kio_media_mounthelper.patch
# kdebase: "Root Shell" sessions will not close, http://bugzilla.redhat.com/301841
Patch31: kdebase-3.5.10-konsolesu-kdesu.patch
# modified version of kubuntu_9915_userdiskmount.diff
# fixes NTFS (#378041) and adds PolicyKit support (#428212)
Patch36: kdebase-3.5.9-userdiskmount.patch
# don't link kcm_colors against libkrdb (and don't call runRdb)
Patch37: kdebase-3.5.10-libkrdb_dep.patch
# find the Samba 4 libsmbclient.h using pkg-config (fixes FTBFS)
Patch39: kdebase-3.5.10-samba4.patch
# remove obsolete MimeType from printmgr/printers.desktop (#587568)
# patch by Ilya Chernykh from openSUSE
Patch40: kdebase-3.5.10-printmanager-desktop-fix.patch
# patch to use libtirpc for RPC, from Cygwin Ports
# https://github.com/cygwinports/kdebase3/blob/master/3.5.10-libtirpc.patch
Patch41: kdebase-3.5.10-libtirpc.patch
Patch42: kdebase-3.5.10-uic.patch

# http://aseigo.blogspot.com/2008/10/dear-kde3-kdesktop-users.html
Patch100: kdebase-3.5.10-minicli-decimal-comma.patch

## Trinity backports
# OpenSSL 1.1 support by Slávek Banko (with prerequisite patches by Timothy
# Pearson), backported by Kevin Kofler
# The patch also fixes OpenSSL 1.0 support, by using the KSSLProxy abstraction.
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=30e57327d5921be080bad5394860fce33b7c3f74
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=4040124e875f442f1ef618c669e108a3d2bc9662
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=48c6b8ff3d2cac37dccce46db29499a14fb025b1
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=d9b4ee04db7e614a59470acc38a6482c15aed032
Patch150: kdebase-3.5.10-openssl-1.1.patch
Patch151: kdebase3-configure-c99.patch

# security fixes

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# fix for autoconf 2.7x
Patch304: kde3-autoconf-version.patch
# fix FTBFS due to gcc14
Patch305: kdebase3-ftbfs-gcc14.patch
Patch306: kdebase3-autoconf-2.72.patch

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?extras} == 0
Obsoletes: kdebase-extras < 6:%{version}-%{release}
Provides: kdebase-extras = 6:%{version}-%{release}
%endif
%if 0%{?pim}
Requires: kdebase3-pim-ioslaves = %{version}-%{release}
%else
Obsoletes: kdebase3-pim-ioslaves < %{version}-%{release}
Provides: kdebase3-pim-ioslaves = %{version}-%{release}
%endif

#Requires(post): coreutils fileutils
#Requires(postun): coreutils fileutils
# /sbin/fuser
Requires: psmisc

%ifnarch s390 s390x
Requires: eject
%endif

BuildRequires: kdelibs3-devel >= %{version}-16
BuildRequires: libxslt-devel libxml2-devel
%if 0%{?_with_samba:1}
BuildRequires: libsmbclient-devel
%endif
BuildRequires: pam-devel
BuildRequires: gettext
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: sed
BuildRequires: automake libtool
BuildRequires: pkgconfig
BuildRequires: doxygen
%ifarch %{ix86} x86_64 ia64 ppc ppc64
%define _with_suspend 1
## drop runtime dep, https://bugzilla.redhat.com/show_bug.cgi?id=1208312
#Requires: pm-utils
%endif
BuildRequires: bzip2-devel
BuildRequires: freetype-devel
BuildRequires: openldap-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libart_lgpl-devel
## X11 support details (xmkmf, bdftopcf)
BuildRequires: bdftopcf mkfontdir mkfontscale
BuildRequires: imake
BuildRequires: xorg-x11-proto-devel
BuildRequires: libfontenc-devel
BuildRequires: libtirpc-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXfixes-devel
BuildRequires: libXext-devel
BuildRequires: libXtst-devel
BuildRequires: libxkbfile-devel
%ifnarch s390 s390x
BuildRequires: libraw1394-devel
%if 0%{?fedora} > 36
BuildRequires: libusb-compat-0.1-devel
%else
BuildRequires: libusb-devel
%endif
%endif
# Moving dependency to compat package openexr2.
BuildRequires: pkgconfig(OpenEXR) < 3
BuildRequires: gtk2-devel
BuildRequires: make

%description
Core runtime files for KDE 3, for compatibility with KDE 3 applications.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: kdelibs3-devel
%description devel
Header files for developing applications using %{name}.
Install %{name}-devel if you want to develop or compile Konqueror,
Kate plugins or KWin styles.

%if 0%{?extras}
%package extras
Summary: Extra applications from %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description extras
%{summary}, including:
 * kappfinder
 * kpager
 * ktip
 * kpersonalizer
%endif

%package libs
Summary: %{name} runtime libraries
Requires: kdelibs3 >= %{version}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libs
%{summary}.

%if 0%{?pim}
%package pim-ioslaves
Summary: PIM KIOslaves from %{name}
%description pim-ioslaves
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp
%endif


%prep
%setup -q -n kdebase-%{version}
%patch -P0 -p1 -b .redhat-pam
%patch -P1 -p1 -b .redhat-startkde
%patch -P2 -p1 -b .vroot
%patch -P3 -p1 -b .shortcuts
%patch -P4 -p1 -b .keymap
%patch -P5 -p1
%patch -P6 -p1 -b .konsole
%patch -P7 -p1 -b .kper
%patch -P8 -p1 -b .logo
%patch -P10 -p1 -b .kdestop-konsole
%patch -P11 -p1 -b .xdg
%{?_with_hal:%patch -P13 -p1 -b .dbus}
%patch -P14 -p1 -b .kdm-readme
%patch -P15 -p1 -b .konsole-fonts
%patch -P18 -p1 -b .klipper
%patch -P20 -p1 -b .keyinit
%patch -P21 -p1 -b .khelpcenter-sort
%patch -P22 -p1 -b .htdig
%patch -P24 -p1 -b .tango-icon-theme
%patch -P25 -p1 -b .konqueror-shortcut
%{?_with_suspend:%patch -P26 -p1 -b .suspend}
%{?_with_hal:%patch -P27 -p1 -b .consolekit}
%patch -P28 -p1 -b .kdm-alternatebackground
%patch -P30 -p1 -b .bz#265801
%patch -P31 -p1 -b .konsolesu-kdesu
%patch -P36 -p1 -b .userdiskmount
%patch -P37 -p1 -b .libkrdb_dep
%patch -P39 -p1 -b .samba4
%patch -P40 -p1 -b .printmanager-desktop
%patch -P41 -p2 -b .libtirpc
%patch -P42 -p1 -b .uic
%patch -P100 -p1 -b .minicli-decimal-comma

%patch -P150 -p1 -b .openssl-1.1
%patch -P151 -p1 -b .configure-c99

# hacks to omit stuff that doesn't support DO_NOT_COMPILE
# colors is pending on http://bugzilla.redhat.com/443343
sed -i.omit -e 's|^FONTINST_SUBDIR=kfontinst|#FONTINST_SUBDIR=kfontinst|' \
  -e 's/background//' -e 's/clock//' -e 's/display//' -e 's/energy//' \
  -e 's/fonts//' -e 's/icons//' \
  -e 's/kdm//' -e 's/kicker//' -e 's/krdb//' -e 's/kthememanager//' \
  -e 's/locale//' \
  -e 's/screensaver//' -e 's/style//' -e 's/taskbar//' -e 's/xinerama//' \
  kcontrol/Makefile.am

# security fixes

%if %redhatify
   cp %{SOURCE1} konsole
   # set Konqueror version
   perl -pi -e "s,^#define.*KONQUEROR_VERSION.*,#define KONQUEROR_VERSION \"%{version}-%{release} Fedora\"," konqueror/version.h
%endif

# add missing icons for package_games_kids
install -p -m644 %{SOURCE9} %{SOURCE10} %{SOURCE11} pics/crystalsvg/

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .autoconf2.7x
%patch -P305 -p1 -b .ftbfs-gcc14
%patch -P306 -p1 -b .autoconf-2.72

make -f admin/Makefile.common cvs


%build
# set some default enviroments
unset QTDIR && . /etc/profile.d/qt.sh

export DO_NOT_COMPILE="kappfinder kdesktop kdesu klipper kdm kmenuedit kpager kpersonalizer ktip nsplugins"
export DO_NOT_COMPILE="$DO_NOT_COMPILE konqueror kscreensaver ksysguard knetattach kwin"
export DO_NOT_COMPILE="$DO_NOT_COMPILE kdialog kicker ksplashml khelpcenter kxkb"
export DO_NOT_COMPILE="$DO_NOT_COMPILE khotkeys kdepasswd kcheckpass drkonqi"
# Keep these (kcontrol for kcms, konsole for KonsolePart, kioslave for ioslaves
# kate for kscope
# export DO_NOT_COMPILE="$DO_NOT_COMPILE kcontrol konsole kioslave kate"

%configure \
   --disable-new-ldflags \
   --disable-dependency-tracking \
   --with-xdmdir=%{_sysconfdir}/X11/xdm \
   --with-pam=yes \
   --with-kdm-pam=kdm \
   --with-kcp-pam=kcheckpass \
   --with-kss-pam=kscreensaver \
%ifnarch s390 s390x
   --with-libraw1394 \
%endif
   --with-openexr \
   --with-xinerama \
   --with-xscreensaver \
   --without-shadow \
   --disable-shadow \
   --disable-rpath \
   --sysconfdir=%{_sysconfdir} \
   --disable-greet-lib \
%if %{arts} == 0
   --without-arts \
%endif
%if %{final}
%ifnarch s390x
   --enable-final \
%endif
%endif
%if %{debug} == 0
   --disable-debug \
   --disable-warnings \
%else
   --enable-debug \
%endif
   --includedir=%{_includedir}/kde \
  %{?_with_hal} %{!?_with_hal:--without-hal} \
  %{?_with_samba} %{!?_with_samba:--without-samba}

%make_build

# build mail setting tool
%{__cxx} $CXXFLAGS -o mailsettings %{SOURCE7}

%install
%make_install RUN_KAPPFINDER=no

# Nuke man2html - we get it from man
find %{buildroot} -name "man2html*" | xargs rm -rf

# nuke default kdm setup in favor of our own
rm -rf  %{buildroot}%{_datadir}/config/kdm

# Make symlinks relative
pushd %{buildroot}/%{_docdir}/HTML/en
for i in */*/*; do
   if [ -d "$i" -a -L "$i"/common ]; then
      rm -f $i/common
      ln -s ../../../common $i
   fi
done
for i in */*; do
   if [ -d "$i" -a -L "$i"/common ]; then
      rm -f $i/common
      ln -s ../../common $i
   fi
done
for i in *; do
   if [ -d "$i" -a -L "$i"/common ]; then
      rm -f $i/common
      ln -s ../common $i
   fi
done
popd

%if %{redhatify}
   rm -f %{buildroot}%{_datadir}/locale/l10n/*/flag.png
   # mark KDE-Only
   pushd %{buildroot}%{_datadir}/applications/kde
      for f in *.desktop ; do
         if [ "$f" == "konqbrowser.desktop" ] ; then
            cat $f | grep -v Categories >$f.o
            echo "Categories=Qt;KDE;Network;" >>$f.o
            mv $f.o $f
         else
            echo "OnlyShowIn=KDE;" >> $f
         fi
      done
   popd
   for f in $(find %{buildroot}%{_datadir}/applnk -name "*.desktop") ; do
      echo "OnlyShowIn=KDE;" >> $f
   done
%endif

# Own Mozilla plugin dir
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins

# exclude fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/override/fonts.dir

# now in kde-filesystem (see #321771)
rm -f %{buildroot}%{_datadir}/applnk/.hidden/.directory

# remove conflicts with kdebase-workspace
pushd %{buildroot}%{_bindir}
rm -f genkdmconf kaccess kappfinder kapplymousetheme kate kbookmarkmerger \
      kblankscrn.kss kcheckrunning kcminit kcminit_startup kcontroledit kdebugdialog \
      kdeinstallktheme kdepasswd kdialog kdm kdmctl keditbookmarks \
      keditfiletype kfind kfmclient kfontinst kfontview khelpcenter khc_* \
      khotkeys kinfocenter klipper \
      kmenuedit konqueror konsole krandom.kss krandrtray kreadconfig ksmserver \
      ksplashsimple kstart ksysguard ksysguardd ksystraycmd ktip ktrash kwin \
      kwin_killer_helper kwin_rules_dialog kwrite kwriteconfig kxkb \
      nspluginscan nspluginviewer startkde kdeeject kcontrol
popd
rm -f %{buildroot}%{_sysconfdir}/ksysguarddrc
rm -f %{buildroot}%{_libdir}/kconf_update_bin/khotkeys_update
rm -f %{buildroot}%{_libdir}/kconf_update_bin/kwin_update_default_rules
rm -f %{buildroot}%{_libdir}/kconf_update_bin/kwin_update_window_settings
rm -f %{buildroot}%{_datadir}/config.kcfg/kcm_useraccount.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/keditbookmarks.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/klaunch.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/konqueror.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/kwin.kcfg
rm -f %{buildroot}%{_datadir}/config/klipperrc
rm -f %{buildroot}%{_datadir}/config/kshorturifilterrc
rm -f %{buildroot}%{_datadir}/xsessions/kde.desktop

# dups of kde4 services
rm -f %{buildroot}%{_datadir}/applications/kde/cookies.desktop
rm -f %{buildroot}%{_datadir}/applications/kde/desktop.desktop

# remove mediamanager stuff #447852 and kdebug:163717
rm -f %{buildroot}%{_libdir}/kde3/kded_mediamanager.*
rm -f %{buildroot}%{_libdir}/kde3/kded_medianotifier.*
rm -f %{buildroot}%{_libdir}/kde3/kcm_media.*
rm -f %{buildroot}%{_datadir}/services/kded/mediamanager.desktop
rm -f %{buildroot}%{_datadir}/services/kded/medianotifier.desktop
rm -f %{buildroot}%{_datadir}/applications/kde/media.desktop

# remove conflicts with kdesdk
rm -f %{buildroot}%{_datadir}/config/katerc

# remove docs
pushd %{buildroot}%{_docdir}/HTML/en/
rm -rf kate kcontrol kdebugdialog kdesu kdm kfind khelpcenter kinfocenter \
       kioslave klipper kmenuedit knetattach konqueror konsole ksysguard \
       kwrite kxkb 
popd
# remove .desktop files for apps we don't ship
pushd %{buildroot}%{_datadir}/applications/kde/
rm -f Help.desktop Home.desktop Kfind.desktop installktheme.desktop \
      kappfinder.desktop kate.desktop kdepasswd.desktop kfmclient.desktop \
      kfmclient_dir.desktop kfmclient_html.desktop kfmclient_war.desktop \
      kinfocenter.desktop klipper.desktop kmenuedit.desktop \
      konqbrowser.desktop konquerorsu.desktop konsole.desktop \
      konsolesu.desktop krandrtray.desktop ksysguard.desktop ktip.desktop \
      kwrite.desktop KControl.desktop

sed -i -e "s,^OnlyShowIn=KDE;,OnlyShowIn=KDE3;," *.desktop
popd

# hicolor
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kappfinder.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kate.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/khelpcenter.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/knetattach.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kfind.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kfm.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/khotkeys.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kmenuedit.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/konqueror.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/konsole.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ksplash.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ktip.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kwrite.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kxkb.*
rm -rf %{buildroot}%{_datadir}/locale/en_US/
rm -rf %{buildroot}%{_datadir}/locale/l10n/
rm -rf %{buildroot}%{_datadir}/autostart/*
rm -rf %{buildroot}%{_datadir}/desktop-directories/*
rm -rf %{buildroot}%{_datadir}/templates/*
rm -rf %{buildroot}%{_datadir}/templates/.source/*
rm -rf %{buildroot}%{_datadir}/wallpapers/*
rm -rf %{buildroot}%{_libdir}/kconf_update_bin
rm -rf %{buildroot}%{_datadir}/fonts
rm -rf %{buildroot}%{_datadir}/apps/kdm
rm -rf %{buildroot}%{_datadir}/apps/konqueror
rm -rf %{buildroot}%{_datadir}/apps/apps/kbookmark
rm -rf %{buildroot}%{_datadir}/apps/ksmserver
rm -rf %{buildroot}%{_datadir}/applnk
rm -rf %{buildroot}/etc/xdg/menus/

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001

# legacy scriptlets
%if 0%{?fedora} < 25
%post
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :

%posttrans
gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg  2> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :
  gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg  &> /dev/null || :
fi

%if 0%{?extras}
%post extras
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null ||:

%posttrans extras
gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg &> /dev/null ||:

%postun extras
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg &> /dev/null ||:
fi
%endif
%endif

%if 0%{?extras}
%files extras
# kappfinder
%{_bindir}/kappfinder
%{_datadir}/applications/kde/kappfinder.desktop
%{_datadir}/applnk/System/kappfinder.desktop
%{_datadir}/apps/kappfinder/
%{_datadir}/icons/hicolor/*/apps/kappfinder.png

# ktip
%{_bindir}/ktip
%{_datadir}/applications/kde/ktip.desktop
%{_datadir}/applnk/Toys/ktip.desktop
%{_datadir}/apps/kdewizard
%{_datadir}/autostart/ktip.desktop
%{_datadir}/icons/hicolor/*/apps/ktip*

# kpersonalizer
%{_bindir}/kpersonalizer
%{_datadir}/applications/kde/kpersonalizer.desktop
%{_datadir}/applnk/System/kpersonalizer.desktop
%{_datadir}/apps/kpersonalizer/
%{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png

# kpager
%{_bindir}/kpager
%{_datadir}/applications/kde/kpager.desktop
%{_datadir}/applnk/Utilities/kpager.desktop
%{_datadir}/icons/hicolor/*/apps/kpager.png
%endif

%files
%if 0%{?extras}
# kappfinder
%exclude %{_datadir}/applications/kde/kappfinder.desktop
%exclude %{_datadir}/applnk/System/kappfinder.desktop
%exclude %{_datadir}/apps/kappfinder/
%exclude %{_datadir}/icons/hicolor/*/apps/kappfinder.png

# ktip
%exclude %{_datadir}/applications/kde/ktip.desktop
%exclude %{_datadir}/applnk/Toys/ktip.desktop
%exclude %{_datadir}/apps/kdewizard
%exclude %{_datadir}/autostart/ktip.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/ktip*

# kpersonalizer
%exclude %{_datadir}/applications/kde/kpersonalizer.desktop
%exclude %{_datadir}/applnk/System/kpersonalizer.desktop
%exclude %{_datadir}/apps/kpersonalizer/
%exclude %{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png

# kpager
%exclude %{_datadir}/applications/kde/kpager.desktop
%exclude %{_datadir}/applnk/Utilities/kpager.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/kpager.png
%endif

%doc AUTHORS README
%license COPYING
%{_docdir}/HTML/en/*
%if "%{name}" == "kdebase"
%{_sysconfdir}/kde/env/*
%config(noreplace) /etc/logrotate.d/kdm
%config(noreplace) /etc/ksysguarddrc
%config(noreplace) /etc/pam.d/*
%config(noreplace) %{_datadir}/xsessions/*
%{_bindir}/drkonqi
%{_bindir}/genkdmconf
%{_bindir}/kaccess
%{_bindir}/kapplymousetheme
%{_bindir}/kate
%{_bindir}/kblankscrn.kss
%{_bindir}/kbookmarkmerger
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/kcontrol
%{_bindir}/kcontroledit
%{_bindir}/kdebugdialog
%{_bindir}/kdeinstallktheme
%{_bindir}/kdepasswd
%{_bindir}/kdesu
%attr(0755,root,root) %{_bindir}/kdesud
%{_bindir}/kdialog
%{_bindir}/kdm
%{_bindir}/kdmctl
%{_bindir}/keditbookmarks
%{_bindir}/keditfiletype
%{_bindir}/kfind
%{_bindir}/kfmclient
%{_bindir}/khelpcenter
%{_bindir}/khotkeys
%{_bindir}/kinfocenter
%{_bindir}/klipper
%{_bindir}/kmenuedit
%{_bindir}/konqueror
%{?_with_libutempter:%attr(2755,root,utempter) }%{_bindir}/konsole
%{_bindir}/krandom.kss
%{_bindir}/krandrtray
%{_bindir}/krdb
%{_bindir}/kreadconfig
%{_bindir}/ksmserver
%{_bindir}/ksplashsimple
%{_bindir}/kstart
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_bindir}/ksystraycmd
%{_bindir}/ktrash
%{_bindir}/kwin
%{_bindir}/kwin_killer_helper
%{_bindir}/kwin_rules_dialog
%{_bindir}/kwrite
%{_bindir}/kwriteconfig
%{_bindir}/kxkb
%{_bindir}/nspluginscan
%{_bindir}/nspluginviewer
%{_bindir}/startkde
%{_bindir}/kcheckrunning
%{_bindir}/kdesktop
%{_bindir}/kdesktop_lock
%{_bindir}/kdm_config
%{_bindir}/kdm_greet
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/krootimage
%{_bindir}/kwebdesktop
%{_datadir}/autostart/*
%{_datadir}/desktop-directories/*
%{_datadir}/locale/*/entry.desktop
%{_datadir}/locale/l10n
%{_datadir}/templates/*
%{_datadir}/templates/.source/*
%{_datadir}/wallpapers/*
%config(noreplace) /etc/xdg/menus/*
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%{_bindir}/appletproxy
%{_bindir}/extensionproxy
%{_bindir}/kasbar
%{_bindir}/kcheckpass
%{_bindir}/kdeeject
%{_bindir}/khc_docbookdig.pl
%{_bindir}/khc_htdig.pl
%{_bindir}/khc_htsearch.pl
%{_bindir}/khc_indexbuilder
%{_bindir}/khc_mansearch.pl
%{_bindir}/kicker
%{_bindir}/knetattach
%{_bindir}/kompmgr
%{_bindir}/kpm
%{_bindir}/ksplash
%{_bindir}/mailsettings
%{_libdir}/kconf_update_bin
%{_datadir}/applnk/*.desktop
%{_datadir}/applnk/*/*
%{_datadir}/applnk/.hidden/*
%config(noreplace) %{_datadir}/config/*
%if ! %{redhatify}
%{_datadir}/fonts/bitmap-fonts/*
%endif
%dir %{_localstatedir}/lib/kdm
%ghost %{_localstatedir}/lib/kdm/kdmsts
%endif
%{_datadir}/config.kcfg/*
%{_bindir}/kde3
%{_bindir}/kio_media_mounthelper
%{_bindir}/kio_system_documenthelper
%{_bindir}/kdcop
%{_bindir}/kdeprintfax
%{_bindir}/kjobviewer
%{_bindir}/klocaldomainurifilterhelper
%{_bindir}/kprinter
%{_datadir}/applications/*/*
%{_datadir}/apps/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/sounds/*
%{_libdir}/kde3/*
%{_libdir}/libkdeinit_*.*
%if 0%{?pim}
# exclude pim-ioslaves files from main package
%exclude %{_libdir}/kde3/kio_ldap.*
%exclude %{_libdir}/kde3/kio_nntp.*
%exclude %{_libdir}/kde3/kio_pop3.*
%exclude %{_libdir}/kde3/kio_smtp.*
%exclude %{_datadir}/services/ldap*.protocol
%exclude %{_datadir}/services/nntp*.protocol
%exclude %{_datadir}/services/pop3*.protocol
%exclude %{_datadir}/services/smtp*.protocol
%endif

%ldconfig_scriptlets libs

%files libs
%exclude %{_libdir}/libkdeinit_*.*
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%if 0%{?pim}
%files pim-ioslaves
%{_libdir}/kde3/kio_ldap.*
%{_libdir}/kde3/kio_nntp.*
%{_libdir}/kde3/kio_pop3.*
%{_libdir}/kde3/kio_smtp.*
%{_datadir}/services/ldap*.protocol
%{_datadir}/services/nntp*.protocol
%{_datadir}/services/pop3*.protocol
%{_datadir}/services/smtp*.protocol
%endif

%files devel
%{_includedir}/kde/*.h
%dir %{_includedir}/kde/kate
%{_includedir}/kde/kate/*
%if "%{name}" == "kdebase"
%dir %{_includedir}/kde/kwin
%{_includedir}/kde/kwin/*
%dir %{_includedir}/kde/ksgrd
%{_includedir}/kde/ksgrd/*
%dir %{_includedir}/kde/ksplash
%{_includedir}/kde/ksplash/*
%endif
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-84
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Than Ngo <than@redhat.com> - 3.5.10-82
- fixed bz#2276345, FTBFS

* Tue Jan 30 2024 Than Ngo <than@redhat.com> - 3.5.10-81
- fixed bz#2261271, FTBFS

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 3.5.10-77
- Port configure script to C99 (#2186679)

* Thu Feb 23 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 3.5.10-76
- Rebuild against openexr2 2.5.8

* Tue Feb 21 2023 Than Ngo <than@redhat.com> - 3.5.10-75
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Than Ngo <than@redhat.com> - 3.5.10-73
- fixed FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 3.5.10-71
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Than Ngo <than@redhat.com> - 3.5.10-69
- Fixed bz1999501 - [F36FTBFS]: kdebase3 fails to build from source in Fedora Rawhide

* Sun Aug 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.5.10-68
- Build with openexr2 package now that openexr has been updated to 3.x.

* Tue Jul 27 2021 Than Ngo <than@redhat.com> - 3.5.10-67
- Disable check-rpath's test for standard runpaths.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-64
- drop -std=gnu++98 to fix FTBFS against new OpenEXR (#1915860)
- fix #1307683 mailsettings.cc FTBFS properly, without -std=gnu++98 (#1915860)

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.10-63
- rebuild against New OpenEXR again

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.5.10-62
- Rebuild for OpenEXR 2.5.3.

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 3.5.10-61
- BuildRequires bdftopcf mkfontdir mkfontscale, not xorg-x11-font-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-58
- Drop BuildRequires: libXxf86misc-devel, fixes F31+ FTBFS (#1735918)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 3.5.10-56
- Rebuild for OpenEXR 2.3.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-54
- Fix aarch64 FTBFS due to libtool not liking the file output on *.so files

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-53
- use %%make_build %%make_install %%license %%ldconfig_scriptlets
- libs unconditional

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Than Ngo <than@redhat.com> - 3.5.10-51
- fixed bz#1583382 - FTBFS

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org>
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org>
- Remove obsolete scriptlets

* Sat Jan 06 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-47
- Build against OpenSSL 1.1, patches from Trinity, backported by Kevin Kofler
- Build against libtirpc (see #1531540), patch from Cygwin Ports

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Than Ngo <than@redhat.com> - 3.5.10-44
- build against kdelibs3-3.5.10-83, fix FTBFS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-42
- Add -std=gnu++98 to the CXXFLAGS to fix FTBFS (#1307683)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-40
- Remove kwrite hicolor icons that conflict with Kate/KWrite 15.12

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.5.10-38
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 01 2015 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-37
- drop some runtime deps that no longer make sense: pm-utils (#1208312), some post/postun scriptlet deps

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-36
- rebuild (openexr)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-33
- trim changelog
- --disable-new-ldflags, fix FTBFS on rawhide

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-32
- rebuild (openexr)

* Sat Nov 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-31
- remove obsolete MimeType from printmgr/printers.desktop (#587568)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-30
- rebuild (openexr)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.5.10-28
- Perl 5.18 rebuild

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-27
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-26
- rebuild (OpenEXR)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-25
- unify KDE 3 autotools fixes between packages

* Fri Mar 08 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-24
- reenable samba (kio_smb)
- find the Samba 4 libsmbclient.h using pkg-config (fixes FTBFS)

* Thu Mar 07 2013 Than Ngo <than@redhat.com> - 3.5.10-23
- fix build failure with new automake
- disable samba (kio_smb)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 25 2012 Than Ngo <than@redhat.com> - 3.5.10-20
- drop BR on hal

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-17
- drop old Obsoletes/Provides: kdebase(-devel)

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-16
- fix FTBFS with autoconf >= 2.64 (#539110)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 3.5.10-15
- Repositioning the KDE Brand (#547361)

* Fri Sep 04 2009 Than Ngo <than@redhat.com> - 3.5.10-14
- openssl-1.0 build fixes

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.5.10-13
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-11
- FTBFS kdebase3-3.5.10-8.fc11 (#511656)
- Requires: %%name-libs%%?_isa ...

* Wed Apr 22 2009 Karsten Hopp <karsten@redhat.com> 3.5.10-10.1
- disable firewire stuff on s390(x)

* Fri Mar 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-10
- optimize scriptlets

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-7
- omit desktop.desktop (f9+)

* Wed Feb 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-6
- omit cookies.desktop (f9+)

* Fri Jan 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-5
- rebuild for new OpenSSL

* Mon Dec 22 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-4
- omit (nonfunctional) kdesu (F9+)

* Mon Dec 08 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-3
- omit kate.png conflicts (w/kdesdk42)

* Wed Oct 08 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-2.1
- add upstream patch to support decimal comma in the minicli calculator

* Sun Sep 21 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-2
- fix libkrdb_dep patch not to call runRdb which is not being linked in
- don't apply libkrdb_dep patch on F8-

* Thu Aug 28 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-1
- kde-3.5.10

* Wed Jul 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-17
- rebuild for new libraw1394

* Wed Jun 11 2008 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.9-16
- remove kded_media* to prevent clashes with Solid from KDE 4 (#447852, kdebug:163717)

* Wed Jun 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-15
- reinclude crystalsvg icons also on f9+ (no longer using crystalsvg from KDE 4)

* Fri May 23 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.9-14.1
- don't set XDG_CONFIG_DIRS (#249109)

* Fri May 16 2008 Rex Dieter <rdieter@fedoraprojecdt.org> - 3.5.9-14
- f9+: omit extraneous kcontrol modules (#446575)

* Wed May 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.9-12
- kcontrol modules appearing in gnome "Other" menu (#446466)

* Mon Apr 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.9-10.1
- create/own: /var/lib/kdm (#442081)

* Tue Apr 08 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-10
- f9+: split off -pim-ioslaves subpackage for kdepim (#441541)

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-9
- add missing BR bzip2-devel (thanks to Karsten Hopp)

* Fri Mar 28 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.9-8
- omit %%_datadir/applnk/.hidden/.directory (#321771)

* Thu Mar 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-7
- actually apply the patch (on F8+ only, not needed on F7)
- fix the patch to actually build

* Thu Mar 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-6
- apply modified Kubuntu patch to fix mounting NTFS partitions (#378041)
- also prompts for the root password on PermissionDeniedByPolicy (#428212)

* Fri Mar 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-5
- f9+: omit all of khelpcenter again, we only need the khelpcenter.desktop
       service description, so move that to kdebase-runtime which actually
       provides khelpcenter

* Mon Mar 03 2008 Than Ngo <than@redhat.com> 3.5.9-4
- apply upstream patch to fix crash in khotkey

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 3.5.9-3
- apply upstream patch to unbreak lmsensors support again

* Wed Feb 27 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.9-2
- f9+: don't omit all of khelpcenter, some is needed for kde3 apps' help

* Thu Feb 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.5.9-1
- kde-3.5.9
- fixup startkde patch, omitting broken bits, for now (#426871)
- update startpage patch, use http://start.fedoraproject.org/

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-37
- sync from F8:
  - kdm: local DoS vulnerability, CVE-2007-5963 (Than Ngo, 3.5.8-31.fc8)
  - updated flash patch to support 64 bit platforms (Lukáš Tinkl, 3.5.8-32.fc8)
- fix detection of struct ucred with current glibc 2.7.90

* Wed Feb 06 2008 Than Ngo <than@redhat.com> 3.5.8-36
- f9+: remove %%{_bindir}/kcontrol %%{_datadir}/applications/kde/Kcontrol*
- f9+: make kde3 config tools hidden

* Thu Jan 24 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-35
- fix file list again (missing libkdeinit_* for f9+)
- f9+: reenable kate (libkateutils and libkateinterfaces needed by kscope)
- f9+: remove %%{_datadir}/config/katerc
- f9+: reenable kdesu for now (until we figure out what to do about it)

* Thu Jan 24 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-34
- f9+: omit kcontrol/kicker and kcontrol/taskbar (don't build because kicker is
       omitted)
- fix file list

* Wed Jan 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-33
- f9+: don't omit all of kcontrol (kcms are used by several applications)

* Wed Jan 23 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.8-32
- (re)enable --with-samba support (now that we have a GPLv3-compat qt)

* Wed Jan 23 2008 Than Ngo <than@redhat.com> 3.5.8-31
- f9+: omit kdesu kdialog kicker kate konqueror kscreensaver \
       ksysguard kwin ksplashml khelpcenter khotkeys kxkb kdepasswd

* Tue Jan 15 2008 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-30.1
- f7: fix libkdeinit_* missing dep errors

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-30
- f9+: omit kcontrol/kfontinst

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-29
- f9+: omit conflicts w/kdebase-workspace-4.0.0
- f9+: DO_NOT_COMPILE="kappfinder kdesktop klipper kdm kmenuedit kpager kpersonalizer kscreensaver ktip nsplugins"
- include %%_libdir/libkdeinit_*.* only in main pkg (not -libs or -devel)

* Sat Jan 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-28
- apply upstream build fix for GCC 4.3 (--enable-final macro redefinition)

* Mon Dec 31 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-27
- fix createGtkrc to set tooltip colors also for GTK+ 2.12+

* Fri Dec 21 2007 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.8-26
- fix kded crash on logout (#426459)

* Tue Dec 18 2007 Lukas Tinkl <ltinkl@redhat.com> - 3.5.8-25
- fix Firefox detection in Klipper (#377171)

* Mon Dec 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-24
- Requires: coreutils mktemp xorg-x11-apps xorg-x11-utils 
            xorg-x11-server-utils (used in startkde)
- include htdig,man deps (and new startkde ones) in non-compat pkg only

* Thu Dec 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-22
- nspluginviewer: respin flash patch with +gtk_init (#410651)
- use kde's kde.desktop for xsession support

* Thu Dec 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-19
- nspluginviewer: XEmbed support (#410651, kde#132138, kde#146784)

* Sat Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-18
- omit pam configs, kdm bits, xsession/gdm support (f9+)

* Tue Dec 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-16
- disable kioslave/smb (f9+, samba-3.2.x/gplv3 ickiness)
- omit kde_settings optionals

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-15
- only set Epoch: 6 when building as kdebase (not kdebase3)
- only obsolete kdebase-kdm here when building as kdebase

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-14
- don't hardcode %%fedora

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-13
- fix summary and description for kdebase3
- for kdebase3, remove .desktop files for apps we don't ship
- don't require /sbin/ldconfig in the main package if we build -libs

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-12
- build as kdebase3 on F9+ (not F10+)
- fix unescaped macros and a typo in changelog
- move kdebase-extras Provides/Obsoletes to the correct place
- fix check of %%{name} against "kdelibs" instead of "kdebase"
- fix Provides/Obsoletes for kdebase3-libs and kdebase3-devel

* Wed Nov 28 2007 Sebastian Vahl <fedora@deadbabylon.de> - 6:3.5.8-11
- renew the list of file conflicts and removals

* Wed Nov 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.8-9
- adapt updated ConsoleKit patch from Mandriva (Nicolas Lécureuil) to fix xdmcp
  issues (#243560, Mandriva#34786)

* Sat Nov 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.8-8
- disable lm_sensors f9+ for now (new lm_sensors api-incompat)

* Wed Oct 31 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-6
- apply GDM socket path patch only on F8+

* Tue Oct 30 2007 Bill Nottingham <notting@redhat.com> - 6:3.5.8-5
- use correct path for gdm socket, so you get proper options on logout
  (http://bugs.kde.org/show_bug.cgi?id=149045)

* Tue Oct 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.8-4
- -libs: Obsoletes: %%name ... to help out multilib upgrades
- -libs conditional (f8+)

* Mon Oct 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.8-3
- respin (for openexr-1.6.0)
- -libs: %%post/%%postun /sbin/ldconfig

* Sat Oct 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.8-2
- update consolekit patch
- omit konsole-bz#244906 (doesn't build)
- --enable-final
- libs subpkg (more multilib friendly)

* Sat Oct 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.8-1
- kde-3.5.8

* Wed Oct 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-17
- Requires: findutils which (#312611)

* Tue Oct 02 2007 Than Ngo <than@redhat.com> - 6:3.5.7-16
- rh#299731, CVE-2007-4569

* Thu Sep 27 2007 Than Ngo <than@redhat.com> - 6:3.5.7-15
- rh#301841, "Root Shell" sessions will not close

* Thu Aug 30 2007 Than Ngo <than@redhat.com> - 6:3.5.7-14
- fix bz#265801, fuser command not found by kio_media_mounthelper

* Wed Aug 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-13
- CVE-2007-3820, CVE-2007-4224, CVE-2007-4225
- License: GPLv2
- Requires: kdelibs3(-devel)

* Fri Jul 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-12
- fix unpackaged files

* Fri Jul 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-9
- %%ifnarch s390 s390x: BR: lm_sensors

* Thu Jul 19 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-7
- omit dirs owned by kde-filesystem

* Mon Jul 02 2007 Than Ngo <than@redhat.com> - 6:3.5.7-6
- fix bz#244906

* Wed Jun 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-5
- Provides: kdebase3(-devel)

* Wed Jun 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-4
- -devel: Requires: %%name... 
- portability++

* Fri Jun 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-3
- specfile portability

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-2
- fix BR: kdelibs-devel
- cleanup Req's wrt kde-settings

* Mon Jun 11 2007 Than Ngo <than@redhat.com> -  6:3.5.7-1.fc7.1
- remove kdebase-3.4.2-npapi-64bit-fixes.patch, it's included
  in new upstream

* Wed Jun 06 2007 Than Ngo <than@redhat.com> -  6:3.5.7-0.1
- 3.5.7

* Thu May 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-12
- -extras: fix Requires: %%name ... (omitting %%_arch)

* Wed May 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-11
- fix /usr/share/config/kdm conflict with kde-settings 

* Tue May 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-10
- drop unconditional --with-sensors, let %%configure autodetect

* Tue May 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-9
- create/own {/usr,/etc/kde}/{env,shutdown} (#178326)

* Tue May 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-8
- cleanup/simplify scriptlets
- drop Req/Prov's that include %%_arch (they don't work)
- Req: +samba-common
- BR: +OpenEXR-devel, -cdparanoia
- env.sh: use XDG_MENU_PREFIX
- npapi-64bit-fixes.patch

* Tue May 15 2007 Than Ngo <than@redhat.com> - 6:3.5.6-7.fc7
- enable userlist by default in KDM, bz#239701
- own %%{_datadir}/apps/kdm/faces, bz#239694
- remove unneeded Rq on kdelibs-devel (#238846)

* Mon Apr 23 2007 Than Ngo <than@redhat.com> - 6:3.5.6-6.fc7
- apply patch KDM to support ConsoleKit, thanks to Kevin Kofler and
  S.Çağlar Onur, #228111
- ktip, kpersonlizer, kpager, kappfinder in kdebase-extras

* Tue Apr 10 2007 Than Ngo <than@redhat.com> 6:3.5.6-5.fc7
- fix unknown protocol smb
- add Buildrequires on libusb-devel

* Thu Mar 22 2007 Than Ngo <than@redhat.com> 6:3.5.6-4.fc7
- add new KDM theme for Fedora 7

* Tue Mar 06 2007 Than Ngo <than@redhat.com> - 6:3.5.6-3.fc7
- cleanup specfile

* Wed Feb 14 2007 Than Ngo <than@redhat.com> - 6:3.5.6-2.fc7
- make konsole binary sgid utempter #213369

* Sun Jan 28 2007 Than Ngo <than@redhat.com> 6:3.5.6-1.fc7
- 3.5.6

* Thu Nov 30 2006 Than Ngo <than@redhat.com> - 6:3.5.5-0.6.fc6
- apply upstream fix:
    #88506, dragged window follows mouse but on wrong screen (dual-head non-xinerama)
    #137889, Title bar font size does not correspond to KControl on first use

* Tue Nov 07 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.5.fc6
- add hibernate/suspend in shutdown dialog

* Fri Nov 03 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.4.fc6
- rebuild

* Thu Nov 02 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.3.fc6
- rebuild

* Thu Nov 02 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.2.fc6
- apply upstream patch to fix #213219, KWin focus issue
- fix pam config issue

* Thu Oct 26 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.1
- 3.5.5

* Wed Oct 04 2006 Than Ngo Than Ngo <than@redhat.com> 6:3.5.4-13
- add shortcut Shift+Left/Shift+Right for tab_move_left/tab_move_right

* Mon Oct 02 2006 Than Ngo Than Ngo <than@redhat.com> 6:3.5.4-12
- fix #178320,#198828, follow menu-spec

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.4-11
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Than Ngo <than@redhat.com> 6:3.5.4-10
- FedoraDNA for KDM
- fix #205566, don't overwrite config files
- fix #178320,#198828, follow menu-spec

* Fri Sep 22 2006 Than Ngo <than@redhat.com> 6:3.5.4-9
- fedora desktop background

* Tue Sep 12 2006 Than Ngo <than@redhat.com> 6:3.5.4-8
- apply upstream patch
   fix #205701, no bold is displayed in konsole
   fix two possible mem leaks
- add missing icons for package_games_kids
- add more icon contexts (Tango icontheme)

* Thu Sep 07 2006 Than Ngo <than@redhat.com> 6:3.5.4-7
- apply upstream patch
   fix #53642, Menubar is always visible after coming back from fullscreen
   fix #133665, crash in kiosk mode

* Mon Aug 28 2006 Than Ngo <than@redhat.com> 6:3.5.4-6
- fix broken deps for s390(x)

* Fri Aug 25 2006 Than Ngo <than@redhat.com> 6:3.5.4-5
- add Requires: eject 
- fix #203279, antialiasing issue
- apply upstream patch to fix kdedesktop crash, kde#132873
- fix #201507, pam config issue
- fix kdm crash

* Mon Aug 21 2006 Than Ngo <than@redhat.com> 6:3.5.4-4
- fix #203221, konsole does not display bold characters

* Fri Aug 18 2006 Than Ngo <than@redhat.com> 6:3.5.4-3
- fix #203083, correct htdig settings

* Tue Aug 15 2006 Than Ngo <than@redhat.com> 6:3.5.4-2
- apply upstream patch to fix argument quoting

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 6:3.5.4-1
- apply upstream patch to fix KDED crashing on startup when D-BUS is unavailable.
- apply upstream patch to fix kde#128552, kicker regression

* Mon Jul 24 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)
- disable --enable-final on s390x in case it would cause problems

* Fri Jul 21 2006 Than Ngo <than@redhat.com> 6:3.5.3-16
- rebuild against new dbus

* Thu Jul 20 2006 Than Ngo <than@redhat.com> 6:3.5.3-15
- apply upstream patches,
    fix kde#130774, Strange lonesome icon in KInfocenter's start page

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> 6:3.5.3-14
- rebuild for dbus
- fixed deprecated dbus functions

* Sun Jul 16 2006 Than Ngo <than@redhat.com> 6:3.5.3-13
- fix 146377, khelpcenter's Browse Info Pages > Alphabetically should sort entries

* Thu Jul 13 2006 Than Ngo <than@redhat.com> 6:3.5.3-12
- cleanup keyinit patch

* Thu Jul 13 2006 David Howells <dhowells@redhat.com> 6:3.5.3-11
- add keyinit instructions to the kdm PAM scripts (#198630)

* Thu Jul 13 2006 Than Ngo <than@redhat.com> 6:3.5.3-10
- cleanup upstream patch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Tue Jul 11 2006 Than Ngo <than@redhat.com> 6:3.5.3-9
- cleanup config files
- upstream patches,
    #kde127971 hard Drive device icons do not show on desktop

* Thu Jul 06 2006 Than Ngo <than@redhat.com> 6:3.5.3-8
- fix #187228, kio_media_mounthelper fails with fuser
- apply upstream patches, fix #87613

* Mon Jun 26 2006 Than Ngo <than@redhat.com> 6:3.5.3-7
- apply patch to check return value

* Wed Jun 14 2006 Than Ngo <than@redhat.com> 6:3.5.3-6 
- apply patch to to fix #194659, CVE-2006-2449 KDM symlink attack vulnerability
  thanks to KDE security team

* Sat Jun 10 2006 Than Ngo <than@redhat.com> 6:3.5.3-5
- add several upstream patches

* Thu Jun 08 2006 Than Ngo <than@redhat.com> 6:3.5.3-4
- fix rpm file list

* Thu Jun 08 2006 Than Ngo <than@redhat.com> 6:3.5.3-3
- move only *.so symlinks to -devel subpackage
- enable --enable-new-ldflags again since ld bug fixed

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 6:3.5.3-2
- move .so symlinks into -devel subpackage

* Thu Jun 01 2006 Than Ngo <than@redhat.com> 6:3.5.3-1
- update to 3.5.3
- drop --enable-new-ldflags, workaround for ld bug
- update kioslave_media_dbus patch

* Wed May 24 2006 Than Ngo <than@redhat.com> 6:3.5.2-12
- don't overwrites user preference

* Tue May 23 2006 Than Ngo <than@redhat.com> 6:3.5.2-11
- apply upstream patches to fix several bugs in konsole, and
  fix #192832, konsole crashes on kde logout

* Fri May 19 2006 Than Ngo <than@redhat.com> 6:3.5.2-10 
- fix #191049, KDE screensaver calls PAM incorrectly
- fix 191306, Kde Help Center can't build an index

* Tue May 16 2006 Than Ngo <than@redhat.com> 6:3.5.2-9
- fix 186425, KDE Terminal Sessions applet does not display konsole bookmarks

* Fri May 12 2006 Than Ngo <than@redhat.com> 6:3.5.2-8
- fix 190836, xmTextFieldClass widgets don't work properly
- fix 153202, startkde gets wrong field from space_tmp/space_home with finnish

* Thu May 04 2006 Than Ngo <than@redhat.com> 6:3.5.2-7
- use XDG_CONFIG_DIRS for kde menu #178320

* Thu May 04 2006 Than Ngo <than@redhat.com> 6:3.5.2-6
- add missing kcheckpass

* Fri Apr 28 2006 Than Ngo <than@redhat.com> 6:3.5.2-5
- fix #189702, kwin crashes when switching windows with Alt-Tab

* Tue Apr 25 2006 Than Ngo <than@redhat.com> 6:3.5.2-4
- fix #189790, kcheckpass cannot authenticate users using a LDAP directory

* Thu Apr 13 2006 Than Ngo <than@redhat.com> 6:3.5.2-3
- fix startkde to look in /usr and /etc/kde for env/ and shutdown/

* Mon Apr 03 2006 Than Ngo <than@redhat.com> 6:3.5.2-2
- update dbus patch

* Sun Mar 26 2006 Than Ngo <than@redhat.com> 6:3.5.2-1
- update to 3.5.2
- update dbus patch
- drop kdebase-3.5.1-kwin-systray.patch, kdebase-3.5.1-keyboardlayout.patch,
  included in new upstream

* Tue Feb 21 2006 Than Ngo <than@redhat.com> 6:3.5.1-5
- fixed rpm file conflict
- added missing Category X-KDE-LookNFeel

* Thu Feb 16 2006 Than Ngo <than@redhat.com> 6:3.5.1-4
- Systray icons not docked sometimes, apply patch to fix this issue #180314

* Wed Feb 15 2006 Than Ngo <than@redhat.com> 6:3.5.1-3
- kscreensaver/kdm/kcheckpass use a separate PAM config file #66902
- cleanup kdm config file #166388 
- apply patch to launch kde scripts in shutdown,env directories #178326
- kdm.log logrotate-enabled #178328
- add konqueror webshortcuts for fedora project #178366
- don't include unnecessary README #169331
 
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Than Ngo <than@redhat.com> 6:3.5.1-2
- apply patch to fix broken xx_XX layouts in kxkb
- cleanup spec file

* Wed Feb 01 2006 Than Ngo <than@redhat.com> 6:3.5.1-1
- 3.5.1
- apply patch to fix kded segfaults for audio/blank cd's
- get rid some of unneeded patches
- add buildrequires on libxkbfile-devel

* Thu Jan 26 2006 Than Ngo <than@redhat.com> 6:3.5.0-3
- add BuildPrereq on dbus-devel >= 0.60, hal-devel >= 0.5

* Wed Jan 25 2006 Than Ngo <than@redhat.com> 6:3.5.0-2
- add dbus support
- backport kde-mount from coolo kde-branch for working with new dbus/hal
- update KDE default setting
- update desktop-database/GTK+ icon cache

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com> 6:3.5.0-1.1
- rebuild for new gcc

* Tue Dec 06 2005 Than Ngo <than@redhat.com> 6:3.5.0-1
- add buildreq on imake

* Thu Dec  1 2005 Jeremy Katz <katzj@redhat.com> - 6:3.5.0-0.2.rc2
- rebuild for new dbus

* Mon Nov 28 2005 Than Ngo <than@redhat.com> 3.5.0-0.1.rc2
- 3.5 rc2

* Sat Nov 19 2005 Bill Nottingham <notting@redhat.com>
- fix paths to openmotif

* Wed Nov 09 2005 Than Ngo <than@redhat.com> 6:3.4.92-4 
- rebuilt against new openssl 

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 6:3.4.92-3
- rebuilt against new openssl

* Mon Oct 24 2005 Than Ngo <than@redhat.com> 6:3.4.92-2
- add separate PAM configuration for kscreensaver #66902

* Mon Oct 24 2005 Than Ngo <than@redhat.com> 6:3.4.92-1
- update to 3.5 beta 2

* Fri Oct  7 2005 Tomas Mraz <tmraz@redhat.com>
- use include instead of pam_stack in pam config
- merged selinux and pam (loginuid) patches

* Thu Sep 29 2005 Than Ngo <than@redhat.com> 6:3.4.91-2
- fix typo

* Tue Sep 27 2005 Than Ngo <than@redhat.com> 6:3.4.91-1
- update to KDE 3.5 Beta1

* Wed Sep 21 2005 Than Ngo <than@redhat.com> 6:3.4.2-5
- fix uic build problem

* Mon Sep 05 2005 Than Ngo <than@redhat.com> 6:3.4.2-4
- apply patch to fix local root vulnerability in kcheckpass CAN-2005-2494, #166997
- apply upstream patch to fix kinfocenter opengl DRI/GLX crash

* Thu Aug 18 2005 Than Ngo <than@redhat.com> 6:3.4.2-3 
- update config files

* Wed Aug 17 2005 Than Ngo <than@redhat.com> 3.4.2-2
- enable switching users #166112

* Mon Aug 01 2005 Than Ngo <than@redhat.com> 3.4.2-1
- update to 3.4.2

* Mon Jul 04 2005 Than Ngo <than@redhat.com> 3.4.1-4
- fix uninitialized variable warning #16231

* Mon Jun 27 2005 Than Ngo <than@redhat.com> 3.4.1-3
- apply patch to fix genkdmconfig crash #161751

* Mon Jun 27 2005 Than Ngo <than@redhat.com> 3.4.1-2
- fix gcc4 build problem

* Mon Jun 06 2005 Than Ngo <than@redhat.com> 3.4.1-1
- 3.4.1
- update pam configuration for the new audit system #159333 

* Tue May 03 2005 Than Ngo <than@redhat.com> 6:3.4.0-7
- fix broken kde-essential.menu

* Tue Apr 19 2005 Than Ngo <than@redhat.com> 6:3.4.0-6
- apply kdebase-3.4.0rc1-konsole-keymap.patch to change backspace key
  to ASCII-DEL, thanks to j.w.r.degoede@hhs.nl

* Wed Apr 13 2005 Than Ngo <than@redhat.com> 6:3.4.0-5
- add more fixes from CVS stable branch
- get rid of unneeded gcc4 workaround in konqueror

* Wed Apr 06 2005 Than Ngo <than@redhat.com> 6:3.4.0-4
- update kdebase-3.4.0rc1-konsole-keymap.patch
- add Bluecurve theme for kdm
- enable show device icons as default

* Fri Apr 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-3
- include config.kcfg directory #153081

* Mon Mar 21 2005 Than Ngo <than@redhat.com> 6:3.4.0-2
- add konsole in desktop menu

* Thu Mar 17 2005 Than Ngo <than@redhat.com> 6:3.4.0-1
- 3.4.0 release

* Wed Mar 16 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.7
- apply gcc4 hack (Dirk Müller) to avoid konqueror crash

* Mon Mar 14 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.6
- default font setting Sans/Monospace
- apply patch to fix the shift cursor left/right strangeness

* Thu Mar 10 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.5
- apply patch (Hans de Goede) to fix incompatibilities between konsole/xterm, #138191

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.4
- rebuilt against gcc-4.0.0-0.31

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.3
- rebuilt against gcc-4

* Sat Feb 26 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.2
- bump release

* Fri Feb 25 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.1
- KDE 3.4.0 rc1

* Wed Feb 16 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.1
- KDE-3.4 beta2

* Thu Feb 10 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.4
- add cleanup patch file from Steve

* Sun Feb 06 2005 Warren Togami <wtogami@redhat.com> 6:3.3.2-0.3
- rebuild against new libraw1394

* Tue Dec 14 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.2
- apply the patch to fix Konqueror Window Injection Vulnerability #142510
  CAN-2004-1158,  Thanks to KDE security team

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.1
- update to 3.3.2
- remove unneeded kdebase-3.3.1-cvs.patch, kdebase-3.3.1-sidebar.patch
- add CVS patch, that fixes a konsole crash

* Thu Nov 25 2004 Than Ngo <than@redhat.com> 6:3.3.1-12
- add patch for kmenu large icons #140842

* Tue Nov 23 2004 Than Ngo <than@redhat.com> 6:3.3.1-11
- the existing icon is lost, add patch to fix this problem #140196

* Tue Nov 23 2004 Than Ngo <than@redhat.com> 6:3.3.1-10
- add patch to fix kfind hang on search #137582

* Fri Nov 12 2004 Than Ngo <than@redhat.com> 6:3.3.1-9 
- fix konqueror crash by dragging some text over the navigation panel

* Thu Nov 11 2004 Than Ngo <than@redhat.com> 6:3.3.1-8
- fix buildrequires on s390/s390x

* Mon Nov 08 2004 Than Ngo <than@redhat.com> 6:3.3.1-7
- apply patch number 86
- add patch to fix man page problem konqueror, thanks to Andy Shevchenko

* Sun Oct 31 2004 Than Ngo <than@redhat.com> 6:3.3.1-6
- remove unneeded require on lm_sensors #137649
- enable devices-symbol
- get rid of unneeded device desktop files

* Sun Oct 31 2004 Than Ngo <than@redhat.com> 6:3.3.1-5
- CVS fixes

* Mon Oct 18 2004 Than Ngo <than@redhat.com> 6:3.3.1-4
- fix a bug in keyboard layout

* Mon Oct 18 2004 Than Ngo <than@redhat.com> 6:3.3.1-3
- add rhel macro to disable fax #134817

* Sat Oct 16 2004 Than Ngo <than@redhat.com> 6:3.3.1-2
- fix KDE default setting
- remove kdm patch, it's included in upstream

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 6:3.3.1-1
- update to 3.3.1

* Thu Oct 07 2004 Than Ngo <than@redhat.com> 6:3.3.0-8
- don't show rpc_pipefs in devices #134940

* Tue Sep 28 2004 Than Ngo <than@redhat.com> 6:3.3.0-7
- fix kdm autologin problem
- get rid of start-here on desktop

* Sun Sep 26 2004 Than Ngo <than@redhat.com> 6:.3.0-6
- cleanup KDE/GNOME menu

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 6:3.3.0-5
- fix kdm segfault

* Mon Sep 20 2004 Than Ngo <than@redhat.com> 6:3.3.0-4
- get rid of requires openssh-client #132148

* Wed Sep 08 2004 Than Ngo <than@redhat.com> 6:3.3.0-3
- Fix ALT-F2 command line opens on wrong desktop bug #129698

* Sun Sep 05 2004 Than Ngo <than@redhat.com> 6:3.3.0-2
- Own mozilla plugin dir, bug #131667
- Fix hangup in kicker when user clears clipboard history fom klipper
- Fix df problem on AFS again

* Thu Aug 19 2004 Than Ngo <than@redhat.com> 6:3.3.0-1
- update to 3.3.0 release

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 6:3.3.0-0.1.rc2
- update to 3.3.0 rc2

* Sun Aug 08 2004 Than Ngo <than@redhat.com> 6:3.3.0-0.1.rc1
- update to 3.3 rc1

* Mon Jul 26 2004 Than Ngo <than@redhat.com> 6:3.2.92-1
- update to 3.3 beta 2
- energy star logo issue
- cleanup some patch files
- fix df problem on AFS

* Mon Jul 19 2004 Than Ngo <than@redhat.com> 6:3.2.3-2
- fix wrong memory info >4GB, bug #125128
- add IM patch, bug #127996

* Fri Jun 18 2004 Than Ngo <than@redhat.com> 6:3.2.3-1 
- update to 3.2.3-1

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 18 2004 Than Ngo <than@redhat.com> 6:3.2.2-6
- fix a bug in keyboard layout with xorg.x11, bug #121950

* Mon May 17 2004 Than Ngo <than@redhat.com> 6:3.2.2-5
- add patch to enable PIE build of kdm

* Tue May 04 2004 Than Ngo <than@redhat.com> 3.2.2-4
- cleanup GNOME/KDE Menu, added OnlyShowIn=KDE

* Sat May 01 2004 Than Ngo <than@redhat.com> 3.2.2-3
- add fix for using /dev/urandom, #118051
- fix wrong translation in desktop file, #121736

* Mon Apr 19 2004 Than Ngo <than@redhat.com> 3.2.2-2
- fix bug #109954, motif resource issue

* Tue Apr 13 2004 Than Ngo <than@redhat.com> 3.2.2-1
- 3.2.2 release

* Thu Apr 01 2004 Than Ngo <than@redhat.com> 3.2.1-1.7
- remove redundant Xsession, bug #119503

* Mon Mar 29 2004 Than Ngo <than@redhat.com> 3.2.1-1.6
- cleanup KDE/GNOME menus

* Mon Mar 22 2004 Than Ngo <than@redhat.com> 3.2.1-1.5
- fix typo bug
- add missing Catagories in konsole, #118864
- add missing requires on kdelibs-devel, bug #118605

* Wed Mar 17 2004 Karsten Hopp <karsten@redhat.de> 3.2.1-1.4 
- use new virtual package 'xfs'

* Tue Mar 16 2004 Than Ngo <than@redhat.com> 3.2.1-1.3
- fixed KDE menus, #118282

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.2
- cleanup Gnome/KDE menu

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.1
- fixed desktop files issues , bug #117822

* Tue Mar 09 2004 Than Ngo <than@redhat.com> 6:3.2.1-1
- rebuild

* Fri Mar 05 2004 Than Ngo <than@redhat.com> 6:3.2.1-0.1
- 3.2.1 release

* Thu Mar 04 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.11
- fixed requires issue on redhat-artwork

* Wed Mar 03 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.10
- respin kde-redhat-config

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Than Ngo <than@redhat.com> 3.2.0-1.9
- don't rename to the contents of the translated Name field
- create desktop files if Desktop directory is empty

* Sun Feb 22 2004 Than Ngo <than@redhat.com> 3.2.0-1.8 
- cleanup startkde
- adapt a patch file to allow different icon size in kicker menu

* Sat Feb 21 2004 Dan Walsh <dwalsh@redhat.com> 6:3.2.0-1.7
- add selinux support to kde pam file

* Thu Feb 19 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.6
- KDM, use standard directory /usr/share/xsessions
- fix a bug in selection of session type in KDM

* Tue Feb 17 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.5
- fix typo bug, _smp_mflags instead smp_mflags

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Than Ngo <than@redhat.com> 3.2.0-0.4 
- improve bluecurve keymap
- fixed broken symlink

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.3
- build against qt 3.3.0
- cleanup specfile
 
* Tue Feb 03 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.2
- 3.2.0 release

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.1
- KDE 3.2 RC1

* Thu Jan 08 2004 Than Ngo <than@redhat.com> 6:3.1.94-0.4
- added kdebase-3.1.94-kpersonalizer.patch (bluecurve as default)

* Wed Dec 10 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.3
- include kdm README

* Tue Dec 02 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.2
- KDE 3.2 Beta 2 respin
- adjusted aboutkde.patch for 3.2
- remove kdebase-3.1.93-menu.patch, it's in upstream

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.1
- KDE 3.2 Beta 2

* Mon Nov 17 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.3
- disable kpersonalizer
- fix konsole desktop file
- get rid of some old workarounds in startkde, speedup startkde
- get rid of theme, it's obsolete in 3.2
- add missing starthere icon
- add missing kde-unknown.directory

* Sun Nov 16 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.2
- start-here protocol
- BlueCure Ksplash as default
- fix menu issue in kicker/kcontrol

* Tue Nov 04 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.1
- KDE 3.2 Beta 1
- remove many patch files, which are now in upstream
- cleanup many patch files
- cleanup startkde
- cleanup rpm file list

* Tue Oct 28 2003 Than Ngo <than@redhat.com> 6:3.1.4-6
- vfolder 0.1.5
- kde-redhat-config-3.1.3-4
- added some missing icons

* Mon Oct 27 2003 Than Ngo <than@redhat.com> 6:3.1.4-5
- add support protocol start-here for vfolder (bug #105667)
- vfolder 0.1.4
  
* Tue Oct 14 2003 Than Ngo <than@redhat.com> 6:3.1.4-4
- add patch to allow different icon size in kicker menu
- don't reset icon size to 20x20 if it's greater than 20

* Fri Oct 10 2003 Than Ngo <than@redhat.com> 6:3.1.4-3
- add patch files from Hans de Goede, (bug #63473, #80650, #80651)

* Tue Oct 07 2003 Than Ngo <than@redhat.com> 6:3.1.4-2
- install kde.desktop in /usr/share/xsession
- add more translations for kde.desktop (stolen from kde 3.2 cvs)

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 6:3.1.4-1
- 3.1.4

* Fri Aug 29 2003 Than Ngo <than@redhat.com> 6:3.1.3-7
- add kde.desktop session for new gdm (bug #103292)

* Thu Aug 28 2003 Than Ngo <than@redhat.com> 6:3.1.3-6
- adopted a patch file from Mandrake, it fixes full screen problem

* Mon Aug 18 2003 Than Ngo <than@redhat.com> 6:3.1.3-5
- fixed kosmetic bug in ksplash (bug #100729)


* Thu Aug 14 2003 Than Ngo <than@redhat.com> 6:3.1.3-4
- adjust the patch file from peter.backlund@home.se for kpersonalizer (bug #100551)

* Mon Aug 11 2003 Than Ngo <than@redhat.com> 6:3.1.3-3
- add better default font setting for konqueror (bug #101735)

* Thu Jul 31 2003 Than Ngo <than@redhat.com> 6:3.1.3-2
- rebuilt

* Wed Jul 30 2003 Than Ngo <than@redhat.com> 6:3.1.3-1
- 3.1.3
- new patch for kicker (bug #86565, #87754, #100728)

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 6:3.1.2-20
- rebuild

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 6:3.1.2-19
- vfolder-0.1.3

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 6:3.1.2-18
- fix a bug in setting of defaultfont

* Thu Jul 17 2003 Than Ngo <than@redhat.com> 6:3.1.2-17
- rebuild

* Thu Jul 10 2003 Than Ngo <than@redhat.com> 6:3.1.2-16
- desktop files issue (bug #98843)

* Wed Jul  9 2003 Than Ngo <than@redhat.com> 6:3.1.2-15
- "open terminal" menu entry

* Thu Jul 3 2003 Than Ngo <than@redhat.com> 6:3.1.2-12
- fix vnc server conflict with DCOPserver (bug #68432)
- cleanup startkde

* Thu Jul  3 2003 Than Ngo <than@redhat.com> 6:3.1.2-11
- fix search path for mozilla plugins (bug #92437)

* Tue Jul  1 2003 Than Ngo <than@redhat.com> 6:3.1.2-10
- fix keydef bug (#97937)

* Wed Jun 25 2003 Than Ngo <than@redhat.com> 6:3.1.2-8
- remove excludearch s390/s390x

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  4 2003 Than Ngo <than@redhat.com> 6:3.1.2-6
- fix to build nsplugins with openmotif
- add buildrequires openmotif-devel instead lesstif-devel
- vfolder-0.1.2

* Mon May 26 2003 Than Ngo <than@redhat.com> 6:3.1.2-4
- KDE launch feedback enable as default bug #90519
- permission fix on kde config file

* Thu May 15 2003 Than Ngo <than@redhat.com> 6:3.1.2-3
- respin

* Mon May 12 2003 Than Ngo <than@redhat.com> 6:3.1.2-1
- 3.1.2

* Thu May  8 2003 Than Ngo <than@redhat.com> 6:3.1.1-9
- klipper can't load URLs with mozilla, bug #87430

* Tue May  6 2003 Than Ngo <than@redhat.com> 6:3.1.1-8
- add patch for using /usr/share/hwdata/usb.ids

* Mon Apr 21 2003 Elliot Lee <sopwith@redhat.com> 6:3.1.1-7
- Unconditionally extract vfolder archive, to allow for patching
- Patch vfolder/admin/cvs.sh to deal with new 'head' options.
- Patch vfolder/xmlcheck/main.cpp to fix typo

* Wed Apr 16 2003 Than Ngo <than@redhat.com> 6:3.1.1-6
- bugfix in vfolder

* Mon Apr 14 2003 Than Ngo <than@redhat.com> 6:3.1.1-5
- add xrandr support

* Mon Apr 14 2003 Than Ngo <than@redhat.com> 6:3.1.1-4
- PS/PDF file handling vulnerability

* Thu Apr  3 2003 Than Ngo <than@redhat.com> 6:3.1.1-3.1
- add patch file to fix smb bug, #80913, #75104

* Tue Apr  1 2003 Than Ngo <than@redhat.com> 6:3.1.1-3
- fix a bug in Xpdf resource file
- use htmlview as preferred browser

* Thu Mar 20 2003 Than Ngo <than@redhat.com> 6:3.1.1-2
- add patch file from CVS to fix: Minicli layout problem,
  KDM user window width is incorrect

* Tue Mar 18 2003 Than Ngo <than@redhat.com> 6:3.1.1-1
- 3.1.1 release
- get rid of some patch files, which are now in new upstream
- adjust some patch files for 3.1.1
- permission fix
- get rid of unneeded pam config file of kscreensaver
- move desktop-create-menu to kdelibs

* Wed Feb 26 2003 Than Ngo <than@redhat.com> 6:3.1-12
- energy star logo issue

* Tue Feb 25 2003 Than Ngo <than@redhat.com> 6:3.1-11
- rpm file list issue (#84999)
- add printer manager icon to panel

* Mon Feb 24 2003 Than Ngo <than@redhat.com> 6:3.1-10
- security fix in kio-fish

* Sat Feb 22 2003 Than Ngo <than@redhat.com> 6:3.1-9
- set default start page to red hat welcome page (#84858)
- add fix for KDE Random Screensaver (#83671)

* Thu Feb 20 2003 Than Ngo <than@redhat.com> 6:3.1-8
- don't show empty folder, #84029

* Thu Feb 13 2003 Thomas Woerner <twoerner@redhat.com> 6:3.1-7
- fixed arts bug #82750, requires rebuild of kdebase

* Sat Feb  8 2003 Than Ngo <than@redhat.com> 6:3.1-6
- i18n issue in kio-vfolder

* Thu Feb  6 2003 Than Ngo <than@redhat.com> 6:3.1-5
- fix scanpath mozilla plugin, #83618
- add a patch file from Leon Ho llch@redhat.com,  #82529
- add some missing KDE screensavers, bug #83671

* Tue Feb  4 2003 Than Ngo <than@redhat.com> 6:3.1-4
- rhn-applet/pam-panel-icon/eggcups applet start correct now, #83264
- set NFSPollInterval=5000, PollInterval=500

* Tue Feb  4 2003 Thomas Woerner <twoerner@redhat.com> 6:3.1-3
- fixed panel button resize probem

* Fri Jan 31 2003 Than Ngo <than@redhat.com> 6:3.1-2
- fix wrong Catagory, bug #82441
- fix mouse focus, bug #82675

* Tue Jan 28 2003 Than Ngo <than@redhat.com> 6:3.1-1
- 3.1 final

* Sun Jan 26 2003 Than Ngo <than@redhat.com> 6:3.1-0.17
- rc7
- remove check_size_t patch
- cleanup specfile

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 6:3.1-0.16
- rebuild

* Wed Jan 15 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.15
- added s390 flags
- included ia64 again

* Mon Jan 13 2003 Karsten Hopp <karsten@redhat.de> 3.1-0.14
- Missing epoch in requires

* Mon Jan 13 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.13
- rc6
- exclude ia64
- ssl uses krb5
- size_t check

* Mon Jan  6 2003 Nalin Dahyabhai <nalin@redhat.com> 3.1-0.12
- add openssl-devel as a buildreq
- add pkgconfig as a buildreq
- if pkgconfig admits to knowing about openssl, incorporate its information

* Sun Dec 29 2002 Than Ngo <than@redhat.com> 3.1-0.11
- fix bug #80307

* Tue Dec 17 2002 Than Ngo <than@redhat.com> 3.1-0.10
- remove unneeded files

* Mon Dec 16 2002 Than Ngo <than@redhat.com> 3.1-0.9
- rebuild
- Fix wrong Start Here Url (bug #78178)

* Sun Dec 15 2002 Than Ngo <than@redhat.com> 3.1-0.8
- Add missing desktop files
- requires redhat-menus-0.30

* Sun Dec  8 2002 Than Ngo <than@redhat.com> 3.1-0.7
- remove unneeded patch file
- fix dependency issue

* Thu Dec  5 2002 Than Ngo <than@redhat.com> 3.1-0.6
- clean up KDE menu/kcontrol center menu
- fix build problem on s390/s390x
- eggcups to kdebase default session (Tim Waugh)
- rpm macros (Mike Harris)

* Wed Dec  4 2002 Than Ngo <than@redhat.com> 3.1-0.5
- move 9x15 fix font to bitmaps font package
- bug fix in kinfo center
- add new catagories

* Sun Dec  1 2002 Than Ngo <than@redhat.com> 3.1-0.4
- bug fixes kcontrol center/file browsing/Look&Feel
- add RH kdm default configuration

* Wed Nov 27 2002 Than Ngo <than@redhat.com> 3.1-0.3
- adjust 2 patch files again
- add correct option in configure
- use %%configure

* Mon Nov 25 2002 Than Ngo <than@redhat.com> 3.1-0.2
- fix desktop file issues

* Wed Nov 20 2002 Than Ngo <than@redhat.com> 3.1-0.1
- 3.1 rc4
- adjust many patch files for 3.1
- remove some patch files, which are now in 3.1

* Tue Nov 19 2002 Than Ngo <than@redhat.com> 3.0.5-4
- fix konsole crash on startup with qt 3.1.0

* Mon Nov 11 2002 Nalin Dahyabhai <nalin@redhat.com> 3.0.5-3
- remove directory names from PAM configuration files so that they can be
  used for all arches on multilib boxes

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 3.0.5-2
- fix lib64 issue

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 3.0.5-1
- update to 3.0.5

* Fri Nov  8 2002 Than Ngo <than@redhat.com> 3.0.4-2.2
- konsole super user mode shouldn't require password to be retyped (bug #77387)
- unpackged files in buildroot

* Sat Oct 12 2002 Than Ngo <than@redhat.com> 3.0.4-1
- cleanup some patch file for 3.0.4
- cleanup configure to build correct on x86_64
- Added /etc/X11/applnk in WatchDir
- KDE screensaver issue (bug #73412)
- better handling of desktop file renames (bug #74071)
- Konsole screen refresh is slow (bug #73303, #75154)
- localiztion fix (bug #75085, #75012)
- Unable to acess the preferences of KNewsTicker (bug #74805)

* Thu Sep  5 2002 Than Ngo <than@redhat.com> 3.0.3-13
- Fixed i18n issue in kio-vfolder 

* Tue Sep  4 2002 Than Ngo <than@redhat.com> 3.0.3-12
- Added KAboutKDE to kicker menu

* Tue Sep  3 2002 Than Ngo <than@redhat.com> 3.0.3-11
- Fixed Url start here
- Set Volume to 20 as default

* Sun Sep  1 2002 Than Ngo <than@redhat.com> 3.0.3-10
- Fixed kdm to read X resource if it's deleted.
- Set Bluecurve theme in kdm as default
- Add share/applnk in WatchDir
- remove merging share/applnk
- Ajust Colors scheme

* Sat Aug 31 2002 Than Ngo <than@redhat.com> 3.0.3-9
- turn on  AntiAliasing in KDM as default (bug #68872)
- fixed KDM using Fonts Sans
- put Red Hat in the version number
- disable Report Bug menu item
- turn off stick button in window title
- added katefiledialogencoding patch from Leon Ho (bug #68214)

* Wed Aug 28 2002 Than Ngo <than@redhat.com> 3.0.3-8
- Fixed kicker not showing buttons if desktop file not found (bug #71141)
- Fixed clock patch to prefer redhat-config-date
- klippper only showed in KDE
- Add icon order patch from Phil Knirsch

* Wed Aug 28 2002 Than Ngo <than@redhat.com> 3.0.3-7
- Added Bluecurve theme for kthememanager
- Fixed a bug in KDE default theme (bug #71413)
- Added missing KDE settings
- Added keymap patch and clock patch from Preston
- Adjusted clock patch

* Tue Aug 27 2002 Than Ngo <than@redhat.com> 3.0.3-6
- Fix vfolder bug again

* Mon Aug 26 2002 Than Ngo <than@redhat.com> 3.0.3-5
- Add fix to resize panel icons (bug #72549)
- Add fix to lauch kdm login manager module from kcontrol (bug #72470)
- remove OnlyShowIn KDE in konqueror (bug #72408)
- Get rid of kpersonalizer from startkde, now KDE supports LANG (bug #72251)
- Fix vfolder bug (bug #71919)
- Set Sans 10 as default font
- Set help_about_kde to false as default
- Rename konsole to Terminal
- Add fix to reload global X resource if it's deleted

* Thu Aug 22 2002 Preston Brown <pbrown@redhat.com> 3.0.3-4
- default keybinding file for Bluecurve theme

* Wed Aug 21 2002 Preston Brown <pbrown@redhat.com> 3.0.3-4
- Default mouse focus should be click to focus (#71816)
- move all "Preferences->System" items to Extras
- move kdm configuration to Extras
- remove "Date & Time" (duplicate functionality) from menus (#59695)
- remove kcmfontinst (incompatible functionality) from menus (#59695)
- Kate into Accessories category (from Programming)
- fix Configure... menu entry in RMB menu of kwin
- default wallpaper mode is Scaled not Centered

* Wed Aug 14 2002 Than Ngo <than@redhat.com> 3.0.3-3
- Some Tweaks in configuration
- lauch rhn-applet-gui instead applet-gui
- Fixed kpersonalizer using Bluecurve instead Wonderland

* Tue Aug 13 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.3-2
- Some fixes in the vfolder ioslave
- Support <Not> queries in the vfolder ioslave
- Add Start Here icon on desktop

* Thu Aug  8 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3
- Added some rh default settings in kicker/kwin
- Fixed a bug in kicker to start menueditor (bug #71164)
- Fixed a bug in setting clock/date
- Added fix to start rhn-applet and pam-panel-icon in systemtray
- Configuration tweaks (bug #70926)
- Added fix to use Bluecurve
- Added new desktop-create-kmenu
- Added a systemtray patch from Harald Hoyer

* Wed Aug  7 2002 Than Ngo <than@redhat.com> 3.0.2-8
- Implemented slotRhDescription in kpersonalizer (bug #70863)
- Added more BuildPrereq (bug #69992, #70011)
- Wonderland icon Theme as default (bug #69654)
- Added fix for looking desktop file with prefix kde
- Fixed a bug Konsole configure (bug #67217)
- don't use prefix kde by some typical KDE appllications
- use -O0 on alpha machine (compiler bug)

* Mon Aug  5 2002 Than Ngo <than@redhat.com> 3.0.2-7.2
- add patch file to fix kicker segfault (bug #69688)
- get rid of Taiwanese Flag in KDE (bug #70235)

* Sun Aug  4 2002 Than Ngo <than@redhat.com> 3.0.2-7.1
- don't merge old kde menus (#69652)
- add fix to show evolution/mozilla in kicker (#69725, #70152, #70618, #69822)
- add fix to have rh panel layout (#59676)
- add some fixes from 3.0.2 stable branch
- add a patch file to fix a bug in startkde, Karsten Hopp
- add requires images for ksplash
- add pam_timestamp support (#69863)
- add fix to make kpersonalizer usable in 640x480 resolution (#68358)
- add fix for looking DesktopEntryName with prefix kde

* Thu Aug  1 2002 Tim Powers <timp@redhat.com> 3.0.2-7
- don't install the ksplash icons since we're using the images in the
  redhat-artwork package

* Tue Jul 23 2002 Than Ngo <than@redhat.com> 3.0.2-6
- Added correct path to load background image

* Mon Jul 22 2002 Than Ngo <than@redhat.com> 3.0.2-5
- Fixed a bug by writing widgetStyle in confile
- default.jpg as default background, if no background image is found
  use plain color #5477A0
- BusyCursor=false as default for rh Style
- use klipper applet rather than tray icon (bug #67107)
- add rh panel layout
- build against gcc 3.2-0.1

* Fri Jul 17 2002 Than Ngo <than@redhat.com> 3.0.2-4
- merge /var/lib/menu/kde/Applications
- Added missing index file for Crystal icons
- Own /usr/share/icons/Crystal, /usr/share/mimelnk/print
- Fixed kwin issue in kpersonalizer
- Added a missing patch file
- Fixed KDE menu issue (bug #69102, #67648)
- Fixed Control Center issue (bug #69031) 
- Tiny tweaks to kdebase .desktop files (bug #69002)
- Added some hacks for KDE screen savers

* Tue Jul 16 2002 Than Ngo <than@redhat.com> 3.0.2-3
- Added patch in konqueror, it should search pluggins on mozilla directory (bug #68599)
- Fixed a bug in merging /etc/X11/applnk (bug #64919,64594)
- Added patch for merging /var/lib/menu/kde
- Fixed a bug in kcontrol, it should search screensavers in /var/lib/menu/kde
- Added desktop-create-kmenu
- Added fix for building against g++-296 (bug #68752)
- Added fix in KDE font installer using xfs reload (bug #64664) (rdieter@math.unl.edu)
- Fixed refresh issue in konsole (Harald Hoyer)
- Fixed font issue in konsole (bug #68476)
- Fixed font issue in terminal emulation under Konqueror (bug #68618)
- correct fonts in KDE startup (bug #68872)
- Redhat Style Kwin has opaque resize as default (bug #68401)
- AntiAliasing on as default in Redhat Style Wonderland
- Added missing screensave desktop files
- Rename the section in screen save desktop files
- Don't strip binaries
- get rid of wallpapers, requires desktop-backgrounds-basic,
  wallpapers are now in desktop-backgrounds-basic
- Fixed colorScheme issue in kpersonalizer
- Added floppy unit icon missing on desktop (bug #68890)
- Adapted kdebase to new desktop background framework (bug #66784)
- 3.0.2 fixed bug #63700

* Wed Jul 10 2002 Than Ngo <than@redhat.com> 3.0.2-2
- use desktop-file-install

* Tue Jul  2 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-1
- 3.0.2

* Thu Jun 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020627.1
- Add Red Hat style to kpersonalizer
- Update

* Tue Jun 25 2002 Bernhard Rosenkraenzer <bero@redhat.com> 
- Change defaults
- Add the vfolder ioslave
- Add hacks to launch desktop-create-kmenu when needed, merge /etc/kde/menu

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 10 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-1
- 3.0.1

* Wed Apr 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-12
- Make kwin more tolerant to missing window hints, fixes #62308
  Patch from Matthias Ettrich

* Wed Apr 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-11
- Fix #63657 and #63473

* Mon Apr 15 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-10
- Move in new splash screen
- Change sonames to take care of compiler changes

* Fri Apr 12 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-9
- Try to fix bug #60811 (kpersonalizer now sets default fonts for CJK)
- Put kicker configuration back in kpersonalizer (#61266) and make sure the
  minimal variant is selected for extremely low resolutions (#63266)

* Thu Apr 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-8
- Don't link desktopconv against libqt
- Update flag patch (#61946)

* Tue Apr  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-7
- Fix default kicker config - it shouldn't point to absolute paths (#62355)
- Add build requirement on samba >= 2.2.3a-5 to build the correct smb
  ioslave (#62202)

* Mon Apr  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-5
- Add fixes from KDE_3_0_BRANCH, except for the "F1 in konsole" change
  (that one breaks things)
- Don't show Taiwanese flag for zh_CN (#61946)
- Move in Red Hat splash screen

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-4
- Fix issues with multiple instances of kbookmarkeditor being opened
  at the same time
- Remove the static cdparanoia hack, we're shipping shared cdparanoia
  libs these days.

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-3
- Merge patches from KDE_3_0_BRANCH:
  - Fix konsole crash
  - Fix Comment vs. GenericName issue in kcm_kdm
  - Fix memory leak in kcontrol

* Thu Mar 28 2002 Than Ngo <than@redhat.com> 3.0.0-2
- fix to use shared xdm config files
- add requires some xdm config files

* Tue Mar 26 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-1
- 3.0 final
- Add fix for minimizing toplevel windows from KDE_3_0_BRANCH

* Tue Mar 26 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020326.1
- Make kdm use the shared {k,x,g}dm config files rather than putting in its own

* Thu Mar 21 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020321.1
- Some more config changes

* Wed Mar 20 2002 Than Ngo <than@redhat.com> 3.0.0-0.cvs20020320.1
- update kdebase config for Red Hat

* Tue Mar 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020314.4
- Fix up kdm

* Mon Mar 18 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020314.3
- Add patches from Than to fix up menu i18n and kdm sessions
- Put back %%{?_smp_mflags}

* Tue Mar 12 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020314.1
- Add patch from Than to scale down icons for submenus pointing to legacy
  applications rather than keeping them at 32x32

* Mon Mar 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020311.1
- Add patch to kicker allowing it to display just the app descriptions instead
  of names

* Fri Mar  1 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020301.1
- Update
- Remove separate kdm package

* Thu Feb 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020214.1
- Build --with-xinerama

* Tue Jan 29 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020129.1
- Manually add Provides: libkateinterfaces.so to work around rpm bug

* Sun Jan 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020120.1
- Update to get API changes
- Clean up old temp files in startkde some more

* Thu Jan 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020117.2
- Make sure the correct kdelibs is in the build environment before building
  kdebase

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020107.1
- Update, sync with kdelibs API changes

* Sat Dec 29 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20011229.1
- Update

* Wed Dec 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20011226.1
- Update
- Disable ia64 temporarily (because of bug #57833)

* Sat Dec 15 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20011215.1
- Update
- Make kdm a separate package

* Fri Dec 14 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20011214.1
- Update
- Exclude alpha for now (compiler bugs)

* Sun Aug  5 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010805.1
- Fix anti-aliased fonts
- Remove Japanese konsole patch, it breaks changing fonts in all other
  languages
- BuildRequire lesstif-devel to make sure recompiled versions of Konqueror
  support Netscape plugins
- Remove language detection hacks from startkde, they're now in kpersonalizer
- Personalize kicker in kpersonalizer
- Power off when halting the system in kdm (#50847)

* Thu Aug  2 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010802.1
- Remove Japanese Konsole patch, it breaks other languages (#50619)

* Tue Jul 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010731.1
- Remove some patches that made it into cvs
- Fix up the Japanese patch, it messed up konsole fonts on "normal"
  languages

* Mon Jul 30 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010730.1
- Fix up audiocd ioslave (#50310)
- Initialize kpersonalizer to $LANG (#50311)
- Add Japanese patch

* Wed Jul 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010725.1
- Fix error messages on first startup

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010724.1
- remove ia64 workarounds
- fix default configurations
- update
- remove dupes from kdeartwork

* Sun Jul 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010722.1
- rebuild after fixing the build root

* Sat Jul 21 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010721.1
- rebuild - somehow an application got linked against an older version of
  itself from the buildroot
- update

* Fri Jul 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010720.1
- update
- get rid of some rpmlint warnings
- remove kappfinder (we maintain /etc/X11/applnk)
- work around ia64 breakage

* Wed Jun 27 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010627.1
- update
- adapt patches

* Sat Jun 16 2001 Alan Eldridge <alane@geeksrus.net> 2.2-0.cvs20010616.1
- updated for current CVS

* Tue May 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.alpha2.2
- Work around NFS-mounted home directories residing on servers with
  ultimately broken OSes (#40711)
- Fix desktopconv compilation without optimizations (#40144)
- Move old config files rather than deleting them (#38107)
- Add explicit requirements on lm_sensors and kdelibs-sound (#32678)
- Fix doc generation (#40087)
- s/Copyright:/License:/

* Sun May 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.alpha2.1
- 2.2 alpha 2

* Sun May 13 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010513.1
- Fix up default settings; KSpell should use Aspell right away
- Split out -devel subpackage; with KWin and Kate moving to plugin systems,
  this is getting big...

* Sat May 12 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010512.1
- Update, adapt patches
- Fix up desktop devices patch, we want the "Eject" action for CD-ROMs,
  CD-Writers, CD-RWs, ZIP and JAZ-Drives and LS120.

* Fri Apr 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.2alpha1
- kill /usr/share/icons/locolor/16x16/actions/bookmark_folder.png
  (dupe from kdelibs)

* Tue Apr  3 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix deadkeys handling in kdm
- Fix uninitialized variable in konsole, patch
  from Tim Waugh (#34452)

* Fri Mar 30 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix rpmfind shortcut (Bugzilla #34057, KDE Bug #21100)
- Add patch from KDE_2_1_BRANCH to get rid of debug output in
  the ktar IO slave

* Wed Mar 28 2001 Than Ngo <than@redhat.com>
- fix a bug in desktopconv (bug #33374)

* Tue Mar 27 2001 Than Ngo <than@redhat.com>
- fix charmap/encoding problem
- fix MinimumFontSize in konqueror, default is 10
- set correct DefaultEncoding for konqueror
- clean up startkde
- disable Israel and Thai, it's broken in qt

* Fri Mar 23 2001 Preston Brown <pbrown@redhat.com>
- remove CD-ROM / Floppy .desktop files, they are generated automatically now
- remove some other old obsolete default config files

* Thu Mar 22 2001 Preston Brown <pbrown@redhat.com>
- patch to dynamically create icons for removable/user controllable 
  devices on desktop

* Wed Mar 21 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.1.1-2
- Log utmp/wtmp correctly in konsole, using utempter
- Remove setuid state from konsole_grantpty, it's no longer needed now
  that we use utempter.
- Fix escaping in the konsole KPart
- Fix grammar and order in the arts control module

* Tue Mar 21 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.1.1-1
- 2.1.1
- Don't crash if kfmexec is invoked without arguments (#32029)
- Various desktopconv fixes:
  - Allow removing or ignoring KDE 1.x files
  - convert the printer icon we had on the desktop by default.
  - Support i18n
- Add mailsettings tool (generates sane kcmemail defaults at first
  startup)
- Fix up support for Brazil Portuguese and Chinese
- Fix loading of child panel config files (harald)
- remove -T and --title in konsole, use instead --caption (#31483) (Than Ngo)
- More i18n fixes (zh_HK is closer to zh_TW than to zh_CN...)

* Mon Mar 20 2001 Than Ngo <than@redhat.com>
- fix Login Screen Red Hat logo (Bug #32241)
- fix kdm background color
- fix a bug in setting font size (Bug #32258)

* Fri Mar 17 2001 Than Ngo <than@redhat.com> 2.1-11
- fix placed icons on desktop (Bug #31985)
- some bugfixes in startkde
- restore support for Russian (bero)
- merge bugfix patch from KDE_2_1_BRANCH, Ctrl-U could crash Konqueror
  under certain circumstances (bero)
- Fix up the effects patch (if everything was disabled, no radio button
  was checked by default, rather than the "No effects" button) (bero)

* Thu Mar 15 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-10
- Fix up i18n support
- Don't use predictable tmp file names in krdb
- Remove the printer icon from the desktop. It uses klpq which is in kdeutils,
  so the icon should come from there.
- fix error.c in kdebase-2.1-fixes.patch, It's broken (Than Ngo)
- better fix for konsole keyboard mappings (Preston Brown)

* Tue Mar 13 2001 Than Ngo <than@redhat.com>
- fix default profile for konqueror in webbrowser mode 
- set lucidatypewriter as fixed-width font for konqueror
  
* Mon Mar 12 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-9
- Fix locale settings (old versions didn't check the user's locale settings
  and always started up in English)
- Fix some braindead code in kwrite

* Sat Mar 10 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-8
- Add option to save backtraces to a file (#30867)
- Fix kdm looking horrible on 8 bit displays
- Revert to /usr/share/config with an exception for kdmrc
- Add /etc/skel/Desktop/.directory (the /etc/skel/Desktop/* glob doesn't include
  /etc/skel/Desktop/.* ...)
- Don't apply konsole-noxft patch anymore (workaround for an X bug
  that was fixed in 11.4)

* Fri Mar  9 2001 Preston Brown <pbrown@redhat.com>
- fix home and end default mapping in konsole

* Wed Feb 28 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- /usr/share/config -> /etc/kde
- Don't throw all config files at every user's home directory; 2.x supports
  changing global defaults
- Get rid of bogus "can't find schema named" warning
- Fix various bugs in konsole (don't connect to a NULL slot, etc.)
- Cripple kxmlrpcd by default (#23253)
- Add a sane icon arrangement at first startup (#25026)
  
* Tue Feb 27 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add fixes from KDE_2_1_BRANCH:
  - Fix up cookie handling in konqueror
  - Fix a potential crash in kcontrol when using config files from
    cvs snapshots
  - Fix possible khotkeys segfault
- Fix up Konqueror User Agent dialog
- Log in to "default" session by default (#29157)

* Thu Feb 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.1 second (and hopefully last) respin

* Wed Feb 21 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.1-respin
- Drop the old anotherlevel session type in kdm (#28593)

* Mon Feb 19 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.1

* Wed Feb 14 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up konsole_grantpty to work with the /dev/pts filesystem and
  /dev/ptmx rather than the old /dev/ptyXX system
- Replace ktip logo with Red Hat logo, the old one could be considered
  offensive by some people
- Fix build with glibc 2.2.2
- Turn off icon view in kdm
- Other minor changes to default config

* Mon Feb 12 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- desktopconv: Don't strip off .png/.xpm/.gif in Icon= if it is
  provided as a full pathname
- Build with --disable-debug
- Fix a bug causing all icons to appear in the upper-left corner
- Don't use antialiased fonts in konsole even if they're turned on.
  Konsole can't deal with them.
- Don't show the postgres and amanda users in kdm
- Add rhbug/bz shortcut to Bugzilla
- Add ftpsearch/fs shortcut to FTP Search
- Add "Eject" option to CD-ROM icon (RFE #26301)
- Fix permissions on some files in /etc/skel/Desktop (having them readable
  by root only is not really useful ;) )
- Fix PAM exiting (#25232, Patch from Tim Waugh)
- Fix utmp handling in konsole (Bug #25048)
- Rewrite desktopconv and run it from startkde, ensures
  clean updates from KDE 1.x (Bug #25473)
- Add $HOME/bin to PATH in kdm (Bug #25743)

* Fri Feb  2 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Link the greeter into kdm statically, pulling in libpthreads
  Fixes crash with glibc-2.2.1-3 i686

* Fri Jan 26 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- exec ksmserver rather than just starting it - there's no need to keep
  that shell in memory.

* Thu Jan 25 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Turn off anti-aliasing by default
- Restore the turning AA on/off and "apply styles to non-KDE-apps"
  functionality, someone managed to break them just in time for
  2.1 beta 2.

* Tue Jan 23 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix bugs #23136 and #24709

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Kill /usr/share/icons/hicolor/22x22/actions/view_tree.png, it's in
  kdelibs
- restore missing /etc/kderc (Bug #24601)

* Sat Jan 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix update if Autostart directory exists, but is empty
- Fix usage of mktemp in startkde (#24415)

* Fri Jan 19 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update CVS (fixed #24298, #24242)
- Hack in support for turning anti-aliasing on and off, as requested
  by Than. Unfortunately, this patch probably won't go into the base 2.1
  because of the message freeze.

* Wed Jan 17 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to CVS; I fixed building with OpenLDAP 2.x in there.

* Tue Jan 16 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add kscreensaver pam file (copy the xscreensaver one, don't
  use the broken one from KDE CVS)

* Thu Jan 11 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't replace a directory with a symlink (#23671)

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix background (#20910)

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- kdm shouldn't show gdm and mailnull users (#23136)
- don't install the konsole fonts, they're now
  included in XFree86 (#23467)
- Obsoletes kdebase2 (from 7.0-preview)
- Add config files (used to be in kdesupport) (#22601)

* Mon Jan  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update

* Wed Dec 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update
- Obsolete kdebase-3d-screensavers, kdebase-locolor-icons,
  kapm kcmlaptop (optional stuff from KDE 1.x)

* Thu Nov  9 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to HEAD branch
- s/Prereq/Requires(post,postun)/

* Thu Nov  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Some fixes to startkde:
  - if /etc/skel/.kde doesn't exist, don't copy it
  - remove stale .DCOPserver* files at startup
- Rebuild with fixed kdoc

* Tue Oct 31 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Move include files to /usr/include/kde
- Don't install any of the mini-lesstif files, we need them at
  build time only
- Fix consolehelper config for kappfinder

* Sat Oct 28 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to KDE_2_0_BRANCH, now that the ".0 release" bugs are fixed
- Get rid of the Red Hat menu, it's merged now
- Fix up the gdm session file
- Fix up kappfinder, run it through consolehelper (Bug #19903)
- Enable Netscape plugin support, add a stripped down version of lesstif
  to allow this

* Mon Oct 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0 final

* Sun Oct  1 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new CVS
- fix installation of fonts

* Sat Sep 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new CVS snapshot
- fix up spec file

* Wed Aug 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- get rid of the 3d-screensavers package - now that qt-GL is part of qt,
  there's no need to keep them separate to avoid the dependency.

* Mon Aug 21 2000 Than Ngo <than@redhat.com>
- fix gnome-session so that KDE2 can be started from gdm
- pam/kde2 instead pam/kde to avoid problem with KDE1
- don't requires qt-GL, It's now in qt

* Sun Aug 20 2000 Than Ngo <than@redhat.com>
- fix dependency problem with KDE1 so that KDE1 and KDE2 can be installed
  at the same time
- add missing ldconfig in %%post and %%postun
- fix for reading config files in /etc/X11/xdm, add Xsession to requires

* Tue Aug  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix keytable in konsole (Bug #15682)

* Sun Aug  6 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild, now that kdelibs2 works on alpha
- use the same ugly hack to get kdebase to compile
- remove ksysguard on alpha (even more compiler problems)

* Fri Aug  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot (fixed libGL detection in CVS)

* Wed Aug  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- move to /usr/lib/kde2
- new snapshot

* Sun Jul 23 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix the --xdmdir arg to be correct (oops)

* Fri Jul 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- move kdm config files from /usr/config to /etc/X11 by forcing xdmdir

* Fri Jul 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot
- some fixes to spec file

* Tue Jul 18 2000 Than Ngo <than@redhat.de>
- rebuilt against glibc-2.1.92-14, gcc-2.96-40

* Sun Jul 16 2000 Than Ngo <than@redhat.de>
- use new snapshot
- disable Motif

* Tue Jul 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- use gcc 2.96
- new snapshot

* Sun Jul  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Epoch 3
- Update to current
- Use egcs++

* Fri Jun 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update (I put the fixes directly to CVS rather than collecting them
  in the spec)

* Fri Jun 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- remove man2html; we get that from man
- new snapshot

* Tue Jun 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot
- ExcludeArch ia64 for now
- remove gnome .desktop file, we get it from gnome-core now.

* Wed Apr  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- remove dependency on xpm (now in XFree86)

* Sat Mar 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot
- move it to /usr, where it belongs

* Sat Dec 25 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- Build the OpenGL screensavers, and move them to a separate package
- Improve the spec file (BuildPrereqs etc.)

* Thu Dec 16 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- remove patch #3 (obsoleted by kwin)

* Sun Oct 24 1999 Bernhard Rosenkraenzer <bero@redhat.de>
- 2.0 CVS snapshot
- fix compilation

* Thu Sep 23 1999 Preston Brown <pbrown@redhat.com>
- clean up files in /tmp from startkde
- mark doc files as such

* Tue Sep 21 1999 Preston Brown <pbrown@redhat.com>
- start autorun if present in startkde
- check for configured soundcard before running sound services

* Mon Sep 20 1999 Preston Brown <pbrown@redhat.com>
- made kdelnks display Name property if they are of type Link

* Thu Sep 16 1999 Preston Brown <pbrown@redhat.com>
- moved png handling here (from kdelibs)
- changed low color icon directory name to locolor

* Tue Sep 14 1999 Preston Brown <pbrown@redhat.com>
- added optional session management to logout dialog
- include GNOME menus

* Mon Sep 13 1999 Preston Brown <pbrown@redhat.com>
- added link to /etc/X11/applnk, .directory file
- included lowcolor icon sub-package
- enable .desktop file access

* Fri Sep 10 1999 Preston Brown <pbrown@redhat.com>
- customized startkde script to set up user environment if not present.
- mention kthememgr in description.

* Wed Sep 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 1.1.2 release
- kvt is back
- kde icon included
- linux console fonts included

* Thu Jul 15 1999 Preston Brown <pbrown@redhat.com>
- PAM console logout problem solved.

* Mon Jul 12 1999 Preston Brown <pbrown@redhat.com>
- now includes screensaver password security fix

* Fri Jun 11 1999 Preston Brown <pbrown@redhat.com>
- snapshot, includes kde 1.1.1 + fixes
- kvt removed for security reasons.  It is a steaming pile of...

* Mon Apr 19 1999 Preston Brown <pbrown@redhat.com> 
- last snapshot before release

* Fri Apr 16 1999 Preston Brown <pbrown@redhat.com>
- today's snapshot makes kfm a bit nicer and some other fixes
- moved default rc files to kdesupport

* Thu Apr 15 1999 Preston Brown <pbrown@redhat.com>
- SUID bit removed from konsole_grantpty -- not needed w/glibc 2.1

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- built with today's snapshot -- had to rebuild to fix pam problems.

* Tue Apr 13 1999 Preston Brown <pbrown@redhat.com>
- new snapshot fixes mimetype video/x-flic problem

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- latest stable snapshot

* Fri Apr 09 1999 Preston Brown <pbrown@redhat.com>
- removed bell.xpm (used to be in fvwm2-icons, don't want installer to see
- this previous connection and autoselect kdebase for upgrade).

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- moved gdm patch

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- added gdm session control file

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- added pam-console stuff to kde pam file

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 07 1999 Preston Brown <pbrown@redhat.com>
- upgraded to KDE 1.1 final.

* Tue Jan 19 1999 Preston Brown <pbrown@redhat.com>
- updated macros for RPM 3.0, removed red hat logo.

* Tue Jan 05 1999 Preston Brown <pbrown@redhat.com>
- re-merged from Duncan Haldane's stuff
