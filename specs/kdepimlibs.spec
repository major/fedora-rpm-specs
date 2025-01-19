%define apidocs 1
%define akonadi_version_min 1.12.90

%global akonadi_version %(pkg-config --modversion akonadi 2>/dev/null || echo %{akonadi_version_min})

%if 0%{?fedora} > 23
%global kf5_akonadi 1
%endif

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    kdepimlibs
Summary: KDE PIM Libraries
Version: 4.14.10
Release: 48%{?dist}

# http://techbase.kde.org/Policies/Licensing_Policy
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kdepimlibs-%{version}.tar.xz

## upstream patches: KDE/4.14 branch
Patch1: 0001-Output-warnings-when-ItemSync-fails-to-delete-an-ite.patch
Patch2: 0002-missing-camelcase-headers-for-Akonadi-KABC-and-Akona.patch
Patch3: 0003-Optimization-avoid-double-lookup-in-QHash.patch
Patch4: 0004-Fix-build-broken-by-592ae642b6.patch
Patch5: 0005-FindLibical.cmake-using-LINK_LIBRARIES-in-try_run.patch
Patch6: 0006-Adjust-to-cmake-policy-change.patch
Patch7: 0007-Adjust-to-cmake-policy-change.patch
Patch8: 0008-Fix-CMP0022-warnings.patch
Patch9: 0009-Fix-option-name.patch
Patch10: 0010-Add-min-required-cmake-version-fix-clashes-on-target.patch
Patch11: 0011-Remove-use-of-command-creating-un-useful-output.patch
Patch12: 0012-gpgme-CMakeLists.txt-don-t-install-GpgmeppLibraryDep.patch
Patch13: 0013-Remove-use-of-non-existant-file.patch
Patch14: 0014-AgentManager-avoid-recursion-agentTypeAdded-readAgen.patch
Patch15: 0015-Allow-child-dialogs-to-have-a-separate-akonadi-not-s.patch
Patch16: 0016-fix-windows-build.patch
Patch17: 0017-subscriptiondialog.cpp-make-default-size-a-little-la.patch
Patch18: 0018-find-libical-from-the-Config-files-if-possible.patch
Patch19: 0019-also-copy-over-the-USE_ICAL-flags.patch
Patch20: 0020-kio_pop3-Fix-missing-mimetype-warnings.patch
Patch21: 0021-kimap-loginjob.cpp-support-for-GSSAPI-authentication.patch
Patch22: 0022-ItemSync-use-RID-merge-by-default-allow-optional-swi.patch
Patch23: 0023-addtransportdialog.cpp-make-default-size-a-little-la.patch
Patch24: 0024-Fix-ItemSync-merge-type-fallback.patch
Patch25: 0025-incidenceformatter.cpp-allow-links-in-todo-and-journ.patch
Patch26: 0026-Check-response-content-size-before-accessing-it-in-s.patch
Patch27: 0027-icalformat_p.cpp-Fix-heap-use-after-free-in-readICal.patch
Patch28: 0028-Better-error-message-in-case-of-an-ical-parse-error.patch
Patch29: 0029-Speed-up-the-default-Identity-constructor.patch
Patch30: 0030-Use-KSharedConfig-openConfig-kmail2rc-to-try-and-opt.patch
Patch31: 0031-Bug-346060-fix-deferral-time-of-date-only-recurring-.patch
Patch32: 0032-holidays_ua_uk-updated-Ukrainian-holidays.patch
Patch33: 0033-Akonadi-SpecialCollectionsRequestJob-increase-timeou.patch
Patch34: 0034-holiday_de-by_de-remove-Bu-und-Bettag-as-public-holi.patch
Patch35: 0035-akonadi-collectionstatisticsdelegate.cpp-backport.patch

## upstream patches: vendor/intevation/4.14 branch
Patch43: 0043-Backport-avoid-to-transform-as-a-url-when-we-have-a-.patch

## upstreamable patches
Patch51: fix-build-with-ical-3.0.diff

%{?kdelibs4_requires}
# for kio_smtp plain/login sasl plugins
Requires: cyrus-sasl-plain

BuildRequires: boost-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: gpgme-devel
BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: openldap-devel
BuildRequires: libical-devel >= 0.33
# workaround libical-3.0/cmake bogosity
%if 0%{?fedora} > 27
BuildRequires: libical-glib-devel
%endif
BuildRequires: pkgconfig(akonadi) >= %{akonadi_version_min}
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(xpm) pkgconfig(xtst)
%if 0%{?fedora}
BuildRequires: prison-devel
%endif

%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: qt4-doc
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake
BuildRequires: make

%description
Personal Information Management (PIM) libraries for KDE 4.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gpgme%{?_isa} = %{version}-%{release}
Requires: %{name}-kxmlrpcclient%{?_isa} = %{version}-%{release}
Requires: %{name}-akonadi%{?_isa} = %{version}-%{release}
%if ! 0%{?kf5_akonadi}
# akonadi test file conflicts
Conflicts: kf5-akonadi-devel
%endif
Obsoletes: kdepimlibs4-devel < %{version}-%{release}
Provides:  kdepimlibs4-devel = %{version}-%{release}
Requires: boost-devel
# FindQGpgme expects gpgme-devel to be present too
Requires: gpgme-devel
Requires: kdelibs4-devel
%description devel
Header files for developing applications using %{name}.

%package akonadi
Summary: Akonadi runtime support for %{name}
# https://bugzilla.redhat.com/1063698
Conflicts: kdepim-runtime < 1:4.11.80
# when pkg split occurrs, not sure if this is really needed, but... -- Rex
#Obsoletes: kdepimlibs < 4.2.0-3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: akonadi%{?_isa} >= %{akonadi_version}
%description akonadi
%{summary}.

%package apidocs
Summary: kdepimlibs API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the kdepimlibs API documentation in HTML
format for easy browsing.

%package kxmlrpcclient
Summary: Simple XML-RPC Client support
# when spilt out
Conflicts: kdepimlibs < 4.9.2-5
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
%description kxmlrpcclient
This library contains simple XML-RPC Client support. It is used mainly
by the egroupware module of kdepim, but is a complete client and is
quite easy to use.

%package gpgme
Summary: C++ bindings/wrapper for gpgme
# when spilt out
Conflicts: kdepimlibs < 4.12.2-2
# enforce minimal gpgme runtime
%global gpgme_version %(gpgme-config --version 2> /dev/null || echo 0)
%if "%{?gpgme_version}" != "0"
Requires: gpgme%{?_isa} >= %{gpgme_version}
%endif
%description gpgme
%{summary}.


%prep
%autosetup -p1


%build

%if 0%{?fedora} > 23
# workaround for rawhide/gcc6 FTBFS
export CXXFLAGS="%{optflags} -Wno-error=deprecated-declarations -Wno-deprecated-declarations"
%endif

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. 
popd

make %{?_smp_mflags} -C %{_target_platform}

# build apidocs
%if 0%{?apidocs}
export QTDOCDIR=`pkg-config --variable=docdir Qt`
kde4-doxygen.sh --doxdatadir=%{_kde4_docdir}/HTML/en/common .
%endif


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# hack around HTML doc multilib conflicts
for doxy_hack in kcontrol/kresources ; do
pushd %{buildroot}%{_kde4_docdir}/HTML/en/${doxy_hack}
bunzip2 index.cache.bz2
sed -i -e 's!<a name="id[a-z]*[0-9]*"></a>!!g' index.cache
bzip2 -9 index.cache
done
popd

# move devel symlinks
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/devel
pushd %{buildroot}%{_kde4_libdir}
for i in lib*.so
do
  case "$i" in
# conflicts with qgppme
    libqgpgme.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
# conflicts with kdelibs3
    libkabc.so | libkresources.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
# conflicts with kdepim3 (compat)
    libkcal.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
  esac
done
popd

# install apidocs
%if 0%{?apidocs}
mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -prf kdepimlibs-%{version}%{?alphatag}-apidocs %{buildroot}%{_kde4_docdir}/HTML/en/kdepimlibs-apidocs
find %{buildroot}%{_kde4_docdir}/HTML/en/ -name 'installdox' -exec rm -fv {} ';'
%endif

## unpackaged files
# conflicts with kf5-akonadi-mime
rm -fv %{buildroot}%{_kde4_datadir}/config.kcfg/specialmailcollections.kcfg
# conflicts with kf5-kmailtransport, mostly harmless, so can remove unconditionally
rm -fv %{buildroot}%{_kde4_datadir}/config.kcfg/mailtransport.kcfg
%if 0%{?kf5_akonadi}
# conflicts with kf5-akonadi-devel
rm -fv %{buildroot}%{_kde4_bindir}/akonaditest
rm -fv %{buildroot}%{_kde4_bindir}/akonadi2xml
rm -frv %{buildroot}%{_kde4_appsdir}/akonadi_knut_resource/
rm -fv %{buildroot}%{_kde4_libdir}/kde4/akonadi_knut_resource.so
rm -fv %{buildroot}%{_kde4_datadir}/akonadi/agents/knutresource.desktop
%endif


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kde4_appsdir}/kabc/
%{_kde4_datadir}/config.kcfg/recentcontactscollections.kcfg
%{_kde4_datadir}/config.kcfg/resourcebase.kcfg
%{_kde4_datadir}/kde4/services/*
%{_kde4_datadir}/kde4/servicetypes/*
%{_kde4_libdir}/libkabc.so.4*
%{_kde4_libdir}/libkabc_file_core.so.4*
%{_kde4_libdir}/libkblog.so.4*
%{_kde4_libdir}/libkcal.so.4*
%{_kde4_libdir}/libkcalcore.so.4*
%{_kde4_libdir}/libkcalutils.so.4*
%{_kde4_libdir}/libkholidays.so.4*
%{_kde4_libdir}/libkimap.so.4*
%{_kde4_libdir}/libkldap.so.4*
%{_kde4_libdir}/libkmbox.so.4*
%{_kde4_libdir}/libkmime.so.4*
%{_kde4_libdir}/libkontactinterface.so.4*
%{_kde4_libdir}/libkpimidentities.so.4*
%{_kde4_libdir}/libkpimtextedit.so.4*
%{_kde4_libdir}/libkpimutils.so.4*
%{_kde4_libdir}/libkresources.so.4*
%{_kde4_libdir}/libktnef.so.4*
%{_kde4_libdir}/libmicroblog.so.4*
%{_kde4_libdir}/libsyndication.so.4*
%{_kde4_libdir}/kde4/kabc_directory.so
%{_kde4_libdir}/kde4/kabc_file.so
%{_kde4_libdir}/kde4/kabc_ldapkio.so
%{_kde4_libdir}/kde4/kabc_net.so
%{_kde4_libdir}/kde4/kabcformat_binary.so
%{_kde4_libdir}/kde4/kcal_local.so
%{_kde4_libdir}/kde4/kcal_localdir.so
%{_kde4_libdir}/kde4/kcm_kresources.so
%{_kde4_libdir}/kde4/kio_imap4.so
%{_kde4_libdir}/kde4/kio_ldap.so
%{_kde4_libdir}/kde4/kio_mbox.so
%{_kde4_libdir}/kde4/kio_nntp.so
%{_kde4_libdir}/kde4/kio_pop3.so
%{_kde4_libdir}/kde4/kio_sieve.so
%{_kde4_libdir}/kde4/kio_smtp.so
%{_kde4_libdir}/kde4/plugins/designer/kholidayswidgets.so
%{_kde4_docdir}/HTML/en/kcontrol/
%{_kde4_docdir}/HTML/en/kioslave/
%{_kde4_appsdir}/libkholidays/
%{_kde4_datadir}/mime/packages/kdepimlibs-mime.xml

%exclude %{_kde4_datadir}/kde4/services/kcm_mailtransport.desktop
%exclude %{_kde4_datadir}/kde4/services/akonadicontact_actions.desktop

%post akonadi -p /sbin/ldconfig
%postun akonadi -p /sbin/ldconfig

%files akonadi
%{_kde4_libdir}/libakonadi-calendar.so.4*
%{_kde4_libdir}/libakonadi-contact.so.4*
%{_kde4_libdir}/libakonadi-kabc.so.4*
%{_kde4_libdir}/libakonadi-kcal.so.4*
%{_kde4_libdir}/libakonadi-kde.so.4*
%{_kde4_libdir}/libakonadi-kmime.so.4*
%{_kde4_libdir}/libakonadi-notes.so.4*
%{_kde4_libdir}/libakonadi-socialutils.so.4*
%{_kde4_libdir}/libakonadi-xml.so.4*
%{_kde4_appsdir}/akonadi/
%{_kde4_appsdir}/akonadi-kde/
%{_kde4_libdir}/libkalarmcal.so.2*
%{_kde4_libdir}/libmailtransport.so.4*
%{_kde4_libdir}/kde4/akonadi_serializer_socialfeeditem.so
%{_kde4_libdir}/kde4/kcm_mailtransport.so
%{_kde4_libdir}/kde4/kcm_akonadicontact_actions.so
%{_kde4_libdir}/kde4/plugins/designer/akonadiwidgets.so
%{_kde4_appsdir}/kconf_update/mailtransports.upd
%{_kde4_appsdir}/kconf_update/migrate-transports.pl
%{_kde4_datadir}/kde4/services/kcm_mailtransport.desktop
%{_kde4_datadir}/kde4/services/akonadicontact_actions.desktop
%{_kde4_datadir}/mime/packages/x-vnd.akonadi.socialfeeditem.xml

%files devel
%if 0%{?fedora} < 24
# Conflicts: kf5-akonadi-devel
%{_kde4_bindir}/akonadi2xml
# akonadi-testing bits
%{_kde4_bindir}/akonaditest
%{_kde4_appsdir}/akonadi_knut_resource/
%{_kde4_libdir}/kde4/akonadi_knut_resource.so
%{_kde4_datadir}/akonadi/agents/knutresource.desktop
%endif
%{_datadir}/dbus-1/interfaces/org.kde.KResourcesManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.pim.IdentityManager.xml
%{_kde4_appsdir}/cmake/modules/*
%{_kde4_includedir}/*
%{_kde4_libdir}/kde4/devel/lib*.so
%{_kde4_libdir}/lib*.so
%{_kde4_libdir}/cmake/KdepimLibs*
%{_kde4_libdir}/gpgmepp/

%if 0%{?apidocs}
%files apidocs
%{_kde4_docdir}/HTML/en/kdepimlibs-apidocs/
%endif

%ldconfig_scriptlets gpgme

%files gpgme
%{_kde4_libdir}/libgpgme++-pth*.so.2*
%{_kde4_libdir}/libgpgme++.so.2*
%{_kde4_libdir}/libqgpgme.so.1*

%ldconfig_scriptlets kxmlrpcclient

%files kxmlrpcclient
%doc kxmlrpcclient/README 
%{_kde4_libdir}/libkxmlrpcclient.so.4*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.14.10-47
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-40
- omit specialmailcollections.kcfg (conflicts with kf5-akonadi-mime)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-33
- rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 4.14.10-31
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 4.14.10-30
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 4.14.10-28
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 4.14.10-27
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 4.14.10-25
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 4.14.10-24
- Rebuild for ICU 60.1

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-23
- rebuild (libical)

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 4.14.10-22
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-19
- update URL, -gpgme: enforce minimal gpgme runtime

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-17
- -devel: avoid conflict with gpgmepp-devel

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 4.14.10-16
- Rebuild for gpgme 1.18

* Thu Oct 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-15
- HTML injection in plain text viewer (#1382286,#1382298)

* Wed Jun 01 2016 Rex Dieter <rdieter@fedoraproject.org> 4.14.10-14
- pull in 4.14 branch fixes

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-13
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> 4.14.10-12
- rebuild (qt), update URL

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 4.14.10-10
- rebuild for ICU 57.1

* Sat Feb 27 2016 Rex Dieter <rdieter@fedoraproject.org> 4.14.10-9
- fix conflicts with kf5-akonadi-devel (#1312563)

* Mon Feb 15 2016 Rex Dieter <rdieter@fedoraproject.org> 4.14.10-8
- Pull in 4.14 branch fixes
- update URL
- make mergeable with < f24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 4.14.10-6
- rebuild for libical 2.0.0

* Mon Dec 21 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.10-5
- move xml dbus interface files to -devel

* Thu Dec 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-4
- -akonadi: drop binaries and conflicting mailtransport.kcfg (#1292325)
- drop akonadi_subpkg macro (unconditional now)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.14.10-2
- rebuild for Boost 1.58

* Sun Jun 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.10-1
- 4.14.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.9-1
- 4.14.9

* Thu May 14 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.8-1
- 4.14.8

* Fri Apr 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.7-1
- 4.14.7

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.6-1
- 4.14.6

* Tue Feb 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.5-1
- 4.14.5

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.4-3
- rebuild (gcc5)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.14.4-2
- Rebuild for boost 1.57.0

* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.4-1
- 4.14.4

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 4.14.1-2
- -devel: Requires: gpgme-devel

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Wed Sep 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.14.0-3
- -akonadi: Conflicts: kdepim-runtime < 1:4.11.80 (#1063698)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Mon Aug 04 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-1
- 4.13.97

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.2-2
- optimize mimeinfo scriptlet

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.13.1-2
- Rebuild for boost 1.55.0

* Sat May 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-1
- 4.13.1

* Fri Apr 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Thu Apr 03 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sat Mar 22 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Mon Mar 17 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.90-1
- 4.12.90

* Sat Mar 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Thu Feb 20 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-2
- -gpgme subpkg
- move Requires: %%name-kxmlrpcclient to -devel (from main pkg)

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Wed Dec 18 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Fri Nov 15 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-3
- some upstream patches, including upstreamed etm refcounting...

* Tue Nov 12 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-2
- test "ETM refcounting fixes", reviewboard #113680 (kde #312460)

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Tue Sep 03 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 4.10.97-2
- Rebuild for boost 1.54.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.90-1
- 4.10.90

* Mon Jun 24 2013 Daniel Vrátil <dvratil@redhat.com> - 4.10.4-3
- install akonadicontact_actions.desktop (#977025)

* Wed Jun 05 2013 Martin Briza <mbriza@redhat.com> - 4.10.4-2
- fixed infinite recursion on ssl handshake error in akonadi_imap_resource (#891620)

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Fri May 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-2
- rebuild (libical)

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.10.0-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.10.0-3
- Rebuild for Boost-1.53.0

* Wed Feb 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.10.0-2
- restore documentation multilib hack for now as per IRC discussion with tosky

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-2
- drop apidoc multilib hacks

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Sat Dec 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.95-3
- drop Find-NepomukCore-if-not-found-yet.patch, breaks kdepim-runtime.

* Fri Dec 21 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-2
- nepomuk-core related upstream patches
- -devel: Requires: nepomuk-core-devel

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95
- BR: nepomuk-core
- fix/prune changelog

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Mon Nov 26 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-2
- cherry-pick a few upstream patches (#815047)

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Thu Nov 1 2012 Lukáš Tinkl<ltinkl@redhat.com> 4.9.2-6
- build against prison only under Fedora

* Mon Oct 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-5
- -kxmlrpcclient subpkg (#855930)

* Mon Oct 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-4
- remove .spec cruft

* Fri Oct 26 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-3
- fix FTBFS against akonadi-1.8.1 

* Thu Oct 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-2
- fix/update HTML docbook multilib hack (#862388)

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Wed Sep 26 2012 Tomas Mraz <tmraz@redhat.com> - 4.9.1-4
- drop libgpgme++-pth.so.2 as gpgme does not ship the pth-linked library
  anymore

* Mon Sep 17 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-3
- Update holiday_sg_en-gb (#857877, kde#306924)
- Update Argentina holidays rule file (kde#306347)
- kmail cannot display html messages with images refered (kde#205791)
- transportlistview: resize to content 

* Sun Sep 16 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-2
- BR: libuuid-devel

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Mon Jul 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-2
- rebuild (boost)

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-2
- akonadi_version_min 1.7.90

* Wed Jun 27 2012 Radek Novacek <rnovacek@redhat.com> - 4.8.95-1
- 4.8.95

* Fri Jun 08 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-2
- respin

* Sat May 26 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Wed Mar 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-3
- drop libkalarmcal.so.2 from base pkg (#804360)

* Sun Mar 18 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-2
- kdepimlibs pulling in kdepimlibs-akonadi (#804360)
- add mime scriptlet

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1
- remove dovecot patch, upstream

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for c++ ABI breakage

* Fri Jan 20 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97
- drop upstreamed patch for bug kde#289693

* Thu Dec 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- Kmail crash on exit (kde#289693)

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Fri Dec 16 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-2
- kio_imap APPEND omits message size without flags (kde#289084)

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90

* Sat Nov 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-2
- kmail does not work with dovecot (#757295,kde#249992)

* Fri Nov 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Thu Oct 27 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-2
- pkgconfig-style deps
- "Mimetype tree is not a DAG!" errors + crashes when using SMI 0.91 (#749618)

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Fri Sep 02 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.0-1
- 4.7.0

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-2
- rebuild (boost)

* Fri Jul 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.95-1
- 4.6.95 (rc2)

* Tue Jun 28 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Mon Jun 27 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.80-2
- Requires: cyrus-sasl-plain

* Fri May 27 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.80-1
- 4.6.80 (beta1)
- add BR prison-devel

* Thu Apr 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-1
- 4.6.3

* Wed Apr 06 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.2-1
- 4.6.2

* Sat Feb 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0

* Thu Jan 20 2011 Rex Dieter <rdieter@fedoraproject.org> 4.5.95-2
- avoid overlapping memcpy in kio_imap

* Wed Jan 05 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1
- 4.5.90 (4.6rc1)

* Wed Dec 08 2010 Thomas Janssen <thomasj@fedoraproject.org> 4.5.85-2
- respun upstream tarball

* Sat Dec 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 4.5.85-1
- 4.5.85 (4.6beta2)

* Tue Nov 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-2
- respun tarball

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Fri Nov 12 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.3-2
- fix Austrian cultural/regional/religious November holidays (kde#245123)

* Sun Oct 31 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Fri Oct 01 2010 Rex Dieter <rdieter@fedoraproject.org> -  4.5.2-1
- 4.5.2

* Fri Aug 27 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.5.1-1
- 4.5.1

* Mon Aug 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.0-3
- apidocs: remove (executable) installdox

* Mon Aug 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.0-2
- akonadi_version_min 1.4.0

* Tue Aug 03 2010 Than Ngo <than@redhat.com> - 4.5.0-1
- 4.5.0

* Tue Jul 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-2
- rebuild (boost)

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Mon Jun 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.90-2
- kdepimlibs pulling in kdepimlibs-akonadi (#608863)

* Fri Jun 25 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.90-1
- 4.5 RC1 (4.4.90)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- 4.5 Beta 1 (4.4.80)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.2-1
- 4.4.2

* Tue Mar 02 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.1-2
- tarball respin

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Tue Feb 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-2
- akonadi_version 1.3.1

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Wed Jan 20 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Sat Jan 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-4 
- rebuild (boost)

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-3
- revive -akonadi

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-2
- akonadi_ver 1.2.90

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- 4.3.90 (4.4 rc1)
- drop -akonadi subpkg

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- 4.3.85 (4.4 beta2)
- tighten deps

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.3.80-2
- Repositioning the KDE Brand (#547361)

* Tue Dec  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)

* Sat Nov 21 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- Update to 4.3.75 snapshot

* Wed Nov 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-3
- rebuild (qt-4.6.0-rc1, fc13+)

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-2
- rhel cleanup, remove Fedora<=9 conditionals

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Tue Aug 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-2
- akonadi_version 1.2.0

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Wed Jul 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.98-3
- Conflicts: kdepim < 4.2.90

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Thu Jul 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.96-2
- License: LGPLv2+

* Sat Jul 11 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Thu Jul 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.95-3
- akonadi_version 1.1.95

* Mon Jun 29 2009 Than Ngo <than@redhat.com> - 4.2.95-2
- respin

* Thu Jun 25 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3 RC1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Sun May 24 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-2
- (min) akonadi_version 1.1.85

* Mon May 11 2009 Than Ngo <than@redhat.com> 4.2.85-1
- 4.2.85

* Mon Apr 06 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.2-3
- fix libkcal devel symlink hack

* Thu Apr 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-2
- -apidocs noarch (f10+)
- package %%_kde4_appsdir/akonadi-kde only once

* Tue Mar 31 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Mon Mar 09 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.1-4
- disable CMake debugging, #475876 should be fixed now

* Tue Mar 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-2
- avoid libkcal conflict with kdepim3

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Than Ngo <than@redhat.com> - 4.2.0-4
- enable akonadi subpkg

* Mon Feb 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-3
- include toggle for -akonadi subpkg (not enabled)
- Provides: -akonadi

* Mon Feb 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-2
- multilib conflicts (#485659)
- kde4/devel symlinks: blacklist only known conflicts

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0
- exclude kdepimlibs-apidocs from main pkg

* Thu Jan 08 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.96-2
- fix build on Fedora 10 (cmake < 2.6.3 seems to have a different
  behaviour here)

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Wed Dec 17 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-2
- versioned akonadi(-devel) deps

* Thu Dec 11 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.85-1
- KDE 4.2beta2

* Wed Dec 10 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.82-2
- add --debug-output to our cmake call, that should fix a reproducible
  bug with cmake and ppc builds (this work-around should be
  removed anyway)

* Tue Dec 09 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.82-1
- 4.1.82

* Tue Dec 02 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.80-3
- -devel: Requires: libical-devel

* Thu Nov 20 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged

* Thu Nov 20 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-1
- 4.1.80
- BR cmake 2.6
- make install/fast

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Sat Nov 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-4
- turn off system libical for now, crashes KOrganizer (#469228)

* Tue Oct 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-3
- build against the system libical (F10+ only for now)

* Sun Sep 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Fri Sep 05 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.1-2
- invitations crasher/regression (kde #170203, rh#462103)

* Thu Aug 28 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Tue Aug 05 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-2
- -devel: Requires: boost-devel

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Thu Jul 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Tue Jun 24 2008 Than Ngo <than@redhat.com> 4.0.83-2
- respun

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Sat Jun 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Mon May 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-2
- add BR akonadi-devel
- update file list

* Fri May 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-1
- update to 4.0.72 (4.1 alpha 1)

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild for NDEBUG and _kde4_libexecdir

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3
- -apidocs: Drop Requires: %%name
- include noarch build hooks (not enabled)

* Thu Mar 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-2
- build apidocs and put them into an -apidocs subpackage (can be turned off)
- BR doxygen, graphviz and qt4-doc when building apidocs

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Wed Jan 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- don't delete kconf_update script, it has been fixed to do the right thing

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-1
- 4.0.1

* Mon Jan 07 2008 Than Ngo <than@redhat.com> 4.0.0-1
- 4.0.0
