
## nepomuk support only for kde < 4.13
%if 0%{?fedora} < 20
%define nepomuk 1
%endif

Name:		rekonq
Version: 	2.4.2
Release:	28%{?dist}
Summary:	KDE browser based on QtWebkit

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://rekonq.kde.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

## upstream patches
Patch101: 0001-Get-sure-fast-typing-work.patch
Patch102: 0002-Fix-rekonqui.rc.patch
Patch104: 0004-Allows-to-build-without-Soprano-and-Nepomuk.patch

BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	kdelibs4-devel
BuildRequires:	kdelibs4-webkit-devel
%if 0%{?nepomuk}
BuildRequires:	nepomuk-core-devel
%endif
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(qoauth)
BuildRequires:	pkgconfig(QtGui) pkgconfig(QtNetwork)

Requires: kde-runtime%{?_kde4_version: >= %{_kde4_version}}
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
rekonq is a KDE browser based on QtWebkit. Its code is based on Nokia 
QtDemoBrowser, just like Arora. It's implementation is going to embrace 
KDE technologies to have a full-featured KDE web browser.


%prep
%setup -q

%patch -P101 -p1 -b .0001
%patch -P102 -p1 -b .0002
%patch -P104 -p1 -b .0004



%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  %{?nepomuk:-DWITH_NEPOMUK:BOOL=ON} \
  ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-kde --all-name

# Don't install own fonts
rm -rfv %{buildroot}%{_kde4_appsdir}/rekonq/fonts


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kde4/rekonq.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog TODO
%{_kde4_bindir}/rekonq
%{_kde4_libdir}/libkdeinit4_rekonq.so
%{_kde4_sharedir}/config.kcfg/rekonq.kcfg
%{_kde4_sharedir}/applications/kde4/rekonq.desktop
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_appsdir}/rekonq/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.2-27
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 2.4.2-4
- BR: kdelibs4-webkit-devel

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.4.2-2
- pull in latest upstream patches
- explictly disable nepomuk support (where kde-4.13 is present)

* Sun Jan 12 2014 Jan Grulich <jgrulich@redhat.com> 2.4.2-1
- 2.4.2

* Sat Nov 16 2013 Jan Grulich <jgrulich@redhat.com> 2.4.0-1
- 2.4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 01 2013 Jan Grulich <jgrulich@redhat.com> 2.3.2-1
- 2.3.2

* Sun Jun 23 2013 Jan Grulich <jgrulich@redhat.com> 2.3.1-1
- 2.3.1

* Tue Jun 4 2013 Jan Grulich <jgrulich@redhat.com> 2.3.0-2
- #970690 - nunito font in private directory

* Sun Apr 28 2013 Jan Grulich <jgrulich@redhat.com> 2.3.0-1
- 2.3.0

* Fri Mar 08 2013 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-2
- +nepomuk support (BR: nepomuk-core-devel)
- don't list HTML docs twice (let %%find_lang handle it)

* Fri Mar 08 2013 Jan Grulich <jgrulich@redhat.com> 2.2.1-1
- 2.2.1

* Thu Feb 28 2013 Jan Grulich <jgrulich@redhat.com> 2.2-1
- 2.2

* Sun Jan 27 2013 Jan Grulich <jgrulich@redhat.com> 2.1-1
- 2.1

* Sat Dec 29 2012 Jan Grulich <jgrulich@redhat.com> 2.0-1
- 2.0

* Mon Nov 05 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3-1
- 1.3

* Sat Oct 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2-1
- 1.2

* Tue Aug 28 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1-1
- rekonq-1.1
- .spec cleanup

* Sat Jul 21 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0-1
- rekonq-1.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Mon Apr 02 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Sun Mar 04 2012 Jaroslav Reznik <jreznik@redhat.com> - 0.9.0.1-1
- Update to 0.9.0-1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 19 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- rekonq 0.8.0
- BR: pkgconfig(QtWebKit), s/kdebase-workspace-devel/kdelibs4-devel/
- Requires: s/kdebase-workspace/kdebase-runtime/
- add tighter, versioned qt runtime dep

* Thu Jul 28 2011 Eelko Berkenpies <fedora@berkenpi.es> 0.7.0-1
- new upstream version
- dropped rekonq_fix_CVE-2010-2536.patch, fixed upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.6.1-1
- rekonq 0.6.1

* Wed Sep 29 2010 jkeating - 0.6.0-2
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.6.0-1
- rekonq 0.6.0

* Tue Aug 03 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.5.0-2
- added patch to fix CVE-2010-2536 (patch by Eelko)
- fixes #620897

* Tue Jul 13 2010 Eelko Berkenpies <fedora@berkenpi.es> 0.5.0-1
- rekonq 0.5.0

* Thu Jun 17 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.95-1
- rekonq 0.4.95

* Wed Apr 07 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.0-1
- rekonq-0.4.0

* Wed Nov 25 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.3.0-2
- fix requirements

* Wed Nov 25 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.3.0-1
- new upstream version

* Mon Aug 31 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.2.0-3
- fix directory ownership in spec file

* Sat Aug 29 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.2.0-2
- fix build requirements in spec file

* Tue Aug 25 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.2.0-1
- version 0.2.0
- multiple spec file improvements

* Fri May 29 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.1.0-1
- version 0.1.0

* Mon Mar 23 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.0.4-2
- cleaning up spec file.

* Tue Mar 17 2009 Eelko Berkenpies <fedora@berkenpies.nl> 0.0.4-1
- Initial package.
