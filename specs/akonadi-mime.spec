Name:    akonadi-mime
Version: 25.07.90
Release: 1%{?dist}
Summary: The Akonadi Mime Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)

# Plasma 6
Obsoletes:      kf5-akonadi-mime < 24.01.80-1

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KPim6Akonadi)
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
find ./po -type f -name libakonadi-kmime5.po -execdir mv {} libakonadi-kmime6.po \;
find ./po -type f -name libakonadi-kmime5-serializer.po -execdir mv {} libakonadi-kmime6-serializer.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name



%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/akonadi/plugins/serializer/
%{_kf6_datadir}/config.kcfg/specialmailcollections.kcfg
%{_kf6_datadir}/mime/packages/x-vnd.kde.contactgroup.xml
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6AkonadiMime.so.*
%{_kf6_qtplugindir}/akonadi_serializer_mail.so

%files devel
%{_includedir}/KPim6/AkonadiMime/
%{_kf6_libdir}/cmake/KPim6AkonadiMime/
%{_kf6_libdir}/libKPim6AkonadiMime.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Thu Mar 20 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80 (Beta)

* Tue Mar 04 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

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

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Backport rename translation files

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old version

* Fri Dec 8 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
