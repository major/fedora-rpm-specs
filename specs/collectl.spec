Summary: A utility to collect various Linux performance data
Name: collectl
Version: 4.3.5
Release: 7%{?dist}
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
Source1: %{name}.service
Source2: %{name}.sysconfig
URL: http://collectl.sourceforge.net
BuildArch: noarch
BuildRequires: perl-generators
BuildRequires: systemd
Requires: perl(Sys::Syslog), perl(Time::HiRes), perl(Compress::Zlib)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A utility to collect Linux performance data


%prep
%setup -q -n %{name}

# rename directory for easier inclusion
mv docs html


%build
# nothing to do


%install
# create required directories
mkdir -p        $RPM_BUILD_ROOT%{_unitdir} \
                $RPM_BUILD_ROOT%{_sysconfdir} \
                $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
                $RPM_BUILD_ROOT%{_bindir} \
                $RPM_BUILD_ROOT%{_datadir}/%{name}/utils \
                $RPM_BUILD_ROOT%{_mandir}/man1/ \
                $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}

# install the files, setting the mode
install -p -m 755  collectl          $RPM_BUILD_ROOT%{_bindir}/
install -p -m 755  colmux            $RPM_BUILD_ROOT%{_bindir}/
install -p -m 644  *.ph              $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644  envrules.std      $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755  client.pl         $RPM_BUILD_ROOT%{_datadir}/%{name}/utils
install -p -m 644  man1/*.1          $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644  collectl.conf     $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644  %{SOURCE1}        $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644  %{SOURCE2}        $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 


%files
%doc ARTISTIC COPYING GPL RELEASE-collectl html
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/%{name}
%{_bindir}/colmux
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/colmux.1*
%{_localstatedir}/log/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 4.3.5-1
- Update to 4.3.5 (#2138458)

* Tue Aug 23 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4 (#2120875)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 Dan Horák <dan[at]danny.cz> - 4.3.3-1
- upgrade to upstream version 4.3.3 (#2071117)

* Fri Mar 11 2022 Dan Horák <dan[at]danny.cz> - 4.3.2-1
- upgrade to upstream version 4.3.2 (#2039370)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.3.1-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Dan Horák <dan[at]danny.cz> - 4.3.1-1
- upgrade to upstream version 4.3.1

* Tue Jun 11 2019 Dan Horák <dan[at]danny.cz> - 4.3.0-5
- update service type to forking (#1719168)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Dan Horák <dan[at]danny.cz> - 4.3.0-1
- upgrade to upstream version 4.3.0 (#1526650)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Dan Horák <dan[at]danny.cz> - 4.2.0-1
- upgrade to upstream version 4.2.0 (#1460836)

* Mon May 15 2017 Dan Horák <dan[at]danny.cz> - 4.1.3-1
- upgrade to upstream version 4.1.3 (#1450536)

* Tue Feb 28 2017 Dan Horák <dan[at]danny.cz> - 4.1.2-1
- upgrade to upstream version 4.1.2 (#1427343)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Dan Horák <dan[at]danny.cz> - 4.1.0-1
- upgrade to upstream version 4.1.0 (#1383847)

* Mon Jul 18 2016 Dan Horák <dan[at]danny.cz> - 4.0.5-1
- upgrade to upstream version 4.0.5 (#1356745)

* Mon May 23 2016 Dan Horák <dan[at]danny.cz> - 4.0.4-1
- upgrade to upstream version 4.0.4 (#1303367)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Dan Horák <dan[at]danny.cz> - 4.0.2-1
- upgrade to upstream version 4.0.2 (#1225669)

* Mon Apr 13 2015 Dan Horák <dan[at]danny.cz> - 4.0.0-2
- workaround perl dependency generator issue in EPEL <= 7

* Thu Apr 09 2015 Dan Horák <dan[at]danny.cz> - 4.0.0-1
- upgrade to upstream version 4.0.0 (#1201069)

* Mon Sep 15 2014 Dan Horák <dan[at]danny.cz> - 3.7.4-1
- upgrade to upstream version 3.7.4 (#1140499)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Dan Horák <dan[at]danny.cz> - 3.7.3-1
- upgrade to upstream version 3.7.3 (#1083898)

* Sat Oct 19 2013 Dan Horák <dan[at]danny.cz> - 3.6.9-1
- upgrade to upstream version 3.6.9

* Fri Oct 18 2013 Dan Horák <dan[at]danny.cz> - 3.6.8-1
- upgrade to upstream version 3.6.8

* Tue Sep 10 2013 Dan Horák <dan[at]danny.cz> - 3.6.7-4
- switch to systemd macros in scriptlets (#850063)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.6.7-2
- Perl 5.18 rebuild
- Build-require systemd-units

* Fri Mar 22 2013 Dan Horák <dan[at]danny.cz> - 3.6.7-1
- upgrade to upstream version 3.6.7

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Dan Horák <dan[at]danny.cz> - 3.6.5-1
- upgrade to upstream version 3.6.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Dan Horák <dan[at]danny.cz> - 3.6.3-1
- upgrade to upstream version 3.6.3

* Thu Feb 23 2012 Dan Horák <dan[at]danny.cz> - 3.6.1-1
- upgrade to upstream version 3.6.1

* Thu Feb 09 2012 Dan Horák <dan[at]danny.cz> - 3.6.0-3
- spec cleanup
- switch from initscript to systemd

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Dan Horák <dan[at]danny.cz> 3.6.0-1
- upgrade to upstream version 3.6.0

* Thu Aug 04 2011 Dan Horák <dan[at]danny.cz> 3.5.1-2
- updated for Perl 5.14

* Thu Jun 02 2011 Dan Horák <dan[at]danny.cz> 3.5.1-1
- upgrade to upstream version 3.5.1

* Fri Mar 25 2011 Dan Horák <dan[at]danny.cz> 3.5.0-1
- upgrade to upstream version 3.5.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 13 2010 Dan Horák <dan[at]danny.cz> 3.4.3-1
- upgrade to upstream version 3.4.3

* Wed Jul 21 2010 Dan Horák <dan[at]danny.cz> 3.4.2-1
- upgrade to upstream version 3.4.2

* Thu Apr  1 2010 Dan Horák <dan[at]danny.cz> 3.4.1-1
- upgrade to upstream version 3.4.1

* Wed Feb 17 2010 Dan Horák <dan[at]danny.cz> 3.4.0-1
- upgrade to upstream version 3.4.0
- updated directory layout to match upstream

* Tue Jan  5 2010 Dan Horák <dan[at]danny.cz> 3.3.6-1
- upgrade to upstream version 3.3.6

* Fri Aug 21 2009 Dan Horák <dan[at]danny.cz> 3.3.5-1
- upgrade to upstream version 3.3.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Dan Horák <dan[at]danny.cz> 3.3.4-2
- install only a symlink into /usr/bin (#508724)

* Mon Jun 15 2009 Dan Horák <dan[at]danny.cz> 3.3.4-1
- upgrade to upstream version 3.3.4
- changelog: http://collectl.sourceforge.net/Releases.html

* Wed Apr 29 2009 Dan Horák <dan[at]danny.cz> 3.3.2-1
- upgrade to upstream version 3.3.2
- install missing file
- changelog: http://collectl.sourceforge.net/Releases.html

* Tue Apr 28 2009 Dan Horák <dan[at]danny.cz> 3.3.1-1
- upgrade to upstream version 3.3.1
- changelog: http://collectl.sourceforge.net/Releases.html

* Sat Mar 21 2009 Dan Horak <dan[at]danny.cz> 3.2.1-1
- upgrade to upstream version 3.2.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Dan Horak <dan[at]danny.cz> 3.1.3-1
- upgrade to upstream version 3.1.3

* Tue Jan 20 2009 Dan Horak <dan[at]danny.cz> 3.1.2-1
- upgrade to upstream version 3.1.2

* Sat Nov  8 2008 Dan Horak <dan[at]danny.cz> 3.1.1-1
- upgrade to upstream version 3.1.1

* Mon Sep 22 2008 Dan Horak <dan[at]danny.cz> 3.1.0-1
- upgrade to upstream version 3.1.0
- remove logrotate support because internal mechanism is used by default

* Tue Jul  8 2008 Karel Zak <kzak@redhat.com> 3.0.0-1
- upgrade to upstream version 3.0.0

* Thu Jun 19 2008 Karel Zak <kzak@redhat.com> 2.6.4-1
- initial packaging (thanks to Dan Horak), based upon upstream srpm
