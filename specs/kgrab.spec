# Review Request:
# https://bugzilla.redhat.com/show_bug.cgi?id=432613

%define kdeversion 4.4.0

Name:           kgrab
Version:        0.1.1
Release:        54%{?dist}
Summary:        A screen grabbing utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://extragear.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/%{kdeversion}/src/extragear/%{name}-%{version}-kde%{kdeversion}.tar.bz2

BuildRequires:  kdelibs4-devel >= 4
BuildRequires:  kde-filesystem >= 4
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires: make

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description
kgrab is a screen grabbing utility for KDE.

%prep
%setup -qn %{name}-%{version}-kde%{kdeversion}


%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}


%install
%make_install -C %{_target_platform}

# validate desktop file
desktop-file-install --vendor ""                          \
        --dir %{buildroot}%{_datadir}/applications/kde4   \
        %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%find_lang %{name}



%files -f %{name}.lang
%license COPYING COPYING.DOC COPYING.LIB
%{_kde4_bindir}/kgrab
%{_datadir}/applications/kde4/kgrab.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kgrab.xml
%{_kde4_iconsdir}/hicolor/*/apps/kgrab.*
%{_kde4_appsdir}/kgrab/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.1-53
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-39
- .spec cleanup, use %%make_build %%make_install %%license

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-36
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.1-30
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 12 2010 Sebastian Vahl <svahl@fedoraproject.org> - 0.1.1-22
- 4.4.0
- drop kgrab-0.1.1-X11_libs.patch (already included)

* Tue Nov 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-21
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Thu Nov 05 2009 Sebastian Vahl <svahl@fedoraproject.org> - 0.1.1-20
- 4.3.3
- optimize scriptlets

* Tue Sep 01 2009 Sebastian Vahl <svahl@fedoraproject.org> - 0.1.1-19
- 4.3.1

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 0.1.1-18
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-16
- 4.2.4

* Tue May 12 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-15
- 4.2.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Than Ngo <than@redhat.com> - 0.1.1-13
- 4.2.0

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.1-12
- rebuild for fixed kde-filesystem (macros.kde4) (get rid of rpaths)

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1.1-11
- Include /usr/share/kde4/apps/kgrab directory.

* Sat Oct 04 2008 Than Ngo <than@redhat.com> 0.1.1-10
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 0.1.1-9
- 4.1.1

* Thu Aug 28 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.1.1-8
- 4.1 (final)

* Mon May 26 2008 Than Ngo <than@redhat.com> 0.1.1-7.kde4.0.80
- 4.1 beta1

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-6
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-5
- rebuild for NDEBUG and _kde4_libexecdir

* Thu Feb 14 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-4
- remove reference to KDE 4 in summary and description

* Wed Feb 13 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-3
- added Requires: kdelibs4 >= 4
- added Requires: oxygen-icon-theme

* Wed Feb 13 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-2
- added requires xdg-utils, kde4-macros(api)

* Wed Feb 13 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-1
- initial version
