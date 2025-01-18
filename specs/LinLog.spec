Name:           LinLog
Version:        0.5
Release:        23%{?dist}
Summary:        A ham radio logbook for Linux

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://linlogbook.sourceforge.net/
Source0:        http://downloads.sourceforge.net/linlogbook/linlogbook-%{version}.tar.gz
Source1:        linlogbook.desktop
Source2:        linlogbook.png
Patch0:         LinLog-gcc11.patch

BuildRequires:  gcc-c++
BuildRequires:  qt4-devel >= 4.3
BuildRequires:  sqlite-devel >= 3
BuildRequires:  desktop-file-utils
BuildRequires:  libstdc++-devel
BuildRequires: make

%description
LinLogBook is a highly configurable amateur radio logbook for Linux.

It uses an sql-database to store its data. For the ease of use sqlite 3 is
used but it should be possible to use other databases like mysql, for instance.


%prep
%setup -q -n linlogbook
%patch -P0 -p1


%build
%{qmake_qt4} -o Makefile linlogbook.pro
make %{?_smp_mflags}


%install
install -p -d %{buildroot}%{_bindir}
install -p -m 755 bin/linlogbook %{buildroot}%{_bindir}/linlogbook

# no upstream .desktop or icon yet
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/linlogbook.png
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 sql/basetables.sql %{buildroot}%{_datadir}/%{name}
install -p -m 644 sql/example.sql %{buildroot}%{_datadir}/%{name}
install -p -m 644 sql/statistics.sql %{buildroot}%{_datadir}/%{name}


%files
%license COPYING
%doc ChangeLog README 
%{_bindir}/linlogbook
%{_datadir}/pixmaps/linlogbook.png
%{_datadir}/applications/linlogbook.desktop
%{_datadir}/%{name}
%{_datadir}/%{name}/*.sql


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.5-12
- Avoid ordered comparisons against zero

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Richard Shaw <hobbes1069@gmail.com> - 0.5-2
- Fix desktop file to correct binary and icon after upstream rename.

* Thu Jul 30 2015 Richard Shaw <hobbes1069@gmail.com> - 0.5-1
- Update to latest upstream release.

* Wed Jan 16 2013 Richard Shaw <hobbes1069@gmail.com> - 0.4-10
- Fix qmake build to respect required build flags.
- Don't pull in sql files twice.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 2 2011 Randall J. Berry <dp67@fedoraproject.org> - 0.4-5
- Rebuild for broken deps

* Thu Nov 26 2009 Lucian Langa <cooly@gnome.eu.org> - 0.4-4
- improve desktop icon (#530836)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Sindre Pedersen Bjordal <sindrepb@fedoraproject.org> - 0.4-1
- New upstream release

* Mon Sep 22 2008 Lucian Langa <cooly@gnome.eu.org> - 0.3.1-1
- new upstream 0.3.1
- add missing sql files
- fixed rpm macros
- fix build requires
- fix desktop file

* Sat Feb 25 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.3-4
- Correct Lic. per Review

* Sat Feb 25 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.3-3
- Submit for Review

* Sat Feb 25 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.3-2
- Add .desktop file and icon

* Sat Feb 16 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.3-1
- Version Update
- Submit for review

* Mon Jan 07 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.2-1
- Version Update

* Thu Dec 06 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.1.2-2
- rpmlint clean up

* Thu Dec 06 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.1.2-1
- Initial SPEC
