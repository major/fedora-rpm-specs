%global appname kImageAnnotator
%global libname lib%{appname}

Name: kimageannotator
Version: 0.7.0
Release: 1%{?dist}

License: LGPL-3.0-or-later
Summary: Library and a tool for annotating images
URL: https://github.com/ksnip/%{appname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(kColorPicker-Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5X11Extras)

BuildRequires: cmake(kColorPicker-Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)


BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

Requires: %{name}-common%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Library and a tool for annotating images. Part of KSnip project.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%package qt6
Summary: QToolButton control with color popup menu (Qt6)
Requires: %{name}-common%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description qt6
%{summary}.
	
%package qt6-devel
Summary: Qt6 Development files for %{name}
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description qt6-devel
%{summary}.

%package common
Summary: Common language translations for Qt5 and Qt6 builds
%description common
%{summary}.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
mkdir qt5
pushd qt5
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF
%cmake_build
popd
mkdir qt6
pushd qt6
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    -DBUILD_WITH_QT6:BOOL=ON
%cmake_build
popd


%install
pushd qt5
%cmake_install
popd
pushd qt6
%cmake_install
popd

%find_lang %{appname} --with-qt

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/%{libname}-Qt5.so.0*

%files devel
%{_includedir}/%{appname}-Qt5/
%{_libdir}/cmake/%{appname}-Qt5/
%{_libdir}/%{libname}-Qt5.so

%files qt6
%doc README.md
%license LICENSE
%{_libdir}/%{libname}-Qt6.so.0*
	
%files qt6-devel
%{_includedir}/%{appname}-Qt6/
%{_libdir}/cmake/%{appname}-Qt6/
%{_libdir}/%{libname}-Qt6.so

%files common -f %{appname}.lang

%changelog
* Sun Jan 21 2024 Marie Loise Nolden <loise@kde.org> - 0.7.0-1
- update to 0.7.0

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.3-1
- Updated to version 0.5.3.

* Tue Sep 14 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-1
- Updated to version 0.5.2.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Updated to version 0.5.1.

* Tue May 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.

* Tue Mar 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.2-1
- Updated to version 0.4.2.

* Mon Feb 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Fri Jul 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.2-1
- Initial SPEC release.
