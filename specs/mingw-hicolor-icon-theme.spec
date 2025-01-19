%{?mingw_package_header}

Name:           mingw-hicolor-icon-theme
Version:        0.17
Release:        13%{?dist}
Summary:        Basic requirement for icon themes in MingGW

License:        GPL-2.0-or-later
URL:            http://icon-theme.freedesktop.org/releases/
Source0:        http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.xz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95

%description
Contains the basic directories and files needed for icon theme support.
This is the MinGW version of this package.


%package -n mingw32-hicolor-icon-theme
Summary:        MinGW hicolor icon theme for MingGW

%description -n mingw32-hicolor-icon-theme
Contains the basic directories and files needed for icon theme support.
This is the MinGW version of this package.


%package -n mingw64-hicolor-icon-theme
Summary:        MinGW hicolor icon theme for MingGW

%description -n mingw64-hicolor-icon-theme
Contains the basic directories and files needed for icon theme support.
This is the MinGW version of this package.


%prep
%autosetup -p1 -n hicolor-icon-theme-%{version}

# for some reason this file is executable in the tarball
chmod 0644 COPYING


%build
# Configure and build once, not per target.
%configure
%make_build


%install
# Install once per target, from a single build tree.
%make_install datadir="%{mingw32_datadir}"
%make_install datadir="%{mingw64_datadir}"

touch %{buildroot}%{mingw32_datadir}/icons/hicolor/icon-theme.cache
touch %{buildroot}%{mingw64_datadir}/icons/hicolor/icon-theme.cache


%files -n mingw32-hicolor-icon-theme
%license COPYING
%doc README
%{mingw32_datadir}/icons/hicolor
%ghost %{mingw32_datadir}/icons/hicolor/icon-theme.cache

%files -n mingw64-hicolor-icon-theme
%license COPYING
%doc README
%{mingw64_datadir}/icons/hicolor
%ghost %{mingw64_datadir}/icons/hicolor/icon-theme.cache

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 0.17-1
- Update to 0.17

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Kalev Lember <klember@redhat.com> - 0.16-1
- Update to 0.16

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 0.15-1
- Update to 0.15
- Use license macro for the COPYING file

* Mon Dec 08 2014 Richard Hughes <richard@hughsie.com> - 0.13-1
- Initial packaging attempt
