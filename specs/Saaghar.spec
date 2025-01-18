Name:           Saaghar
Version:        3.0.0
Release:        22%{?dist}
Summary:        A Cross-Platform Persian Poetry Software

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://pozh.org/saaghar/
Source0:        https://github.com/srazi/Saaghar/releases/download/v%{version}/Saaghar-%{version}.tar.gz
# Fedora specific: do not install doc files
Patch0:         %{name}-installfix.patch

BuildRequires: make
BuildRequires:  gcc-c++ qt-devel desktop-file-utils phonon-devel
Recommends:     %{name}-data

%description
Saaghar is a cross-platform Persian poetry software. It uses 
http://ganjoor.net database. It has lots of features:
* Tabbed UI
* Tabbed and dock-able search widgets
* Print and Print Preview
* Export, It supports exporting to "PDF", "HTML", "TeX", "CSV" and "TXT"
* Copy and Multi-selection
* Customisable interface

%package        data
Version:        67.92.11
Release:        21.%{release}
Summary:        Database for %{name}
BuildArch:      noarch
Source1:        http://downloads.sourceforge.net/saaghar/%{name}-data-%{version}.xz

%description    data
This package contains the database for %{name}.

%prep
%setup -q -n %{name}
%patch -P0 -p1 -b .installfix
xz -dc %{SOURCE1} > data/ganjoor.s3db
chmod a-x data/Saaghar.desktop
sed -i.dosfix "s/\r//g" data/Saaghar.desktop
rm -rf data/fonts/

%build
%{qmake_qt4} -config release
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}
install -Dp -m 0644 data/ganjoor.s3db %{buildroot}%{_datadir}/saaghar/

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS GPLv3 CHANGELOG README.md TODO LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/saaghar/themes
%{_datadir}/saaghar/*.pdf
%{_datadir}/saaghar/*.qm
%{_datadir}/saaghar/*.gdb
%dir %{_datadir}/saaghar

%files data
%{_datadir}/saaghar/ganjoor.s3db

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 67.92.11-20.21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.0-5
- Add gcc-c++ build dependency

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.94-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.94-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.94-12
- use %%qmake_qt4 macro to ensure proper build flags

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.94-10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.94-4
- Fix -data subpackage release tag so it'll be automatically incremented when
  base package release changes. It should be still manually incremented for new
  versions. :( It must be a separate package completely.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.94-1
- Updated to upstream version 1.0.94
- Files are not executable anymore, so removed the chmod section
- Applied patch has become smaller

* Sun Nov 20 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.69-1
- Updated to Saaghar version 0.9.69 and db version 59.90.07

* Wed May 25 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.8.21-1
- Updated to 0.8.21 version
- Add a separate version tag for data sub-package

* Sat Apr 30 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.8.13-1
- Update to latest upstream version
- Updated the project's URL
- Added desktop-file-utils build dependency

* Mon Mar 14 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.2-2.1051
- A little cleaning up
- Adding comments for patches
- Validating installed .desktop file

* Fri Feb 18 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.2-1
- Initial version

