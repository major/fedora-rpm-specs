
Name:           kapow
Version:        1.6.3
Release:        1%{?dist}
Summary:        A punch clock program

License:        GPL-3.0-or-later
URL:            http://gottcode.org/%{name}
Source0:        https://github.com/gottcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-linguist
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  cmake
Requires:       hicolor-icon-theme

%description
Kapow is a punch clock program designed to easily keep track of your hours,
whether you're working on one project or many. Simply clock in and out with the
Start/Stop button. If you make a mistake in your hours, you can go back and
edit any of the entries by double-clicking on the session in question. Kapow
also allows you to easily keep track of the hours since you last billed a
client, by providing a helpful "Billed" check box--the totals will reflect your
work after the last billed session.

%prep
%autosetup
# Delete invalid <icon> tag
sed -i '/<icon type="stock">kapow<\/icon>/d' icons/%{name}.appdata.xml

%build
%{cmake}
%{cmake_build}


%install
%{cmake_install}

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc CREDITS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Thu Jan 09 2025 Vasiiy Glazov <vascom2@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Vasiiy Glazov <vascom2@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Vasiiy Glazov <vascom2@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Fri Dec 02 2022 Vasiiy Glazov <vascom2@gmail.com> - 1.6.0-2
- Fixed source path and directory owning

* Fri Dec 02 2022 Vasiiy Glazov <vascom2@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.8-1
- Update to 1.5.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.7-1
- Update to 1.5.7

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-1
- Update to latest version

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.5-4
- Add g++ to BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.5-2
- Remove obsolete scriptlets

* Sat Dec 30 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.5-1
- update to latest upstream release (rhbz#1529406)

* Sun Dec 17 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.4-1
- Update to latest release (rhbz#1508412)

* Wed Oct 25 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.3-1
- Update to latest release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 18 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.0-2
- Remove appdata file - has been added to source

* Sun Sep 18 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.0-1
- Update to 1.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.4.4.2-6
- use %%qmake_qt5 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.4.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.4.4.2-1
- Update to new upstream release

* Mon Nov 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.4.1-2
- rebuild (qt5 qreal/arm)

* Tue Oct 22 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.4.4.1-1
- Correct directory ownership
- Correct ld flags
- https://bugzilla.redhat.com/show_bug.cgi?id=979767#c8

* Mon Oct 21 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.4.4.1-1
- Update as per https://bugzilla.redhat.com/show_bug.cgi?id=979767#c6
- Remove comments 
- Own datadir/name directory
- Own icon directories
- Add an appdata file

* Sun Jun 30 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.4.4.1-1
- Initial build
- Cosmetic changes #979767

