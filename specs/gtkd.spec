# debug info seem not works with D compiler
%global debug_package %{nil}

%global sover 0

Name:           gtkd
Version:        3.10.0
Release:        14%{?dist}
Summary:        D binding and OO wrapper of GTK+

License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/GtkD/
Source0:        https://github.com/gtkd-developers/GtkD/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{ldc_arches}

BuildRequires:  ldc
# Explicit require since gtkd use dlopen internally so rpm can't detect this.
Requires:       atk%{?_isa}
Requires:       cairo%{?_isa}
Requires:       gdk-pixbuf2%{?_isa}
Requires:       gstreamer1%{?_isa}
Requires:       gstreamer1-plugins-base%{?_isa}
Requires:       gtk3%{?_isa}
Requires:       gtksourceview4%{?_isa}
Requires:       libcurl%{?_isa}
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
Requires:       libpeas1%{?_isa}
Requires:       libpeas1-gtk%{?_isa}
%else
Requires:       libpeas%{?_isa}
Requires:       libpeas-gtk%{?_isa}
%endif
Requires:       librsvg2%{?_isa}
Requires:       mesa-libGL%{?_isa}
Requires:       mesa-libGLU%{?_isa}
Requires:       pango%{?_isa}
Requires:       vte291%{?_isa}

%description
GTK+ is a highly usable, feature rich toolkit for creating graphical user
interfaces which boasts cross platform compatibility and an easy to use API.

%description -l fr
GTK+ est très utilisable, cet outil contient de nombreuses fonctionnalités
permettant de créer des interfaces graphiques multi-plateforme.
De plus, gtkd fournit une API facile à utiliser.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The gtkd-devel package contains header files for developing gtkd
applications.

%description devel -l fr
Le paquet gtkd-devel contient les fichiers d'entêtes pour développer
des applications utilisant gtkd.

%package geany-tags
Summary:        Support for enable autocompletion in geany
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  geany
BuildRequires:  make
Requires:       geany

%description geany-tags
Enable autocompletion for gtkd library in geany (IDE)

%description -l fr geany-tags
Active l'autocompletion pour pour la bibliothèque gtkd dans geany (IDE)

%prep
%autosetup -n GtkD-%{version} -p1

# Fedora's pkgconfig for gtksourceview is 4, not 4.0
sed -i 's/gtksourceview-4.0/gtksourceview-4/g' GNUmakefile

# temp geany config directory for allow geany to generate tags
mkdir geany_config

%build
make %{?_smp_mflags} DC=ldc2 libdir=%{?_lib} DCFLAGS="%{_d_optflags}" LDFLAGS="" \
     shared-gtkdgl \
     shared-libs
# generate geany tags
geany -c geany_config -g gtkd.d.tags $(find src* -name "*.d")

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{?_lib} \
     install-shared-gtkdgl install-headers-gtkdgl \
     install-shared install-headers

# geany tags
mkdir -p %{buildroot}%{_datadir}/geany/tags/
install -m0644 gtkd.d.tags %{buildroot}%{_datadir}/geany/tags/

%check
make %{?_smp_mflags} DC=ldc2 libdir=%{?_lib} DCFLAGS="%{_d_optflags}" LDFLAGS="" test

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libgstreamerd-3.so.%{sover}*
%{_libdir}/libgtkd-3.so.%{sover}*
%{_libdir}/libgtkdgl-3.so.%{sover}*
%{_libdir}/libgtkdsv-3.so.%{sover}*
%{_libdir}/libpeasd-3.so.%{sover}*
%{_libdir}/libvted-3.so.%{sover}*

%files devel
%{_d_includedir}/gtkd-3/
%{_libdir}/libgstreamerd-3.so
%{_libdir}/libgtkd-3.so
%{_libdir}/libgtkdgl-3.so
%{_libdir}/libgtkdsv-3.so
%{_libdir}/libpeasd-3.so
%{_libdir}/libvted-3.so
%{_libdir}/pkgconfig/gstreamerd-3.pc
%{_libdir}/pkgconfig/gtkd-3.pc
%{_libdir}/pkgconfig/gtkdgl-3.pc
%{_libdir}/pkgconfig/gtkdsv-3.pc
%{_libdir}/pkgconfig/peasd-3.pc
%{_libdir}/pkgconfig/vted-3.pc

%files geany-tags
%{_datadir}/geany/tags/gtkd.d.tags

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 3.10.0-13
- Rebuilt for ldc 1.40

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 3.10.0-12
- Rebuilt for ldc 1.39

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Kalev Lember <klember@redhat.com> - 3.10.0-8
- Require libpeas1 compat package rather than libpeas in F39+

* Tue Oct 17 2023 Kalev Lember <klember@redhat.com> - 3.10.0-7
- Rebuilt for ldc 1.35

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 3.10.0-6
- Rebuilt for ldc 1.33

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Kalev Lember <klember@redhat.com> - 3.10.0-4
- Rebuilt for ldc 1.32

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Kalev Lember <klember@redhat.com> - 3.10.0-2
- Rebuild (#2134875)

* Sat Nov 19 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.10.0-1
- Update to 3.10.0

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 3.9.0-10
- Rebuilt for ldc 1.30

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Kalev Lember <klember@redhat.com> - 3.9.0-7
- Backport an upstream patch to fix the build with ldc 1.27

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 3.9.0-5
- Rebuilt for ldc 1.25

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Kalev Lember <klember@redhat.com> - 3.9.0-3
- Rebuilt for ldc 1.23

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 3.9.0-1
- Update to 3.9.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 3.8.5-5
- Rebuilt for ldc 1.15

* Sat Mar 30 2019 Kalev Lember <klember@redhat.com> - 3.8.5-4
- Add missing librsvg2 dep (#1694324)

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 3.8.5-3
- Rebuilt for ldc 1.14

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.8.5-1
- Update to 3.8.5

* Fri Jan 04 2019 Kalev Lember <klember@redhat.com> - 3.8.4-2
- Fix the version in .pc files

* Fri Jan 04 2019 Kalev Lember <klember@redhat.com> - 3.8.4-1
- Update to 3.8.4
- Drop ldconfig scriptlets

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 3.8.3-2
- Rebuilt for ldc 1.12

* Tue Aug 21 2018 Kalev Lember <klember@redhat.com> - 3.8.3-1
- Update to 3.8.3

* Tue Aug 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 3.8.2-4
- Rebuild for aarch64 enablement

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 3.8.2-2
- Rebuilt for ldc 1.11

* Wed May 16 2018 James Ye <jye836@gmail.com> - 3.8.2-1
- Update to 3.8.2

* Mon Mar 19 2018 Kalev Lember <klember@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 3.7.3-3
- Rebuilt for ldc 1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Kalev Lember <klember@redhat.com> - 3.7.3-1
- Update to 3.7.3

* Thu Oct 12 2017 Kalev Lember <klember@redhat.com> - 3.6.6-2
- Minor packaging cleanup

* Wed Oct 04 2017 Kalev Lember <klember@redhat.com> - 3.6.6-1
- Update to 3.6.6

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.6.5-4
- Rebuilt for ldc 1.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 3.6.5-1
- Update to 3.6.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Kalev Lember <klember@redhat.com> - 3.5.1-2
- Depend on libpeas-gtk now that it's split out in a subpackage

* Wed Jan 11 2017 Kalev Lember <klember@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Sat Jan 07 2017 Kalev Lember <klember@redhat.com> - 3.5.0-1
- Update to 3.5.0

* Sun Jan 01 2017 Kalev Lember <klember@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Thu Dec 29 2016 Kalev Lember <klember@redhat.com> - 3.4.0-1
- Update to 3.4.0
- Build gstreamer1 and libpeas bindings
- Tighten dependencies with the _isa macro

* Wed Nov 30 2016 Kalev Lember <klember@redhat.com> - 3.3.1-4
- Rebuilt for new ldc compiler

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 3.3.1-3
- Use new ldc_arches macro

* Wed Oct 26 2016 Kalev Lember <klember@redhat.com> - 3.3.1-2
- Build vte bindings
- Use license macro
- Don't set group tags

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 3.3.1-1
- Update to 3.3.1
- Enable arm architecture now that ldc is available there

* Tue Jul 19 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.2-3
- Remove bogus glade3 dependency (#1294369)

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.2.2-2
- Fix Requires

* Sat Feb 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Jonathan MERCIER <bioinfornatics@gmail.com> - 3.2.1-57
- Rebuild with latest ldc release

* Tue Jan 05 2016 Jonathan MERCIER <bioinfornatics@gmail.com> - 3.2.1-56
- Fix several deprecated requires
- update to latest release 3.2.1

* Sun Sep 06 2015 Jonathan MERCIER <bioinfornatics@gmail.com> - 3.1.4-52
- update to latest release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 bioinfornatics - 2.4.2-50
- Update to latest revision

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 2.3.2-47
- update to latest rev

* Mon Mar 10 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 2.0.0-46.20140301gitaf01da8
- Fix requires
* Sun Mar 09 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 2.0.0-45.20140301gitaf01da8
- Update to latest rev

* Mon Oct 28 2013 Jonathan MERCIER <bioinfornatics@gmail.com> - 2.0.0-44.20131026git33f6aeb
- Update to rev 33f6aeb

* Thu Oct 24 2013 Jonathan MERCIER <bioinfornatics@gmail.com> - 2.0.0-43.20131022git3948a30
- Update to rev 3948a30

* Wed Jun 26 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-42.20130624gitdb5921d
- update url

* Wed Jun 26 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-41.20130624gitdb5921d
- update url

* Mon Jun 24 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-40.20130624gitdb5921d
- Update to rev db5921d

* Sun Jun 23 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-39.20130619git7e95380
- Update to rev 7e95380

* Sun Jun 09 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-38.20130526git5073a70
- Update to rev 5073a70

* Fri May 24 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-37.20130519gitc19a533
- Update to rev c19a533

* Sat May 18 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 2.0.0-36.20130508git516693e
- rebuild

* Fri May 17 2013  <bioinfornatics at fedoraproject dot org> - 2.0.0-35.20130508git516693e
- Update to rev 516693e

* Thu May 16 2013  <bioinfornatics at fedoraproject dot org> - 2.0.0-34.20130508git516693e
- Update to rev 516693e

* Thu May 09 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-33.20130508git516693e
- Update to rev 516693e

* Wed May 08 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-32.20130508gitd53e7af
- Update to rev d53e7af

* Tue May 07 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-31.20130507gitc6f7e92
- Update to rev c6f7e92

* Tue May 07 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-30.20130506git4c3922d
- Update to rev 4c3922d

* Wed Oct 03 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-29.20120815git9ae9181
- rebuild dmdfe 2.060

* Sun Aug 12 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-28.20120603gitcb35d25
- temprorally disable check section

* Sun Aug 12 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-27.20120603gitcb35d25
- Update to lastest revision cb35d25

* Wed Jun 06 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-26.20120530gitf45bb5b
- update to latest revision
- build with dmdfe 2.059

* Sat Mar 17 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-25.20120227git0c468d2
- fix macro in comment

* Thu Mar 15 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-24.20120227git0c468d2
- latest ldc fix soname issue, the use ldc instead of gcc for this

* Mon Feb 27 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-23.20120227git0c468d2
- add libglade2 as require
- update to latest revision 0c468d2

* Thu Feb 23 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-22.20120219git2cfd194
- Fix license

* Mon Feb 20 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-21.20120219git2cfd194
- source move to github
- fix license
- update to latest git rev

* Tue Feb 14 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-20.20120208svn933
- Update to latest svn rev 933

* Sun Feb 05 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-19.20120205svn932
- Update to latest svn rev 932

* Sat Feb 04 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-18.20120204svn928
- Update to latest svn rev 928

* Fri Feb 03 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-17.20120201svn927
- update to rev svn 927

* Tue Jan 31 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-16.20120130svn924
- update to latest svn rev 924

* Sat Jan 28 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-15.20120113svn920
- Enable shared lib

* Thu Jan 19 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-14.20120113svn920
- Remove %%file devel section

* Thu Jan 19 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.0.0-13.20120113svn920
- Do not build as shared lib do not works yet
- Remove 'it is a' from Summary
- gtkd load shared lib at runtime with dlopen then add corresponding requires
- Change gtkd code source for use versioned lib

* Mon Jan 16 2012 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-12.20120113svn920
- remove require devel from non devel (sub)package
- remove require gtk2-devel from -devel
- apply %%post and %%postun on main package

* Fri Jan 13 2012 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-11.20120113svn920
- update to latest release who fix a problem around soname

* Fri Jan 13 2012 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-10.20120113svn919
- update to latest release who he apply my patch

* Tue Jan 10 2012 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-9.20120111svn915
- update to latest release
- fix fsf adress
- fix soname
- add devel package
- little change in french description
- add geany tag and devhelp supackage to noarch

* Sun Jan 8 2012 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-8.201110243svn906
- prefix python script by python command

* Sun Dec 11 2011 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-7.201110243svn906
- remove %%defattr and Group section
- generate devhelp book in  %%build section

* Fri Dec 9 2011  Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-6.201110243svn906
- Add doc for devhelp
- Add tag for geany

* Mon Oct 24 2011 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-5.201110243svn906
- Update to release 906

* Mon Sep 19 2011 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-4.20110915svn897
- Update to release 897

* Mon Aug 02 2010 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-3.20100720svn797
- fix gtkd spec

* Mon Aug 02 2010 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-2.20100720svn797
- Update to release 797

* Sun Jul 04 2010 Jonathan MERCIER <bioinfornatics at gmail.com> 2.0.0-1.20100407svn796
- Initial release
