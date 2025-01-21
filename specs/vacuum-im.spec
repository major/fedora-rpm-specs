%undefine __cmake_in_source_build

# https://github.com/vacuum-im/vacuum-im/commit/0abd5e11dd3e2538b8c47f5a06febedf73ae99ee
%global         commit 0abd5e11dd3e2538b8c47f5a06febedf73ae99ee
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         commitdate 20211209
%global         sname vacuum

Name:           %{sname}-im
Summary:        XMPP/Jabber client
Version:        1.3.0
Release:        0.33.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Url:            http://www.vacuum-im.org/
Source0:        https://github.com/Vacuum-IM/vacuum-im/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-fix-building-with-qt5.5.patch
Patch1:         %{name}-fix-type-mismatch.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(qxtglobalshortcut)
BuildRequires:  qtlockedfile-qt5-devel
BuildRequires:  chrpath
BuildRequires:  openssl-devel
BuildRequires:  hunspell-devel
BuildRequires:  libidn-devel
BuildRequires:  jdns-devel
BuildRequires:  zlib-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:      %{name}-data = %{version}
Requires:       fedora-logos
Requires:       hicolor-icon-theme

%description
Full-featured cross platform Jabber/XMPP client.
The core program is just a plugin loader - all functionality is made
available via plugins. This enforces modularity and ensures well defined
component interaction via interfaces.

%package data
Summary:       Images, themes and translatons for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains images, themes and translations.

%package devel
Summary:  Development Files for Vacuum-IM
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes files needed to develop Vacuum-IM modules.

%prep
%autosetup -p0 -n %{name}-%{commit}
#%%patch0 -p0

# Fix W: wrong-file-end-of-line-encoding /usr/share/doc/vacuum-im/AUTHORS
sed -i 's/\r$//' AUTHORS CHANGELOG README TRANSLATORS

# Fix W: spurious-executable-perm
chmod a-x src/plugins/spellchecker/{spellchecker,spellbackend}.cpp

# delete bundled qxtglobalshortcut sources
rm -rf src/thirdparty/qxtglobalshortcut

# delete bundled zlib sources
rm -rf src/thirdparty/zlib

%build
%cmake \
          -DINSTALL_LIB_DIR=%{_lib} \
          -DINSTALL_APP_DIR=%{name} \
          -DLFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed" \
          -DCFLAGS="%{optflags}"    \
          -DCXXFLAGS="%{optflags}"

%cmake_build

%install
%cmake_install
install -D -m644 resources/menuicons/shared/mainwindowlogo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
sed -i "s/Exec=%{sname}/Exec=%{name}/;s/Icon=%{sname}/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{sname}.desktop
mv %{buildroot}%{_datadir}/applications/%{sname}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_datadir}/pixmaps/%{sname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mv %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{name}

find %{buildroot}%{_datadir}/%{name}/translations -name "*.qm" | sed 's:'%{buildroot}'::
s:.*/\([a-zA-Z]\{2\}\).qm:%lang(\1) \0:' > %{name}.lang

rm -f %{buildroot}%{_defaultdocdir}/%{name}/COPYING
rm -f %{buildroot}%{_datadir}/%{name}/resources/adiummessagestyles/renkoo/Contents/Resources/*LICENSE.txt

# Remove rpath E: binary-or-shlib-defines-rpath /usr/bin/vacuum-im ['$ORIGIN', '$ORIGIN/../lib64/']
chrpath --delete %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%doc CHANGELOG AUTHORS README TRANSLATORS
%license COPYING
%license resources/adiummessagestyles/renkoo/Contents/Resources/*LICENSE.txt
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/plugins
%{_libdir}/libvacuumutils.so.*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/pixmaps/%{name}.png

%files data
%{_datadir}/%{name}

%files devel
%{_libdir}/libvacuumutils.so
%{_includedir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.33.20211209git0abd5e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.32.20211209git0abd5e1
- Add %%{name}-fix-type-mismatch.patch

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.0-0.31.20211209git0abd5e1
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.30.20211209git0abd5e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.29.20211209git0abd5e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.28.20211209git0abd5e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.27.20211209git0abd5e1
- Update to 1.3.0-0.27.20211209git0abd5e1

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.26.20200608gitb6c5dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.25.20200608gitb6c5dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.24.20200608gitb6c5dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.23.20200608gitb6c5dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.22.20200608gitb6c5dad
- Rebuilt

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.21.20200608gitb6c5dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.20.20200608gitb6c5dad
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.19.20200608gitb6c5dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.18.20200608gitb6c5dad
- Update to 1.3.0-0.18.20200608gitb6c5dad

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.17.20191014git9f3952b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.16.20191014git9f3952b
- Update to 1.3.0-0.16.20191014git9f3952b

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.15.20181129git52c2a8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.14.20181129git52c2a8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.13.20181129git52c2a8c
- Update to 1.3.0-0.13.20181129git52c2a8c
- Add lang files

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1.3.0-0.12.20180214git01910e9
- rebuild for hunspell 1.7.0

* Tue Sep 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.11.20180214git01910e9
- Remove BR minizip-compat-devel
- Add BR pkgconfig(Qt5Svg)

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com> - 1.3.0-0.10.20180214git01910e9
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.9.20180214git01910e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.8.20180214git01910e9
- Remove scriptlets
- Update to 1.3.0-0.8.20180214git01910e9

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.7.20180127git58ad802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.6.20180127git58ad802
- Update to 1.3.0-0.6.20180127git58ad802
- Dropped %%{name}-unbundle-qxtglobalshortcut.patch
- Delete bundled qxtglobalshortcut sources

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-0.5.20171028git6b614da
- Remove obsolete scriptlets

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 1.3.0-0.4.20171028git6b614da
- rebuild for hunspell 1.6.2

* Fri Nov 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.3.20171028git6b614da
- Adjusted summary description

* Sun Oct 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.2.20171028git6b614da
- Update to 1.3.0-0.2.20171028git6b614da
- Do not run update-desktop-database on Fedora 25+ as per packaging guidelines
- Remove %%dir %%{_libdir}/%%{name}/plugins, it's marked as listed twice

* Thu Oct 26 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-0.1.20170415git3f1cd42
- Add LFLAGS flag to fix unused-direct-shlib-dependency warnings
- Add %%{name}-unbundle-qxtglobalshortcut.patch
- Initial build
