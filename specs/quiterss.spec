Name:		quiterss
Version:	0.19.4
Release:	14%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
Summary:	RSS/Atom aggregator
URL:		http://quiterss.org/
Source0:	https://github.com/QuiteRSS/quiterss/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# sqlite-devel
BuildRequires: make
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qtsingleapplication-qt5-devel
# qt5-qtwebkit-devel
BuildRequires:  pkgconfig(Qt5WebKit)
# qt5-qtmultimedia-devel
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  qt5-linguist
BuildRequires:	desktop-file-utils

%description
Qt-based RSS/Atom aggregator.

%prep
%autosetup
# be asure
rm -rf 3rdparty/{qtsingleapplication,sqlite}

%build
%{qmake_qt5} PREFIX=%{_prefix} SYSTEMQTSA=True

%make_build release

%install
make install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/sound/
%{_datadir}/%{name}/style/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19.4-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 TI_Eugene <ti.eugene@gmail.com> - 0.19.4-1
- Version bump

* Wed Jan 29 2020 TI_Eugene <ti.eugene@gmail.com> - 0.19.2-3
- Fixed: import data from 18.x

* Wed Jan 29 2020 TI_Eugene <ti.eugene@gmail.com> - 0.19.2-2
- Bug fixes with intermediate git commits

* Tue Dec 17 2019 TI_Eugene <ti.eugene@gmail.com> - 0.19.2-1
- Version bump

* Sun Nov 17 2019 TI_Eugene <ti.eugene@gmail.com> - 0.19.0-1
- Version bump
- Switch to Qt5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.18.12-3
- rebuild for fixed buildsys/toolchain (#1705060)
- use %%make_build

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 TI_Eugene <ti.eugene@gmail.com> - 0.18.12-1
- Version bump

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 TI_Eugene <ti.eugene@gmail.com> - 0.18.9-1
- Version bump

* Fri Aug 25 2017 TI_Eugene <ti.eugene@gmail.com> - 0.18.8-1
- Version bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 10 2016 TI_Eugene <ti.eugene@gmail.com> - 0.18.4-1
- Version bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.18.2-2
- use %%qmake_qt4 macro to ensure proper build flags

* Tue Oct 06 2015 TI_Eugene <ti.eugene@gmail.com> - 0.18.2-1
- Version bump
- all patches removed

* Tue Jun 30 2015 TI_Eugene <ti.eugene@gmail.com> - 0.17.7-1
- Version bump
- some spec fixes

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.17.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 15 2015 TI_Eugene <ti.eugene@gmail.com> - 0.17.6-1
- Version bump

* Mon Jan 19 2015 TI_Eugene <ti.eugene@gmail.com> - 0.17.4-1
- Version bump

* Tue Nov 18 2014 TI_Eugene <ti.eugene@gmail.com> - 0.17.1-1
- Version bump

* Tue Sep 23 2014 TI_Eugene <ti.eugene@gmail.com> - 0.17.0-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 TI_Eugene <ti.eugene@gmail.com> - 0.16.1-1
- Version bump

* Fri Jun 13 2014 TI_Eugene <ti.eugene@gmail.com> - 0.16.0-1
- Version bump

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 TI_Eugene <ti.eugene@gmail.com> - 0.15.4-1
- Version bump

* Thu Mar 20 2014 TI_Eugene <ti.eugene@gmail.com> - 0.15.2-1
- Version bump

* Fri Jan 31 2014 TI_Eugene <ti.eugene@gmail.com> - 0.14.3-1
- Version bump

* Fri Jan 03 2014 TI_Eugene <ti.eugene@gmail.com> - 0.14.2-1
- Version bump

* Sun Dec 08 2013 TI_Eugene <ti.eugene@gmail.com> - 0.14.1-1
- Version bump
- phonon-devel BR added

* Sat Nov 16 2013 TI_Eugene <ti.eugene@gmail.com> - 0.14.0-1
- Version bump

* Sat Aug 31 2013 TI_Eugene <ti.eugene@gmail.com> - 0.13.3-1
- Version bump

* Wed Jul 31 2013 TI_Eugene <ti.eugene@gmail.com> - 0.13.2-1
- Version bump

* Mon Jul 01 2013 TI_Eugene <ti.eugene@gmail.com> - 0.13.1-1
- Version bump

* Sat Jun 01 2013 TI_Eugene <ti.eugene@gmail.com> - 0.13.0-1
- Version bump

* Tue May 07 2013 TI_Eugene <ti.eugene@gmail.com> - 0.12.5-3
- icon scriptlet update

* Sun May 05 2013 TI_Eugene <ti.eugene@gmail.com> - 0.12.5-2
- qmake-qt4 used directly
-_smp_flags added to make

* Sat Apr 27 2013 TI_Eugene <ti.eugene@gmail.com> - 0.12.5-1
- initial packaging for Fedora
