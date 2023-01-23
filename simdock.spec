%global commit 1578d0d2b4f4873c81f81142aebd8983c67971cc
%global scommit %(c=%{commit}; echo ${c:0:7})

Summary:       Fast and customizable dockbar
Name:          simdock
Version:       1.5.3
Release:       10%{?dist}
License:       GPLv2+
URL:           https://github.com/onli/simdock
Source0:       https://github.com/onli/simdock/archive/%{commit}/simdock-%{version}-%{scommit}.tar.gz
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libwnck-1.0)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: compat-wxGTK3-gtk2-devel
%description
SimDock is a fast and customizable dockbar. It is written in c++ and
wxWidgets and fits well in Gnome but works on most desktop
environments. Does not require Compiz nor 3D acceleration.

%prep
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags} CCFLAGS="%{optflags} -fPIC"

%install
make DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/simdock
%{_datadir}/simdock
%{_datadir}/pixmaps/simdock.png

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Scott Talbert <swt@techie.net> - 1.5.3-1
- New upstream release 1.5.3 and rebuild with wxWidgets 3.0 (GTK+2 build)

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.4-1
- Add C++ compiler
- Drop git date in release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.20160212git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.20160210git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.20160209git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.20160208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.4-0.20160207git
- Update from git

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-7.20130128git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-6.20130128git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.6-5.20130128git
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4.20130128git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3.20130128git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2.20130128git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.2.6-1.20130128git
- Latest from upstream
- New upstream location

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.2-12
- Rebuilt for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.2-10
- rebuilt against wxGTK-2.8.11-2

* Thu Feb 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.2-9
- Build with optflags

* Sun Feb 14 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.2-8
- Add DSO patch

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.2.6
- Convert spec to utf8

* Thu Apr 30 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.2-5
- Patch to honor $RPM_OPT_FLAGS during build.
- Disable autotools dependency tracking during build for cleaner build logs
  and possible slight build speedup.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 20 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.2-3
- rebuild

* Thu Oct  2 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.2-2
- fix patch macro
- install desktop file

* Wed Mar 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.2-1
- initial build
