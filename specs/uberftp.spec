Name:           uberftp
Version:        2.9.1
Release:        6%{?dist}
Summary:        GridFTP-enabled ftp client

License:        NCSA
URL:            https://gridcf.org/
Source0:        https://repo.gridcf.org/uberftp/sources/uberftp-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  globus-gssapi-gsi-devel

%description
UberFTP is the first interactive, GridFTP-enabled ftp client.
It supports GSI authentication, parallel data channels and
third party transfers.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/uberftp
%{_mandir}/man1/uberftp.1*
%doc Changelog.mssftp ChangeLog
%license COPYING

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Steve Traylen <steve.traylen@cern.ch> - 2.9.1-1
- Upstream to 2.9.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Steve Traylen <steve.traylen@cern.ch> - 2.9-1
- Upstream to 2.9

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 8 2021 Steve Traylen <steve.traylen@cern.ch> - 2.8-17
- Upstream is now GridCF project
  https://mailman.egi.eu/pipermail/discuss/2019-March/000273.html

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Steve Traylen <steve.traylen@cern.ch> - 2.8-13
- Make specfile more modern.

* Thu Jan 9 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 2.8-12
- Add patch to prevent hanging when command socket closes

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-2
- Adapt to Globus Toolkit 6.0

* Tue Sep 2 2014 Steve Traylen <steve.traylen@cern.ch> - 2.8-1
- Upstream to 2.8, upstream has moved to github.
- Add patch for 32 bit.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 2 2012 Steve Traylen <steve.traylen@cern.ch> - 2.6-4
- Adapt for globus toolkit 5.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 Steve Traylen <steve.traylen@cern.ch> - 2.6-1
- Update to uberftp-2.6

* Fri Sep 11 2009 Steve Traylen <steve.traylen@cern.ch> - 2.5-1
- Update to uberftp-2.5

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.4-5
- rebuilt with new openssl

* Wed Jul 22 2009 Steve Traylen <steve.traylen@cern.ch> 2.4-4
- Update source to version 2.4
- Include copyright file in package.

* Tue Jun 23 2009 Steve Traylen <steve.traylen@cern.ch> 2.3-3
- Better inclusion of globus header files.
* Fri Jun 19 2009 Steve Traylen <steve@traylen.net> -  2.3-2
- Remove my debugging.
* Fri Jun 19 2009 Steve Traylen <steve@traylen.net> -  2.3-1
- Initial version.


