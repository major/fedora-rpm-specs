
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    kdepim4
Summary: KDE4 PIM (Personal Information Manager) applications
Version: 4.14.10
Release: 56%{?dist}

# code is GPLv2 and docs GFDL
# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://cgit.kde.org/kdepim.git
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/Attic/applications/15.04.3/src/kdepim-%{version}.tar.xz

## upstream patches
Patch1: 0001-Fix-crash-when-we-click-on-search-button.patch
Patch2: 0002-Adjust-to-new-cmake-policy-don-t-use-LOCATION.patch
Patch3: 0003-Use-proper-targets-while-linking.patch
Patch4: 0004-Adjust-to-cmake-policy-change.patch
Patch5: 0005-Fix-the-build-after-yet-another-cmake-policy-change.patch
Patch6: 0006-really-rename-this-pointer-here-too.patch
Patch7: 0007-Fix-CMS-key-generation-defaults.patch
Patch8: 0008-korganizer-cmake-discovery-for-Perl-needed-for-ical2.patch
Patch9: 0009-Fix-error-in-sub-repetition-value-from-command-line-.patch
Patch10: 0010-Build-with-recent-Boost.patch
Patch11: 0011-feed.cpp-in-findArticle-use-QHash-values-as-intended.patch
Patch12: 0012-main.cpp-wrap-mMainWindow-in-QPointer-for-safety.patch
Patch13: 0013-Bug-352889-allow-typing-in-New-Alarm-dialog-while-al.patch
Patch14: 0014-attachmentcontrollerbase.cpp-don-t-crash-in-showCont.patch
Patch15: 0015-kontact-src-iconsidepane.cpp-Fix-bogus-pointer-to-bo.patch
Patch16: 0016-Deal-with-akregator-part-main-widget-being-externall.patch
Patch17: 0017-Bug-338575-Warn-user-if-mail-fails-to-send-if-using-.patch
Patch18: 0018-When-we-disable-from-checked-accounts-only-we-don-t-.patch
Patch19: 0019-Hide-less-than-3-characters-warning-when-all-words-a.patch
Patch20: 0020-Generate-unique-identifier-when-duplicating-a-filter.patch
Patch21: 0021-Fix-duplicate-signature-when-we-use-CTRL-N-in-compos.patch
Patch22: 0022-Fix-configure-with-cmake-3.4.patch
Patch23: 0023-kmcommands.cpp-in-execute-make-sure-the-URL-starts-w.patch
Patch24: 0024-Fix-specification-on-command-line-of-a-reminder-afte.patch
Patch25: 0025-Fix-missing-description-of-t.patch
Patch26: 0026-Use-keyword.patch
Patch27: 0027-Correct-date.patch
Patch28: 0028-Update.patch
Patch29: 0029-Improve-layout-of-monthly-recurrence-editor.patch
Patch30: 0030-Backport-extra-safety-1-hour-timer.patch
Patch31: 0031-CVE-2017-9604.patch

## upstreamable patches
# only link minimal BALOO_PIM_LIBRARY instead of all of BALOO_LIBRARIES
Patch50: kdepim-4.14.10-minimal_baloo_linking.patch
Patch51: 0001-Fix-ordered-comparison-of-pointer-against-zero.patch

#Requires: knode = %{version}-%{release}
#Requires: ktimetracker = %{version}-%{release}

BuildRequires: baloo-devel >= 4.14
BuildRequires: bison flex
BuildRequires: boost-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: grantlee-devel >= 0.5.0
BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: kdelibs4-webkit-devel
BuildRequires: kdepimlibs-devel >= 4.14.7
BuildRequires: libassuan-devel
BuildRequires: pkgconfig(akonadi) >= 1.12.90
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: sed
BuildRequires: zlib-devel
BuildRequires: make

%description
%{summary}, including:
* knode: newsreader
* ktimetracker: Time and task management

%package -n knode
Summary: A newsreader application
Requires: knode-libs%{?_isa} = %{version}-%{release}
%{?kde_runtime_requires}
%description -n knode
%{summary}.

%package -n knode-libs
Summary: Runtime libraries for KNode
Conflicts: kdepim-common < 4.14.10-50
Conflicts: kdepim-libs   < 7:4.14.10-50
Requires: knode = %{version}-%{release}
%description -n knode-libs
%{summary}.

%package -n ktimetracker
Summary: Time and task management
%{?kde_runtime_requires}
%description -n ktimetracker
%{summary}.


%prep
%autosetup -p1 -n kdepim-%{version}

# Ensure app .desktop files have Comment= fields to make appstream happier
grep '^Comment=' knode/KNode.desktop || echo "Comment=Usenet news (nntp) client" >> knode/KNode.desktop

# omit icons conflicting with oxygen-icons-5.19
# https://bugzilla.redhat.com/show_bug.cgi?id=1308475
sed -i -e 's|add_subdirectory(icons)|#add_subdirectory(icons)|g' CMakeLists.txt ||:
mv icons icons.BAK ||:


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DKDEPIM_BUILD_MOBILE:BOOL=OFF \
  -DBUILD_akonadiconsole:BOOL=OFF \
  -DBUILD_akregator:BOOL=OFF \
  -DBUILD_blogilo:BOOL=OFF \
  -DBUILD_console:BOOL=OFF \
  -DBUILD_grantleeeditor:BOOL=OFF \
  -DBUILD_importwizard:BOOL=OFF \
  -DBUILD_kaddressbook:BOOL=OFF \
  -DBUILD_kalarm:BOOL=OFF \
  -DBUILD_kjots:BOOL=OFF \
  -DBUILD_kleopatra:BOOL=OFF \
  -DBUILD_kmail:BOOL=OFF \
  -DBUILD_kmailcvt:BOOL=OFF \
  -DBUILD_knotes:BOOL=OFF \
  -DBUILD_kontact:BOOL=OFF \
  -DBUILD_korgac:BOOL=OFF \
  -DBUILD_korganizer:BOOL=OFF \
  -DBUILD_ksendemail:BOOL=OFF \
  -DBUILD_ktnef:BOOL=OFF \
  -DBUILD_mboximporter:BOOL=OFF \
  -DBUILD_pimsettingexporter:BOOL=OFF \
  -DBUILD_sieveeditor:BOOL=OFF \
  -DBUILD_storageservicemanager:BOOL=OFF
popd

#  -DBUILD_mailimporter:BOOL=OFF \

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/agents/sendlateragent
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/akonadi_next
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/calendarsupport
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/grantleetheme
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/incidenceeditor-ng
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/kaddressbookgrantlee
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/kdgantt2
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/knode
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/doc/knode
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/ktimetracker
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/doc/ktimetracker
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/libkdepim
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/libkdepimdbusinterfaces
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/libkpgp
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/libkleo
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/mailcommon
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/mailimporter
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/messagecore
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/messagecomposer
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/messageviewer
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/pimcommon
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/templateparser

## unpackaged files
rm -fv %{buildroot}%{_kde4_libdir}/lib*.so
rm -fv %{buildroot}%{_kde4_libdir}/libincidenceeditorsngmobile.so*
rm -fv %{buildroot}%{_kde4_libdir}/kde4/kcm_ldap.so
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/kcmldap.desktop
rm -fv %{buildroot}%{_kde4_appsdir}/kconf_update/kpgp*
rm -fv %{buildroot}%{_datadir}/dbus-1/interfaces/org.kde.{addressbook,mailtransport}.service.xml
rm -frv %{buildroot}%{_kde4_appsdir}/kmail2/pics/key*
rm -fv %{buildroot}%{_kde4_bindir}/akonadi_sendlater_agent
rm -fv %{buildroot}%{_kde4_datadir}/akonadi/agents/sendlateragent.desktop
rm -frv %{buildroot}%{_kde4_appsdir}/akonadi_sendlater_agent/


%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


#files
# empty metapackage

%files -n knode
%license COPYING*
%doc knode/README
%{_kde4_bindir}/knode
%{_kde4_libdir}/kde4/kcm_knode.so
%{_kde4_libdir}/kde4/knodepart.so
%{_kde4_datadir}/applications/kde4/KNode.desktop
%{_kde4_datadir}/kde4/services/knode_*.desktop
%{_kde4_appsdir}/knode/
%{_kde4_appsdir}/kconf_update/knode.upd
%{_datadir}/dbus-1/interfaces/org.kde.knode.xml
%{_kde4_datadir}/icons/hicolor/*/apps/knode.*
%lang(en) %{_kde4_docdir}/HTML/en/knode/
# libpimcommon icons, moved here to avoid more icon scriptets in -libs
%{_kde4_datadir}/icons/hicolor/*/apps/kdepim-dropbox.png
#{_kde4_datadir}/icons/hicolor/*/apps/kdepim-googledrive.png

%ldconfig_scriptlets -n knode-libs

%files -n knode-libs
%{_kde4_libdir}/libknodecommon.so.*
## stuff that used to be in kdepim-libs, now used only by knode:
# agents
%{_kde4_libdir}/libsendlater.so.*
# akonadi_next
%{_kde4_libdir}/libakonadi_next.so.*
# grantleetheme
%{_kde4_appsdir}/kconf_update/grantleetheme.upd
%{_kde4_libdir}/libgrantleetheme.so.*
# incidenceeditor-ng
%{_kde4_bindir}/kincidenceeditor
%{_kde4_libdir}/libincidenceeditorsng.so.*
# libcalendarsupport
%{_kde4_datadir}/kde4/servicetypes/calendarplugin.desktop
%{_kde4_libdir}/libcalendarsupport.so.*
%{_kde4_libdir}/libcalendarsupportcollectionpage.so.*
# kaddressbookgrantlee
%{_kde4_libdir}/libkaddressbookgrantlee.so.*
# kdgantt2
%{_kde4_libdir}/libkdgantt2.so.*
# libkdepim
%{_kde4_appsdir}/kdepimwidgets/
%{_kde4_libdir}/libkdepim.so.*
%{_kde4_libdir}/kde4/plugins/designer/kdepimwidgets.so
# libkdepimdbusinterfaces
%{_kde4_libdir}/libkdepimdbusinterfaces.so.*
# libkleo
%{_kde4_datadir}/config/libkleopatrarc
%{_kde4_appsdir}/libkleopatra/
%{_kde4_libdir}/libkleo.so.*
# libkpgp
%{_kde4_libdir}/libkpgp.so.*
# mailcommon
%{_kde4_libdir}/libmailcommon.so.*
%{_kde4_libdir}/kde4/plugins/designer/mailcommonwidgets.so
# mailimporter
%{_kde4_libdir}/libmailimporter.so.*
# messagecompoer
%{_kde4_libdir}/libmessagecomposer.so.*
# messagecore
%{_kde4_libdir}/libmessagecore.so.*
# messageviewer
%{_kde4_libdir}/libmessageviewer.so.*
%{_kde4_appsdir}/messageviewer/
%{_kde4_appsdir}/libmessageviewer/
%{_kde4_datadir}/config/messageviewer_header_themes.knsrc
%dir %{_kde4_libdir}/kde4/plugins/accessible/
%{_kde4_libdir}/kde4/plugins/accessible/messagevieweraccessiblewidgetfactory.so
%dir %{_kde4_libdir}/kde4/plugins/grantlee/
%dir %{_kde4_libdir}/kde4/plugins/grantlee/*/
%{_kde4_libdir}/kde4/plugins/grantlee/*/grantlee_messageheaderfilters.so
# pimcommon
%{_kde4_libdir}/libpimcommon.so.*
%{_kde4_libdir}/kde4/plugins/designer/pimcommonwidgets.so
# templateparser
%{_kde4_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kde4_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kde4_libdir}/libtemplateparser.so.*

%files -n ktimetracker
%license COPYING*
%doc ktimetracker/README
%{_kde4_bindir}/karm
%{_kde4_bindir}/ktimetracker
%{_kde4_libdir}/kde4/kcm_ktimetracker.so
%{_kde4_libdir}/kde4/ktimetrackerpart.so
%{_kde4_datadir}/kde4/services/ktimetracker*.desktop
%{_kde4_appsdir}/ktimetracker/
%{_kde4_datadir}/icons/hicolor/*/apps/ktimetracker.*
%{_datadir}/dbus-1/interfaces/org.kde.ktimetracker.ktimetracker.xml
%{_kde4_datadir}/applications/kde4/ktimetracker.desktop
%lang(en) %{_kde4_docdir}/HTML/en/ktimetracker/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.14.10-55
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 4.14.10-45
- Fix ordered pointer comparison against zero

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Petr Viktorin <pviktori@redhat.com> - 4.14.10-43
- Remove BuildRequires on python2-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-40
- rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.14.10-37
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-36
- fix URL, use %%make_build %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.10-34
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Than Ngo <than@redhat.com> - 4.14.10-31
- fixed bz#1461758 - CVE-2017-9604 kdepim4: kmail: Send Later with Delay bypasses OpenPGP

* Fri Mar 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-30
- update URL, drop BR: kactivities-devel

* Mon Mar 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-29
- drop BR: kde-baseapps-devel

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 4.14.10-27
- Rebuild for gpgme 1.18

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-26
- rebuild (baloo)

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-25
- minimal_baloo_linking.patch (link only libbaloo_pim)

* Sat Apr 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-24
- rebuild

* Sat Apr 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-23
- knode: move icons in -libs to main pkg
- knode-libs: own %%{_kde4_libdir}/kde4/plugins/accessible/
- add %%license files
- update URL, Source URL

* Sat Mar 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-22
- omit grantleeeditor (to avoid conflicts)

* Sat Mar 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-21
- adjust Conflicts, drop unused -common subpkg

* Thu Mar 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-20
- kdepim4 compat pkg: knode, ktimetracker
