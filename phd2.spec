Name:           phd2
Version:        2.6.11
Release:        4%{?dist}
Summary:        Telescope guiding software
# Main program files are BSD licensed
# Some components have different licenses:
# QHY camera headers are GPLv2+
# SX camera headers are ICU
# INDI GUI is LGPLv2+
License:        BSD and (GPLv2+ and MIT and LGPLv2+)
URL:            http://openphdguiding.org/
# Download upstream tarball from
# https://github.com/OpenPHDGuiding/%%{name}/archive/v%%{version}.tar.gz
# and then run ./generate-tarball.sh %%{version}
Source0:        %{name}-%{version}-purged.tar.xz
# Script to purge binaries and unneeded files from downloaded sources
Source1:        generate-tarball.sh

# Do not force c++ std
Patch99:        phd2_2.9.10_std_cflags.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  gtest-devel
BuildRequires:  libappstream-glib
BuildRequires:  libindi-static
BuildRequires:  libnova-devel
BuildRequires:  wxGTK-devel

BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libindi) >= 1.5
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)

Recommends:     libindi


%description
PHD2 is telescope guiding software that simplifies the process of tracking
a guide star, letting you concentrate on other aspects of deep-sky imaging
or spectroscopy.


%prep
%autosetup -p1

# Remove spurious executable bit set on icons and docs
find icons -type f -print0 |xargs -0 chmod -x
chmod -x PHD_2.0_Architecture.docx


%build
%{cmake} -DUSE_SYSTEM_CFITSIO=ON \
            -DUSE_SYSTEM_LIBUSB=ON \
            -DUSE_SYSTEM_EIGEN3=ON \
            -DUSE_SYSTEM_GTEST=ON \
            -DUSE_SYSTEM_LIBINDI=ON \
            -DOPENSOURCE_ONLY=ON

# Build is not parallel safe
# https://github.com/OpenPHDGuiding/phd2/issues/972
%cmake_build -j1


%install
%cmake_install

%find_lang %{name}

%check
env CTEST_OUTPUT_ON_FAILURE=1 make test -C %{_vpath_builddir}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f %{name}.lang
%doc README.txt PHD_2.0_Architecture.docx
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/phd2/
%{_datadir}/pixmaps/*


%changelog
* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.6.11-4
- Rebuild with wxWidgets 3.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 26 2022 Mattia Verga <mattia.verga@protonmail.com> - 2.6.11-2
- Disable parallel build

* Thu Feb 24 2022 Mattia Verga <mattia.verga@protonmail.com> - 2.6.11-1
- Update to 2.6.11 (fedora#2057427)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 31 2021 Mattia Verga <mattia.verga@protonmail.com> - 2.6.10-3
- Replace _target_platform macro with _vpath_builddir
- Fixes rhbz#1987803

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Mattia Verga <mattia.verga@protonmail.com> - 2.6.10-1
- Update to 2.6.10
- Fixes rhbz#1976560

* Thu Feb 11 2021 Mattia Verga <mattia.verga@protonmail.com> - 2.6.9-6
- Rebuilt for cfitsio soname bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.6.9-4
- Another rebuild attempt for F33 Mass Rebuild after gettext has been fixed
- Use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.6.9-1
- Upgrade to 2.6.9
- Fixes rhbz#1853866

* Mon May 18 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.6.8-1
- Upgrade to 2.6.8

* Sat Feb 08 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.6.7-1
- Upgrade to 2.6.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Mattia Verga <mattia.verga@protonmail.com> - 2.6.6-1
- Upgrade to 2.6.6
- Enable tests on i686

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 2.6.5-2
- rebuilt for cfitsio 3.450

* Mon May 07 2018 Mattia Verga <mattia.verga@email.it> - 2.6.5-1
- Upgrade to 2.6.5
- Remove obsolete scriptlets
- Use upstream patch to disable third party drivers
- Specify libindi to be >= 1.5

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.6.4-6
- rebuilt for cfitsio 3.420 (so version bump)

* Tue Feb 13 2018 Mattia Verga <mattia.verga@email.it> - 2.6.4-5
- Enable test output on failures

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Mattia Verga <mattia.verga@email.it> - 2.6.4-3
- Fix spurious exec bits and line endings
- Use more macros
- Purge another unneeded directory from sources
- Use C++14 flag

* Sat Nov 04 2017 Mattia Verga <mattia.verga@email.it> - 2.6.4-2
- Breakdown components licenses
- Add some useful docs
- Add weak dependency to libindi

* Thu Nov 02 2017 Mattia Verga <mattia.verga@email.it> - 2.6.4-1
- Initial packaging
