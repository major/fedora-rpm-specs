Summary:	Run an entire GNOME session under valgrind
Name:		gnome-valgrind-session
Version:	1.1
Release:	34%{?dist}
License:	LicenseRef-Fedora-Public-Domain
URL:		http://hp.cl.no/proj/gnome-valgrind-session/
Source0:	http://hp.cl.no/proj/gnome-valgrind-session/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-desktop.patch
Patch1:		%{name}-%{version}-use-gnome-session-suffix-pid-drop-alignment.patch
Patch2:		%{name}-%{version}-add-xorg-label.patch

Requires:	gnome-session 
Requires:	valgrind

BuildArch:	noarch

%description
GNOME Valgrind Session adds new types of GNOME session to the login manager's
session menu. These let you instrument your entire session with Valgrind for
debugging purposes. The generated logs are collected and subjected to simple
postprocessing when you log out. The result is saved to a file in your home
directory.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xsessions

# Startup and post-processing scripts for the sessions.
install -p -m0755 gnome-valgrind-errors $RPM_BUILD_ROOT/%{_bindir}
install -p -m0755 gnome-valgrind-errors-postprocess $RPM_BUILD_ROOT/%{_bindir}
install -p -m0755 gnome-valgrind-leaks $RPM_BUILD_ROOT/%{_bindir}
install -p -m0755 gnome-valgrind-leaks-postprocess $RPM_BUILD_ROOT/%{_bindir}

# These desktop files represent sessions, not GUI apps, so we don't use
# desktop-file-install upon them (following precedent in the gnome-session
# package).
install -p -m0644 gnome-valgrind-errors.desktop \
  $RPM_BUILD_ROOT/%{_datadir}/xsessions
install -p -m0644 gnome-valgrind-leaks.desktop \
  $RPM_BUILD_ROOT/%{_datadir}/xsessions

%files
%doc LICENSE
%{_bindir}/gnome-valgrind-errors
%{_bindir}/gnome-valgrind-errors-postprocess
%{_bindir}/gnome-valgrind-leaks
%{_bindir}/gnome-valgrind-leaks-postprocess
%{_datadir}/xsessions/gnome-valgrind-errors.desktop
%{_datadir}/xsessions/gnome-valgrind-leaks.desktop

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Debarshi Ray <rishi@fedoraproject.org> - 1.1-29
- Drop support for Fedora 8

* Wed May 10 2023 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.1-28
- Add "on Xorg" to session names

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Debarshi Ray <rishi@fedoraproject.org> - 1.1-16
- Drop --alignment=8 because it is not a valid value on at least x86_64
  (RH #1376444)
- Drop Group and BuildRoot

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.1-3
- Explicitly mention the PID as the suffix of the log files for all
  distributions, except Fedora 8.

* Fri Sep 12 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.1-2
- Removed Encoding and fixed Type value in Desktop Entry.

* Fri Apr 25 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.1-1
- Initial build. Imported SPEC written by David Malcolm and Matthias Clasen.
