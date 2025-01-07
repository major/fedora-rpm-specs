# adblock requires rust and corrosion
%bcond adblock 1

Name:    kdepim-addons
Version: 24.12.0
Release: 2%{?dist}
Summary: Additional plugins for KDE PIM applications
# Cargo license summary:
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:   %{ix86}
%endif

## upstream patches

## upstream patches (master)
Patch0: 0001-use-adblock-0.9.patch

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# libphonenumber is not build for i686 anymore (i686 is not in
# %%{java_arches}), see https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
# Since libphonenumber is a transitive dependency of this package, we must
# drop i686 support as well
%{?qt6_qtwebengine_arches:ExclusiveArch: %(echo %{qt6_qtwebengine_arches} | sed -e 's/i686//g')}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6GuiAddons)

BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6WebEngineViewer)
BuildRequires:  cmake(KPim6TemplateParser)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6AddressbookImportExport)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KF6TextGrammarCheck)
BuildRequires:  cmake(KF6TextTranslator)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6IncidenceEditor)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6MessageList)
BuildRequires:  cmake(KPim6CalendarSupport)
BuildRequires:  cmake(KPim6EventViews)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6Gravatar)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6KSieveUi)
BuildRequires:  cmake(KPim6LdapWidgets)

BuildRequires:  cmake(KPim6Tnef)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6ImportWizard)
BuildRequires:  cmake(KPim6MailImporterAkonadi)
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(KPim6Itinerary)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  pkgconfig(libmarkdown)

%if %{with adblock}
BuildRequires:  cmake(Corrosion)
BuildRequires:  rust-packaging >= 25
%endif

Conflicts:      kdepim-common < 16.04.0

# at least until we have subpkgs for each -- rex
Supplements:    kaddressbook
Supplements:    kmail
Supplements:    korganizer

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1
%if %{with adblock}
pushd plugins/webengineurlinterceptor/adblock
%cargo_prep
popd
%endif


%if %{with adblock}
%generate_buildrequires
pushd plugins/webengineurlinterceptor/adblock > /dev/null
%cargo_generate_buildrequires
popd > /dev/null
%endif


%build
%cmake_kf6 \
  -DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=FALSE

%cmake_build

%if %{with adblock}
# Rust dependency handling
pushd plugins/webengineurlinterceptor/adblock
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
popd
%endif


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%if %{with adblock}
%license plugins/webengineurlinterceptor/adblock/LICENSE.dependencies
%endif
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%if %{with adblock}
%{_kf6_libdir}/libadblockplugin.so.*
%endif
%{_kf6_libdir}/libakonadidatasetools.so.*
%{_kf6_libdir}/libdkimverifyconfigure.so.*
%{_kf6_libdir}/libexpireaccounttrashfolderconfig.so.*
%{_kf6_libdir}/libfolderconfiguresettings.so.*
%{_kf6_libdir}/libkmailconfirmbeforedeleting.so.*
%{_kf6_libdir}/libopenurlwithconfigure.so.*
%{_kf6_qmldir}/org/kde/plasma/PimCalendars/
%{_kf6_qtplugindir}/pim6/mailtransport/mailtransport_sendplugin.so
%{_kf6_qtplugindir}/plasmacalendarplugins/pimevents.so
%{_kf6_qtplugindir}/plasmacalendarplugins/pimevents/
%{_kf6_qtplugindir}/pim6/webengineviewer/
%{_kf6_qtplugindir}/pim6/contacteditor/editorpageplugins/cryptopageplugin.so
%{_kf6_libdir}/libkaddressbookmergelibprivate.so*
%{_kf6_qtplugindir}/pim6/kaddressbook/

# KMail
%{_kf6_bindir}/kmail_*.sh
%{_kf6_libdir}/libkmailmarkdown.so.*
%{_kf6_libdir}/libkmailquicktextpluginprivate.so.*
%{_kf6_qtplugindir}/pim6/akonadi/
%{_kf6_qtplugindir}/pim6/importwizard/
%{_kf6_qtplugindir}/pim6/kmail/
%{_kf6_qtplugindir}/pim6/libksieve/
%{_kf6_qtplugindir}/pim6/templateparser/
%{_kf6_sysconfdir}/xdg/kmail.antispamrc
%{_kf6_sysconfdir}/xdg/kmail.antivirusrc

# PimCommon
%{_kf6_libdir}/libshorturlpluginprivate.so*
%{_kf6_qtplugindir}/pim6/pimcommon/

# BodyPartFormatter, MessageViewer, MessageViewer_headers
%{_kf6_qtplugindir}/pim6/messageviewer/


%changelog
* Tue Dec 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 24.12.0-2
- Drop i686 support beginning with Fedora 42 (leaf package)

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Dec 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-2
- Backport upstream change to use adblock 0.9

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Sat Nov 16 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-2
- Fix for calendar colors being wrong

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Sat Sep 14 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-2
- Add optional Discount

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Thu May 23 2024 Alessandro Astone <ales.astone@gmail.com> - 24.05.0-2
- Respin tarball with stable release

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Mar 27 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.02.0-3
- Drop vendorized build mode for adblock extension

* Tue Mar 26 2024 Kevin Kofler <Kevin@tigcc.ticalc.org> - 24.02.0-2
- Use system rust-adblock (review #2266634), now in Fedora (#2266623)

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Mon Feb 05 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.01.95-2
- Enable adblock

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 14 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

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
