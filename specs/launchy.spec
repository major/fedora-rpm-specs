Name:           launchy
Version:        2.5
Release:        43%{?dist}
Summary:        Open Source Keystroke Launcher

License:        GPL-1.0-or-later
URL:            http://www.launchy.net
Source0:        http://www.launchy.net/downloads/src/launchy-2.5.tar.gz

Patch0:         %{name}-X11-lib.patch
Patch1:         %{name}-xdg-icon-path.patch


BuildRequires:  gcc-c++
BuildRequires:  qt-devel boost-devel
BuildRequires:  desktop-file-utils
BuildRequires: make

%description
Launchy is a free cross-platform utility designed to help you forget about your
start menu, the icons on your desktop, and even your file manager.
Launchy indexes the programs in your start menu and can launch your documents,
project files, folders, and bookmarks with just a few keystrokes!


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
# convert DOS to UNIX
%{__sed} -i 's/\r//' LICENSE.txt readme.txt


%build
%{_libdir}/qt4/bin/qmake "CONFIG+=debug" Launchy.pro
make %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# prefix is hardcoded in the makefile 
install -Dpm 0755 debug/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
install -Dpm 0755 debug/plugins/*so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/
install -Dpm 0755 release/plugins/*so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/icons/
install -Dpm 0644 plugins/*/*png $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/icons/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -Dpm 0644 misc/Launchy_Icon/launchy_icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/
install -dpm 0755 skins $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/
install -dpm 0755 skins/Black_Glass $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass
install -dpm 0755 skins/Spotlight_Wide $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Spotlight_Wide
install -dpm 0755 skins/Simple $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Simple
install -dpm 0755 skins/Note $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Note
install -dpm 0755 skins/Default $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Default
install -dpm 0755 skins/Mercury_Wide $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury_Wide
install -dpm 0755 skins/Black_Glass_Wide $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass_Wide
install -dpm 0755 skins/Mercury $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury
install -dpm 0755 skins/QuickSilver2 $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/QuickSilver2
install -Dpm 0644 skins/Black_Glass/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass
install -Dpm 0644 skins/Spotlight_Wide/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Spotlight_Wide
install -Dpm 0644 skins/Simple/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Simple
install -Dpm 0644 skins/Note/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Note
install -Dpm 0644 skins/Default/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Default
install -Dpm 0644 skins/Mercury_Wide/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury_Wide
install -Dpm 0644 skins/Black_Glass_Wide/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass_Wide
install -Dpm 0644 skins/Mercury/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury
install -Dpm 0644 skins/QuickSilver2/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/QuickSilver2
install -dm 0755 $RPM_BUILD_ROOT%{_includedir}/%{name}
install -Dpm 0644 "Plugin API"/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
desktop-file-install    \
        --dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart       \
        --add-only-show-in=GNOME                                \
        linux/%{name}.desktop
desktop-file-install   \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --remove-category Application \
        linux/%{name}.desktop

# autostart is disabled by default
echo "X-GNOME-Autostart-enabled=false" >> \
    $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/%{name}.desktop




%files
%doc LICENSE.txt readme.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/pixmaps/launchy_icon.png
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop


%files devel
%{_includedir}/%{name}/*.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-41
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-26
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.5-23
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.5-21
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.5-20
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.5-18
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.5-17
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.5-15
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.5-13
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.5-12
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.5-9
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.5-7
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 06 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 2.5-3
- review by msuchy

* Mon Sep 06 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 2.5-2
- correcting XDG icon path

* Mon Sep 06 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 2.5-1
- initial package
