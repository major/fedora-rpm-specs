Summary:  A free and open source recipe management software 
Name:     anymeal
License:  GPL-3.0-or-later
Version:  1.21
Release:  1%{?dist}

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
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5UiPlugin)

Requires:       hicolor-icon-theme

%description
AnyMeal is a free and open source recipe management software developed
using SQLite3 and Qt5. It can manage a cookbook with more than 250,000
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
# Current build system uses Googletest sources,
# checking if upstream can support using shared libraries
make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/de.wedesoft.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/de.wedesoft.%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
#doc ChangeLog
%license LICENSE
%{_bindir}/anymeal
%{_mandir}/man1/anymeal.1*
%{_datadir}/applications/de.wedesoft.%{name}.desktop
%{_metainfodir}/de.wedesoft.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png


%changelog
* Mon Oct 16 2023 Benson Muite <benson_muite@emailplus.org> - 1.21-1
- Initial packaging
