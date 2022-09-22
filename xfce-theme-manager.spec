%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global pkgname Xfce-Theme-Manager
Name:		xfce-theme-manager
Version:	0.3.8
Release:	9%{?dist}
Summary:	A theme manager for Xfce

License:	GPLv3	
URL:		https://github.com/KeithDHedger/Xfce-Theme-Manager
# wget https://github.com/KeithDHedger/Xfce-Theme-Manager/archive/xfce-theme-manager-0.3.8.tar.gz
Source0:	https://github.com/KeithDHedger/Xfce-Theme-Manager/archive/%{name}-%{version}.tar.gz
# https://github.com/KeithDHedger/Xfce-Theme-Manager/pull/4
Patch0:		Wformat-security.patch

BuildRequires:	cairo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfconf-devel

%description
A theme manager allowing easy configuration of themes,
window borders, controls, icons and cursors for Xfce

%prep
%autosetup -n %{pkgname}-%{name}-%{version} -p1


%build
%configure
make %{?_smp_mflags} xfcethememanager_CFLAGS="%{optflags} -export-dynamic" xfcethememanager_CXXFLAGS="%{optflags} -export-dynamic -Wunused -Wunused-function -Wno-unused-result -fPIC"


%install
make install DESTDIR=%{buildroot} docfilesdir="%{_pkgdocdir}"
desktop-file-install	\
--delete-original	\
--dir=%{buildroot}%{_datadir}/applications	\
--remove-key=Categories	\
--add-category=GTK	\
--add-category=Settings	\
--add-category=DesktopSettings	\
--add-category=X-XFCE-SettingsDialog	\
--add-category=X-XFCE-PersonalSettings	\
--add-category=X-XFCE	\
--set-name="Xfce Theme Manager"	\
%{buildroot}/%{_datadir}/applications/%{pkgname}.desktop


%files
%doc  ChangeLog* Xfce-Theme-Manager/resources/docs/gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{pkgname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/Xfce-Theme-Manager/scripts
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.8-6
- Fix FTBFS on F34 fixes rhbz#1911082 and rhbz#1923318

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.8-1
- Update to 0.3.8

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 01 2015 Eduardo Echeverria  <echevemaster@gmail.com> - 0.3.6-1
- Updated to the version 0.3.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.5-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.3.5-3
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 06 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.3.5-1
- Updated to the version 0.3.5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 22 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.3.3-1
- Updated to the version 0.3.3
- switch to unversioned documentation directory

* Sat Feb 02 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.2.4-1
- Update to version 0.2.4

* Sat Jan 05 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.2.3-1
- Update to version 0.2.3

* Sat Dec 08 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.1.20-1
- Update to version 0.1.20

* Fri Nov 30 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.1.19-3
- Remove mirrored Source0 and added original url

* Mon Nov 26 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.1.19-2
- Added comments on how to download the source
- Created man page for the application
- Patch the build process to use the normal rpm opt flags
- Added parameter -g to g++ in patch file to prepare the application to use GDB

* Sun Nov 18 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.1.19-1
- Update to version 0.1.19 with license included

* Mon Nov 12 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.1.18-1
- Initial packaging

