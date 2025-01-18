Name:    akonadi-notes
Version: 24.08.3
Release: 3%{?dist}
Summary: The Akonadi Notes Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  cmake(KPim6Mime)
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

# Remove together with move-translations.patch once released
find ./po -type f -name akonadinotes5.po -execdir mv {} akonadinotes6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiNotes.so.*

%files devel
%{_includedir}/KPim6/AkonadiNotes/
%{_kf6_libdir}/cmake/KPim6AkonadiNotes/
%{_kf6_libdir}/libKPim6AkonadiNotes.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 14 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.3-2
- Rebuild (kmime)

* Wed Nov 06 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
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

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-4
- Backport rename translation files

* Tue Dec 19 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Don't obsolete kf5-akonadi-notes, this is coinstallable

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old version

* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
