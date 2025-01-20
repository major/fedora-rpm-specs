%undefine __cmake_in_source_build

Name:           q4wine
Version:        1.3.13
Release:        10%{?dist}
Summary:        Qt GUI for wine

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://q4wine.brezblock.org.ua/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.appdata.xml

BuildRequires:  qt5-qtbase-devel qt5-linguist qt5-qtsvg-devel cmake
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  icoutils

Requires:       wine-core icoutils

ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
Q4Wine is a qt GUI for wine. It will help
you manage wine prefixes and installed applications.

General features:
* Can export QT color theme into wine colors settings.
* Can easy work with different wine versions at same time;
* Easy creating, deleting and managing prefixes (WINEPREFIX);
* Easy controlling for wine process;
* Autostart icons support;
* Easy cd-image use;
* You can extract icons from PE files (.exe .dll);
* Easy backup and restore for managed prefixes.
* Winetriks support.

%prep
%setup -q
# Make sure we do not use bundled qtsingleapplication
rm -r src/qtsingleapplication

%build
%{cmake} -DWITH_SYSTEM_SINGLEAPP=ON -DQT5=ON -DUSE_GZIP=ON -DRELEASE=ON ..
%cmake_build

%install
%cmake_install

# metadata magic
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

rm -f %{buildroot}%{_datadir}/icons/ubuntu-mono-dark/scalable/apps/q4wine.svg

# no %find_lang macro as l10n go to main /usr/share/q4wine dir

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/q4wine.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_bindir}/q4wine*
%{_libdir}/q4wine
%{_datadir}/applications/q4wine.desktop
%{_mandir}/man1/q4wine*.gz
%{_datadir}/icons/hicolor/scalable/apps/q4wine*.svg
%{_datadir}/metainfo/%{name}.*.xml
%{_datadir}/q4wine

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.13-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.13-3
- Update q4wine.appdata.xml for cs translation.
- Release bump.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 31 2022 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.13-1
- Updated to new 1.3.13.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.12-2
- Fix metadata magic. Again.

* Thu Apr 23 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.12-1
- Update to latest vertion.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.6-2
- Fix appdata and add it's install via appstream-util.
- Drop unused metainfo file.

* Mon Nov 27 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.6-1
- Update to 1.3.6.

* Tue Aug 29 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.5-2
- Fix q4wine.metainfo.xml.

* Tue Aug 15 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.5-1
- Update to 1.3.5.
- Add metadata.xml and metainfo.xml.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.4-1
- Update to 1.3.4.
- Drop aarch64 patch (it's in upstream).

* Sun Aug 21 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.1-3
- Add upstream patch to fix aarch64 lib locations

* Sat Aug 20 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.1-2
- Build on aarc64

* Tue Aug 02 2016 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.3.1-1
- Update to new 1.3.1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 1.1-9.r2
- Rebuild for qtsingleapplication.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-7.r2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Dmitrij S. Kryzhevich <krege@land.ru> 1.1-6.r2
- Drop fuseiso support.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Dmitrij S. Kryzhevich <krege@land.ru> 1.1-3.r2
- Update to 1.1-r2 release.

* Thu Nov 14 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1-2
- Fix setup macros parameters.

* Thu Nov 14 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1-1
- Update to 1.1 release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2.r3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 1.0-1.r3
- Update to 1.0-r3 release.

* Thu Mar 07 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 1.0-1.r2
- Update to 1.0-r2 release.

* Tue Feb 12 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 1.0-1.r1
- Update to 1.0-r1 release.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.121-3
- WINE is supported on ARM too

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 14 2011 Dmitrij S. Kryzhevich <krege@land.ru> - 0.121-1
- Update to 0.121.
- Some spec-file cleanup.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.120-6
- Upstream sources updated to 0.120-r1.
- Remove bundle qtsingleapplication while rpm building.
- Drop qtsingleapplication patch (applied in upstream).
- Drop fix for LICENSE file (applied in upstream).

* Wed Nov 10 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.120-5
- Use system qtsingleapplication.

* Mon Nov 01 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.120-4
- Add ExclusiveArch, there no wine for non *86 archs.

* Wed Oct 27 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.120-3
- Put desktop-file-validate to proper place.
- Own %%{_libdir}/q4wine.

* Tue Oct 26 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.120-2
- post and postun scripts added.
- Source0 changed for Packaging:SourceURL.
- fix for © symbol in LICENSE.

* Wed Oct 06 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.120-1
- initial build.
