Name:           ckb-next
Version:        0.6.0
Release:        7%{?dist}
Summary:        Unofficial driver for Corsair RGB keyboards

License:        GPL-2.0-only

URL:            https://github.com/ckb-next/ckb-next
Source0:        %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# Upstream provides none of the following files
Source1:        ckb-next.appdata.xml
Source2:        ckb-next.1
Source3:        99-ckb-next.preset

# CMakeLists need to be adjusted to compile properly with un-bundled kissfft
Patch1: 0001-unbundle-kissfft.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libappstream-glib
BuildRequires:  qt5-linguist

BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  kiss-fft-devel
BuildRequires:  libappindicator-devel
BuildRequires:  libgudev-devel
BuildRequires:  libxcb-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt5-qtbase-devel >= 5.2.0
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  quazip-qt5-devel >= 0.7.3
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  zlib-devel

BuildRequires:  systemd-devel
%{?systemd_requires}

Requires:       qt5-qtbase >= 5.2.0
Requires:       qt5ct

# ckb-next, as the name suggests, is a re-activation and continuation of "ckb".
# The last released version of the original "ckb" was 0.2.7.
Obsoletes:      ckb < 0.2.8-0


%description
ckb-next is an open-source driver for Corsair keyboards and mice. It aims to
bring the features of their proprietary CUE software to the Linux operating
system. This project is currently a work in progress, but it already
supports much of the same functionality, including full RGB animations.


%prep
%autosetup -p1

# Remove the bundled libraries
rm -rf src/libs/kissfft

# Fedora uses /usr/libexec for daemons
sed -e '/^ExecStart/cExecStart=%{_libexecdir}/ckb-next-daemon' -i linux/systemd/ckb-next-daemon.service.in

# Fedora has merged /lib into /usr/lib
sed -e 's|"/lib/udev/rules.d"|"%{_udevrulesdir}"|g' -i CMakeLists.txt


%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_INSTALL_LIBEXECDIR=libexec \
  -DDISABLE_UPDATER=1 \
  -DFORCE_INIT_SYSTEM=systemd \
  -DSAFE_INSTALL=OFF \
  -DSAFE_UNINSTALL=OFF \

%cmake_build


%install
%cmake_install

# Move the daemon from /usr/bin/ to /usr/libexec
mv %{buildroot}%{_bindir}/ckb-next-daemon %{buildroot}%{_libexecdir}/ckb-next-daemon

install -Dp -m 0644 %{SOURCE3}  %{buildroot}%{_presetdir}/99-ckb-next.preset
install -Dp -m 0644 %{SOURCE1}  %{buildroot}%{_datadir}/metainfo/ckb-next.appdata.xml
install -Dp -m 0644 %{SOURCE2}  %{buildroot}%{_mandir}/man1/ckb-next.1


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ckb-next.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ckb-next.appdata.xml


%post
%systemd_post ckb-next-daemon.service
if [ $1 -eq 1 ]; then
    # starting daemon also at install
    systemctl start ckb-next-daemon.service >/dev/null 2>&1 || :
fi
udevadm control --reload-rules 2>&1 > /dev/null || :


%preun
%systemd_preun ckb-next-daemon.service


%postun
%systemd_postun_with_restart ckb-next-daemon.service
udevadm control --reload-rules 2>&1 > /dev/null || :


%files
%license LICENSE
%doc CHANGELOG.md FIRMWARE README.md
%{_bindir}/ckb-next
%{_bindir}/ckb-next-dev-detect
%{_libexecdir}/ckb-next-daemon
%{_libexecdir}/ckb-next-sinfo
%{_libexecdir}/ckb-next-animations/
%{_libdir}/cmake/ckb-next/
%{_datadir}/applications/ckb-next.desktop
%{_datadir}/metainfo/ckb-next.appdata.xml
%{_datadir}/icons/hicolor/**/apps/ckb-next.png
%{_datadir}/icons/hicolor/**/apps/ckb-next-monochrome.png
%{_datadir}/icons/hicolor/**/status/ckb-next_battery*.png
%{_mandir}/man1/ckb-next.1*
%{_presetdir}/99-ckb-next.preset
%{_udevrulesdir}/*.rules
%{_unitdir}/ckb-next-daemon.service


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0-5
- Fix FTBFS
- Replace kissfft static linking with dynamic linking

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0-1
- Update to v0.6.0
- Drop Patch0 (buffer overflow fix - backported from this release)

* Fri May 05 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-5
- Rebuilt for quazip 1.4

* Tue May 02 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.0-4
- Add a patch to fix program aborting on launch
- Un-bundle kissfft
- Convert License tag to SPDX

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.0-1
- Update to v0.5.0
- Remove the Qt QPA fix from desktop file

* Wed Apr 20 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.4-5
- Fix FTBFS

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 0.4.4-3
- Rebuild (quazip)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.4-1
- Update to v0.4.4

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.3-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.3-1
- Update to v0.4.3
- Remove Patch0 (missing "extern" qualifiers - fixed upstream)
- Simplify the install section (rely on %%cmake_install)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Artur Iwicki <fedora@svgames.pl> - 0.4.2-3
- Add a patch to fix build failures

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Artur Iwicki <fedora@svgames.pl> - 0.4.2-1
- Update to latest upstream release

* Tue Aug 27 2019 Artur Iwicki <fedora@svgames.pl> - 0.4.1-1
- Update to latest upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Artur Iwicki <fedora@svgames.pl> - 0.4.0-1
- Update to latest upstream release

* Sat Feb 16 2019 Artur Iwicki <fedora@svgames.pl> - 0.3.2-4
- Use "install -p" (preserve timestamps)
- Do not use the bundled quazip library

* Sat Jan 26 2019 Artur Iwicki <fedora@svgames.pl> - 0.3.2-3
- Tidy up the spec file
- Remove obsolete scriptlets

* Tue Oct 16 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.2-2
- Fixed animations dir

* Sat Oct 13 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.2-1
- Update to 0.3.2 release

* Sun Oct 7 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.1-1
- Update to 0.3.1 release

* Sat Jun 16 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.0-2
- Fixed Epel build
- Fixed animations dir

* Fri Jun 15 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.0-1
- Update to 0.3.0 release
- set QT_QPA_PLATFORMTHEME only for binary

* Mon Jan 22 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.9-0.1.20180122git2316518
- Update to latest snapshot.

* Sun Dec 17 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.9.20171217git142b307
- Update to latest snapshot.
- Disable debugsource due to build error with empty file debugsourcefiles.list.

* Fri Nov 17 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.8.20171111gitb88d8be
- Update to latest snapshot.

* Fri Oct 20 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.7.20171014gitda28864
- Update to latest snapshot.

* Sun Aug 20 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.6.20170820git6af2773
- Update to latest snapshot.

* Wed Jul 26 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.5.20170726git9dc8216
- Update to latest snapshot.
- Color change freeze workaround by requiring qt5ct and adding to environment.

* Fri Jul 07 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.4.20170707git1331253
- Update to latest snapshot.

* Fri Jun 23 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.3.20170621gitae7346b
- Update to latest snapshot.

* Thu May 25 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.2.20170525gite54c911
- Fix animation path.
- Update to latest snapshot.

* Thu May 18 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.1.20170518git5a34841
- Update to 0.2.8 latest snapshot.

* Fri Apr 14 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.7-0.7.20170414git565add5
- Added systemd preset.
- Update to latest snapshot.

* Sun Feb 19 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.7-0.6.20170219gitb59d179
- Changed package name to ckb-next.
- Update to latest snapshot.

* Sun Jan 22 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.7-0.2.20170120git89e8750
- Update to latest snapshot.

* Thu Dec 1 2016 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.6-0.1
- Created spec file for Fedora based on the Suse spec file
- added appdata file
- added man page

* Thu Aug 25 2016 - aloisio@gmx.com
- Update to version 0.2.6
- Use external quazip only when available
- Replaced ckb-fix-desktop-file.patch with %suse_update_desktop_file
- Replaced ckb-daemon-path.patch and ckb-animations-path.patch with macros \
  for consistency.

* Sun Apr 17 2016 - herbert@graeber-clan.de
- Add hicolor folder, too

* Sun Apr 17 2016 - herbert@graeber-clan.de
- Fix icon folder

* Fri Apr 15 2016 - herbert@graeber-clan.de
- Initial package
- Use /var/run instead of /dev/input for communication with the daemon.
- move the daemon and the animations into the libexec folder
