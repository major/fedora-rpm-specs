%undefine __cmake_in_source_build

Name:           kjots
Summary:        KDE Notes application
Version:        5.1.0
Release:        8%{?dist}
License:        GPLv2
URL:            https://userbase.kde.org/KJots

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# upstream changes for compatibility with latest Akonadi/KPIM libraries
Patch0:         kjots-akonadi-update.patch

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5XmlGui)

BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5KontactInterface)

BuildRequires:  cmake(Grantlee5)

# xsltproc
BuildRequires:  libxslt

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
KJots is an application for writing and organizing notes.


%prep
%autosetup -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang kjots --with-kde


%check
for f in %{buildroot}%{_kf5_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}/%{_kf5_metainfodir}/org.kde.kjots.appdata.xml


%files -f kjots.lang
%license COPYING COPYING.LIB
%doc README
%{_kf5_bindir}/kjots
%{_kf5_qtplugindir}/kjotspart.so
%{_kf5_qtplugindir}/kcm_kjots.so
%{_kf5_qtplugindir}/kontact5/kontact_kjotsplugin.so
%dir %{_kf5_datadir}/kontact/
%dir %{_kf5_datadir}/kontact/ksettingsdialog/
%{_kf5_datadir}/kontact/ksettingsdialog/kjots.setdlg
%{_kf5_datadir}/kservices5/kjotspart.desktop
%{_kf5_datadir}/kservices5/kjots_config_misc.desktop
%dir %{_kf5_datadir}/kservices5/kontact/
%{_kf5_datadir}/kservices5/kontact/kjotsplugin.desktop
%{_kf5_datadir}/applications/org.kde.kjots.desktop
%{_kf5_metainfodir}/org.kde.kjots.appdata.xml
%{_kf5_datadir}/icons/hicolor/*/apps/kjots.*
%{_kf5_datadir}/kjots/
%{_kf5_datadir}/kxmlgui5/kjots/
%{_kf5_datadir}/config.kcfg/kjots.kcfg


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.1.0-3
- Exclude arches ppc64le,s390x

* Fri May 21 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.1.0-2
- New dependency KF5Libkdepim added

* Fri May 21 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.1.0-1
- 5.1.0
- Source URL changed
- Old source version removed
- Files section fixed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2-8
- Remove obsolete scriptlets

* Tue Dec 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-7
- rebuild (pim-17.12.0)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-6
- release++

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-5.1
- rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-3
- rebuild (kde-apps-16.12.x)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-1
- 5.0.2, update URL

* Fri Jul 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-3
- update URL

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.0.1-2
- fix url
- fix scriptlets
- fix %%license and %%doc
- validate appdata

* Sat Feb 13 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.0.1-1
- initial package
