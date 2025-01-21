Name:       virtualbox-guest-additions
Version:    7.1.4
Release:    2%{?dist}
Summary:    VirtualBox Guest Additions
License:    GPL-3.0-only AND (GPL-3.0-only OR CDDL-1.0)
URL:        https://www.virtualbox.org/wiki/VirtualBox

Source0:    https://download.virtualbox.org/virtualbox/%{version}/VirtualBox-%{version}.tar.bz2
Source1:    vboxservice.service
Source3:    VirtualBox-60-vboxguest.rules
Source4:    vboxclient.service
Source5:    mount.vboxsf

Patch60:    VirtualBox-7.0.2-xclient-cleanups.patch

BuildRequires:  gcc-c++
BuildRequires:  kBuild >= 0.1.9998.r3093
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
# for xsltproc
BuildRequires:  libxslt
BuildRequires:  makeself
BuildRequires:  yasm
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  zlib-devel
# For the OpenGL passthru libs, these are statically linked against libstdc++
# like mesa itself is to avoid trouble with game-runtimes providing their
# own older libstdc++ (e.g. steam does this)
BuildRequires:  libstdc++-static
%{?systemd_requires}
BuildRequires: systemd

# Obsoletes/provides for upgrade path from the rpmfusion guest-additions pkg
Obsoletes:      VirtualBox-guest-additions < %{version}-%{release}
Provides:       VirtualBox-guest-additions = %{version}-%{release}
# VirtualBox guests are always x86, no need to build for other archs
ExclusiveArch:  i686 x86_64

# kernel 5.6.14 have the fixes for vboxguest on VBox 6.1.x
Requires: kernel >= 5.6.14

# VBoxOGL was removed in 6.1.0
# we need obsolete it to fix upgrade path
Obsoletes:  %{name}-ogl < 6.0.14-2

%description
This package replaces the application of Virtualbox's own methodology to
install Guest Additions (in menu: Devices | Insert Guest Additions CD-image file).
VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for
enterprise as well as home use. This package contains the VirtualBox
Guest Additions which support better integration of VirtualBox guests
with the Host, including file sharing, clipboard sharing and Seamless mode.
Aditional note: this package can be installed on an non-guest system, because it is
harmless and services would not run anyway.


%prep
%autosetup -p1 -n VirtualBox-%{version}
# Remove prebuilt binaries
find -name '*.py[co]' -delete
rm -r src/VBox/Additions/WINNT
rm -r src/VBox/Additions/os2
rm -r kBuild/
rm -r tools/
# Remove bundle X11 sources and some lib sources, before patching.
rm -r src/VBox/Additions/x11/x11include/
rm -r src/VBox/Additions/3D/mesa/mesa-21.3.8/
rm -r src/VBox/Runtime/r3/darwin
rm -r src/VBox/Runtime/r0drv/darwin
rm -r src/VBox/Runtime/darwin
rm -r src/libs/liblzf-3.*/
rm -r src/libs/libpng-1.6.*/
rm -r src/libs/libxml2-2.*/
rm -r src/libs/openssl-3.*/
rm -r src/libs/zlib-1.2.*/
rm -r src/libs/curl-8.*/
rm -r src/libs/libvorbis-1.3.*/
rm -r src/libs/libogg-1.3.*/
rm -r src/libs/libtpms-0.9.*/


%build
./configure --only-additions --disable-kmods
. ./env.sh
umask 0022

# VirtualBox build system installs and builds in the same step,
# not always looking for the installed files in places they have
# really been installed to. Therefore we do not override any of
# the installation paths, but install the tree with the default
# layout under 'obj' and shuffle files around in %%install.
kmk %{_smp_mflags}                                             \
    VBOX_ONLY_ADDITIONS=1                                      \
    KBUILD_VERBOSE=2                                           \
    PATH_OUT="$PWD/obj"                                        \
    TOOL_YASM_AS=yasm                                          \
    VBOX_USE_SYSTEM_XORG_HEADERS=1                             \
    VBOX_USE_SYSTEM_GL_HEADERS=1                               \
    VBOX_NO_LEGACY_XORG_X11=1                                  \
    SDK_VBoxLibPng_INCS=/usr/include/libpng16                 \
    SDK_VBoxLibXml2_INCS=/usr/include/libxml2                 \
    SDK_VBoxLzf_LIBS="lzf"                                    \
    SDK_VBoxLzf_INCS="/usr/include/liblzf"                    \
    SDK_VBoxOpenSslStatic_INCS="/usr/include/openssl"                                   \
    SDK_VBoxOpenSslStatic_LIBS="ssl crypto"                         \
    SDK_VBoxZlib_INCS=""                                      \
    VBOX_BUILD_PUBLISHER=_Fedora


%install
# The directory layout created below attempts to mimic the one of
# the commercially supported version to minimize confusion
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}/security

# Guest-additions tools
install -m 0755 -t %{buildroot}%{_sbindir}   \
    obj/bin/additions/VBoxService            \
    %{SOURCE5}

install -m 0755 -t %{buildroot}%{_bindir}    \
    obj/bin/additions/VBoxDRMClient          \
    obj/bin/additions/VBoxClient             \
    obj/bin/additions/VBoxControl            \
    obj/bin/additions/vboxwl

# Guest libraries
install -m 0755 -t %{buildroot}%{_libdir}/security \
    obj/bin/additions/pam_vbox.so

install -p -m 0755 -D src/VBox/Additions/x11/Installer/98vboxadd-xclient \
    %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient.sh
ln -s ../..%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient.sh \
    %{buildroot}%{_bindir}/VBoxClient-all
desktop-file-install --dir=%{buildroot}%{_sysconfdir}/xdg/autostart/ \
    --remove-key=Encoding src/VBox/Additions/x11/Installer/vboxclient.desktop
desktop-file-validate \
    %{buildroot}%{_sysconfdir}/xdg/autostart/vboxclient.desktop

install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_unitdir}/vboxservice.service
install -p -m 0644 -D %{SOURCE3} %{buildroot}%{_udevrulesdir}/60-vboxguest.rules
install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_unitdir}/vboxclient.service


%pre
# Add a group "vboxsf" for Shared Folders access
# All users which want to access the auto-mounted Shared Folders have to
# be added to this group.
getent group vboxsf >/dev/null || groupadd -r vboxsf 2>&1
getent passwd vboxadd >/dev/null || \
    useradd -r -g 1 -d /var/run/vboxadd -s /sbin/nologin vboxadd 2>&1

%post
%systemd_post vboxclient.service
%systemd_post vboxservice.service

%preun
%systemd_preun vboxclient.service
%systemd_preun vboxservice.service

%postun
%systemd_postun_with_restart vboxclient.service
%systemd_postun_with_restart vboxservice.service


%files
%license COPYING*
%{_bindir}/vboxwl
%{_bindir}/VBoxClient
%{_bindir}/VBoxControl
%{_bindir}/VBoxClient-all
%{_bindir}/VBoxDRMClient
%{_sbindir}/VBoxService
%{_sbindir}/mount.vboxsf
%{_libdir}/security/pam_vbox.so
%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient.sh
%{_sysconfdir}/xdg/autostart/vboxclient.desktop
%{_unitdir}/vboxclient.service
%{_unitdir}/vboxservice.service
%{_udevrulesdir}/60-vboxguest.rules


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 19 2024 Sérgio Basto <sergio@serjux.com> - 7.1.4-1
- Update virtualbox-guest-additions to 7.1.4 (#2315230)

* Sat Sep 28 2024 Sérgio Basto <sergio@serjux.com> - 7.1.2-1
- Update virtualbox-guest-additions to 7.1.2 (#2311545)

* Wed Sep 25 2024 Sérgio Basto <sergio@serjux.com> - 7.1.0-3
- (#2314406) Remove /usr/bin/VBoxAudioTest

* Sat Sep 21 2024 Sérgio Basto <sergio@serjux.com> - 7.1.0-2
- Add /usr/bin/vboxwl and /usr/bin/VBoxAudioTest

* Tue Sep 17 2024 Sérgio Basto <sergio@serjux.com> - 7.1.0-1
- Update virtualbox-guest-additions to 7.1.0 (#2311545)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sérgio Basto <sergio@serjux.com> - 7.0.20-1
- Update virtualbox-guest-additions to 7.0.20 (#2298095)

* Thu May 16 2024 Sérgio Basto <sergio@serjux.com> - 7.0.18-1
- Update virtualbox-guest-additions to 7.0.18 (#2278895)

* Thu Apr 18 2024 Sérgio Basto <sergio@serjux.com> - 7.0.16-1
- Update virtualbox-guest-additions to 7.0.16 (#2275339)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 7.0.14-1
- Update to 7.0.14 (#2258642)

* Tue Oct 17 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 7.0.12-1
- Update to 7.0.12 (#2244635)

* Tue Aug 22 2023 Sérgio Basto <sergio@serjux.com> - 7.0.10-1
- Update virtualbox-guest-additions to 7.0.10 (#2223732)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Sérgio Basto <sergio@serjux.com> - 7.0.8-1
- Update virtualbox-guest-additions to 7.0.8 (#2187763)
- Replaces with sed -i "s/VBOX_ZLIB_STATIC/VBoxZlibStatic/; s/VBOX_ZLIB-x86/VBoxZlib-x86/; s/VBOX_ZLIB/VBoxZlib/; s/VBOX_LIBXML2/VBoxLibXml2/; s/VBOX_VPX/VBoxLibVpx/;s/VBOX_LZF/VBoxLzf/;s/VBOX_LIBPNG/VBoxLibPng/; s/VBOX_LIBCURL/VBoxLibCurl/;s/VBOX_DXVK/VBoxDxVk/;s/VBOX_OGG/VBoxLibOgg/;s/VBOX_VORBIS/VBoxLibVorbis/; s/VBOX_TPMS/VBoxLibTpms/" virtualbox-guest-additions.spec

* Mon Jan 30 2023 Sérgio Basto <sergio@serjux.com> - 7.0.6-1
- Update virtualbox-guest-additions to 7.0.6 (#2161718)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Sérgio Basto <sergio@serjux.com> - 7.0.4-1
- Update virtualbox-guest-additions to 7.0.4

* Sat Nov 05 2022 Sérgio Basto <sergio@serjux.com> - 7.0.2-1
- Update to 7.0.2
- Add mount.vboxsf script wrapper
- (#2049736) Add a note into the description informing this packages replaces
  Virtualbox's own method to install Guest Additions.

* Mon Oct 31 2022 Sérgio Basto <sergio@serjux.com> - 6.1.40-1
- Update virtualbox-guest-additions to 6.1.40

* Sat Sep 03 2022 Sérgio Basto <sergio@serjux.com> - 6.1.38-1
- Update virtualbox-guest-additions to 6.1.38

* Wed Aug 03 2022 Sérgio Basto <sergio@serjux.com> - 6.1.36-1
- Update Virtualbox Guest Additions to 6.1.36 (#2108937)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 22 2022 Sérgio Basto <sergio@serjux.com> - 6.1.34-1
- Update Virtualbox Guest Additions to 6.1.34 (#2076755)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Sérgio Basto <sergio@serjux.com> - 6.1.32-1
- Update Virtualbox Guest Additions to 6.1.32 (#2042010)

* Wed Nov 24 2021 Sérgio Basto <sergio@serjux.com> - 6.1.30-1
- Update Virtualbox Guest Additions to 6.1.30 (#2025728)

* Fri Oct 22 2021 Sérgio Basto <sergio@serjux.com> - 6.1.28-1
- Update Virtualbox Guest Additions to 6.1.28 (#2015655)

* Wed Aug 11 2021 Sérgio Basto <sergio@serjux.com> - 6.1.26-1
- Update Virtualbox Guest Additions to 6.1.26 (#1984089)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Sérgio Basto <sergio@serjux.com> - 6.1.22-1
- Update Virtualbox Guest Additions to 6.1.22 (#1955281)

* Fri Apr 23 2021 Sérgio Basto <sergio@serjux.com> - 6.1.20-1
- Update Virtualbox Guest Additions to 6.1.20 (#1951631)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.1.18-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 6.1.18-1
- Update to 6.1.18 (#1918032)

* Fri Oct 23 2020 Sérgio Basto <sergio@serjux.com> - 6.1.16-1
- Update Virtualbox Guest Additions to 6.1.16a

* Sun Sep 13 2020 Sérgio Basto <sergio@serjux.com> - 6.1.14-1
- Update Virtualbox Guest Additions to 6.1.14a

* Sun Aug 02 2020 Sérgio Basto <sergio@serjux.com> - 6.1.12-1
- Update Virtualbox Guest Additions to 6.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Hans de Goede <hdegoede@redhat.com> - 6.1.10-2
- Install the new VBoxDRMClient binary and make vboxclient.service
  run that instead of VBoxClient, this fixes VM display resizing when
  the guest is running a Wayland session

* Sat Jun 06 2020 Sérgio Basto <sergio@serjux.com> - 6.1.10-1
- Update Virtualbox Guest Additions to 6.1.10

* Wed May 20 2020 Hans de Goede <hdegoede@redhat.com> - 6.1.8-2
- Add a vboxclient.service which runs VBoxClient --vwsvga when using the
  VMSVGA virtual GPU, this fixes resizing in wayland sessions (rhbz 1789545)
- Drop VBoxClient --vwsvga-x11 from VBoxClient-all, it is not necessary
  now that we run VBoxClient --vwsvga as service and it was breaking resize
  support with the VBoxSVGA virtual GPU (rhbz 1789545)
- Drop ExecStartPre modprove vboxvideo vboxsf from vboxservice.service,
  this is not necessary, they will be loaded automatically

* Sat May 16 2020 Sérgio Basto <sergio@serjux.com> - 6.1.8-1
- Update Virtualbox Guest Additions to 6.1.8

* Thu Apr 16 2020 Sérgio Basto <sergio@serjux.com> - 6.1.6-1
- Update Virtualbox Guest Additions to 6.1.6

* Wed Mar 11 2020 Sérgio Basto <sergio@serjux.com> - 6.1.4-4
- koji test

* Wed Mar 11 2020 Sérgio Basto <sergio@serjux.com> - 6.1.4-3
- Fix for clipboard
- Obsoletes virtualbox-guest-additions-ogl

* Tue Mar  3 2020 Hans de Goede <hdegoede@redhat.com> - 6.1.4-2
- Fix VBoxClient --vmsvga-x11 crash (rhbz#1806778)

* Sat Feb 22 2020 Sérgio Basto <sergio@serjux.com> - 6.1.4-1
- Update Virtualbox Guest Additions to 6.1.4
- Remove hack "Conflicts VirtualBox-server > %%{version}". With kernel 5.5.6
  (more or less), vboxsf is included in Fedora kernel and
  virtualbox-guest-additions don't need akmod-VirtualBox, anymore.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Sérgio Basto <sergio@serjux.com> - 6.1.2-1
- Update Virtualbox Guest Additions to 6.1.2

* Fri Dec 20 2019 Sérgio Basto <sergio@serjux.com> - 6.1.0-1
- Upgrade to 6.1.0
- Seems that VBoxOGL was removed in 6.1.0

* Wed Nov 13 2019 Sérgio Basto <sergio@serjux.com> - 6.0.14-2
- Change BR from python2 to python3

* Thu Oct 17 2019 Sérgio Basto <sergio@serjux.com> - 6.0.14-1
- Update Virtualbox Guest Additions to 6.0.14

* Fri Sep 06 2019 Sérgio Basto <sergio@serjux.com> - 6.0.12-1
- Update Virtualbox Guest Additions to 6.0.12

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Sérgio Basto <sergio@serjux.com> - 6.0.10-1
- Update Virtualbox Guest Additions to 6.0.10

* Fri May 24 2019 Sérgio Basto <sergio@serjux.com> - 6.0.8-2
- Just force same version and not same release

* Sun May 19 2019 Sérgio Basto <sergio@serjux.com> - 6.0.8-1
- Update Virtualbox Guest Additions to 6.0.8

* Fri Apr 26 2019 Sérgio Basto <sergio@serjux.com> - 6.0.6-1
- Update Virtualbox Guest Additions to 6.0.6

* Wed Mar 20 2019 Hans de Goede <hdegoede@redhat.com> - 6.0.4-2
- Fix automounted shares not working on 6.0.x hosts

* Thu Mar 07 2019 Sérgio Basto <sergio@serjux.com> - 6.0.4-1
- Update Virtualbox Guest Additions to 6.0.4

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Hans de Goede <hdegoede@redhat.com> - 6.0.2-1
- Update Virtualbox Guest Additions to 6.0.2, security fix version

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 6.0.0-2
- Rebuilt for libcrypt.so.2 (#1666033)
- Add a patch to fix build on Fedora 30

* Thu Dec 20 2018 Sérgio Basto <sergio@serjux.com> - 6.0.0-1
- VirtualBox 6.0.0

* Mon Nov 12 2018 Sérgio Basto <sergio@serjux.com> - 5.2.22-1
- Update Virtualbox Guest Additions to 5.2.22, security fix version

* Sat Oct 20 2018 Sérgio Basto <sergio@serjux.com> - 5.2.20-1
- Update Virtualbox Guest Additions to 5.2.20, bugfix version

* Thu Aug 30 2018 Sérgio Basto <sergio@serjux.com> - 5.2.18-1
- Update Virtualbox Guest Additions to 5.2.18

* Wed Aug 01 2018 Sérgio Basto <sergio@serjux.com> - 5.2.16-2
- Force instalation of same version VirtualBox-kmodsrc and
  virtualBox-guest-additions

* Sat Jul 21 2018 Sérgio Basto <sergio@serjux.com> - 5.2.16-1
- Update Virtualbox Guest Additions to 5.2.16

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
- https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Mon Jul 02 2018 Sérgio Basto <sergio@serjux.com> - 5.2.14-1
- Update Virtualbox Guest Additions to 5.2.14

* Sat May 12 2018 Sérgio Basto <sergio@serjux.com> - 5.2.12-1
- Update to 5.2.12

* Sun Apr 22 2018 Sérgio Basto <sergio@serjux.com> - 5.2.10-1
- Update to 5.2.10

* Thu Mar  1 2018 Hans de Goede <hdegoede@redhat.com> - 5.2.8-1
- Update to 5.2.8
- Use https for all URLs

* Wed Feb  7 2018 Hans de Goede <hdegoede@redhat.com> - 5.2.6-4
- Do not use pkg-config for includes, as pkg-config prefixes an unwanted -I
- Fix /etc/X11/xinit/xinitrc.d/98vboxadd-xclient.sh to now show an error
  notification when not running under vbox, as we will be part of the
  Workstation livecd which may run anywhere

* Mon Jan 29 2018 Hans de Goede <hdegoede@redhat.com> - 5.2.6-3
- Update to 5.2.6
- Drop VirtualBox-4.3.0-no-bundles.patch, set make variables instead
- Adjust automount vboxservice for mainline vboxsf filesystem driver
- Drop mount.vboxsf, the mainline vboxsf filesystem driver works with the
  regular mount binary
- Drop commented out Requires: kernel, this is bad idea (rhbz#1534595)
- Use pkgconfig to get include/libs instead of hardcoding (rhbz#1534595)
- Rename to lowercaps virtualbox-guest-additions, add Obsoletes / Provides
  for upgradepath from rpmfusion (rhbz#1534595)
- Add Provides: VirtualBox-kmod-common for rpmfusion upgradepath (rhbz#1534595)
- Latest rpmfusion Release is 2, set our Release field to 3

* Sun Nov 26 2017 Hans de Goede <hdegoede@redhat.com> - 5.2.2-1
- Update to 5.2.2

* Thu Sep 21 2017 Hans de Goede <hdegoede@redhat.com> - 5.2.0-0.1.svn68769
- Switch to a 5.2 svn snapshot, as 5.2 has a new /dev/vboxguest ioctl API
  which the mainline version of the vboxguest drivers implement

* Mon Aug 28 2017 Hans de Goede <hdegoede@redhat.com> - 5.1.26-3
- Put the libGL.so.1 replacement libs and VBoxOGLRun scripts in an -ogl
  subpackage, so that people can install both the i686 and x86_64 versions.
- Filter out libGL.so.1 provides

* Mon Aug 14 2017 Hans de Goede <hdegoede@redhat.com> - 5.1.26-2
- Initial Fedora package based on the guest-addition parts of the
  rpmfusion VirtualBox package
