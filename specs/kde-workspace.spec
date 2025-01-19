
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
%global systemd_login1 1
%endif

#if 0%{?fedora} < 24
%global kdm 1
#endif

%if 0%{?fedora} > 23
%global kdm_settings 1
%endif

%if 0%{?fedora} < 25
%define strigi 1
%endif

Summary: KDE Workspace
Name:    kde-workspace
Epoch:   1
Version: 4.11.22
Release: 43%{?dist}

License: GPL-2.0-only
URL:     https://github.com/KDE/%{name}
Source0: https://github.com/KDE/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: kdm-settings-2.tar.gz

# add konsole menuitem
# FIXME?  only show menu when/if konsole is installed? then we can drop the hard-dep
Patch2: kde-workspace-4.9.90-plasma_konsole.patch

# make strigi optional
Patch3: kde-workspace-strigi.patch

# RH/Fedora-specific: Force kdm and kdm_greet to be hardened
Patch4: kde-workspace-4.10.4-kdm-harden.patch

# kubuntu kudos! bulletproof-X bits ripped out
# SUSE kudos! plymouth fixed by Laercio de Sousa and Stefan Brüns
Patch19: kde-workspace-4.11.1-kdm_plymouth081.patch
Patch20: kdebase-workspace-4.4.92-xsession_errors_O_APPEND.patch

# add support for automatic multi-seat provided by systemd using existing reserve seats in KDM
Patch27: kde-workspace-4.11.1-kdm-logind-multiseat.patch

# avoid conflict between kcm_colors 4 and plasma-desktop 5
Patch28: kde-workspace-4.11.16-colorschemes-kde4.patch

# use /etc/login.defs to define a 'system' account instead of hard-coding 500
Patch52: kde-workspace-4.8.2-bz#732830-login.patch

# kdm overwrites ~/.Xauthority with wrong SELinux context on logout
# http://bugzilla.redhat.com/567914
# http://bugs.kde.org/242065
Patch53: kde-workspace-4.7.95-kdm_xauth.patch

# kdm (local) ipv6
# https://bugzilla.redhat.com/show_bug.cgi?id=1187957
Patch56: kde-workspace-kdm_local_ipv6.patch

# pam/systemd bogosity: kdm restart/shutdown does not work
# http://bugzilla.redhat.com/796969
Patch57: kde-workspace-4.8.0-bug796969.patch

Patch58: kde-workspace-4.9.11-new_rundir.patch
Patch59: kdm-settings-new_rundir.patch
## upstream patches

## plasma active patches

## Fedora specific patches

# rhel patches

## trunk (Plasma 5) patches

# kdmtheme's functionality is provided here

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= 4.14.4
BuildRequires: kdelibs4-webkit-devel
BuildRequires: kactivities-devel
BuildRequires: libjpeg-devel
BuildRequires: pam-devel

# TODO: Can we strip this even more?
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(libpng)
%if 0%{?strigi}
BuildRequires: pkgconfig(libstreamanalyzer)
%endif
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xres)

# For AutoReq cmake-filesystem
BuildRequires: cmake

%description
The KDE Workspace consists of what is the desktop of the
KDE Desktop Environment.

%package devel
Summary:  Development files for %{name}
Obsoletes: kdebase-workspace-devel < 4.7.97-10
Provides:  kdebase-workspace-devel = %{version}-%{release}
Provides: solid-bluetooth-devel = %{version}-%{release}
#Requires: ksysguard-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: libkworkspace%{?_isa} = %{epoch}:%{version}-%{release}
Requires: kdelibs4-devel
%description devel
%{summary}.

%package -n kcm_colors
Summary: Colors KDE Control Module
Conflicts: kde-workspace < 4.8.0-2
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%{?kde_runtime_requires}
%description -n kcm_colors
The Color Selection module is comprised of several sections:
* The Scheme tab, used to manage schemes
* The Options tab, used to change the options of the current scheme
* The Colors tab, used to change the colors of the current scheme
* The state effects tabs (Inactive, Disabled)

%package -n kde-platform-plugin
Summary: KDE4 Platform plugin
Requires: %{name}-common = %{epoch}:%{version}-%{release}
#if 0%{?fedora} > 22
## skip Supplements until dnf handling is better/fixed:
## https://bugzilla.redhat.com/show_bug.cgi?id=1325471
%if 0
Supplements: (kde-runtime and plasma-workspace)
%endif
%description -n kde-platform-plugin
%{summary}.

%package -n kdm
Summary: The KDE login manager
Provides: kdebase-kdm = %{version}-%{release}
Provides: service(graphical-login) = kdm
%if 0%{?kdm_settings}
Requires: kdm-settings = %{epoch}:%{version}-%{release}
%else
Requires: kde-settings-kdm
%endif
Requires: kgreeter-plugins = %{epoch}:%{version}-%{release}
Requires: libkworkspace%{?_isa} =  %{epoch}:%{version}-%{release}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description -n kdm
KDM provides the graphical login screen, shown shortly after boot up,
log out, and when user switching.

%if 0%{?kdm_settings}
%package -n kdm-settings
Summary: Configuration files for kdm
Obsoletes: kde-settings-kdm < 1:4.11
Provides:  kde-settings-kdm = %{epoch}:%{version}-%{release}
BuildRequires: systemd
BuildRequires: make
Requires: kdm = %{epoch}:%{version}-%{release}
Requires: desktop-backgrounds-compat
Requires: system-logos
Requires: xorg-x11-xinit
Requires(pre): coreutils
Requires(post): coreutils grep sed
Requires(post): kde4-macros(api) = %{_kde4_macros_api}
%{?systemd_requires}
BuildArch: noarch
%description -n kdm-settings
%{summary}.
%endif

%package -n kdm-themes
Summary: Extra KDM Themes
Obsoletes: kdm < 4.7.3-9
Requires: kdm = %{epoch}:%{version}-%{release}
# http://bugzilla.redhat.com/753409
# http://bugzilla.redhat.com/784389
Requires: kde-wallpapers
# kdm already pulls in -common
#Requires: %{name}-common = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description -n kdm-themes
A collection of extra kdm themes, including: circles, horos, oxygen, oxygen-air,
as well as stripes wallpaper.

%package -n kgreeter-plugins
Summary: KDE Greeter Plugin Components
# kgreet_* plugins moved
Conflicts: kdm < 4.6.90-4
Conflicts: kde-workspace < 4.7.80-3
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description -n kgreeter-plugins
%{summary} that are needed by KDM and Screensaver unlocking.

%package -n ksysguard-libs
Summary: Runtime libraries for KDE 4 version of ksysguard
# when spilt occurred
Conflicts: kdebase-workspace-libs < 4.7.2-2
Requires: libksysguard-common >= 5
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%{?kdelibs4_requires}
%description -n ksysguard-libs
%{summary}.

%package -n ksystraycmd
Summary:  Allows any application to be kept in the system tray
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description -n ksystraycmd
%{summary}.

%package -n libkworkspace
Summary: Runtime libkworkspace library
# when spilt occurred
Conflicts: kdebase-workspace-libs < 4.7.2-2
Obsoletes: kdebase-workspace-libs-kworkspace < 4.7.2-3
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%{?kdelibs4_requires}
%description -n libkworkspace
%{summary}.

%package common
Summary: KDE Workspace 4 legacy package
BuildArch: noarch
Obsoletes: kdebase-workspace < 4.7.97-10
Obsoletes: kdebase-workspace-akonadi < 4.7.97-10
Obsoletes: kdebase-workspace-googlegadgets < 4.5.80-7
Obsoletes: kdebase-workspace-ksplash-themes < 4.7.97-10
Obsoletes: kdebase-workspace-libs < 4.7.97-10
Obsoletes: kded_randrmonitor < 4.9.98-5
Obsoletes: kde-base-artwork < 1:14.12.3
## Let plasma-desktop be the only pkg that Obsoletes: kde-workspace,
## at least until dnf is fixed to match yum's behavior
#Obsoletes: kde-workspace < 1:4.11.16-2
Obsoletes: kde-workspace-akonadi < 1:4.11.16-2
Obsoletes: kde-workspace-libs < 1:4.11.16-2
Obsoletes: kde-workspace-python-applet < 4.5.80-7
%if ! 0%{?kdm}
Obsoletes: kdm < %{epoch}:%{version}-%{release}
Obsoletes: kdm-themes < %{epoch}:%{version}-%{release}
Obsoletes: kgreeter-plugins < %{epoch}:%{version}-%{release}
%endif
Obsoletes: kdmtheme < 1.3
Obsoletes: ksplash-themes < 1:4.11.16-2
Obsoletes: ksysguard-libs < 1:4.11.22-30
Obsoletes: plasma-scriptengine-googlegadgets < 4.7.1
Obsoletes: plasma-scriptengine-python < 1:4.11.16-2
Obsoletes: plasma-scriptengine-ruby < 1:4.11.16-2
Obsoletes: ktux < 1:14.12.3
## other kde4-only plasmoids
Obsoletes: kde-plasma-daisy < 0.1
Obsoletes: kde-plasma-quickaccess < 0.8.1-20
Obsoletes: kde-plasma-runcommand < 2.4-20
Obsoletes: kde-plasma-smooth-tasks < 0.1
Obsoletes: kde-plasma-translatoid < 1.30-20
%description common
%{summary}.


%prep
%setup -q -n kde-workspace-%{version} %{?kdm_settings:-a1}

# Well, I looked at doing this using the context menu plugin system and it
# looked like a lot more work than this simple patch to me. -- Kevin
# FIXME/REBASE -- rex
%patch 2 -p1 -b .plasma-konsole
%patch 3 -p1 -b .strigi
%patch 4 -p1 -b .harden
# no backup file, since the whole dir gets installed
%patch 19 -p1 -b .kdm_plymouth
%patch 20 -p1 -b .xsession_errors_O_APPEND
%patch 27 -p1 -b .kdm_logind
%patch 28 -p1 -b .colorschemes-kde4

# upstreamable patches
%patch 52 -p1 -b .bz#732830-login
%patch 53 -p1 -b .kdm_xauth
%patch 56 -p0 -b .kdm_local_ipv6
%patch 57 -p1 -b .bug796969
%patch 58 -p1 -b .new_rundir
%if 0%{?kdm_settings}
pushd kdm-settings
#this patch can't have backups
%patch 59 -p1
popd
%endif

# upstream patches

# Fedora patches

# rhel patches

# trunk (Plasma 5) patches


# Disable some libs (only keep kworkspace, kdm)
for lib in kephal ksysguard oxygen plasmaclock plasmagenericshell taskmanager; do
    sed -i "/add_subdirectory($lib)/s/^/#/" libs/CMakeLists.txt
done

# make libs/kdm optional
sed -i -e 's/add_subdirectory(kdm)/macro_optional_add_subdirectory(kdm)/' \
  kdm/CMakeLists.txt \
  libs/CMakeLists.txt \
  doc/CMakeLists.txt

# Disable all docs except for KDM and kcontrol
for doc in klipper kfontview kmenuedit ksysguard plasma-desktop systemsettings kinfocenter PolicyKit-kde; do
    sed -i "/add_subdirectory($doc)/s/^/#/" doc/CMakeLists.txt
done

# Disable all kcontrol docs except for colors
for doc in clock desktopthemedetails joystick kcmaccess kcmstyle solid-actions splashscreen powerdevil kwincompositing kwinscreenedges \
           autostart bell cursortheme fonts fontinst keys keyboard kwindecoration desktop mouse paths screensaver windowspecific \
           windowbehaviour kwintabbox kcmsmserver workspaceoptions khotkeys; do
    sed -i "/add_subdirectory($doc)/s/^/#/" doc/kcontrol/CMakeLists.txt
done

# Disable all KCMs except for colors
for kcm in randr keyboard bell input access screensaver dateandtime autostart launch krdb style desktoptheme standard_actions keys \
           workspaceoptions hardware desktoppaths fonts kfontinst; do
    sed -i "/add_subdirectory( $kcm )/s/^/#/" kcontrol/CMakeLists.txt
done


%build

# workaround bug #1316964
export CFLAGS="%{optflags} -Dinline=__inline__"

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DKDE4_ENABLE_FPIE:BOOL=ON \
  -DKDE4_KDM_PAM_SERVICE=kdm \
  -DKDE4_KCHECKPASS_PAM_SERVICE=kcheckpass \
  -DKDE4_KSCREENSAVER_PAM_SERVICE=kscreensaver \
  -DBUILD_kdm:BOOL=%{?kdm:ON}%{!?kdm:OFF} \
  -DBUILD_systemsettings:BOOL=OFF \
  -DBUILD_kcheckpass:BOOL=OFF \
  -DBUILD_kwin:BOOL=OFF \
  -DBUILD_ksmserver:BOOL=OFF \
  -DBUILD_ksplash:BOOL=OFF \
  -DBUILD_powerdevil:BOOL=OFF \
  -DBUILD_qguiplatformplugin_kde:BOOL=ON \
  -DBUILD_ksysguard:BOOL=OFF \
  -DBUILD_klipper:BOOL=OFF \
  -DBUILD_kmenuedit:BOOL=OFF \
  -DBUILD_krunner:BOOL=OFF \
  -DBUILD_solid-actions-kcm:BOOL=OFF \
  -DBUILD_kstartupconfig:BOOL=OFF \
  -DBUILD_freespacenotifier:BOOL=OFF \
  -DBUILD_kscreensaver:BOOL=OFF \
  -DBUILD_kinfocenter:BOOL=OFF \
  -DBUILD_ktouchpadenabler:BOOL=OFF \
  -DBUILD_kcminit:BOOL=OFF \
  -DBUILD_khotkeys:BOOL=OFF \
  -DBUILD_kwrited:BOOL=OFF \
  -DBUILD_appmenu:BOOL=OFF \
  -DBUILD_cursors:BOOL=OFF \
  -DBUILD_plasma:BOOL=OFF \
  -DBUILD_statusnotifierwatcher:BOOL=OFF \
  -DBUILD_kstyles:BOOL=OFF
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# move devel symlinks
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/devel
pushd %{buildroot}%{_kde4_libdir}
for i in lib*.so
do
  case "$i" in
    libksgrd.so|libksignalplotter.so|liblsofui.so|libprocesscore.so|libprocessui.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
    *)
      ;;
  esac
done
popd

## unpackaged files
%if 0%{?kdm}
# remove extraneous files
rm -rfv %{buildroot}%{_kde4_appsdir}/kdm/sessions/
rm -rfv %{buildroot}%{_datadir}/config/kdm

# own %%{_kde4_appsdir}/kdm/faces and set default user image
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/faces
pushd %{buildroot}%{_kde4_appsdir}/kdm/faces
ln -sf ../pics/users/default1.png .default.face.icon
popd

%if 0%{?kdm_settings}
# kdm-settings
pushd kdm-settings/
tar cpf - . | tar --directory %{buildroot} -xvpf -
popd

# config dir kdm symlink
ln -sf ../../../etc/kde/kdm %{buildroot}%{_datadir}/config/kdm

# own these
mkdir -p %{buildroot}%{_localstatedir}/lib/kdm
mkdir -p %{buildroot}%{_rundir}/{kdm,xdmctl}
%endif

%endif

# Keep dreaming...
rm -rfv %{buildroot}/%{_kde4_bindir}/startkde

# Remove ksysguard processlisthelper (provided by libksysguard-common)
rm -rfv %{buildroot}/%{_sysconfdir}/dbus-1
rm -rfv %{buildroot}/%{_kde4_libexecdir}/ksysguardprocesslist_helper
rm -rfv %{buildroot}/%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
rm -rfv %{buildroot}/%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

# colors doc conflicts with plasma-desktop-doc
rm -rfv %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/colors/


%files common
%doc COPYING README

%files devel
%{_kde4_includedir}/*
%{_kde4_appsdir}/cmake/modules/*.cmake
%{_kde4_libdir}/cmake/KDE4Workspace/
%{_kde4_libdir}/libkworkspace.so
# ksysguard-libs
%if 0
%{_kde4_libdir}/kde4/devel/libksgrd.so
%{_kde4_libdir}/kde4/devel/libksignalplotter.so
%{_kde4_libdir}/kde4/devel/liblsofui.so
%{_kde4_libdir}/kde4/devel/libprocesscore.so
%{_kde4_libdir}/kde4/devel/libprocessui.so
%endif

%files -n kde-platform-plugin
%{_kde4_libdir}/kde4/plugins/gui_platform/libkde.so

%files -n kcm_colors
%{_kde4_datadir}/kde4/services/colors.desktop
%{_kde4_libdir}/kde4/kcm_colors.so
%{_kde4_configdir}/colorschemes-kde4.knsrc
%{_kde4_appsdir}/color-schemes/Honeycomb.colors
%{_kde4_appsdir}/color-schemes/Norway.colors
%{_kde4_appsdir}/color-schemes/ObsidianCoast.colors
%{_kde4_appsdir}/color-schemes/Oxygen.colors
%{_kde4_appsdir}/color-schemes/OxygenCold.colors
%{_kde4_appsdir}/color-schemes/Steel.colors
%{_kde4_appsdir}/color-schemes/WontonSoup.colors
%{_kde4_appsdir}/color-schemes/Zion.colors
%{_kde4_appsdir}/color-schemes/ZionReversed.colors

%if 0%{?kdm}
%files -n kdm
%{_kde4_bindir}/genkdmconf
%{_kde4_bindir}/kdm
%{_kde4_bindir}/kdmctl
%{_kde4_libexecdir}/kdm_config
%{_kde4_libexecdir}/kdm_greet
%{_kde4_libexecdir}/krootimage
%{_kde4_docdir}/HTML/en/kdm/
%dir %{_kde4_appsdir}/doc
%{_kde4_appsdir}/doc/kdm/
%dir %{_kde4_appsdir}/kdm/
%{_kde4_appsdir}/kdm/faces/
%{_kde4_appsdir}/kdm/patterns/
%{_kde4_appsdir}/kdm/pics/
%{_kde4_appsdir}/kdm/programs/
%dir %{_kde4_appsdir}/kdm/themes/
# kcm
%{_kde4_appsdir}/kcontrol/
%{_kde4_libdir}/kde4/kcm_kdm.so
%{_kde4_libexecdir}/kcmkdmhelper
%{_kde4_datadir}/config/background.knsrc
%{_kde4_datadir}/config/kdm.knsrc
%{_kde4_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkdm.service
%{_kde4_datadir}/kde4/services/kdm.desktop
%{_kde4_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkdm.policy

%if 0%{?kdm_settings}
%post -n kdm-settings
%{?systemd_post:%systemd_post kdm.service}
(grep '^UserAuthDir=/run/kdm$' %{_sysconfdir}/kde/kdm/kdmrc > /dev/null && \
 sed -i.rpmsave -e 's|^UserAuthDir=/run/kdm$|#UserAuthDir=/tmp|' \
 %{_sysconfdir}/kde/kdm/kdmrc
) ||:

%preun -n kdm-settings
%{?systemd_preun:%systemd_preun kdm.service}

%postun -n kdm-settings
%{?systemd_postun}

%files -n kdm-settings
%config(noreplace) /etc/pam.d/kdm*
# compat symlink
%{_datadir}/config/kdm
%dir %{_sysconfdir}/kde/kdm
%config(noreplace) %{_sysconfdir}/kde/kdm/kdmrc
%dir %{_localstatedir}/lib/kdm
%config(noreplace) %{_localstatedir}/lib/kdm/backgroundrc
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/kde/kdm/README*
%config(noreplace) %{_sysconfdir}/kde/kdm/Xaccess
%config(noreplace) %{_sysconfdir}/kde/kdm/Xresources
%config(noreplace) %{_sysconfdir}/kde/kdm/Xsession
%config(noreplace) %{_sysconfdir}/kde/kdm/Xsetup
%config(noreplace) %{_sysconfdir}/kde/kdm/Xwilling
# own logrotate.d/ avoiding hard dep on logrotate
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/kdm
%{_tmpfilesdir}/kdm.conf
%attr(0711,root,root) %dir %{_rundir}/kdm
%attr(0711,root,root) %dir %{_rundir}/xdmctl
%{_unitdir}/kdm.service
# default/generic fedora theme
%{_kde4_appsdir}/kdm/themes/fedora/
%endif

%files -n kdm-themes
%{_kde4_appsdir}/kdm/themes/ariya/
%{_kde4_appsdir}/kdm/themes/circles/
%{_kde4_appsdir}/kdm/themes/elarun/
%{_kde4_appsdir}/kdm/themes/horos/
%{_kde4_appsdir}/kdm/themes/oxygen/
%{_kde4_appsdir}/kdm/themes/oxygen-air/
# not sure why this is included in kdm sources... ? -- rex
%{_kde4_datadir}/wallpapers/stripes.png*

%files -n kgreeter-plugins
%{_kde4_libdir}/kde4/kgreet_classic.so
%{_kde4_libdir}/kde4/kgreet_generic.so
%{_kde4_libdir}/kde4/kgreet_winbind.so
%endif

%if 0
%ldconfig_scriptlets -n ksysguard-libs

%files -n ksysguard-libs
%{_kde4_libdir}/kde4/plugins/designer/ksignalplotterwidgets.so
%{_kde4_libdir}/libksignalplotter.so.4*
%{_kde4_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%{_kde4_libdir}/kde4/plugins/designer/ksysguardlsofwidgets.so
%{_kde4_libdir}/libksgrd.so.4*
%{_kde4_libdir}/liblsofui.so.4*
%{_kde4_libdir}/libprocesscore.so.4*
%{_kde4_libdir}/libprocessui.so.4*
%{_kde4_appsdir}/ksysguard
%endif

%files -n ksystraycmd
%{_kde4_bindir}/ksystraycmd

%ldconfig_scriptlets -n libkworkspace

%files -n libkworkspace
%{_kde4_libdir}/libkworkspace.so.4*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Than Ngo <than@redhat.com> - 4.11.22-38
- migrated to SPDX license
- Fix deprecated patch rpm macro

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Than Ngo <than@redhat.com> - 4.11.22-34
- fixed bz#2036362, update URL

* Sat Dec 18 2021 Sérgio Basto <sergio@serjux.com> - 1:4.11.22-33
- Fix the annoying warnings of systemd tmpfiles
  /usr/lib/tmpfiles.d/kdm.conf:1: Line references path below legacy directory /var/run/, updating /var/run/kdm/ → /run/kdm/; please update the tmpfiles.d/ drop-in file accordingly.
  /usr/lib/tmpfiles.d/kdm.conf:2: Line references path below legacy directory /var/run/, updating /var/run/xdmctl → /run/xdmctl; please update the tmpfiles.d/ drop-in file accordingly.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-31
- -common: Obsoletes: ksysguard-libs < 1:4.11.22-30

* Mon Mar 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-30
- drop ksysguard-libs, no longer needed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-25
- rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:4.11.22-22
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1:4.11.22-20
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-16
- KDM uses f23-kdm-theme... (#1344920)

* Wed Jun 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-15
- disable strigi support (f25+)

* Fri May 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-14
- kdm-settings: (explicit) BuildRequires: systemd (for macros.systemd)

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-13
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-12
- update URL

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-11
- rebuild (qt)

* Mon Apr 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-10
- kde-plastform-plugin: drop use of Supplements, workaround bug #1325471

* Tue Mar 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-9
- kdm-settings: replaces kde-settings-kdm

* Mon Mar 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-7
- kde-platform-plugin: Supplements: (kde-runtime and plasma-workspace)

* Sat Mar 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.22-6
- re-enable kdm (and kcm_kdm)
- workaround systemd bug #1316964
- drop a few more unused BuildRequires

* Fri Mar 11 2016 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.22-5
- drop kdm f24+

* Fri Mar 11 2016 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.22-4
- kde-platform-plugin: Supplements: plasma-workspace (f23+)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.22-2
- (re)enable ksystraycmd, strip some unused BR's

* Wed Aug 26 2015 Daniel Vrátil <dvratil@redhat.com> 1:4.11.22-1
- 4.11.22

* Mon Jun 29 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.21-1
- 4.11.21

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.11.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.20-2
- consistently use Requires: %%{name}-common in subpkgs

* Wed Jun 03 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.20-1
- 4.11.20
- drop deprecated nepomuk bits
- kde-platform-plugin subpkg

* Thu May 14 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.19-1
- 4.11.19

* Sat May 09 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.18-3
- -common: Obsoletes: kde-plasma-daisy kde-plasma-smooth-tasks

* Mon Apr 27 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.18-2
- -common: Obsoletes: kde-plasma-quickaccess kde-plasma-runcommand kde-plasma-translatoid

* Sun Apr 12 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.18-1
- 4.11.18

* Fri Mar 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.16-11
- -devel: fix conflicts with libksysguard-devel

* Fri Mar 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.16-10
- kcm_colors: fix conflict with plasma-desktop-doc

* Mon Mar 16 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.16-9
- -common: drop Obsoletes: kde-workspace (for now, at least until dnf is fixed)

* Thu Mar 12 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.16-8
- s/kde4_runtime_requires/kde_runtime_requires/

* Sat Mar 07 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.11.16-7
- fix the colorschemes.knsrc file conflict correctly (also patch the code)

* Thu Mar 05 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.16-6
- -common: Obsoletes: kde-base-artwork

* Thu Mar 05 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.16-5
- Epoch: 1, to ensure upgrade path (and with 4.11-related Obsoletes)
- drop Provides: kdebase-workspace
- drop Provides: plasma4(scriptengine-declarativescript) (no longer ship kwin4 that needs this)
- use %%{?kdelibs4_requires} %%{?kde4_runtime_requires} macros
- -common: Obsoletes: ktux

* Wed Mar 04 2015 Daniel Vrátil <dvratil@redhat.com> 4.11.16-4
- fix -devel dependencies (kde-workspace-libs no longer exists)

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> 4.11.16-3
- remove Provides: firstboot(windowmanager) = kwin

* Wed Feb 25 2015 Daniel Vrátil <dvratil@redhat.com> 4.11.16-2
- strip down kde-workspace - disable and remove everything provided by Plasma 5
- create kde-workspace-common which obsoletes all removed subpackages

* Mon Feb 23 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.16-1
- 4.11.16

* Wed Feb 11 2015 Than Ngo <than@redhat.com> 4.11.15-6
- rebuilt

* Sat Feb 07 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.15-5
- KDM writing incorrect XAUTHORITY file for XDMCP sessions (#1187957)

* Tue Feb 03 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.15-4
- -devel: drop dep on kwin-gles-libs (#1188877)

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> 4.11.15-3
- split kinfocenter, kmenuedit and khotkeys to subpackages

* Sun Jan 11 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.15-2
- make pykde4 dep unversioned

* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.11.15-1
- 4.11.5
- bump BR: kdelibs4-devel, for new %%kdelibs_requires, %%kde_runtime_requires macros

* Wed Dec 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.14-3
- rename kde-plasma-safe.desktop => kde-plasma99-safe.desktop (#1164783)

* Wed Nov 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.11.14-2
- move kwin and kwin-libs to subpackages

* Tue Nov 11 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.14-1
- 4.11.14

* Thu Oct 16 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.13-2
- -libs: make kde-style-oxygen dep unversioned
- enable kscreen support for el7

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.13-1
- 4.11.13

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.12-1
- 4.11.12

* Fri Aug 22 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.11-4
- Requires: kactivities (unversioned)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11.11-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.11-2.1
- rebuild (f20 against kde-4.13)

* Thu Jul 24 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.11-2
- -libs: drop Requires: kde-workspace

* Sat Jul 12 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.11-1
- 4.11.11

* Sat Jul 05 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.11.10-8
- backport upstream patch to fix choppy fullscreen with OpenGL compositing on
  the latest xorg-x11-drv-intel driver from KWin 5 (kde#336589, fdo#80349)

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-7
- QT_PLUGIN_PATH contains repeated paths (#1115268)

* Wed Jul 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-6
- BuildConflicts: nepomuk-core-devel

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-5
- BR: kdelibs4-webkit-devel

* Wed Jun 11 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-4
- revert patch for "Fix ... cut off ... in digital clock"

* Wed Jun 11 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-3
- Fix the numbers cut off problem in digital clock applet (kde#228902)

* Sun Jun 08 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-2
- respin

* Sat Jun 07 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.10-1
- 4.11.10

* Fri May 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.9-4
- backports++ (kdm crasher in particular)

* Thu May 01 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.9-3
- backport some post-4.11.9 upstream commits

* Tue Apr 29 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.9-2
- respin

* Fri Apr 25 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.9-1
- 4.11.9

* Thu Apr 24 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-7
- another batch of upstream commits, including final versions of screenlocker fixes

* Tue Apr 22 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-6
- pull in proposed screenlocker fixes (kde#224200, kde#327947, kde#329076)

* Sat Apr 19 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-5
- plasma-dataengine-extractor love
- move calendar dataengine to -akonadi subpkg (currently unused)

* Mon Apr 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-4
- disable nepomuk support (kde-4.13, f21+)

* Mon Apr 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-3
- startkde.cmake: PAM_KWALLET_LOGIN typo

* Fri Apr 11 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-2
- pull in some post 4.11.8 commits
- ... namely adds support for pam-kwallet and XDG_CURRENT_DESKTOP

* Thu Apr 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.8-1
- 4.11.8

* Tue Mar 25 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.11.7-6
- bbcukmet: fix processing of weather conditions (regression in -5)

* Mon Mar 24 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.11.7-5
- bbcukmet: fix typo in the condition->icon matching ("clar sky" -> "clear sky")
- bbcukmet: fix a crash (#1079296/kde#332392) and improve error handling

* Sat Mar 15 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.11.7-4
- apply fixes for kde#330773 (BBC weather no longer working) from bugs.kde.org

* Thu Mar 13 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.11.7-3
- do not mess with XDG_DATA_DIR in startkde, fixes default apps (kde#332107)
- change the startkde patch to a modified copy to prevent more such regressions

* Fri Mar 07 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.11.7-2
- pull in some upstream fixes
- drop f18-related (systemd) hacks

* Fri Feb 28 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.7-1
- 4.11.7

* Wed Feb 26 2014 Lukáš Tinkl <ltinkl@redhat.com> 4.11.6-3
- fix broken suspend/resume with systemd >= 209 (kdebug331403)

* Thu Feb 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.6-2
- fix runtime deps (%%version vs. %%_kde4_version)

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.11.6-1
- 4.11.6

* Mon Jan 27 2014 Adam Jackson <ajax@redhat.com> 4.11.5-2
- Rebuild for new sonames in libxcb 1.10

* Fri Jan 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.5-1
- 4.11.5

* Tue Dec 31 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.4-2
- disable session management for screensavers (kde#314859,review#109609))

* Tue Dec 10 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.4-1
- 4.11.4

* Mon Nov 25 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-5
- followup screenlocker fixes/polish (#1029917, #1032612)

* Sat Nov 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-4
- screenlocker improvements (#1029917, #1032612)

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-3
- kdm-themes: fix kde-wallpapers dep (make unversioned)

* Mon Nov 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-2
- include upstream commit for upower-1.0 support

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Mon Oct 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.2-3
- startkde adding /bin to $PATH (#1023999)

* Mon Sep 30 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.2-2
- kde-style-oxygen subpkg

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Mon Sep 23 2013 Martin Briza <mbriza@redhat.com> - 4.11.1-3
- updated the KDM plymouth with work by guys from SUSE
- respin of the KDM multiseat patch

* Mon Sep 09 2013 Lukáš Tinkl <ltinkl@redhat.com> - 4.11.1-2
- #1005133:  fix application specific icons (kdebz#324574)
- fix shutdown vs logout messup (kdebz#307288)

* Tue Sep 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Wed Aug 21 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-4
- use backlight actual_brightness interface

* Tue Aug 20 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-3
- Remove kio_sysinfo dep from kde-workspace (#998016)

* Mon Aug 19 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-2
- plasma startup delay 4-7 (kde#321695)

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Wed Aug 07 2013 Martin Briza <mbriza@redhat.com> - 4.10.97-3
- Changed the KDM hardening to -fpic -pic

* Mon Aug 05 2013 Martin Briza <mbriza@redhat.com> - 4.10.97-2
- Made kdm and kdm_greet hardened (#983619)

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Thu Jul 11 2013 Martin Briza <mbriza@redhat.com> - 4.10.90-2
- fix some multiseat issues in kdm, (XDG_SEAT, plymouth cooperation) as per discussion in #975079,
  thanks go to Stefan Brüns and Laercio de Sousa

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Wed Jun 26 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.4-6
- kmix: media track change memory leaks with pulseaudio+oxygen widget style (kde#309464, #912457)

* Fri Jun 14 2013 Lukáš Tinkl <ltinkl@redhat.com> - 4.10.4-5
- fix kickoff menu kbd navigation (kdebz#310166)

* Fri Jun 14 2013 Daniel Vrátil <dvratil@redhat.com> - 4.10.4-4
- add upstream patch for #921742

* Thu Jun 13 2013 Martin Briza <mbriza@redhat.com> - 4.10.4-3
- Fix VT numbers on starting a new session (#857366)

* Tue Jun 11 2013 Daniel Vrátil <dvratil@redhat.com> - 4.10.4-2
- backport upstream patch for #921781

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3
- restore patch omitting broken launchers

* Fri May 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-12
- -DKDE4_ENABLE_FPIE:BOOL=ON
- don't write fonts.conf on load (kde#105797)

* Mon Apr 29 2013 Than Ngo <than@redhat.com> - 4.10.2-11
- drop old patch for aurora
- fix multilib issue

* Mon Apr 29 2013 Martin Briza <mbriza@redhat.com> 4.10.2-10
- changed the systemd-displaymanager patch to switch the sessions using systemd-logind, too

* Thu Apr 25 2013 Martin Briza <mbriza@redhat.com> 4.10.2-9
- regenerated the systemd-displaymanager patch against latest upstream master
- worked around #955374 before I fix it clean upstream

* Wed Apr 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-8
- avoid/revert commit to avoid plasma crash on wallpaper change (kde#318806)

* Mon Apr 22 2013 Than Ngo <than@redhat.com> - 4.10.2-7
- fedora/rhel condition

* Sun Apr 21 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-6
- sync to latest 4.10 branch commits

* Thu Apr 18 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-5
- drop LD_BIND_NOW from startkde (#908380)
- fold all startkde-related patches into redhat_startkde.patch

* Thu Apr 11 2013 Daniel Vrátil <dvratil@redhat.com> 4.10.2-4
- clear screenlocker password on ESC (#949452)

* Thu Apr 11 2013 Martin Briza <mbriza@redhat.com> 4.10.2-3
- added basic support for automatic multi-seat in KDM (#884271)

* Tue Apr 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-2
- rebase systray_ktp-presence patch for applet rename

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-1
- 4.10.2

* Sun Mar 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-3
- don't apply no_HAL on el6

* Wed Mar 13 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-2
- PowerDevil should use upower to suspend on F17 (#920874)
- other small upstream fixes (xrandrbrightness, login1 leak, stop screensaver)

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Wed Feb 20 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-11
- python-scriptengine-python: s/Requires: PyKDE4/Requires: pykde4/

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-10
- respin BUILD_KCM_RANDR.patch, avoid failure in startkde when krandrstartup doesn't exist

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-9
- drop solid_krunner_disable patch (seems better now)

* Thu Feb 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-8
- kscreen support => disable all of kcontrol/randr (f19+ currently)

* Sat Feb 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-7
- fedora-plasma-cache.sh: don't delete Trolltech.conf

* Sat Feb 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-6
- tweak fedora-plasma-cache.sh for plasma-svgelements*, Trolltech.conf too
- enable powerdevil-login1 support on f18

* Fri Feb 08 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-5
- fix fedora-plasma-cache.sh (to not exit)

* Thu Feb 07 2013 Lukáš Tinkl <ltinkl@redhat.com> 4.10.0-4
- fix wrong description and size for 2-stage USB storage devices

* Mon Feb 04 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-3
- refresh Powerdevil login1 patch

* Sat Feb 02 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.10.0-2
- fix kcmdatetimehelper search path so hwclock and zic are found (#906854)

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Wed Jan 30 2013 Lukáš Tinkl <ltinkl@redhat.com> 4.9.98-7
- update Powerdevil login1 patch

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-6
- unconditionally Obsoletes: kded_randrmonitor

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-5
- Requires: kscreen, Obsoletes: kded_randrmonitor (f19+)

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-4
- drop Requires: kde-display-management (for now)
- switch fedora-plasma-cache hack to env script

* Fri Jan 25 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-3
- add fedora-plasma-cache kconf_update script

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-2
- respin systemd_login1 patch

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 4.9.97-6
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-5
- refresh powerdevil_systemd_login1 patch (kde review#108407)

* Mon Jan 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-4
- proper powerdevil systemd-login1 support (kde review#108407)

* Thu Jan 10 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-3
- hack to use org.freedesktop.login1 to handle suspend (instead of upower),
  seems to help avoid double-sleep (#859227)

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-2
- kded_xrandrmonitor subpkg, to allow use of it or kscreen

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Thu Dec 06 2012 Martin Briza <mbriza@redhat.com> 4.9.90-2
- Merged and cleaned the systemd shutdown and logout patches.
- It is possible to use systemd and/or CK without defining it at compile time

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Fri Nov 16 2012 Martin Briza <mbriza@redhat.com> - 4.9.3-3
- user switching dialog now doesn't list inactive (closing) sessions and more information is retrieved from logind

* Thu Nov 15 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-2
- pull upstream fix for some regressions (krunner, analog clock)
- drop unused llvm_whitelist patch

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Fri Nov 02 2012 Than Ngo <than@redhat.com> - 4.9.2-10
- rhel/fedora condition

* Thu Nov 1 2012 Lukáš Tinkl<ltinkl@redhat.com> 4.9.2-9
- build against prison only under Fedora

* Tue Oct 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-8
- more systemd_inhibit love (#859227, kde#307412)

* Fri Oct 26 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-7
- rework fontconfig patch to ensure $XDG_CONFIG_HOME/fontconfig exists

* Thu Oct 18 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-6
- monitor sleep settings reset, resulting in monitor turning off (kde#295164)

* Mon Oct 08 2012 Martin Briza <mbriza@redhat.com> 4.9.2-5
- Fixing user switching with SystemD (#859347), for LightDM

* Thu Oct 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-4
- ongoing systemd_inhibit work (#859227) 

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-3
- tarball respin (includes plasma/python2 patch)

* Mon Oct 01 2012 Lukáš Tinkl <ltinkl@redhat.com> - 4.9.2-2
- fix loading of Python2 plasmoids

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Thu Sep 27 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-7
- disable plasma-runner-solid by default (kde#307445)

* Fri Sep 21 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-6
- update the systemd PowerDevil Policy Agent patch to match the upstream
  version (part of KDE 4.9.2)
- update clock applets on system date/time changes

* Tue Sep 18 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-5
- fix device notifier Free Space meter

* Thu Sep 13 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-4
- hopefully also solve the screen dimming issue when inactive session goes idle

* Thu Sep 13 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-3
- Resolves #849334 - screen lock failure (laptop lid)

* Wed Sep 05 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-2
- upstream patch for kwin regression (kde#306260, kde#306275)

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1 

* Mon Aug 27 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.0-6
- Resolves #851887 - KDE Logout does not Suspend to RAM/Disk
  
* Tue Aug 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-5
- Add apper to default kickoff favorites (#850445)

* Thu Aug 09 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-4
- upstream patch for aurora/qml-based kwin decorations

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-3
- window keeps status 'asking for attention' after gaining focus (kde#303208)

* Fri Aug 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-2
- kcm_fonts should use $XDG_CONFIG_HOME/fontconfig/fonts.conf for storage settings for fontconfig > 2.10.0 (kde#304317)

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Than Ngo <than@redhat.com> - 4.8.97-2
- remove obsolete stuffs in startkde, kde-4.6.x already uses QLocale
  to try obtain a default country.

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Tue Jul 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-4
- fix tooltip for OpticalDisc

* Mon Jul 09 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-3
- Battery Monitor widget stops tracking charging state changes after suspend/resume cycle (#837345, kde#287952)

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-2
- restore stable kdecoration API to 4.8 (#831958, kde#301728)

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95
- remove battery size patch

* Mon Jun 25 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-3
- Requires: konsole

* Tue Jun 19 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-2
- battery plasmoid icon does not scale below a certain size (kde#301877)

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-4
- respin
- remove kwin check opengl patch

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.80-3
- Provides: plasma4(scriptengine-declarativescript)

* Sat May 26 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.8.80-2
- new showremainingtime patch, now just defaults the option to true
  (It doesn't have ugly side effects anymore with the rewritten plasmoid.)

* Sat May 26 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80
- remove remaining time patch, should be enabled in kde-settings

* Tue May 08 2012 Than Ngo <than@redhat.com> - 4.8.3-4
- add rhel/fedora conditions

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-3
- more work on plasma clock widget/locale crash (kde#299237)

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-2
- plasma clock widget/locale crash (kde#299237)

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3
- kdm grub2 integration upstreamed

* Tue Apr 3 2012 Lukas Tinkl <ltinkl@redhat.com> 4.8.2-3
- respin 4.8.2 tarball

* Sun Apr 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.2-2
- Kwin does not repaint window shadow regions after closing window (#808791, kde#297272)

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 19 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.1-7
- rebuild for plasma4.prov fix (no more spaces in Plasma runner auto-Provides)

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-6
- Requires: kactivities >= %%{version}

* Wed Mar 14 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.1-5
- fix another bug in the systemd shutdown/restart patch (missing parameter)

* Tue Mar 13 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.1-4
- fix bugs in the systemd shutdown/restart patch

* Mon Mar 12 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-3
- Port shutdown/restart code from ConsoleKit to systemd (#788171)

* Thu Mar 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-2
- 4.8 branch commit for settings_style support

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1
- removed powerdevil verb., eDP and gcc47 patches

* Tue Feb 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-12
- kdm restart/shutdown does not work (#796969)

* Wed Feb 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-11
- drop ConsoleKit support f17+

* Wed Feb 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-10
- kdm: Requires: ConsoleKit-x11 (#787855)

* Tue Feb 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-9
- add ktp_presence applet to default systray

* Tue Feb 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-8
- omit kwin_llvmpipe_whitelist patch, not ready/testable (#794835)

* Mon Feb 13 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-7
- kwin llvmpipe whitelist (#790142)
- powerdevil verbosity++ (kde#289760)

* Sat Feb 11 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-6
- kdm-grub2 integration (#785849)

* Tue Feb 07 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.0-5
- kde-workspace: Requires: ConsoleKit (shutdown/restart, works around #788171)
- kdm: Requires: ConsoleKit (works around #787855, nasty error message on login)

* Thu Feb 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-4
- eDP patch (kde#289760)

* Tue Jan 31 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-3
- kgreeter-plugins subpkg (#785817)

* Tue Jan 24 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-2
- kcm_colors subpkg (#761184)
- kdm-themes: Requires: kde-wallpapers unconditionally (#784389)
- s/kdebase-runtime/kde-runtime/

* Fri Jan 20 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-10
- rename kdebase-workspace -> kde-workspace

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Tue Jan 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-3
- kdm overwrites ~/.Xauthority with wrong SELinux context on logout (#567914,kde#242065)
- gcc47 fixes

* Thu Dec 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- startkde: omit MALLOC_CHECK_ debug'ery

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> 4.7.95-1
- 4.7.95
- Add Ariya kdm theme

* Wed Dec 14 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-3
-libs: move libkworkspace (versioned) dep here (from -devel)

* Thu Dec 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-2
- kwin-gles: move kwin4_effect_gles_builtins here 

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90
- BR: libjpeg-devel (ksplash)

* Thu Dec 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-6
- get some kwin-gles love

* Tue Nov 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-5
- BR: kactivities-devel

* Thu Nov 24 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-4
- Respin with new upstream tarball
- Drop patch: don't use INSTALL to copy file to current binary dir

* Thu Nov 24 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-3
- Fixed file listed twice
- Remove big cursors from files (they are no longer in upstream tarball)
- Add new files: libkwinglutils.so*, liboxygenstyleconfig.so*
  libpowerdevilconfigcommonprivate.so*, kfontinst.knsrc
- New ksplash theme Minimalistic
- patch: don't use INSTALL to copy file to current binary dir

* Thu Nov 24 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-2
- Drop "only show in kde" patch (applied upstream)

* Fri Nov 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Thu Nov 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-13
- add plasma-active patches

* Thu Nov 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-12
- Crash in TaskManager::TaskItem::task (kde#272495)
- Crashes When Adding Weather Widgets (Geolocation) (kde#277036)

* Thu Nov 17 2011 Lukas Tinkl <ltinkl@redhat.com> 4.7.3-11
- battery plasmoid fixes (#753429)

* Wed Nov 16 2011 Lukas Tinkl <ltinkl@redhat.com> 4.7.3-10
- fix kwin + twinview

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-9
- kdm-themes subpkg (#753409)

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-8
- rebuild (libpng)

* Mon Nov 07 2011 Than Ngo <than@redhat.com> - 4.7.3-7
- Fix possible uninitialized variable use in ksplashx multi-screen code

* Fri Nov 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-6
- build against libkactivities-6.1

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-5
- drop kde-wallpapers (now packaged separately)

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-4
- tarball respin

* Mon Oct 31 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-3
- kde-wallpapers: Obsoletes: kdebase-workspace-wallpapers < 4.7.2-10

* Mon Oct 31 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-2
- Requires: kde-settings-ksplash kde-settings-plasma (f16+)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3
- -devel: Provides: kde-workspace-devel
- -libs: Provides: kde-workspace-libs

* Sat Oct 29 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.2-12
- kcm_clock helper: Sync the hwclock after setting the date (#749516)

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-11
- Rebuilt for glibc bug#747377

* Tue Oct 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-10
- BR: libkactivities-devel

* Mon Oct 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-9
- kdebase-workspace-wallpapers -> kde-wallpapers

* Fri Oct 21 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.7.2-8
- revert patch adding broken launchers (#747982)

* Mon Oct 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-7
- Generate texture coordinates for limited NPOT support (kde#269576)

* Sat Oct 15 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.2-6
- drop displayEvents patch, moved to kde-settings (in kde-settings-4.7-12)

* Thu Oct 13 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-5
- ksysguard: include ksysguard.desktop

* Wed Oct 12 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-4
- plasmaclock displayEvents=false default

* Mon Oct 10 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-3
- ksysguard(-libs) subpkg
- libkworkspace subpkg
- kdm: Requires: libkworkspace

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Tue Sep 20 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-3
- switch to pkgconfig-style deps

* Fri Sep 16 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-2
- upstream kwin_performance patch
- Use /etc/login.defs to define a 'system' account instead of hard-coding 500 (#732830)

* Wed Sep 14 2011 Radek Novacek <rnovacek@redhat.com> 4.7.1-1
- Remove upstreamed patch kdebase-workspace-4.7.0-kde#278206.patch

* Tue Sep 06 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Tue Aug 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-9
- disable google-gadget support (f16+)

* Sun Aug 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.0-8
- rebuild again for the fixed RPM dependency generators for Plasma (#732271)

* Sun Aug 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.0-7
- rebuild for the RPM dependency generators for Plasma (GSoC 2011)

* Wed Aug 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-6
- upstream kwin malloc patch

* Sat Aug 13 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-5
- upstream kwin software rasterizer patch

* Thu Aug 11 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-4
- modularize googlegadget/gpsd support a bit

* Sat Aug 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-3
- drop Requires: nepomukcontroller (included in kde-runtime now)

* Thu Jul 28 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.0-2
- fix GDM getting misdetected as LightDM (kde#278206, patch by Alex Fiestas)

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.0-1
- 4.7.0
- kde4workspace_version is not needed anymore
- Provides: kde-workspace kde-wallpapers (to match new upstream tarballs)

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-4
- rebuild (qt48)

* Mon Jul 18 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-3
- Conflicts: kdm < 4.6.90-4 (when kgreet_* plugins moved) 

* Tue Jul 12 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-2
- fix redhat_startkde.patch

* Fri Jul 08 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.95-1
- 4.6.95 (rc2)

* Wed Jul 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-4
- move kgreet_* plugins to main pkg, needed by kscreenlocker (#711234)

* Tue Jul 05 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-3
- startkde: omit MALLOC_CHECK pieces

* Thu Jun 30 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-2
- cleanup/remove some old/deprecated pieces

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Fri May 27 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.80-1
- 4.6.80 (beta1)
- add BR prison-devel

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-9
- drop BR: libcaptury-devel

* Wed May 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-8
- virtual desktop names are lost after log out (kde#272666)

* Sat May 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-7
- multilib QT_PLUGIN_PATH (#704840)

* Thu May 19 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.6.3-6
- make nm-09-compat patch F15-only, it won't work on Rawhide anyway

* Sun May 15 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-5
- kde4/plugins/styles/oxygen.so is not multilib (#704840)

* Sun May 08 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.6.3-4
- nm-09-compat: reenable Solid NM backend build with NM 0.9 (disabled in 4.6.3)

* Sat Apr 30 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.3-3
- fix spurious "Networking system disabled" message (#700831)

* Fri Apr 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-2
- use updated plymouth patch trying new method first

* Thu Apr 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-1
- 4.6.3

* Thu Apr 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.2-4
- fix kde#270942 (direct rendering disabled on Intel graphics since mesa 7.10.1)

* Fri Apr 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.2-3
- fix the temperature plasmoids and ksysguard temperature sensors regression

* Thu Apr 07 2011 Lukas Tinkl <ltinkl@redhat.com> - 4.6.2-2
- #694222 - Brightness controls no longer work
- kdebug#257948 - Powerdevil can no longer control brightness
- drop obsolete HAL backlight patch

* Wed Apr 06 2011 Than Ngo <than@redhat.com> - 4.6.2-1
- 4.6.2

* Tue Apr 05 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-7.1
- apply no_HAL patches on f14 too

* Sun Apr 03 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.6.1-7
- Restore lost hunks from redhat_startkde patch, fixes regressions with running
  Qt 3 binaries (Qt 3 Assistant etc.) and with the initial background color
- Fix incorrectly rebased hunk from redhat_startkde patch, fixes regression with
  language setting

* Wed Mar 30 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.1-6
- Autohide panel gets visible and does not hide itself (#690450)

* Thu Mar 24 2011 Dan Williams <dcbw@redhat.com> 4.6.1-5
- Rebuild with NM 0.9 compat patches (F15+)

* Thu Mar 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-4
- Notification size increases randomly and cant be restored (#688967)

* Mon Mar 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-3
- solid_nm_emit patch

* Mon Mar 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-2
- use system-kde-theme again (ie, lovelock-kde-theme on f15)
- -Requires: system-backgrounds-kde
- +Requires: system-plasma-desktoptheme 
- -ksplash-themes: move Default (Air+Horos) ksplash theme here

* Sat Feb 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Fri Feb 11 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-8
- include Horos wallpaper (upstream default) in main pkg, not -wallpapers

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-6
- drop Requires: system-{backgrounds,ksplash}-kde, use
  generic/upstream theming, for now.

* Thu Feb 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-5
- oxygen theme crasher (#674792, kde#265271)

* Wed Jan 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-4
- startkde: drop MALLOC_CHECK bits

* Tue Jan 25 2011 Lukas Tinkl <ltinkl@redhat.com> - 4.6.0-3
- respun tarball, omit (now upstreamed) PowerDevil 
  fixes from 4.6.0-2

* Mon Jan 24 2011 Lukas Tinkl <ltinkl@redhat.com> - 4.6.0-2
- handle PowerDevil config migration

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0

* Tue Jan 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-3
- require nepomukcontroller (temporary)

* Fri Jan 14 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-2
- add optional BR libdmtx (data matrix bar-codes support)

* Wed Jan 05 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1
- 4.5.90 (4.6rc1)

* Sat Dec 04 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.5.85-2
- adjust the HALsectomy patches
- remove solid-powermanagement

* Sat Dec 04 2010 Thomas Janssen <thomasj@fedoraproject.org> - 4.5.85-1
- 4.5.85 (4.6beta2)

* Wed Dec 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-7
- -googlegadgets => plasma-scriptengine-googlegaddgets
- -python-applet => plasma-scriptengine-python
- (new) plasma-scriptengine-ruby

* Wed Nov 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-6
- drop old polkit conditionals
- don't include libpowerdevil{core,ui}.so in -devel

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-5
- drop Obsoletes: -python-applet

* Tue Nov 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-4
- respun tarball, includes Python script engine fixes

* Mon Nov 22 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.5.80-3
- disable PowerDevil's HAL backend (aka project HALsectomy)

* Mon Nov 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-2
- backport upstream fixes to reenable and fix the Python script engine

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Mon Nov 15 2010 Than Ngo <than@redhat.com> - 4.5.3-3
- apply patch to fix crash on automatic re-login after automatic login

* Sat Nov 06 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.3-2
- drop classicmenu-games patch, upstream fixed the same issue differently and
  now the 2 fixes conflict (classic menu confuses Name and Description)

* Fri Oct 29 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Wed Oct 27 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.2-5
- use upstream ck-shutdown patch from 4.6 trunk (instead of my old one),
  supports GDM session switching (#560511, kde#186198)
- drop old F11- version of the ck-shutdown patch, F11 is EOL

* Wed Oct 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-4
- kdebase-workspace depends on xorg-x11-apps (#537609)

* Sat Oct 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-3
- backport kwin ui for unredirecting fullscreen windows

* Fri Oct 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-2
- include better, upstream fix for: krandr: Display Settings are Lost
  on Logout (kdebug183143, rh#607180)

* Fri Oct 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- 4.5.2

* Wed Sep 29 2010 jkeating - 4.5.1-5
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-4
- kdm is not localized when changing lang using system-config-language (#631861)

* Wed Sep 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-3
- Provides: firstboot(windowmanager)  (#605675)

* Sun Aug 29 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-2
- "fonts/package" is an invalid MIME type (#581896)

* Fri Aug 27 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.5.1-1
- 4.5.1

* Thu Aug 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.0-4
- Requires: iso-codes (for kcm_keyboard)

* Fri Aug 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.0-3
- krunner "run command" doesn't keep any history (kde#247566)

* Thu Aug 12 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.5.0-2
- disable malloc checking in startkde for releases

* Tue Aug 03 2010 Than Ngo <than@redhat.com> - 4.5.0-1
- 4.5.0
- kde4workspace_version

* Tue Jul 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1.py27
- rebuild for python27

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.4.92-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-2
- omit non-essential xsession .desktop files, runs afoul of selinux (#588130)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri Jun 25 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.90-2
- port and reapply rootprivs (#434824) patch

* Fri Jun 25 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.90-1
- 4.5 RC1 (4.4.90)

* Wed Jun 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.85-5
- krandr: Display Settings are Lost on Logout (kdebug183143, rh#607180)

* Mon Jun 21 2010 Karsten Hopp <karsten@redhat.com> 4.4.85-4
- don't require raw1394 on s390, s390x

* Sun Jun 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.85-3
- Significant CPU penalty for using Kwin effects (kde#239963)

* Tue Jun 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.85-2
- Adding "Enable networking" button to knetworkmanager (rh#598765, kde#238325)
- drop < f12 conditionals
- pciutils, raw1394 & qualculate BRs
- added kcmkdm helper and policy (from kdelibs)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Fri May 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.80-3
- Conflicts: kdebase < 6:4.4.80

* Tue May 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.80-2
- Blur shadow around widgets does not smoothly fade out (kde#235620)

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- 4.5 Beta 1 (4.4.80)
- kxkb and safestartkde has been removed
- add newly installed files

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.3-2
- rebuild (gpsd,kdelibs)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Tue Apr 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-5
- powerdevil only autosuspends once/twice (kde#221648) 
- CVE-2010-0436 

* Mon Apr 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-4
- another stab at f13 kdm/plymouth love (#577482)
- powerdevil always suspends twice (kde#221637)

* Wed Apr 07 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.2-3
- rip out bulletproof X changes (cf. kubuntu_33_kdm_bulletproof_x.diff) from
  our copy of kubuntu_34_kdm_plymouth_transition.diff
- drop experimental novt patch, should not be needed with the working Plymouth
  integration and may have side effects (can readd it later if really needed)
- fix icon name in plasma-konsole patch: use XDG icon instead of kappfinder one

* Tue Apr 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-2
- try to workaround "X server hogs the CPU (#577482)" by letting X
  choose vt itself
- include (but not yet apply) kubuntu_34_kdm_plymouth_transition.diff

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.2-1
- 4.4.2

* Thu Mar 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.1-2
- fix KSysGuard and KRunner System Activity dialog not refreshing (kde#230187)

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Fri Feb 26 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-8
- fix the Games menu in the classic menu mixing up Name and Description

* Fri Feb 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-7
- version solid-bluetooth(-devel) better

* Fri Feb 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-6
- solid-bluetooth and Requires: bluez ... pulls unwanted baggage (#566306)

* Tue Feb 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-5.1
- Requires: kbluetooth (<f13)

* Sat Feb 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-5
- fix incorrectly rebased classicmenu-logout patch (#564536)

* Thu Feb 11 2010 Than Ngo <than@redhat.com> - 4.4.0-4
- move xsession desktop files to main package
  (cannot start kde from gdm if kdm not installed)
- Desktop locking crashes (kde#217882#16)

* Thu Feb 11 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.0-3
- requires bluez for solid-bluetooth

* Tue Feb 09 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-2.1
- use old ck-shutdown patch without the CanStop check on F11 (#562851)

* Mon Feb 08 2010 Than Ngo <than@redhat.com> - 4.4.0-2
- apply upstream patch to fix Plasma Memory Leak and High CPU usage

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0

* Tue Feb 02 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.98-3
- support the widgetStyle4 hack in the Qt KDE platform plugin

* Mon Feb 01 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.98-2
- rebase battery-plasmoid-showremainingtime patch and remove references to 4.2

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Sat Jan 30 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.95-2
- ck-shutdown: don't offer shutdown/restart when not allowed by CK (#529644)

* Thu Jan 21 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Thu Jan 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.90-10
- fix polkit-1 conditionals

* Wed Jan 20 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.90-9
- fix infinite recursion in the patch for #556643

* Tue Jan 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-8
- SELinux is preventing /sbin/setfiles "read" access on
  /var/spool/gdm/force-display-on-active-vt (deleted) (#556643)

* Sun Jan 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-7
- rebuild (libxklavier)

* Thu Jan 14 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.90-6
- fix KDM's missing header build problem
- polkit-qt BR for polkit-1

* Mon Jan 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-5
- do not link calendar dataengine with Akonadi (kde#215150, rh#552473)
- s/plasma-engine/plasma-dataengine/

* Sat Jan 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-4
- krunner crasher (kde#221871)

* Fri Jan 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-3
- rebuild (kdelibs polkit-1 macros)

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-2
- drop -akonadi subpkg

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- kde-4.3.90 (4.4rc1)

* Tue Jan 05 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.85-3
- F13+: don't Obsoletes: PolicyKit-kde, let polkit-kde obsolete it
- F13+: explicitly require polkit-kde instead of PolicyKit-authentication-agent

* Sat Jan 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-2
- startkde: disable MALLOC_CHECK_

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- kde-4.3.85 (4.4beta2)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.3.80-5
- Repositioning the KDE Brand (#547361)

* Fri Dec 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.80-4
- SELinux is preventing access to a leaked .xsession-errors-:0 file descriptor (#542312)

* Wed Dec 09 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.80-3
- drop polkit-qt* Obsoletes, we have a new polkit-qt now

* Wed Dec 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.80-2
- BR: shared-desktop-ontologies-devel

* Tue Dec 01 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)
- kdm_plymouth patch (#475890)

* Sat Nov 28 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.75-0.4.svn1048496
- backport battery plasmoid from current pre-4.3.80 trunk for showremainingtime
- rebase battery-plasmoid-showremainingtime patch
- rebase brightness-keys patch for the above backport

* Sat Nov 28 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.75-0.3.svn1048496
- rebase plasma-konsole patch

* Wed Nov 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.75-0.2.svn1048496
- Requires: PolicyKit-authentication-agent unconditionally

* Sat Nov 21 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- update to 4.3.75 snapshot

* Wed Nov 18 2009 Lukáš Tinkl <ltinkl@redhat.com> 4.3.3-8
- correctly try to deduce LANG (kubuntu_13_startkde_set_country.diff)

* Fri Nov 13 2009 Rex Dieter <rdieter@fedoraproject.org> 4.3.3-7
- kubuntu_101_brightness_fn_keys_and_osd.diff (#509295)

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-6
- rhel cleanup, fix conditional for RHEL

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-5
- fix logic on Requires: kdm  (ie, make F-12 builds not include it)

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-4
- try experimental patch for "keyboard stops working" (kde#171685)

* Wed Nov 11 2009 Than Ngo <than@redhat.com> - 4.3.3-3
- rhel cleanup, drop BR on libcaptury-devel

* Mon Nov 09 2009 Rex Dieter <rdieter@fedoraprojectg.org> - 4.3.3-2
- Obsoletes: polkit-qt-examples (f12+)
- -devel: Obsoletes: polkit-qt-devel (f12+)

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3
- BR: libXau-devel libXdmcp-devel

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.2-2
- drop Requires: oxygen-icon-theme (dep moved to kdebase-runtime)

* Sun Oct 04 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Sun Sep 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-9
- fix classicmenu-logout ("Leave...") patch

* Sun Sep 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-8
- support "Leave..." which brings up complete shutdown dialog in classic menu

* Fri Sep 25 2009 Than Ngo <than@redhat.com> - 4.3.1-7
- don't include googlegadgets on RHEL

* Thu Sep 24 2009 Than Ngo <than@redhat.com> - 4.3.1-6
- rhel cleanup

* Wed Sep 23 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.1-5
- fix spontaneous Plasma crashes due to uninitialized vars

* Mon Sep 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-4
- drop PolicyKit 0.9 support (PolicyKit-kde) on F12+/EL

* Sat Sep 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-3
- -python-applet: Provides: plasma-scriptengine-python
- Requires: system-ksplash-theme (f12+,rhel6+)

* Fri Sep 11 2009 Than Ngo <than@redhat.com> - 4.3.1-2
- drop  BR: lm_sensors-devel on s390(x)

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1
- drop Requires: kde-plasma-folderview, rely on comps instead

* Fri Aug 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.3.0-102
- Fix typo

* Thu Aug 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-101
- inflate Release tag, avoiding possible upgrade/obsoletes pain 
- -devel: drop Provides: PolicyKit-kde-devel, bump Obsoletes

* Thu Aug 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-12
- PolicyKit-kde subpkg (#519172, #519654)

* Wed Aug 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-11
- Requires: system-backgrounds-kde (f12+)

* Tue Aug 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-10
- Requires: kde-plasma-folderview

* Sun Aug 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-9
- -akonadi: move plasma_engine_calendar here
- drop Requires: kdm (F-12+)

* Wed Aug 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-8
- adjust default-applets patch to not load plasma-networkmanagement

* Tue Aug 18 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.0-7
- move akonadi stuff to subpackage

* Fri Aug 07 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-6
- Requires: oxygen-icon-theme >= 4.3.0

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 4.3.0-5
- respin

* Mon Aug 03 2009 Than Ngo <than@redhat.com> - 4.3.0-4
- respin

* Mon Aug 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.0-3
- show the remaining time in the battery plasmoid's popup (as in 4.2) (#515166)

* Sat Aug 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-2
- move designer plugins to -libs, fixes
  Multilib conflicts for index.cache.bz2 (#515088)
- tighten -libs deps, using %%{?_isa}
- %%check: desktop-file-validate

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Mon Jul 27 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.98-3
- backport forgotten method impl in Solid from 4.3 branch, r1000715

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Thu Jul 09 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Mon Jul 06 2009 Than Ngo <than@redhat.com> - 4.2.95-7
- plasma-desktop crashes when closing/opening windows (upstream patch)

* Fri Jul 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-6
- add kde-plasma-networkmanagement to the default panel if installed

* Wed Jul 01 2009 Michel Salim <salimma@fedoraproject.org> - 4.2.95-5
- rebuild (google-gadgets)

* Wed Jul 01 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.95-4
- rebuild (libxklavier)

* Mon Jun 29 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.95-3
- omit a few kdm bits from main pkg (#508647)

* Mon Jun 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-2
- port and reapply rootprivs (#434824) patch (#508593)
- fix internal version number (otherwise it mismatches with our file list)

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Thu Jun 18 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-3
- startkde: make MALLOC_CHECK opt-in (default off)

* Fri Jun 12 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-2
- bump Obsoletes: PolicyKit-kde

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Sun May 31 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.85-5
- make default_leonidas.png the default face icon on F11

* Sat May 30 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-4
- -devel:  exclude libkickoff.so, libsystemsettingsview.so
- drop old cmake crud

* Fri May 29 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-3
- omit/revert session-button patch (kde#194506,rh#502953)
- drop unused knotificationitem-1 patch

* Wed May 27 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-2
- upgrade path broken (F-11+), Obsoletes: guidance-power-manager (#502892)
- drop < F-10 crud, have_bluez3

* Mon May 11 2009 Than Ngo <than@redhat.com> 4.2.85-1
- 4.2.85
- Obsoletes/Provides: PolicyKit-kde(-devel)

* Wed May 06 2009 Than Ngo <than@redhat.com> - 4.2.3-2
- Requires: oxygen-icon-theme >= 4.2.2
- fix oxygen-cursor-themes noarch'ness

* Sun May 03 2009 Than Ngo <than@redhat.com> - 4.2.3-1
- 4.2.3

* Tue Apr 28 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-5
- #497657 -  kpackagekit/kopete notification misrendering/missing 
  buttons with qt-4.5.1

* Wed Apr 22 2009 Than Ngo <than@redhat.com> - 4.2.2-4
- dropp unused BR on libraw1394, it breaks the build on s390(x)

* Sun Apr 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-3
- Calendar standalone plasmoid on Desktop using 100% of CPU (kde#187699)

* Wed Apr 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-2
- optimize scriptlets
- drop upstreamed patches

* Mon Mar 30 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Mon Mar 23 2009 Than Ngo <than@redhat.com> - 4.2.1-12
- upstream patch to fix suspending issue

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-11
- Obsoletes: guidance-power-manager (-> powerdevil upgrade path, F-11+)

* Wed Mar 18 2009 Than Ngo <than@redhat.com> - 4.2.1-10
- upstream patch to fix MenuEntryActions created from khotkeys

* Mon Mar 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-9
- kdm subpkg
- -devel: move cmake modules here
- Requires: kdelibs4%%{?_isa} ..
- BR: libutempter-devel (drops need for kwrited helper)

* Thu Mar 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-8
- oxygen-cursor-themes: make noarch (f10+)

* Thu Mar 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-7
- fix quicklauch (kdebug#185585,rh#489769)
- -wallpapers: make noarch (f10+)

* Tue Mar 10 2009 Than Ngo <than@redhat.com> - 4.2.1-6
- fix konsole patch to use invokeTerminal

* Mon Mar  9 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.1-5
- fix pager not displaying desktop numbers (kdebug#184152)

* Mon Mar 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-4
- kde 4.2 update crashes plasma (kdebug#185736)

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-3
- move designer plugins to main/runtime (#487622)

* Tue Mar 03 2009 Than Ngo <than@redhat.com> - 4.2.1-2
- respin

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Thu Feb 26 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.0-17
- kio_sysinfo kick-off integration

* Tue Feb 24 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.0-16
- no klipper action on selection for Arora browser

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-15
- Provides: service(graphical-login) = kdm

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-14
- Requires: oxygen-icon-theme >= %%version

* Thu Feb 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-13
- dpms issues (kdebug#177123)

* Wed Feb 18 2009 Than Ngo <than@redhat.com> - 4.2.0-12
- drop the BR on PyKDE4, it's just needed for runtime
- python-applet subpackage

* Tue Feb 17 2009 Than Ngo <than@redhat.com> - 4.2.0-11
- googlegadgets subpackage

* Mon Feb 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-10
- fix shutdown dialog not centered, sometimes entirely off screen (kde#181199)

* Wed Feb 11 2009 Than Ngo <than@redhat.com> - 4.2.0-9
- fix kdm crash with Qt-4.5

* Mon Feb 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-8
- kickoff logout shuts down system (#484737, kdebug#180576)

* Sun Feb 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-7
- include awol rss dataengine, BR: kdepimlibs-devel (see also kdebug#179050)

* Fri Jan 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4.2
- respin default_applets patch for kpowersave too (#483163)

* Thu Jan 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-4.1
- conditionalize bluetooth backport on F10+
- F9: revert solid-bluetooth to the version from KDE 4.1.4

* Thu Jan 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4
- omit ldap hack (#457638), kde42's reduced linkage to the rescue

* Thu Jan 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-3
- Requires: PyKDE4 (for plasmascript bits)
- solid-bluetoothTrunkTo42.diff (bug #481801), and 
  +Provides: solid-bluetooth(-devel) = 4.3

* Wed Jan 28 2009 Than Ngo <than@redhat.com> - 4.2.0-2
- readd the patch that omist battery applet when guidance-power-manager is installed

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Fri Jan 16 2009 Than Ngo <than@redhat.com> - 4.1.96-4
- backport fix from trunk to allow symlinks in wallpaper theme

* Wed Jan 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.1.96-3
- BR: google-gadgets-devel > 0.10.5

* Fri Jan 09 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- remove Provides: plasma-devel  

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Tue Dec 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-7
- Obsoletes: kpowersave (kpowersave -> powerdevil upgrade path, F-11+)

* Mon Dec 22 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-6
- (re)enable edje, google-gadget support

* Thu Dec 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.85-5
- drop BR edje-devel, we need QEdje instead, which we don't have yet
- comment out BR google-gadgets-* for now, need 0.10.4, have 0.10.3

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-4
- BR: edje-devel
- BR: google-gadgets-devel

* Tue Dec 16 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-3
- respun tarball

* Fri Dec 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-2
- BR: PyKDE4-devel >= %%version

* Thu Dec 11 2008 Than Ngo <than@redhat.com> -  4.1.85-1
- 4.2beta2

* Wed Dec 10 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.82-1
- 4.1.82
- rebase redhat-startkde patch

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-12
- move libplasma_applet-system-monitor.so from -devel to -libs (not a symlink)

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-11
- drop devel symlink (parallel -devel) hacks, not needed anymore in this package

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-10
- keep libtaskmanager.so in libdir

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-9
- keep libweather_ion.so in libdir

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-8
- keep libplasmaclock.so in libdir

* Mon Dec 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-7
- rebuild for Python 2.6

* Thu Nov 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-6
- disable Logitech mouse KCM again until #399931 is fixed

* Thu Nov 27 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-5
- use python_sitearch for x86_64 systems
- kephal seems to be disabled/removed, re-adapted file lists

* Tue Nov 25 2008 Than Ngo <than@redhat.com> 4.1.80-4
- respin

* Sun Nov 23 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-3
- rebase kdebase-workspace-4.1.1-show-systemsettings.patch
- new library: Kephal -> adapt file lists

* Wed Nov 19 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged
- drop kdebase-workspace-4.1.2-kdm-i18n.patch, it's included in upstream
- drop kdebase-workspace-4.0.85-plasma-default-wallpaper.patch, it's included in upstream
- drop kdebase-workspace-4.1.65-consolekit-kdm.patch
- add kdebase-workspace-4.1.80-session-button.patch
- add kdebase-workspace-4.1.2-ldap.patch

* Wed Nov 19 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-1
- 4.1.80
- BR cmake >= 2.6.2
- make install/fast
- drop _default_patch_fuzz 2
- rebase startkde patch
- rebase plasma-konsole patch
- rebase ck-shutdown patch
- add PyKDE4-devel, python-devel and PyQt4-devel to build plasma's python
  scripting interface
- BR google-gadgets-devel for google gadgets scriptengine
- BR libusb-devel for Logitech USB support in KControl

* Thu Nov 13 2008 Than Ngo <than@redhat.com> 4.1.3-5
- apply upstream patch to fix X crash when disabling compositing

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Fri Nov 07 2008 Than Ngo <than@redhat.com> 4.1.2-14
- only omit battery applet when guidance-power-manager is installed

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-13
- omit battery applet from default panel

* Wed Nov 05 2008 Than Ngo <than@redhat.com> 4.1.2-12
- fix i18n issue in kdm

* Tue Nov 04 2008 Than Ngo <than@redhat.com> 4.1.2-11
- add workaround for ldap issue (#457638)

* Sun Nov 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-10
- never touch PATH in startkde, prepending $QTDIR/bin is unnecessary on Fedora
  and breaks locating Qt 3 Assistant and other Qt 3 stuff (startkde gets run
  with a full path by KDM)

* Sat Nov 01 2008 Than Ngo <than@redhat.com> 4.1.2-9
- previous session button should be enabled

* Fri Oct 31 2008 Than Ngo <than@redhat.com> 4.1.2-8
- apply patch to fix multihead issue
- bz#469235, use non-blocking QProcess:startDetacted

* Sat Oct 25 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-7
- F10: use KDM default face icon from solar-kde-theme, require it

* Sat Oct 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-6
- reenable panel-autohide-fix-flicker patch
- backport revision 866998 to fix the CPU consumption problem (kde#172549)
- backport panelview.cpp coordinate fixes (revisions 869882, 869925, 870041)
- backport revision 871058 (request config sync when panel controller goes away)

* Fri Oct 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-5
- disable panel-autohide-fix-flicker patch for now, eats CPU

* Thu Oct 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-4
- backport panel autohide from 4.2 / plasma-4.1-openSUSE

* Wed Oct  8 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.2-3
- fix crash when invoking a klipper command for a second time

* Sun Sep 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Mon Sep 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-2
- show KCM icon in rootprivs patch (thanks to Harald Sitter "apachelogger")

* Thu Aug 28 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Mon Aug 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-8
- patch another place where systemsettings was hidden from the menu (#457739)

* Mon Aug 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-7
- enable KWin taskbarthumbnail effect (used by backported tooltip manager)

* Fri Aug 01 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-6
- patch to help krandr issues/crashes (kde#152914)

* Fri Aug 01 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.0-5
- fix 457479: "Run as root" dialog of kdm system settings is shown twice
  (due to activated signal being connected to twice)

* Fri Aug 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-4
- fix KDM configuration using the wrong appsdir for themes (#455623)

* Mon Jul 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-3
- respun tarball

* Sun Jul 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-2
- updated tooltip manager from 4.2 (fixes Plasma crash on theme change, #456820)

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Wed Jul 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-5
- F10+: fix circular kdebase<->kdebase-workspace dependency: don't Obsolete or
  Require kdebase, as kdebase now requires kdebase-workspace, obviating the
  upgrade path hack

* Tue Jul 22 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-4
- oxygen-cursor-themes, -wallpapers subpkgs

* Sat Jul 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-3
- BR soprano-devel (optional dependency of the Plasma Engine Explorer)

* Sat Jul 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-2
- backport Plasma tooltip manager from KDE 4.2 (fixes regression from 4.0)
  WARNING: Adds some new APIs from 4.2 (Plasma::popupPosition, Plasma::viewFor,
           Plasma::ToolTip*), use at your own risk, we have no control to
           guarantee that they will not change!

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Wed Jul 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-8
- fix KDM ConsoleKit patch to use x11-display-device instead of display-device

* Wed Jul 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-7
- fix segfault in KDM ConsoleKit patch (#455562)

* Tue Jul 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-6
- move systemsettings back from System to Settings in the menu

* Mon Jul 14 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-5
- new consolekit-kdm patch using libck-connector, BR ConsoleKit-devel (#430388)

* Mon Jul 14 2008 Rex Dieter <rdieter@fedorproject.org> 4.0.98-4
- install circles kdm theme

* Sun Jul 13 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-3
- sync kickoff-suspend patch from F9 (loads ksmserver translations)

* Fri Jul 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-2
- respun tarball (with systray patch)

* Thu Jul 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Wed Jul 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.85-3
- rewrite and reapply plasma-default-wallpaper patch
- (no more separate plasma-default-wallpaper-config part)
- rediff kde#154119 patch one last time

* Wed Jul 09 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-2
- systray icon patch (kde#164786)

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Fri Jun 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.83-2
- port and apply kde#154119/kde#158301 patch for moving icons on panel (#439587)

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Tue Jun 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-2
- +Provides: kdm

* Sat Jun 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Wed Jun 04 2008 Than Ngo <than@redhat.com> 4.0.80-4
- fix #449881, ksysguard OnlyShowIn=KDE

* Tue Jun 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.80-3
- enable NetworkManager support, now compatible with NM 0.7

* Thu May 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.80-2
- BR: libcaptury-devel

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Wed May 21 2008 Than Ngo <than@redhat.com> 4.0.72-4
- fix #447030, hyperlinks do not open correctly in firefox

* Thu May 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.72-3
- ksysguardd subpkg (#426543)
- %%config(noreplace) systemsettingsrc

* Thu May 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.72-2
- gtkrc patch (rh#443309, kde#146779)

* Wed May 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-1
- update to 4.0.72
- update file list (Lorenzo Villani)
- port plasma-konsole, ck-shutdown, rootprivs, plasma-default-wallpaper patches
- remove NoDisplay=true in systemsettings onlyshowkde patch (still add
  OnlyShowIn=KDE), rename to show-systemsettings
- drop upstreamed suspend patch
- drop backported kde#155362 and menu-switch patches
- drop rh#443610 patch, "Zoom Out" should be working in 4.1
- disable kde#158301 patch for now (fails to apply, looks hard to port)

* Fri May 02 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-20
- Requires: kdebase , so it doesn't go missing on upgrades from kde3 (#444928)

* Mon Apr 28 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-19
- #444141: Initial wallpaper chooser has "EOS" preselected but wallpaper is "Fedora Waves"

* Sun Apr 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-18
- don't show "Zoom Out" toolbox action (#443610, patch from openSUSE branch)

* Sat Apr 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-17
- allow moving plasmoids on panels (#439587, kde#158301) (upstream patch)

* Fri Apr 18 2008 Than Ngo <than@redhat.com> 4.0.3-16
- fix #442559, Suspend/Hibernate issue on logout

* Tue Apr 15 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-15
- workaround #434824: KDE4 System Settings - No Method To Enter Administrative Mode
- fix #441062: packagekit tools do not show icons correctly on KDE

* Tue Apr 15 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.3-13
- update redhat-startkde.patch to match waves background color (#442312)

* Fri Apr 11 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-12
- allow to define a default wallpaper (plasmarc:wallpaper)

* Wed Apr 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-11
- read the default KSplash theme from kde-settings in startkde (#441565)

* Mon Apr 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-7
- own %%{_kde4_appsdir}/kdm/faces and set default user image (#441154)

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-6
- rebuild for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-5
- update file list for _kde4_libexecdir

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-4
- backport context menu switch between Kickoff and simple menu from 4.1

* Sat Mar 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- add support for shutdown/reboot through ConsoleKit >= 0.2.4 (#431817)

* Fri Mar 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- most of the kde#155362 patch has been merged, keep only the config part

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.2-9
- add onlyshowin=KDE for systemsetting

* Thu Mar 13 2008 Than Ngo <than@redhat.com> 4.0.2-8
- backport upstream patch to fix crash in kmenuedit when users
  delete entry and save it

* Wed Mar 12 2008 Than Ngo <than@redhat.com> 4.0.2-7
- apply upstream patch to fix changing wallpaper causes desktop to go white
- apply upstream patch to check whether the to-be-embedded window has been destroyed, (bz#437058)

* Mon Mar 10 2008 Than Ngo <than@redhat.com> 4.0.2-6
- add gestures=false in kde-settings, remove kdebase-workspace-4.0.2-Gestures.patch

* Thu Mar 06 2008 Than Ngo <than@redhat.com> 4.0.2-5
- typo fix

* Tue Mar 04 2008 Than Ngo <than@redhat.com> 4.0.2-4
- disable gestures as default
- add konsole in desktop menu

* Mon Mar 03 2008 Than Ngo <than@redhat.com> 4.0.2-3
- apply upstream patch to fix crash in khotkeys

* Fri Feb 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-2
- drop upstreamed kde#155974 patch
- update kde#155362 patch

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-8
- %%files: don't own %%_kde4_libdir/kde4/plugins (thanks wolfy!)

* Sat Feb 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-7
- omit broken disk space checking hunk from redhat-startkde patch (#426871)

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-6
- revert Conflicts, it matches against Provides from kdelibs3.

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-5
- Conflicts: kdelibs < 6:4 (temporary, to ease upgrade pain)
- -devel: Requires: %%name-libs

* Mon Feb 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-4
- backport enhancement to allow multi-line taskbar from 4.1 (kde#155974)

* Mon Feb 04 2008 Than Ngo <than@redhat.com> 4.0.1-3
- respin

* Fri Feb 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- update kde#155362 (simple menu) patch for 4.0.1 (thanks to Jan Mette)

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-1
- 4.0.1

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-8
- respin (qt4)

* Sat Jan 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-7
- backport simple menu enhancement to show .desktop Name from 4.1 (kde#155362)

* Wed Jan 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-6
- Obsoletes: kdebase < 6:4

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-5
- initial login with white background (#428131, kde#155122)

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-4
- use upstream systemtray patch (#427442, kde#153193)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-3
- respun tarball
- omit gtk_applet patch (for now, doesn't build)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-2
- omit plasma-pager patch
- pull upstream patch to workaround gtk applet crasher (#427442)

* Mon Jan 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-1
- update to 4.0.0
- drop upstreamed creategtkrc-gtk212 patch
- update redhat-startkde and consolekit-kdm patches

* Mon Dec 31 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.97.0-5
- fix createGtkrc to set tooltip colors also for GTK+ 2.12+

* Sun Dec 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-4
- Obsoletes: kdmtheme

* Mon Dec 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-3
- Requires: coreutils dbus-x11 xorg-x11-apps xorg-x11-utils
            xorg-x11-server-utils (used in startkde)
- drop pam configs that were previously moved to kde-settings

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-2
- rebuild for changed _kde4_includedir

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraprojec.torg. 3.97.0-1
- kde-3.97.0
- move pam configs to kde-settings
- Requires: kde-settings-kdm

* Tue Dec 04 2007 Than Ngo <than@redhat.com> 3.96.2-3
- fix kdm/kcheckpass/kscreensaver to get working

* Sat Dec 01 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.2-2
- BR: dbus-devel
- crystalsvg icons are not part of kdebase-workspace anymore
- make sure libkdeinit_plasma.so is in normal package

* Sat Dec 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.2-1
- kde-3.96.2

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.1-4
- Obsoletes and Provides kdebase-kdm for upgrades from old kde-redhat

* Fri Nov 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.1-3
- update and apply redhat-startkde patch
- update and apply KDM ConsoleKit patch (#228111, kde#147790)
- ConsoleKit patch also includes xdmcp fixes from Mandriva (#243560)

* Wed Nov 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.1-2
- %%doc README COPYING
- -libs subpkg
- -libs: Requires: kdelibs4
- don't remove libplasma.so from %%{_kde4_libdir}
- %%files: use %%_datadir for dbus-1/interfaces,xsessions

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.1-1
- kde-3.96.1

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-7
- use kde.desktop from /usr/share/apps/kdm/sessions/kde.desktop
- use %%config(noreplace) for /etc/ksysguarddrc
- Requires: kdebase, kdebase-runtime, oxygen-icon-theme
- fix url

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-6
- add patch to get pager in plasma bar
- re-added BR: libraw1394-devel

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-5
- leave libkworkspace.so for kate
- BR: kde-filesystem >= 4

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-4
- BR: libXtst-devel
- BR: libXScrnSaver-devel

* Fri Nov 16 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-3
- own some more directories
- add %%defattr to package devel
- some spec cleanups
- -R: kdepimlibs-devel
- +BR: libXpm-devel
- +BR: glib2-devel (do we really need this?)

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-2
- BR: libXxf86misc-devel
- BR: libXxf86misc-devel
- BR: libXcomposite-devel
- BR: bluez-libs-devel
- BR: libxklavier-devel
- BR: pam-devel
- BR: lm_sensors-devel
- BR: libXdamage-devel
- BR: libXv-devel
- BR: libXres-devel

* Wed Nov 14 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-1
- kde-3.96.0

* Wed Nov 14 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.95.2-1
- Initial version of kdebase-workspace
