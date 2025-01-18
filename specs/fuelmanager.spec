Name:     fuelmanager
Version:  0.5.1
Release:  9%{?dist}
Summary:  Manage fuel mileage

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later

URL:     https://gitlab.com/kc8hfi/fuelmanager
Source0: https://gitlab.com/kc8hfi/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils
BuildRequires: make

Requires: hicolor-icon-theme
Requires: qt-assistant

%description
Application that keeps track of four things, miles, gallons, cost, and 
the date of each fill-up.  It generates monthly and yearly summaries of 
miles driven, cost of fuel,how many gallons, and fuel mileage.

%prep
%setup -q

%build

%{qmake_qt5} %{name}.pro PREFIX=%{_prefix}
make %{?_smp_mflags}

%install

make install INSTALL_ROOT=%{buildroot} 

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

for s in 16 22 24 32 48 256; do
     %{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
     %{__cp} icons/${s}x${s}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%{__cp} %{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# install the AppData file
%__mkdir_p %{buildroot}%{_datadir}/appdata
cp fuelmanager.appdata.xml %{buildroot}%{_datadir}/appdata/


%files
%doc COPYING
%doc documentation/fuelmanager.qhc
%{_bindir}/%{name}
%{_datadir}/appdata/*.*
%{_datadir}/applications/*.*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 09 2022 kc8hfi <kc8hfi@gmail.com> - 0.5.1-1
- Build for release 0.5.1-1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 02 2018 kc8hfi <kc8hfi@gmail.com> - 0.5-1
- Build for release 0.5-1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-8
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 09 2016 kc8hfi <kc8hfi@gmail.com> - 0.4.2-4
- Fixed the source path

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-2
- Use %%qmake_qt4 macro

* Thu Jan 07 2016 kc8hfi <kc8hfi@gmail.com> - 0.4.2-1
- Build for release 0.4.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Richard Hughes <richard@hughsie.com> - 0.4.1-3
- Install the upstream AppData file

* Fri Jun 13 2014 kc8hfi <kc8hfi@gmail.com> - 0.4.1-2
- Build for release 0.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Charles Amey <kc8hfi@gmail.com> - 0.4.0-1
- Build for release 0.4.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Charles Amey <kc8hfi@gmail.com> - 0.3.9.1-1
- built for release 0.3.9.1

* Wed Dec 19 2012 Charles Amey <kc8hfi@gmail.com> - 0.3.9
- built for release 0.3.9

* Fri Aug 31 2012 Charles Amey <kc8hfi@gmail.com> - 0.3.8.1-1
- added the documentation file to the files macro

* Sun Jul 22 2012 Charles Amey <kc8hfi@gmail.com> - 0.3.8-1
- added qt assistant in Requires section

* Thu Jun 21 2012 Charles Amey <kc8hfi@gmail.com> - 0.3.7-2
- removed the gcc-c++ from the build requirement

* Thu Jun 21 2012 Charles Amey <kc8hfi@gmail.com> - 0.3.7-1
- built for latest version
  using buildroot macro instead of a variable
  added hicolor-icon-theme for build requirement

* Thu May 31 2012 Charles Amey kc8hfi@gmail.com - 0.3.6-6
- removed unnecessary sections
  fixed spelling errors in the description
 
* Thu Jun 23 2011 Charles Amey kc8hfi@gmail.com - 0.3.6-5
- Built for Release 0.3.6-5

* Sat Jun 11 2011 Charles Amey kc8hfi@gmail.com - 0.3.4-3
- Built for Release 0.3.4

* Thu Jun 09 2011 Charles Amey kc8hfi@gmail.com - 0.3.3-1
- Built for Release 0.3.3

