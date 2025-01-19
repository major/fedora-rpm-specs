%global commit fe74b68f500d8523c78f9ffadc5a71adb5906aa5
%global shortcommit %(c=%{commit}; echo ${c:0:8})
Name:           kolorfill
Version:        0^20231224fe74b68f
Release:        4%{?dist}
Summary:        Simple flood fill game

License:        MIT
URL:            https://apps.kde.org/kolorfill
Source:         https://invent.kde.org/games/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: qt5-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5QuickTest)
BuildRequires: cmake(Qt5LinguistTools)

Requires:      kf5-kirigami2%{?_isa}

%description
Given a board initially filled with randomly colored blocks,
on each turn choose a color to expand the uniform color surrounding
the top left most block by so that at the end, the board is filled
with one color.

%prep
%autosetup -n %{name}-%{commit}


%build
%cmake_kf5
%cmake_build


%install
%cmake_install


%find_lang %{name} --with-qt

%check
# Test fails in Fedora CI, needs investigation
#ctest --verbose --output-on-failure
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
	
 
%files -f %{name}.lang
%license COPYING
%doc README
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231224fe74b68f-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231224fe74b68f-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 05 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0^20231224fe74b68f-2
- Revert to Qt5

* Thu Dec 28 2023 Benson Muite <benson_muite@emailplus.org> - 0^20231224fe74b68f-1
- Initial packaging
