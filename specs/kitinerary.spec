Name:    kitinerary
Version: 24.12.2
Release: 2%{?dist}
Summary: A library containing itinerary data model and itinerary extraction code

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND ODbL-1.0
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:   %{ix86}
%endif

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kpublictransport
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(ZXing)
BuildRequires:  cmake(KF6I18n)

# kde-pim pkgs
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Archive)

# kde-pim cmake
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6PkPass)

BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)

BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler)
%if 0%{?fedora}
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
%endif
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  osmctools

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6PkPass)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KF6Contacts)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Itinerary.so.*
%{_libexecdir}/kf6/kitinerary-extractor
%{_kf6_datadir}/mime/packages/application-vnd-kde-itinerary.xml

%files devel
%{_includedir}/KPim6/kitinerary/
%{_includedir}/KPim6/KItinerary/
%{_includedir}/KPim6/kitinerary_version.h
%{_kf6_libdir}/libKPim6Itinerary.so
%{_kf6_libdir}/cmake/KPim6Itinerary/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Mon Feb 10 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild (for poppler 25.02.0)

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Alessandro Astone <ales.astone@gmail.com> - 24.12.1-3
- devel subpackage requires KPim6PkPass, KF6CalendarCore, KF6Contacts

* Wed Jan 08 2025 Alessandro Astone <ales.astone@gmail.com> - 24.12.1-2
- devel subpackage requires KPim6Mime

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Mon Jan 06 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 24.12.0-3
- Drop i686 support (leaf package)

* Sat Dec 14 2024 Adam Williamson <awilliam@redhat.com> - 24.12.0-2
- Rebuild for new libphonenumber

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Tue Nov 19 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 19 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-2
- Version bump for libphonenumber

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

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

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Thu Feb 08 2024 Marek Kasik <mkasik@redhat.com> - 24.01.95-2
- Rebuild for poppler 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Fri Dec 8 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
