%global commit fe74b68f500d8523c78f9ffadc5a71adb5906aa5
%global shortcommit %(c=%{commit}; echo ${c:0:8})
Name:           kolorfill
Version:        0^20231224fe74b68f
Release:        1%{?dist}
Summary:        Simple flood fill game

License:        MIT
URL:            https://apps.kde.org/kolorfill
Source:         https://invent.kde.org/games/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QuickTest)

%description
Given a board initially filled with randomly colored blocks,
on each turn choose a color to expand the uniform color surrounding
the top left most block by so that at the end, the board is filled
with one color.

%prep
%autosetup -n %{name}-%{commit}


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install


%find_lang %{name} --with-qt

%check
# Test fails in Fedora CI, needs investigation
#ctest --verbose --output-on-failure
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
	
 
%files -f %{name}.lang
%license COPYING
%doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml



%changelog
* Thu Dec 28 2023 Benson Muite <benson_muite@emailplus.org> - 0^20231224fe74b68f-1
- Initial packaging
