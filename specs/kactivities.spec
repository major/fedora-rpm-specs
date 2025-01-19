
## include -nepomuk subpkg support
%if 0%{?fedora} < 24
%define nepomuk 1
%endif

## favor kf5-kactivities
%if 0%{?fedora} > 21
%define plasma5 1
%endif

Name:    kactivities
Summary: API for using and interacting with Activities 
Version: 4.13.3
Release: 43%{?dist}

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdelibs/kactivities
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: kdelibs4-devel >= %{version}
%if ! 0%{?nepomuk}
Obsoletes: kactivities-nepomuk < 4.13.3-20
%endif

%if 0%{?rhel} == 6
# see http://people.centos.org/tru/devtools-1.1/
BuildRequires: devtoolset-1.1-gcc-c++
%global devtoolset 1
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake

# libkactivities moved from kdelibs, but turns out there's no actual conflicts
# kactivitymanagerd moved here from kde-runtime 
Conflicts: kdebase-runtime < 4.7.3-10

Obsoletes: libkactivities < 6.1-100
Provides:  libkactivities = 6.2-1

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
API for using and interacting with Activities as a consumer, 
application adding information to them or as an activity manager.

%package libs
Summary: Runtime libraries for %{name}
Requires: kdelibs4%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
# upgrade path, -libs was originally split out in 4.13.1-3, but bumping
# due to one irc user who somehow still had 4.13.3-1.i686 (on x86_64)
# bumped again to -7 for bug#1172523
Obsoletes: kactivities < 4.13.3-7
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Obsoletes: libkactivities-devel < 6.1-100
Provides:  libkactivities-devel = 6.2-1
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if ! 0%{?nepomuk}
Obsoletes: kactivities-nepomuk-devel < 4.13.3-20
%endif
Requires: kdelibs4-devel
%description devel
%{summary}.

%if 0%{?nepomuk}
%package nepomuk
Summary: KActivities nepomuk support
BuildRequires: nepomuk-core-devel >= %{version}
BuildRequires: pkgconfig(soprano)
BuildRequires: make
# upgrade path
Obsoletes: kactivities < 4.13.0-2
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# not sure if an explicit dep is needed or worth it -- rex
#Requires: nepomuk-core%{?_isa} >= %{version}
%description nepomuk
%{summary}.

%package nepomuk-devel
Summary: KActivities nepomuk development files
Obsoletes: kactivities-devel < 4.13.3-2
Requires: %{name}-nepomuk%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description nepomuk-devel
%{summary}.
%endif


%prep
%setup -q 


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}

%if 0%{?devtoolset:1}
# build missing pieces with separate compiler
PATH=`scl enable devtoolset-1.1 'echo "$PATH"'`; export PATH

CXXFLAGS=`echo $RPM_OPT_FLAGS | sed 's|-g |-gdwarf-3 -gstrict-dwarf |g'`

mkdir %{_target_platform}-devtoolset
pushd %{_target_platform}-devtoolset
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}-devtoolset/src/service
%make_build -C %{_target_platform}-devtoolset/src/workspace
%endif


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%if 0%{?devtoolset:1}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-devtoolset/src/service
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-devtoolset/src/workspace
%endif

## unpackaged files
%if ! 0%{?nepomuk}
rm -rfv %{buildroot}%{_kde4_datadir}/ontology/kde/
%endif
%if 0%{?plasma5}
rm -fv %{buildroot}%{_kde4_bindir}/kactivitymanagerd
rm -fv %{buildroot}%{_kde4_libdir}/kde4/activitymanager_plugin_{activityranking,globalshortcuts,slc,sqlite,virtualdesktopswitch}.so
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/activitymanager-plugin-{activityranking,globalshortcuts,slc,sqlite,virtualdesktopswitch}.desktop
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/kactivitymanagerd.desktop
rm -fv %{buildroot}%{_kde4_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%endif


%if ! 0%{?plasma5}
%files
%{_kde4_bindir}/kactivitymanagerd
%{_kde4_libdir}/kde4/activitymanager_plugin_activityranking.so
%{_kde4_libdir}/kde4/activitymanager_plugin_globalshortcuts.so
%{_kde4_libdir}/kde4/activitymanager_plugin_slc.so
%{_kde4_libdir}/kde4/activitymanager_plugin_sqlite.so
%{_kde4_libdir}/kde4/activitymanager_plugin_virtualdesktopswitch.so
%{_kde4_datadir}/kde4/services/activitymanager-plugin-activityranking.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-globalshortcuts.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-sqlite.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-virtualdesktopswitch.desktop
%{_kde4_datadir}/kde4/services/kactivitymanagerd.desktop
%{_kde4_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%endif

%ldconfig_scriptlets libs

%files libs
%{_kde4_libdir}/libkactivities.so.6*
%{_kde4_libdir}/kde4/kcm_activities.so
%{_kde4_datadir}/kde4/services/kcm_activities.desktop
%{_kde4_appsdir}/activitymanager/

%files devel
%{_kde4_libdir}/libkactivities.so
%{_kde4_libdir}/cmake/KActivities/
%{_kde4_libdir}/pkgconfig/libkactivities.pc
%{_kde4_includedir}/KDE/KActivities/
%{_kde4_includedir}/kactivities/

%if 0%{?nepomuk}
%ldconfig_scriptlets nepomuk

%files nepomuk
%{_kde4_libdir}/kde4/kio_activities.so
%{_kde4_libdir}/libkactivities-models.so.1*
%{_kde4_libdir}/kde4/activitymanager_plugin_nepomuk.so
%{_kde4_libdir}/kde4/kactivitymanagerd_fileitem_linking_plugin.so
%{_kde4_datadir}/kde4/services/activities.protocol
%{_kde4_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_kde4_datadir}/kde4/services/kactivitymanagerd_fileitem_linking_plugin.desktop
%{_kde4_datadir}/ontology/kde/
%dir %{_kde4_libdir}/kde4/imports/org/kde
%{_kde4_libdir}/kde4/imports/org/kde/activities

%files nepomuk-devel
%{_kde4_libdir}/libkactivities-models.so
%{_kde4_libdir}/cmake/KActivities-Models/
%{_kde4_libdir}/pkgconfig/libkactivities-models.pc
%{_kde4_includedir}/kactivities-models/
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.13.3-42
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-32
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-26
- use %%make_build %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.3-24
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-20
- disable nepomuk support f24+

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-9
- omit kactivities base pkg where plasma5 is present (#1226502)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.13.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-7
- -libs: include qml stuff here (#1172523)

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-6
- -libs: bump Obsoletes: kactivities ...

* Sat Aug 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-5
- -libs: drop Requires: kactivities
- Provides: libkactivities = 6.2

* Thu Aug 21 2014 Daniel Vrátil <dvratil@redhat.com> - 4.13.3-4
- Move KCM to -libs so that we can configure activities even when running kf5-kactivities

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-2
- -nepomuk-devel subpkg

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-3
- -libs subpkg

* Tue May 13 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-2
- -nepomuk subpkg instead (still needed by plasma-mobile, at least)

* Sat May 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-1
- 4.13.1

* Mon Apr 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.0-2
- drop nepomuk support

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Thu Apr 03 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sat Mar 22 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Tue Mar 18 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.90-1
- 4.12.90

* Sat Mar 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

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

* Fri Nov 15 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Tue Sep 03 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Fri Apr 26 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-2
- kactivitymanager doesn't respond on SIGTERM when shutdown the system (kde#305353)

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Fri Jun 08 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-2
- respin

* Fri May 25 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Radek Novacek <rnovacek@redhat.com> 4.8.1-1
- 4.8.1

* Fri Jan 20 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org>  4.7.80-1
- libkactivities -> kactivities rename

* Fri Nov 04 2011 Rex Dieter <rdieter@fedoraproject.org>  6.1-2
- License: GPLv2+ and LGPLv2+

* Tue Oct 25 2011 Rex Dieter <rdieter@fedoraproject.org>  6.1-1
- first try

