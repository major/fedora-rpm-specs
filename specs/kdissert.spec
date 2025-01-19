# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name:           kdissert
Version:        1.0.7
Release:        43%{?dist}
Summary:        Mind-mapping tool

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://freehackers.org/~tnagy/kdissert/
Source0:        http://freehackers.org/~tnagy/%{name}/%{name}-%{version}.tar.bz2

Patch1: kdissert-1.0.7-gcc43.patch
Patch2: kdissert-1.0.7-dt.patch
Patch3: kdissert-1.0.7-dsolinking.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kdelibs3-devel
# waf: #!/usr/bin/python
BuildRequires:  python2-devel

%description
Kdissert is a mindmapping-like tool to help students to produce complicated 
documents very quickly and efficiently : presentations, dissertations, 
thesis, reports, etc. The concept is innovative : mindmaps produced using 
kdissert are processed to output near-ready-to-use documents. While 
targetted mostly at students, kdissert can also help teachers, decision 
makers, engineers and businessmen.


%prep 
%setup -q

%patch -P1 -p1 -b .gcc43
%patch -P2 -p1 -b .dt
%patch -P3 -p1 -b .dsolinking


%build

unset QTDIR || : ; . /etc/profile.d/qt.sh

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

%if 0%{?fedora} > 23
export CXXFLAGS="$CXXFLAGS -std=gnu++98"
%endif

%{__python2} ./waf configure \
    --prefix=%{_prefix} \
    --execprefix=%{_exec_prefix} \
    --datadir=%{_datadir} \
    --libdir=%{_libdir} \
    --nocache \
    --want-rpath=0

## HACK ALERT ##
## I can't get waf to find/use libkdeui otherwise.  wtf?  -- Rex
cat >> _build_/_cache_/default.cache.py << HACK
LIB_KDEUI = 'kdeui'
HACK

%{__python2} ./waf -v build
# %{?_smp_mflags}


%install
%{__python2} ./waf -v install --destdir=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk

desktop-file-install \
    --delete-original \
    --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications/kde \
    --remove-category X-KDE-More \
    --remove-category Utility \
    --add-category Office \
    $RPM_BUILD_ROOT%{_datadir}/applications/kde/kdissert.desktop

%find_lang %{name} --with-kde

# set execute permissions on the plugins so debuginfo extraction works
chmod +x $RPM_BUILD_ROOT%{_libdir}/kde3/*.so

# I *think* these are safe to omit, but haven't tested much -- Rex
#rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la


%files -f %{name}.lang
%doc AUTHORS README ROADMAP
%license COPYING
%{_bindir}/kdissert
%{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/kdissert/
%{_datadir}/apps/kdissertpart/
%{_datadir}/applications/kde/kdissert.desktop
# FIXME: add xdg mimetype too
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/kdissertpart.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/config.kcfg/kdissert.kcfg


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.7-42
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 1.0.7-35
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.7-27
- BR: python2-devel (for %%__python2 macro)
- BR: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.7-25
- .spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.7-19
- kdissert: FTBFS in rawhide (#1307687)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.7-16
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 26 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.7-9
- set execute permissions on the plugins so debuginfo extraction works

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.7-7
- hack around - FTBFS kdissert-1.0.7-6.fc12: ImplicitDSOLinking (#564927)
- optimize scriptlets

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 01 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.7-4
- fix rawhide build (#434133)
- d-f-i: fix double vendor
- Summary: s/for KDE// 
- License: GPLv2
- scriptlet deps

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.7-3
- Autorebuild for GCC 4.3

* Fri Aug 31 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.7-2
- Configuring belongs to the build phase.

* Sun Dec 17 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.0.7-1
- Upstream 1.0.7
- Fixes for updated waf script

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.0.6b-1
- Version 1.0.6b
- Move flags to configure stage
- We don't want rpath, thanks

* Sat Jul 22 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.0.6-1
- Version 1.0.6
- No longer using scons
- Rework to use the shipped-with waf
- BR gettext

* Mon Feb 13 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.0.5-1.1
- FC5 Rebuild.

* Fri Oct 28 2005 Konstantin Ryabitsev <icon@fedoraproject.org> 1.0.5-1
- Extras rebuild.

* Mon Oct 24 2005 Konstantin Ryabitsev <icon@fedoraproject.org> 1.0.5-0.4
- Update the tarball to match the upstream version.

* Fri Oct 21 2005 Konstantin Ryabitsev <icon@fedoraproject.org> 1.0.5-0.3
- Remove rpath from SConstruct

* Thu Oct 20 2005 Konstantin Ryabitsev <icon@fedoraproject.org> 1.0.5-0.2
- Do not install icon into pixmaps
- Use post/postun to handle icon cache

* Thu Oct 20 2005 Konstantin Ryabitsev <icon@fedoraproject.org> 1.0.5-0.1
- Initial packaging

