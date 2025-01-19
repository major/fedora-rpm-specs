Name: kiwix-desktop
Version: 2.3.1
Release: 9%{?dist}

License: GPL-3.0-or-later
Summary: Kiwix desktop application

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: aria2
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: libkiwix-devel
BuildRequires: libzim-devel
BuildRequires: make
BuildRequires: mustache-devel
BuildRequires: pugixml-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qtsingleapplication-qt5-devel

Requires: aria2%{?_isa}
Requires: hicolor-icon-theme
Requires: qt5-qtsvg%{?_isa}
Requires: shared-mime-info

# Required qt5-qtwebengine is not available on some arches.
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
The Kiwix-desktop is a view/manager of zim files for GNU/Linux
and Windows. You can download and view your zim files as you
which.

%prep
%autosetup -p1
mkdir %{_vpath_builddir}
sed -e "/static {/,+2d" -i %{name}.pro
rm -rf subprojects

%build
pushd %{_vpath_builddir}
    %qmake_qt5 PREFIX=%{_prefix} CONFIG+=qtsingleapplication ..
popd

%make_build -C %{_vpath_builddir}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_vpath_builddir}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.1-4
- Rebuilt due to libzim update.

* Sat Apr 01 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.1-3
- Rebuilt due to libzim package rename.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.1-1
- Updated to version 2.3.1.

* Thu Sep 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.0-1
- Updated to version 2.3.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.2-1
- Updated to version 2.2.2.

* Fri Mar 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.1-1
- Updated to version 2.2.1.

* Sat Mar 05 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Updated to version 2.2.0.

* Mon Jan 24 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.5-4
- Added explicit dependency on qt5-qtsvg.

* Wed Feb 10 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.5-3
- Always use HTTPS for the catalog downloads.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.5-1
- Updated to version 2.0.5.

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.4-3
- Rebuilt due to kiwix-lib update.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.4-1
- Updated to version 2.0.4.

* Fri Jul 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.3-1
- Updated to version 2.0.3.

* Wed Jul 01 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.2-1
- Updated to version 2.0.2.

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Updated to version 2.0.1.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-1
- Updated to version 2.0.

* Mon Feb 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.7.rc4
- Updated to version 2.0 RC4.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.6.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.5.rc3
- Updated to version 2.0 RC3.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.4.rc1
- Updated to version 2.0 RC1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.2.beta5
- Added aria2 to dependencies.

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.1.beta5
- Initial SPEC release.
