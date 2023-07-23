Name:           puzzle-master
Version:        2.5.3
Release:        16%{?dist}
Summary:        Fun jigsaw puzzle game

License:        GPLv2+
URL:            https://github.com/Venemo/puzzle-master

Source0:        https://github.com/Venemo/puzzle-master/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: pkgconfig(Qt5Core), pkgconfig(Qt5Gui), pkgconfig(Qt5Quick)
BuildRequires: desktop-file-utils

%description
%{name} is a jigsaw puzzle game that lets you use your own
images (and contains some built-in ones) for generating puzzles.
You can decide the size and the difficulty of the puzzle.

%prep
%setup -q

%build
# These flags ensure that the files will be placed to the correct location
QMAKEFLAGS=''
QMAKEFLAGS+=' -after target.path=%{_bindir}'
QMAKEFLAGS+=' -after desktopfile.path=%{_datadir}/applications'
QMAKEFLAGS+=' -after iconfile.path=%{_datadir}/icons/hicolor/scalable/apps'
QMAKEFLAGS+=' -after appdatafile.path=%{_datadir}/appdata'

%{qmake_qt5} $QMAKEFLAGS
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{make_install} INSTALL_ROOT=$RPM_BUILD_ROOT
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%attr(644,root,root) %{_datadir}/appdata/%{name}.appdata.xml
%doc LICENSE
%doc LICENSE-DOCS

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Timur Kristóf <venemo@fedoraproject.org> - 2.5.3-1
- Use new upstream release v2.5.3
- Use the %%make_install macro instead of plain make install

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-9
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 5 2012 Timur Kristóf <venemo@fedoraproject.org> 2.0.0-1
- Using new upstream release 2.0.0
- Changed file path for the icon

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 7 2011 Timur Kristóf <venemo@fedoraproject.org> 1.2.4-1
- Using new upstream release 1.2.4

* Sat May 7 2011 Timur Kristóf <venemo@fedoraproject.org> 1.2.3-1
- Using new upstream release 1.2.3
- Ensuring proper placement of the files with some qmake flags

* Wed May 4 2011 Timur Kristóf <venemo@fedoraproject.org> 1.2.2-2
- Fixed the issues raised during the review process, see
  https://bugzilla.redhat.com/show_bug.cgi?id=701785

* Tue May 3 2011 Timur Kristóf <venemo@fedoraproject.org> 1.2.2-1
- Initial version of the RPM package, using latest upstream 1.2.2 version.

