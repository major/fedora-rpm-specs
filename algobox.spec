Name:           algobox
Version:        1.0.3
Release:        6%{?dist}
Summary:        Algorithmic software
Summary(fr):    Logiciel d'algorithmique

License:        GPLv2+
URL:            https://www.xm1math.net/algobox
Source0:        %{url}/algobox-%{version}.tar.bz2

# Because qtwebengine is not always available
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel >= 5.7
BuildRequires:  qt5-qtwebengine-devel

BuildRequires:  desktop-file-utils
BuildRequires: make

%description
Algobox is an initiation to algorithmic software at high school level.

%description(fr)
Algobox est un logiciel d'initiation à l'algorithmique au niveau lycée.


%prep
%autosetup -p1
chmod -x license.txt


%build

%{qmake_qt5}

%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/algobox.desktop


%files
%license license.txt
%doc utilities/AUTHORS utilities/CHANGELOG.txt
%{_bindir}/algobox
%{_datadir}/algobox
%{_datadir}/applications/algobox.desktop
%{_datadir}/mime/packages/x-algobox.xml
%{_datadir}/pixmaps/algobox.png


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.0.3-1
- Initial spec file
