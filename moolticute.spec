%bcond_without  tests

Name:           moolticute
Version:        1.01.0
Release:        2%{?dist}
Summary:        Companion GUI application for Mooltipass password manager devices

# The entire source code is GPL-3.0-or-later except:
# src/AnsiEscapeCodeHandler.[cpp|h] which is GPL-3.0-only WITH Qt-GPL-exception-1.0,
# src/CyoEncode/ which is BSD-2-Clause,
# src/QtAwesome/ which is MIT AND OFL-1.1 AND CC-BY-3.0 (see src/QtAwesome/README.md for details),
# src/SimpleCrypt/ which is BSD-3-Clause,
# src/http-parser/ which is MIT,
# src/qtcsv/ which is MIT,
# src/qtcsv6/ which is MIT,
# src/zxcvbn-c which is BSD-3-Clause.
#
# Note: src/qwinoverlappedionotifier.[cpp|h] is not compiled, and thus ignored.
# Note: Missing license files are being added: https://github.com/mooltipass/moolticute/pull/1098
License:        GPL-3.0-or-later AND (GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-2-Clause AND BSD-3-Clause AND MIT AND OFL-1.1 AND CC-BY-3.0
URL:            https://github.com/mooltipass/moolticute
Source0:        https://github.com/mooltipass/%{name}/archive/refs/tags/v%{version}.tar.gz
# Add missing license: https://github.com/mooltipass/moolticute/pull/1098
Source1:        LICENSE.CyoEncode
Source2:        LICENSE.SimpleCrypt
Source3:        LICENSE.zxcvbn-c

# QSimpleUpdater is licensed under DBAD, which isn't approved. The updater isn't used anyway, so this patch removes it
# until it is fixed upstream: https://github.com/alex-spataru/QSimpleUpdater/issues/28
Patch0:         0001-remove-updater.patch
# Udev rules are in the mooltipass-udev package
Patch1:         0002-makefile-remove-udev.patch

Requires:       systemd
Requires:       hicolor-icon-theme
Requires:       mooltipass-udev

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
Moolticute is an easy to use companion app to your Mooltipass device and extends
the power of the device to more platform/tools. It allows you to manage your
Mooltipass with a cross-platform app and daemon service that handles all USB
communication with the device.

Moolticute comes with a daemon that runs in the background, and a user interface
app to control your Mooltipass. Other clients can also connect and talk to the
daemon (it uses a WebSocket connection and simple JSON messages).

%prep
%autosetup -p1

# Change the version from git to the specific release version.
# Also set the APP_TYPE to deb to disable the update checker. This isn't
# used anywhere else, so doesn't really matter.
cat <<EOF > ./src/version.h
#ifndef VERSION__H
#define VERSION__H
#define APP_VERSION "v%{version}"
#define APP_TYPE "deb"
#endif
EOF


%build
mkdir -p build
cd build
%{qmake_qt5} PREFIX=%{_prefix} ../Moolticute.pro
%make_build

%install
%make_install
install -Dpm 0644 systemd/moolticuted.service %{buildroot}%{_unitdir}/moolticuted.service

# Collect licenses
mkdir LICENSES
install -pm 0644 LICENSE LICENSES/LICENSE.GPL3
install -pm 0644 src/AnsiEscapeCodeHandler/LICENSE.GPL3-EXCEPT LICENSES/LICENSE.AnsiEscapeCodeHandler
install -pm 0644 src/QtAwesome/LICENSE.md LICENSES/LICENSE.QtAwesome
install -pm 0644 src/http-parser/LICENSE-MIT LICENSES/LICENSE.http-parser
install -pm 0644 src/qtcsv/LICENSE LICENSES/LICENSE.qtcsv
install -pm 0644 src/qtcsv6/LICENSE LICENSES/LICENSE.qtcsv6
# Install missing licenses
install -pm 0644 %{SOURCE1} LICENSES/LICENSE.CyoEncode
install -pm 0644 %{SOURCE2} LICENSES/LICENSE.SimpleCrypt
install -pm 0644 %{SOURCE3} LICENSES/LICENSE.zxcvbn-c


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/moolticute.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%if %{with tests}
%make_build test
%endif


%post
%systemd_post moolticuted.service

%preun
%systemd_preun moolticuted.service

%postun
%systemd_postun_with_restart moolticuted.service

%files
%license LICENSES/*
%doc README.md
%{_bindir}/moolticute
%{_bindir}/moolticuted
%{_metainfodir}/*.metainfo.xml
%{_datadir}/applications/moolticute.desktop
%{_datadir}/icons/hicolor/scalable/apps/moolticute.svg
%{_datadir}/icons/hicolor/32x32/apps/moolticute.png
%{_datadir}/icons/hicolor/128x128/apps/moolticute.png
%{_unitdir}/moolticuted.service

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 09 2023 Arthur Bols <arthur@bols.dev> - 1.01.0-1
- Upstream release 1.01.0

* Sun Jan 22 2023 Arthur Bols <arthur@bols.dev> - 1.00.1-5
- Split off udev rules to mooltipass-udev
- Rename patch

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Arthur Bols <arthur@bols.dev> - 1.00.1-3
- Specify udev rules source by commit hash

* Sun Jan 01 2023 Arthur Bols <arthur@bols.dev> - 1.00.1-2
- Add missing license files

* Thu Dec 01 2022 Arthur Bols <arthur@bols.dev> - 1.00.1-1
- Upstream release 1.00.1
- Update license field for SPDX change
- Enable LTO

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 27 2022 Arthur Bols <arthur@bols.dev> - 0.55.0-1
- Upstream release 0.55.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Arthur Bols <arthur@bols.dev> - 0.53.2-1
- Upstream release 0.53.2

* Fri Dec 03 2021 Arthur Bols <arthur@bols.dev> - 0.53.0-1
- Upstream release 0.53.0

* Tue Sep 14 2021 Arthur Bols <arthur@bols.dev> - 0.52.0-1
- Upstream release 0.52.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Arthur Bols <arthur@bols.dev> - 0.50.1-1
- Initial package
