
%undefine __cmake_in_source_build

Name:    oxygen-gtk2
Summary: Oxygen GTK+2 theme
Version: 1.4.6
Release: 28%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/oxygen-gtk.git/
Source0: http://download.kde.org/stable/oxygen-gtk2/%{version}/src/%{name}-%{version}.tar.bz2

## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gtk2-devel

Obsoletes: oxygen-gtk < 1.2.1

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk-based and
qt-based applications running under KDE. A secondary objective is to also
have a stand-alone nice looking gtk theme that would behave well on other
Desktop Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this
attempt does not depend on Qt (via some Qt to Gtk conversion engine), 
nor does render the widget appearance via hard-coded pixmaps, which 
otherwise breaks every time some setting is changed in KDE.


%prep
%autosetup


%build
%cmake \
  -DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0

%cmake_build


%install
%cmake_install


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/oxygen-gtk-demo
%{_libdir}/gtk-2.0/*/engines/liboxygen-gtk.so
%{_datadir}/themes/oxygen-gtk/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.6-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.4.6-17
- FTBFS, use new cmake macros, use %%autosetup

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.4.6-10
- BR: gcc-c++, update URL, use %%license %%make_build

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Rex Dieter <rdieter@fedoraproject.org> 1.4.6-2
- Obsoletes: oxygen-gtk (f22+)

* Wed Oct 22 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.6-1
- oxygen-gtk2-1.4.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.5-1
- oxygen-gtk2-1.4.5

* Sat Mar  8 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.4-1
- oxygen-gtk2-1.4.4

* Fri Jan 24 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.3-1
- oxygen-gtk2-1.4.3

* Mon Jan 20 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.2-1
- oxygen-gtk2-1.4.2

* Tue Dec 10 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.1-1
- oxygen-gtk2-1.4.1

* Sat Aug 31 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.0-1
- oxygen-gtk2-1.4.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.4-1
- oxygen-gtk2-1.3.4

* Mon Apr 22 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.3-1
- oxygen-gtk2-1.3.3

* Wed Feb 13 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.2.1-1
- oxygen-gtk2-1.3.2.1

* Fri Feb 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-2
- Upgrade to oxygen-gtk2 1.3.2 is buggy (kde#314545)

* Wed Jan 30 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.2-1
- oxygen-gtk2-1.3.2

* Fri Oct  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.1-1
- oxygen-gtk2-1.3.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.0-1
- oxygen-gtk2-1.3.0

* Fri Jun 15 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.5-1
- oxygen-gtk2-1.2.5

* Mon May 14 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.4-1
- oxygen-gtk2-1.2.4

* Sat Apr 14 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.3-1
- oxygen-gtk2-1.2.3

* Sat Mar 24 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.2.1-1
- oxygen-gtk2-1.2.2-1
- drop badwindow patch

* Tue Mar 20 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.2-2
- fix crash in claws-mail (#804790, kde#295875)

* Mon Mar 12 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.2-1
- oxygen-gtk2-1.2.2
- drop BR: dbus-glib-devel

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.1-1
- oxygen-gtk2-1.2.1

* Mon Jan 23 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-3
- drop Obsoletes: oxygen-gtk < 1.2.0-2

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-2
- renamed to oxygen-gtk2

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-1
- oxygen-gtk2-1.2.0
- License: LGPLv2+

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Fri Nov 18 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.5-1
- 1.1.5

* Fri Oct 28 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-3
- disable forcing KDE icons and fonts

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for glibc bug#747377

* Sun Oct 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-1
- 1.1.4

* Mon Oct  3 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-3
- fix mozilla applications detection kde#283251

* Fri Sep 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-2
- BR: dbus-glib-devel

* Fri Sep 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Sat Aug 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.2-1
- 1.1.2

* Fri Jul 15 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Tue Jun 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-1
- 1.1.0

* Fri May 20 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- 1.0.5

* Tue Apr 12 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- 1.0.4

* Mon Mar 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- 1.0.3

* Fri Feb 11 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-1
- 1.0.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1
- oxygen-gtk-1.0.1

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-2
- drop extraneous BR: cairo-devel

* Sun Dec 12 2010 Rex Dieter <rdieter@fedoraproject.org> -  1.0.0-1
- first try




