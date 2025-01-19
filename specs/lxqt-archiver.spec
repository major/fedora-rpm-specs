Name:          lxqt-archiver
Summary:       A simple & lightweight desktop-agnostic Qt file archiver
Version:       1.1.0
Release:       2%{?dist}
License:       GPL-2.0-or-later
URL:           https://lxqt.github.io/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       %{name}.appdata.xml
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(fm-qt6)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: desktop-file-utils
BuildRequires: json-glib-devel
BuildRequires: libexif-devel
BuildRequires: libappstream-glib
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-archiver
Requires:       lxqt-archiver
%description l10n
This package provides translations for the lxqt-archiver package.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/lxqt/translations/%{name}
mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name} --with-qt

%files
%doc CHANGELOG AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml
%dir %{_datadir}/%{name}

%files l10n -f %{name}.lang
%doc CHANGELOG AUTHORS README.md
%license LICENSE
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_arn.qm
%{_datadir}/%{name}/translations/%{name}_ast.qm

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- 1.1.0

* Thu Apr 18 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- 1.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 0.9.0-1
- Update version to 0.9.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 0.8.0-1
- Update version to 0.8.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 0.7.0-1
- Update version to 0.7.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 0.6.0-1
- new version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Zamir SUN <sztsian@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Sat Aug 07 2021 Zamir SUN <sztsian@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.3.0-4
- Fix FTBFS
- Fixes RHBZ#1987686

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Aug 26 2020 Zamir SUN <sztsian@gmail.com> - 0.2.0-1
- Initial lxqt-archiver 0.2.0
