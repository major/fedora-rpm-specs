Name:           crossfire-maps
Version:        1.71.0
Release:        20%{?dist}
Summary:        Map files for the crossfire server

# All files GPL+ except python/misc/CFInsulter.py which is BSD
License:        GPL-2.0-or-later
URL:            http://crossfire.real-time.com
Source0:        http://downloads.sourceforge.net/crossfire/crossfire-%{version}.maps.tar.bz2
Patch0:		crossfire-maps-1.60.0-python.patch
BuildArch:      noarch
BuildRequires:      perl-generators
# Requires for directory ownership
Requires:       crossfire
Obsoletes:      crossfire-maps-devel

%description
Map files for the crossfire server.

%prep
%setup -q -c -n %{name}-%{version}

%patch -P0 -p0

chmod -x maps/python/IPO/README
chmod -x maps/python/IPO/*.py
chmod -x maps/scorn/misc/beginners2
chmod -x maps/styles/monsterstyles/sylvan/*
chmod -x maps/planes/*
chmod -x maps/pup_land/s_f/*
chmod -x maps/pup_land/ancient/castle/*
chmod -x maps/pup_land/ancient/volcano/*
chmod -x maps/pup_land/ancient/mountain/*
chmod -x maps/pup_land/lone_town/cave/*
chmod -x maps/templates/keep/*.tpl
#chmod -x maps/templates/guild/bigchest
chmod -x maps/navar_city/troll_canyon/*
chmod -x maps/brest/sow/sow.1
chmod -x maps/lake_country/elven_moon/*
#chmod -x maps/unlinked/casino/casino_infernal
chmod -x maps/santo_dominion/shaft/*
chmod -x maps/santo_dominion/temple_naive/*
chmod -x maps/darcap/temple_justice/*
chmod -x maps/brest/sow/sow

%{__sed} -i 's/\r//' maps/templates/keep/keep1.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep2.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep3.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep_b.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep_roof.tpl

%build
# Nothing to build!


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/crossfire
cp -a maps $RPM_BUILD_ROOT%{_datadir}/crossfire/
rm -f $RPM_BUILD_ROOT%{_datadir}/crossfire/maps/COPYING



%files
%doc maps/COPYING
%{_datadir}/crossfire/maps

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.71.0-15
- SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 01 2016 Jon Ciesla <limburgher@gmail.com> - 1.71.0-1
- New upstream.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.70.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.70.0-4
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.70.0-1
- New upstream.

* Wed Jan 11 2012 Jon Ciesla <limburgher@gmail.com> - 1.60.0-1
- New upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Wart <wart@kobold.org> 1.11.0-1
- Update to 1.11.0

* Sat Aug 18 2007 Wart <wart@kobold.org> 1.10.0-3
- License tag clarification

* Wed Jul 11 2007 Wart <wart@kobold.org> 1.10.0-2
- Add Requires: on the game server for proper directory ownership

* Tue May 22 2007 Wart <wart@kobold.org> 1.10.0-1
- Update to 1.10.0

* Mon Jul 10 2006 Wart <wart@kobold.org> 1.9.1-2
- Remove unnecessary 'Provides: crossfire-maps-devel'

* Thu Jul 6 2006 Wart <wart@kobold.org> 1.9.1-1
- Update to 1.9.1, which now includes a license file.
- Obsolete the -devel subpackage since upstream now requires some of the
  map devel files for non-devel purposes.

* Thu Mar 9 2006 Wart <wart@kobold.org> 1.9.0-1
- Initial spec file following Fedora Extras conventions
