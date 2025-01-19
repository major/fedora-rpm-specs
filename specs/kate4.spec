
%define obsoletes_evr 4.14.3-10

## We currently only build/ship -part
## Other bits are replaced by kf5 kate-14.12+

Name:    kate4
Summary: Advanced Text Editor for KDE4
Version: 4.14.3
Release: 38%{?dist}

# kwrite LGPLv2+
# kate: app LGPLv2, plugins, LGPLv2 and LGPLv2+ and GPLv2+
# ktexteditor: LGPLv2
# katepart: LGPLv2
# Automatically converted from old format: LGPLv2 and LGPLv2+ and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:     https://projects.kde.org/projects/kde/applications/kate
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/kate-%{version}.tar.xz

## upstreamable patches
# fix gcc7 FTBFS
Patch100: kate-4.14.3-gcc7.patch

BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: make

%description
%{summary}.

%package part
Summary: KDE4 Kate kpart plugin
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
# when split occurred
Conflicts: kdelibs < 6:4.6.95-10
# katesyntaxhighlightingrc conflicts with kdelibs3, see http://bugzilla.redhat.com/883529
Conflicts: kdelibs3 < 3.5.10-40
Obsoletes: kate-libs < %{obsoletes_evr}
## nothing else should depend on -libs, so skip Provides for now -- rex
#Provides:  kate-libs = %{version}-%{release}
#Provides:  kate-libs%{?_isa} = %{version}-%{release}
Obsoletes: kate-part < %{obsoletes_evr}
Provides:  kate-part = %{version}-%{release}
Provides:  kate-part%{?_isa} = %{version}-%{release}
%description part
%{summary}, needed by some KDE4 applications.


%prep
%setup -q -n kate-%{version}

%patch -P100 -p1 -b .gcc7


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}/part
%make_build -C %{_target_platform}/addons/ktexteditor


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/part
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/addons/ktexteditor

## unpackaged files
rm -fv %{buildroot}%{_kde4_libdir}/libkatepartinterfaces.so


%ldconfig_scriptlets part

%files part
%doc COPYING.LIB
%doc part/INDENTATION part/README*
%{_kde4_libdir}/kde4/katepart.so
%{_kde4_libdir}/kde4/ktexteditor_*.so
%{_kde4_libdir}/libkatepartinterfaces.so.4*
%{_kde4_appsdir}/katepart/
%{_kde4_appsdir}/ktexteditor_*/
%{_kde4_configdir}/katemoderc
%{_kde4_configdir}/kateschemarc
%{_kde4_configdir}/katesyntaxhighlightingrc
%{_kde4_configdir}/ktexteditor_codesnippets_core.knsrc
%{_kde4_datadir}/kde4/services/katepart.desktop
%{_kde4_datadir}/kde4/services/ktexteditor_*.desktop
%{_kde4_iconsdir}/hicolor/*/apps/ktexteditor*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.14.3-37
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-22
- use %%make_build %%ldconfig_scriptlets

*  Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.3-20
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-17
- fix gcc7 FTBFS (#1423800)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 4.14.3-14
- Added ktexteditor/katepart plugins (#1226071)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.14.3-13
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-12
- -part: Obsoletes: kate-libs (fix upgrade path)

* Wed Feb 25 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-11
- improve pkg %%summary, %%description

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-10
- rename to kate4

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-4
- kwrite: use %%{?kde_runtime_requires}

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-3
- -part: Provides: kate4-part

* Fri Jan 16 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-2
- kde-applications cleanups

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Sun Aug 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-5
- kwrite needs update-desktop-database scriptlet too

* Sun Aug 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-4
- fix scriptlets (need update-desktop-database instead of update-mime-database)

* Fri Aug 08 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-3
- re-enable -pate (hopefully pykde4 is fixed for real this time)

* Fri Aug 08 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-2
- disable -pate, FTBFS against latest pykde4 (dont know exactly why yet...)

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 30 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.2-2
- BR: qtwebkit ...

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sat Mar 22 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Fri Mar 07 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.3-2
- implement upstreamable PYTHON_LIBRARY_REALPATH fix (#1050944)

* Sat Mar 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.0-2
- workaround libpython dlopen failure (#1050944)

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Mon Dec 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.97-2
- (re)enable pate, add dependencies (#1028819)

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90, omit -pate (bootstrap)

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-2
- kate: pate(python) plugins not built/packaged (#922280)

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Wed Oct 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.2-2
- respin tarball

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Tue Sep 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Thu Apr 04 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-2
- -libs: Obsoletes: kdesdk-libs (instead of Conflicts)

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Tue Mar 19 2013 Than Ngo <than@redhat.com> - 4.10.1-3
- backport to fix python indentation mode

* Tue Mar 19 2013 Than Ngo <than@redhat.com> - 4.10.1-2
- Fix documentation multilib conflict in index.cache

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-2
- kate has a file conflict with kdelibs3 (#883529)

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
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

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-2
- respin

* Sat May 26 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-2
- s/kdebase-runtime/kde-runtime/

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Radek Novacek <rnovacek@redhat.com> - 4.8.1-1
- 4.8.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for c++ ABI breakage

* Fri Jan 20 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90

* Thu Nov 24 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 07 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Thu Jul 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-2
- -part: move %%_kde4_appsdir/katepart/ here

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.0-1
- 4.7.0

* Mon Jul 18 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-1
- first try

