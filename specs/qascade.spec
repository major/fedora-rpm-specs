Name:           qascade
Version:        0.1
Release:        43%{?dist}
Summary:        Classic puzzle game

License:        GPL-2.0-or-later
URL:            http://www.bitsnpieces.org.uk/qascade/
Source0:        http://www.bitsnpieces.org.uk/qascade/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-dblsep.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt3-devel
BuildRequires:  desktop-file-utils

%description
Qascade is a port of the simple yet addictive and enjoyable puzzle
game that came with the Psion Revo PDA.


%prep
%setup -q
%patch -P0


%build
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
qmake INSTALL_ROOT=$RPM_BUILD_ROOT qascade.pro
perl -pi -e 's|^(C(XX)?FLAGS\s*=.*)$|$1 \$(RPM_OPT_FLAGS)|g' Makefile
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%makeinstall
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{SOURCE1}
install -D -p -m 644 %{name}.hscr \
  $RPM_BUILD_ROOT%{_localstatedir}/lib/games/%{name}.hscr
install -D -p -m 644 blue.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/qascade.png


%files
%doc *.htm
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/qascade.png
%attr(0664,games,games) %config(noreplace) %{_localstatedir}/lib/games/%{name}*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.1-38
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-26
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-20
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.1-16
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 24 2008 Jon Ciesla <limb@jcomserv.net> - 0.1-10
- qt3 rename BR fix.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 0.1-9
- GCC 4.3 rebuild.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-8
- License tag correction.

* Fri Mar 02 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-7
- Corrected desktop categories.

* Fri Mar 02 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-6
- Rebuild for FC-6 and devel.  Will need cleanup but should work.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1-5
- Rebuild.

* Thu Nov  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1-4
- Clean up build dependencies.
- Drop workaround for #150528.
- Install icon to %%{_datadir}/icons/hicolor, update GTK icon cache.

* Fri Mar 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1-3
- Add workaround for UIC segfault (#150528).
- Various cosmetic desktop entry and UI tweaks.

* Sun Aug 24 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1-0.fdr.2
- Fix URL.
- Ensure that QTDIR is also defined in %%install.

* Sun Aug  3 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1-0.fdr.1
- First build.

