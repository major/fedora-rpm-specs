
# Versioning this package is a little odd. It seems that the Mageia packager
# grabs from Git and creates version numbers as 1.7.{number of commits since 1.7}
# which means upstream don't tag releases since it breaks his script.
# (see: https://github.com/oferkv/phototonic/issues/214 ) so I will now package from Git.

%global commit0 d2176fee17a86abb09b229f8b99385a3f6d77f16
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           phototonic

# here 12 is the number of commits since 2.1 - this seems to be the style for upstream.
# since the first version packaged for Fedora was 1.7.20 this format needs to be kept
# for upgrades to work - I can't drop the number and just use the git tag unfortunately.
Version:        2.1.12
Release:        20190932git%{shortcommit0}%{?dist}
Summary:        Image viewer and organizer

License:        GPLv3
URL:            https://github.com/oferkv/phototonic
Source0:  https://github.com/oferkv/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel 
BuildRequires:  qt5-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  exiv2-devel

%description
phototonic is a fast and functional image viewer and organizer, inspired by the
traditional image viewer design (i.e. thumbnails and viewer layouts).


%prep
%setup -q -n %{name}-%{commit0}


%build
%{qmake_qt5}
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%doc

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190932gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190931gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190930gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190929gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190928gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190927gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190926gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190925gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190924gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-20190923gitd2176fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Michael Cullen <michael@cullen-online.com> - 2.1.12-20190922gitd2176fe
- Fix FTBFS
- Updated

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161110git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161109git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.7.21-20161108git24d7b78
- rebuild (exiv2)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161107git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161106git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161105git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161104git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7.21-20161103git24d7b78
- rebuild (exiv2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-20161102git24d7b78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Michael Cullen <michael@cullen-online.com> - 1.7.21-20161101git24d7b78
- Updated to newer upstream commit, adding Portuguese language support.
* Tue May 10 2016 Michael Cullen <michael@cullen-online.com> - 1.7.20-2
- Fixed review comment. Added update-desktop-database calls.
* Thu May  5 2016 Michael Cullen <michael@cullen-online.com> - 1.7.20-1
- Pulled in properly tagged release from upstream
* Mon May  2 2016 Michael Cullen <michael@cullen-online.com> - 1.7.1-1
- Initial Package 
