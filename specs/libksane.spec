Name:    libksane
Summary: SANE Library interface for KDE
Version: 24.12.1
Release: 2%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/graphics/%{name}
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gettext

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KSaneCore6)

BuildRequires: pkgconfig(sane-backends)

Conflicts: kf5-libksane < 24.01
Obsoletes: kf5-libksane < 24.01
Obsoletes: %{name}-common < 24.12.0
Obsoletes: %{name}-qt5 < 24.12.0
Obsoletes: %{name}-qt6 < 24.12.0


%description
%{summary}.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Widgets)
Obsoletes: kf5-libksane-devel < 24.01
Obsoletes: %{name}-qt5-devel < 24.12.0
Obsoletes: %{name}-qt6-devel < 24.12.0

%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc AUTHORS
%license COPYING*
%license LICENSES/*
%{_datadir}/icons/hicolor/*/actions/*
%{_libdir}/libKSaneWidgets6.so.{6,%{version}}

%files devel
%{_includedir}/KSaneWidgets6/
%{_libdir}/libKSaneWidgets6.so
%{_libdir}/cmake/KSaneWidgets6/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Fri Dec 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-2
- Unify into one package and add proper obsoletes

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.05.2-2
- Fix libksane-qt6-devel dependencies

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Wed Dec 13 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Explicit conflicts libksane-common

* Mon Dec 11 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-1
- Replaces kf5-libksane, providing both a qt5 and a qt6 build
