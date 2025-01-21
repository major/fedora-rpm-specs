Name:          sailcut
Version:       1.4.1
Release:       18%{?dist}
Summary:       A sail design and plotting software

License:       GPL-2.0-only
URL:           http://www.sailcut.com/
Source0:       https://github.com/sailcut/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       sailcut.desktop
Source2:       sailcut.xml

# Add a couple of missing includes
Patch0:        sailcut_includes.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: transfig
BuildRequires: desktop-file-utils
BuildRequires: shared-mime-info


%description
Sailcut CAD is a sail design and plotting software.
It allows you to design and visualize your own sail and compute the accurate
development of all panels in flat sheets.


%prep
%autosetup -p1


%build
%qmake_qt5 PREFIX=%{_prefix} %{name}.pro
%make_build
pushd doc
mkdir build
./makedocs $PWD/build
popd


%install
make INSTALL_ROOT=%{buildroot} install
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
install -p -D -m 644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -p -D -m 644 icons/%{name}-file.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}.svg
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt


%files -f %{name}.lang
%doc AUTHORS ChangeLog README doc/build/en/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}.svg


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 1.4.1-4
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-2
- Remove obsolete scriptlets

* Sun Sep 10 2017 Sandro Mani <manisandro@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 1.3.902-1
- Update to 1.3.902

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.5-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.5-6
- update icon/mime scriptlets, s|qt-devel|qt4-devel|

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Sandro Mani <manisandro@gmail.com> - 1.3.5-2
- Add patch to fix FSF addresses
- Fix spelling

* Tue May 07 2013 Sandro Mani <manisandro@gmail.com> - 1.3.5-1
- Initial package
