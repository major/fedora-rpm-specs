Summary:  A free and open source recipe management software 
Name:     anymeal
License:  GPL-3.0-or-later
Version:  1.33
Release:  2%{?dist}

URL:      https://github.com/wedesoft/anymeal
Source0:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:  https://www.wedesoft.de/gnupg-wedekind.asc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libappstream-glib
BuildRequires:  recode-devel
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  which

Requires:       hicolor-icon-theme

%description
AnyMeal is a free and open source recipe management software developed
using SQLite3 and Qt6. It can manage a cookbook with more than 250,000
MealMaster recipes, thereby allowing to import, export, search, display,
edit, and print them.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}

%build

autoreconf -fi
%configure
%make_build

%install
%make_install

%find_lang %{name} --with-qt

%check
make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/de.wedesoft.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/de.wedesoft.%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/anymeal
%{_mandir}/man1/anymeal.1*
%{_datadir}/applications/de.wedesoft.%{name}.desktop
%{_metainfodir}/de.wedesoft.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Benson Muite <benson_muite@emailplus.org> - 1.33-1
- Update to latest release that uses Qt6

* Fri Sep 06 2024 Benson Muite <benson_muite@emailplus.org> - 1.32-1
- Update to latest release

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 02 2024 Benson Muite <benson_muite@emailplus.org> - 1.27-1
- Update to latest release

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 16 2023 Benson Muite <benson_muite@emailplus.org> - 1.21-1
- Initial packaging
