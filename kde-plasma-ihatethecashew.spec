Name:           kde-plasma-ihatethecashew
Version:        0.4
Release:        25%{?dist}
Summary:        Removes the KDE Plasma Cashew From the Corner of the Display

License:        GPLv2
URL:            http://www.kde-look.org/content/show.php/I+HATE+the+Cashew?content=91009
Source0:        http://www.kde-look.org/CONTENT/content-files/91009-iHateTheCashew-4.4.tbz

Patch1:         ihatethecashew-kde-46-fix.patch


BuildRequires:  kdebase-workspace-devel >= 4.2.0
BuildRequires: make

%description
Removes the KDE Plasma Cashew From the Corner of the Display.

%prep
%setup -qn iHateTheCashew

%patch1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

sed -i -e 's/-fno-exceptions -fno-check-new -fno-common//' \
-e 's/-fno-threadsafe-statics -fvisibility=hidden -fvisibility-inlines-hidden//' \
-e 's/-ansi//' %{_target_platform}/CMakeFiles/plasma_applet_ihatethecashew.dir/flags.make

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}

%files
%doc COPYING
%{_kde4_libdir}/kde4/plasma_applet_ihatethecashew.so
%{_kde4_datadir}/kde4/services/plasma-applet-ihatethecashew.desktop

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 3 2011 Eli Wapniarski <eli@orbsky.homelinux.org> 0.4-2
- Patch added to support KDE 4.6

* Mon Dec 21 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.4-1
- Version Upgrade
- support KDE 4.4

* Tue Feb 17 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.3-1
- Update to version 0.3
- adds the ability to remove cashew on serveral activities

* Thu Feb 05 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.2c-2
- Added command to remove non Fedora GCC compilation flags

* Wed Feb 04 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.2c-1
- Fixes licenses test

* Tue Feb 03 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.2b-3
- Corrected packaging errors

* Tue Feb 03 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.2b-2
- Corrected packaging errors

* Mon Feb 02 2009 Eli Wapniarski <eli@orbsky.homelinux.org> 0.2b-1
- Initial package
