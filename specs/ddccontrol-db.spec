Name:             ddccontrol-db
URL:              https://github.com/ddccontrol/ddccontrol-db
Version:          20250106
Release:          1%{?dist}
# Agreed by usptream to be GPLv2+
# http://sourceforge.net/mailarchive/message.php?msg_id=29762202
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
Summary:          DDC/CI control database for ddccontrol
Source0:          https://github.com/ddccontrol/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# use autopoint instead of gettextize that is interactive tool
BuildRequires:    gettext
BuildRequires:    gettext-devel
BuildRequires:    libtool
BuildRequires:    intltool
BuildRequires:    perl(XML::Parser)
BuildRequires:    gcc
BuildRequires:    make
BuildArch:        noarch

%description
DDC/CU control database for DDCcontrol.

%prep
%setup -q

./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/%{name}

%changelog
* Mon Jan  6 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 20250106-1
- New version
  Resolves: rhbz#2335819

* Tue Sep 24 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 20240920-1
- New version
  Resolves: rhbz#2313911

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 20240304-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 20240304-1
- New version
  Resolves: rhbz#2267854

* Wed Feb 14 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 20240209-1
- New version
  Resolves: rhbz#2263604

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20231004-1
- New version
  Resolves: rhbz#2242097

* Mon Sep 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230911-1
- New version
  Resolves: rhbz#2238704

* Fri Aug 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230821-1
- New version
  Resolves: rhbz#2233453

* Tue Aug  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230727-1
- New version
  Resolves: rhbz#2227117

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230627-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul  4 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230627-1
- This is new version of ddccontrol-db
  Resolves: rhbz#2218069

* Wed Apr 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230424-1
- New version
  Resolves: rhbz#2189471

* Tue Mar 28 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230328-1
- New version
  Resolves: rhbz#2182316

* Thu Mar  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230223-1
- New version
  Resolves: rhbz#2173147

* Thu Jan 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 20230124-1
- New version
  Resolves: rhbz#2124090

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220829-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 20220829-1
- New version
  Resolves: rhbz#2122446

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220629-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 20220629-1
- New version
  Resolves: rhbz#2102037

* Tue Apr 19 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 20220414-1
- New version
  Resolves: rhbz#2075645

* Thu Apr  7 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 20220406-1
- New version
  Resolves: rhbz#2055479

* Thu Jan 20 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 20220119-1
- New version
  Resolves: rhbz#2041455

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210812-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 20210812-1
- New version
  Resolves: rhbz#2013474

* Thu Aug  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 20210804-1
- New version
  Resolves: rhbz#1990127

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210505-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May  6 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 20210505-1
- New version
  Resolves: rhbz#1957541

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201221-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 20201221-1
- New version
  Resolves: rhbz#1909641

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190825-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190825-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 20190825-1
- New version
  Resolves: rhbz#1747028

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180602-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180602-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180602-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 20180602-1
- New version
  Resolves: rhbz#1587984

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171217-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 20171217-2
- Fixed URL

* Tue Dec 19 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 20171217-1
- New version
  Resolves: rhbz#1527446

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170716-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 20170716-1
- New version
- Dropped autopoint patch (not needed)

* Fri Jun 23 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-10.20170623git9dd986fb
- New snapshot
- New source URL (GitHub)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20061014-9.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20061014-8.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-7.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-6.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-5.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-4.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep  4 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-3.20120904gite8cc385a
- Updated to latest git head

* Tue Sep  4 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-2
- License tag changed to GPLv2+ (agreed by upstream)

* Wed Aug 29 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-1
- Initial version
