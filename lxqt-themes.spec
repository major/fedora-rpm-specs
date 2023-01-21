%define __cmake_in_source_build 1

Name:           lxqt-themes
Version:        1.2.0
Release:        2%{?dist}
Summary:        LXQt standard themes

License:        LGPLv2+
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Pagure do not provide tarballs yet.
# To generate this tarball, clone from pagure
# https://pagure.io/lxqt-themes-fedora/
# Remove the .git dir and manual compress it
Source1:        lxqt-themes-fedora-1.0.tar.xz
# Upstream dropped openbox config. But we missed the change deadline, so let's keep it for one more release and drop it in the next
Source2:        lxqt-rc.xml

BuildArch:      noarch

BuildRequires:  lxqt-build-tools >= 0.6.0
BuildRequires:  pkgconfig(lxqt) >= 1.0.0

Requires:       hicolor-icon-theme
Requires:       desktop-backgrounds-compat
Requires:       breeze-cursor-themes
Requires:       breeze-icon-theme

# The themes were essential part of the previous lxqt-common package which
# no longer exists. Therefore we obsolete and provide it here:
Provides:       lxqt-common = %{version}-%{release}
Obsoletes:      lxqt-common < 0.12.0
# The old name for the theme subpackage was lxqt-theme
Provides:       lxqt-theme = %{version}-%{release}
Obsoletes:      lxqt-theme < 0.12.0

%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, dark, frost, kde-plasma, light and system.

%package fedora
Summary: Default Fedora theme for LXQt
Requires: lxqt-theme = %{version}
Requires: breeze-cursor-theme
Requires: breeze-icon-theme
%if 0%{?rhel}
Requires: redhat-logos
%endif
%if 0%{?fedora}
Requires: fedora-logos
%endif
# Obsolete and provide the old subpackage of lxqt-common
Provides:       lxqt-theme-fedora = %{version}-%{release}
Obsoletes:      lxqt-theme-fedora < %{version}-%{release}

%description fedora
%{summary}.

%prep
%autosetup
%setup -b 1

%build
mkdir build
cd build

%cmake3 -DPULL_TRANSLATIONS=NO ..
%cmake_build

%if 0%{?fedora} >= 29

pushd %{_builddir}/lxqt-themes-fedora-1.0
tar Jxf %{SOURCE1}
mkdir build
cd build
%cmake3 ..
popd

%endif

%install
cd build
%cmake_install
pushd %{_builddir}/lxqt-themes-fedora-1.0/build
%cmake_install
popd
mkdir -p %{buildroot}%{_sysconfdir}/xdg/openbox/
install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/openbox/lxqt-rc.xml

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_datadir}/lxqt/graphics
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/{ambiance,dark,frost,kde-plasma,light,system,Clearlooks,Leech,kvantum,silver,Arch-Colors,KDE-Plasma,Valendas}
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/lxqt/palettes
%{_datadir}/lxqt/wallpapers

%files fedora
%{_datadir}/sddm/themes/02-lxqt-fedora/
%{_datadir}/lxqt/themes/fedora-lxqt
%{_sysconfdir}/xdg/openbox/lxqt-rc.xml

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 1.2.0-1
- Update version to 1.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- new version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 zsun <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Tue Aug 11 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-5
- Obsolete and provide the old subpackage of lxqt-common
- Fixes RHBZ 1624739

* Sun Aug 26 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-4
- Merge lxqt-themes-fedora into lxqt-themes

* Fri Aug 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-3
- Bump for package review

* Sun Jun 03 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-2
- add requirements for the themes

* Sun Jun  3 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-1
- initial package

