Name:    kdepim-addons
Version: 23.08.1
Release: 2%{?dist}
Summary: Additional plugins for KDE PIM applications

License: GPLv2 and LGPLv2+
URL:     https://invent.kde.org/pim/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstream patches (master)

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# libphonenumber is not build for i686 anymore (i686 is not in
# %%{java_arches}), see https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
# Since libphonenumber is a transitive dependency of this package, we must
# drop i686 support as well
%{?qt5_qtwebengine_arches:ExclusiveArch: %(echo %{qt5_qtwebengine_arches} | sed -e 's/i686//g')}

BuildRequires:  extra-cmake-modules >= 5.39.0
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WebEngine)

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(KF5TextGrammarCheck)
BuildRequires:  cmake(KF5TextTranslator)
BuildRequires:  cmake(KF5XmlGui)

BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiNotes)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5EventViews)
BuildRequires:  cmake(KPim5GrantleeTheme)
BuildRequires:  cmake(KPim5Gravatar)
BuildRequires:  cmake(KPim5IncidenceEditor)
BuildRequires:  cmake(KPim5KontactInterface)
BuildRequires:  cmake(KPim5AddressbookImportExport)

BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5Libkleo)
BuildRequires:  cmake(KPim5MailCommon)
BuildRequires:  cmake(KPim5MailImporterAkonadi)
BuildRequires:  cmake(KPim5MessageComposer)
BuildRequires:  cmake(KPim5MessageCore)
BuildRequires:  cmake(KPim5MessageList)
BuildRequires:  cmake(KPim5MessageViewer)
BuildRequires:  cmake(KPim5PimCommon)
BuildRequires:  cmake(KPim5Tnef)
BuildRequires:  cmake(KPim5ImportWizard)
BuildRequires:  cmake(KPim5Itinerary)
BuildRequires:  cmake(KPim5PkPass)

#global majmin_ver %%(echo %%{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  akonadi-import-wizard-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-notes-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-calendarsupport-devel >= %{majmin_ver}
BuildRequires:  kf5-eventviews-devel >= %{majmin_ver}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
BuildRequires:  kf5-incidenceeditor-devel >= %{majmin_ver}
BuildRequires:  kf5-kitinerary-devel >= %{majmin_ver}
BuildRequires:  kf5-kontactinterface-devel >= %{majmin_ver}
BuildRequires:  kf5-kpkpass-devel >= %{majmin_ver}
BuildRequires:  kf5-ktnef-devel >= %{majmin_ver}
BuildRequires:  kf5-libgravatar-devel >= %{majmin_ver}
BuildRequires:  kf5-libkleo-devel >= %{majmin_ver}
BuildRequires:  kf5-libksieve-devel >= %{majmin_ver}
BuildRequires:  kf5-mailcommon-devel >= %{majmin_ver}
BuildRequires:  kf5-mailimporter-devel >= %{majmin_ver}
BuildRequires:  kf5-messagelib-devel >= %{majmin_ver}
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}
BuildRequires:  libkgapi-devel >= %{majmin_ver}

BuildRequires:  cmake(Grantlee5)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(shared-mime-info)

Conflicts:      kdepim-common < 16.04.0

# at least until we have subpkgs for each -- rex
Supplements:    kaddressbook
Supplements:    kmail
Supplements:    korganizer

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf5 \
  -DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=FALSE

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/icons/hicolor/scalable/status/moon-phase-*
%{_kf5_datadir}/kconf_update/webengineurlinterceptoradblock.upd
%{_kf5_datadir}/qlogging-categories5/*%{name}.*
%{_kf5_libdir}/libadblocklibprivate.so.5*
%{_kf5_libdir}/libakonadidatasetools.so.5*
%{_kf5_libdir}/libdkimverifyconfigure.so.5*
%{_kf5_libdir}/libexpireaccounttrashfolderconfig.so.5*
%{_kf5_libdir}/libfolderconfiguresettings.so.5*
%{_kf5_libdir}/libkmailconfirmbeforedeleting.so.5*
%{_kf5_libdir}/libopenurlwithconfigure.so.5*
%{_kf5_libdir}/libscamconfiguresettings.so.5*
%{_kf5_qmldir}/org/kde/plasma/PimCalendars/
%{_kf5_qtplugindir}/pim5/mailtransport/mailtransport_sendplugin.so
%{_kf5_qtplugindir}/plasmacalendarplugins/pimevents.so
%{_kf5_qtplugindir}/plasmacalendarplugins/pimevents/
%{_kf5_qtplugindir}/pim5/webengineviewer/

# TODO: Split to per-app subpackages?
# KAddressBook
%{_kf5_qtplugindir}/pim5/contacteditor/editorpageplugins/cryptopageplugin.so
%{_kf5_libdir}/libkaddressbookmergelibprivate.so*

%{_kf5_qtplugindir}/pim5/kaddressbook/

# KMail
%{_kf5_bindir}/kmail_*.sh
%{_kf5_libdir}/libkmailmarkdown.so.*
%{_kf5_libdir}/libkmailquicktextpluginprivate.so.*
%{_kf5_qtplugindir}/pim5/akonadi/
%{_kf5_qtplugindir}/pim5/importwizard/
%{_kf5_qtplugindir}/pim5/kmail/
%{_kf5_qtplugindir}/pim5/libksieve/
%{_kf5_qtplugindir}/pim5/templateparser/
%{_kf5_sysconfdir}/xdg/kmail.antispamrc
%{_kf5_sysconfdir}/xdg/kmail.antivirusrc

# KOrganizer
%{_kf5_qtplugindir}/pim5/korganizer/

# PimCommon
%{_kf5_libdir}/libshorturlpluginprivate.so*
%{_kf5_qtplugindir}/pim5/pimcommon/

# BodyPartFormatter, MessageViewer, MessageViewer_headers
%{_kf5_qtplugindir}/pim5/messageviewer/

# qtcreator templates
%dir %{_datadir}/qtcreator
%dir %{_datadir}/qtcreator/templates
%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/
%{_datadir}/qtcreator/templates/kmaileditorplugins/


%changelog
* Mon Sep 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-2
- Rebuild against ktextaddons 1.5.1
- Fix cmake dependencies

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Thu Dec 01 2022 Jiri Kucera <jkucera@redhat.com> - 22.08.3-3
- Drop i686

* Wed Nov 30 2022 Jiri Kucera <jkucera@redhat.com> - 22.08.3-2
- Rebuild for gpgme 1.17.1

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 20 2021 Marc Deop <marcdeop@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Tue Apr 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 15:32:11 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Fri Mar 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-2
- Supplements: kaddressbook kmail korganizer
- use %%make_build %%ldconfig_scriptlets

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Fri Jan 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-2
- pull in upstream fixes in particular...
- High memory usage when adding PIM Events in Digital Clock Widget (kde#367541)

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-3
- rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-2
- rebuild (gpgme)

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Fri Oct 28 2016 Than Ngo <than@redhat.com> - 16.08.2-2
- don't build on ppc64/s390x as qtwebengine is not supported yet

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Tue May 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 16.04.0-1
- Initial version
