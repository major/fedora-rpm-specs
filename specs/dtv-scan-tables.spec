%global date 2024-03-24
%global git 7098bdd27548

#WARNING: should be monotonically incremented
%global rel 11

# WARNING: You should probably never touch those fields
Version:	1
Name:		dtv-scan-tables
Summary:	Digital TV scan tables
Release:	%{rel}.%(echo %{date} | tr -d -)git%{git}%{?dist}.1

#2013-07-19: License discussed in: https://bugzilla.redhat.com/show_bug.cgi?id=986051#c4
#and https://gitlab.com/fedora/legal/fedora-license-data/-/issues/580#note_2155500881
License:	LicenseRef-Not-Copyrightable
URL:		https://git.linuxtv.org/dtv-scan-tables.git
Source0:	https://linuxtv.org/downloads/dtv-scan-tables/dtv-scan-tables-%{date}-%{git}.tar.bz2
BuildArch:	noarch
%if 0%{?fedora} >= 40
BuildRequires:	dvb-tools
%else
BuildRequires:	v4l-utils >= 1.4.0
%endif
BuildRequires:  make
# FPC permission for Conflicts:
# https://lists.fedoraproject.org/pipermail/packaging/2013-July/009346.html
# https://fedorahosted.org/fpc/ticket/316
Conflicts:	dvb-apps < 1.1.2-6.1488.f3a70b206f0f

%description
This package contains digital TV scan tables that are used by TV applications
to scan for channels.

%package legacy
Summary:	Digital TV scan tables in the legacy DVBv3 format

%description legacy
This package contains digital TV scan tables that are used by TV applications
to scan for channels in the legacy DVBv3 format, compatible with the old
dvb-apps.

%prep
%setup -T -c
%{__tar} xf %{SOURCE0} --transform="s,/usr/share/dvb/,,"

%build
make dvbv3

%install
make DATADIR=%{buildroot}/%{_datadir} install install_v3

%files legacy
%license COPYING COPYING.LGPL
%{_datadir}/dvbv3/

%files
%license COPYING COPYING.LGPL
%{_datadir}/dvbv5/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-11.20240324git7098bdd27548.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 Xavier Bachelot <xavier@bachelot.org> - 1-11.20240324git7098bdd27548
- Update to 2024-03-24 (RHBZ#2249290)
- Fix FTBFS on F40+ (RHBZ#2300632)
- Fix bogus date in %%changelog

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220311git04b8c9ae856e.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220311git04b8c9ae856e.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220311git04b8c9ae856e.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220311git04b8c9ae856e.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220311git04b8c9ae856e.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220311git04b8c9ae856e.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Mauro Carvalho Chehab <m.chehab@samsung.com> - 1-10.20220311git04b8c9ae856e
- Update to the latest release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20190922gitf07bde777d4d.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20190922gitf07bde777d4d.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20190922gitf07bde777d4d.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20190922gitf07bde777d4d.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20190922gitf07bde777d4d.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 22 2019 Mauro Carvalho Chehab <m.chehab@samsung.com> - 1-10.20190922gitf07bde777d4d
- Update to the latest release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-9.20180606gitc2b6af67f7d8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-9.20180606gitc2b6af67f7d8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Mauro Carvalho Chehab <m.chehab@samsung.com> - 1-9.20180606gitc2b6af6
- Update to latest release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-2.20171226git07b18ecef174
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Till Maas <opensource@till.name> - - 1-1.20171207gitb18ecef174
- Update to new release
- Update URLs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-8.20161007git0b42d8e8b44e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-7.20161007git0b42d8e8b44e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-6.20161007git0b42d8e8b44e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Ville Skyttä <ville.skytta@iki.fi> - 1-5.20161007git0b42d8e8b44e
- Update to 2016-10-07-0b42d8e8b44e

* Sun Oct  9 2016 Ville Skyttä <ville.skytta@iki.fi> - 1-5.20160731gitb00d55fab082
- Update to 2016-07-31-b00d55fab082

* Tue Mar 01 2016 Mauro Carvalho Chehab <m.chehab@samsung.com> - 1-5.20160106git9d6094a7c41e
- Update to the latest release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-4.20151108gitfe6079b60c6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Ville Skyttä <ville.skytta@iki.fi> - 1-3.20151108gitfe6079b60c6b
- Update to 2015-11-08-fe6079b60c6b, ship COPYING* as %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-3.20140905git4aad313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 27 2014 Mauro Carvalho Chehab <m.chehab@samsung.com> - 1-2.20140905git4aad313
- Update to latest release and create a package for the legacy format

* Sun Aug 31 2014 Till Maas <opensource@till.name> - 0-7.20140512git1246b27
- Update to latest release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.20140309git177b522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Mauro Carvalho Chehab <m.chehab@samsung.com> 0-5.20140309git177b522
- Update to the latest DTV tables

* Mon Jan 13 2014 Till Maas <opensource@till.name> - 0-4.20130713gitd913405
- Update Conflicts
- Move license files to %%{_pkgdocdir}

* Fri Nov 08 2013 Till Maas <opensource@till.name> - 0-3.20130713gitd913405
- Include date and git hash in changelog
- Update Conflicts

* Fri Nov 01 2013 Till Maas <opensource@till.name> - 0-2
- Update license

* Thu Jul 18 2013 Till Maas <opensource@till.name> - 0-1
- initial Package
