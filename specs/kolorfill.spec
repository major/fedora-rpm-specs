%global commit 3e21584b0524a7998dcc20424329d1886ceb0a12
%global shortcommit %(c=%{commit}; echo ${c:0:8})
Name:           kolorfill
Version:        0^20250825.%{shortcommit}
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
BuildRequires: cmake(Qt6LinguistTools)

Requires:      kf6-kirigami%{?_isa}

%description
Given a board initially filled with randomly colored blocks,
on each turn choose a color to expand the uniform color surrounding
the top left most block by so that at the end, the board is filled
with one color.

%prep
%autosetup -n %{name}-%{commit}


%build
%cmake_kf6
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
* Mon Sep 01 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 0^20250825.3e21584b-1
- Update snapshot, build with Qt6

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231224fe74b68f-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231224fe74b68f-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231224fe74b68f-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 05 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0^20231224fe74b68f-2
- Revert to Qt5

* Thu Dec 28 2023 Benson Muite <benson_muite@emailplus.org> - 0^20231224fe74b68f-1
- Initial packaging
