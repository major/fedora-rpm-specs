%global revision 20240501
Name:           tack
Version:        1.10
Release:        3.%{revision}%{?dist}
Summary:        Terminfo action checker

License:        GPL-2.0-only
URL:            https://invisible-island.net/ncurses/tack.html
Source0:        https://invisible-mirror.net/archives/ncurses/current/tack-%{version}-%{revision}.tgz

BuildRequires: make
BuildRequires:  gcc ncurses-devel

%description
The tack program has three purposes: to help you build a new terminfo
entry describing an unknown terminal, to test the correctness of an
existing entry, and to develop the correct pad timings needed to ensure
that screen updates don't fall behind the incoming data stream.

%prep
%setup -q -n %{name}-%{version}-%{revision}

%build
%configure --with-ncurses
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS CHANGES COPYING HISTORY README
%{_bindir}/tack
%{_mandir}/man1/tack.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3.20240501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2.20240501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 02 2024 Miroslav Lichvar <mlichvar@redhat.com> 1.10-1.20240501
- update to 1.10-20240501

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-16.20230201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Miroslav Lichvar <mlichvar@redhat.com> 1.09-15.20230201
- convert license tag to SPDX
- update to 1.09-20230201

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-14.20220528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-13.20220528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-12.20220528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Miroslav Lichvar <mlichvar@redhat.com> 1.09-11.20220528
- update to 1.09-20220528

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-10.20210619
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-9.20210619
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.09-8.20210619
- update to 1.09-20210619

* Thu May 20 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.09-7.20210429
- update to 1.09-20210429

* Thu Mar 25 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.09-6.20210324
- update to 1.09-20210324

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-5.20201128
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.09-4.20201128
- update to 1.09-20201128

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3.20200220
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.09-2.20200220
- update to 1.09-20200220

* Mon Feb 10 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.09-1.20200202
- update to 1.09-20200202

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-8.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Miroslav Lichvar <mlichvar@redhat.com> 1.08-7.20190721
- update to 1.08-20190721

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-6.20170726
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.08-5.20170726
- add gcc to build requirements

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-4.20170726
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-3.20170726
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2.20170726
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Miroslav Lichvar <mlichvar@redhat.com> 1.08-1.20170726
- update to 1.08-20170726

* Fri May 26 2017 Miroslav Lichvar <mlichvar@redhat.com> 1.07-15.20170318
- update to 1.07-20170318

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-14.20150606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-13.20150606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 05 2015 Miroslav Lichvar <mlichvar@redhat.com> 1.07-12.20150606
- update to 1.07-20150606

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-11.20130713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 12 2014 Miroslav Lichvar <mlichvar@redhat.com> 1.07-10.20130713
- update to 1.07-20130713

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 05 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.07-6
- update config.guess and config.sub for aarch64 (#926606)
- remove obsolete macros

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 05 2010 Miroslav Lichvar <mlichvar@redhat.com> 1.07-1
- update to 1.07

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.06-2
- Autorebuild for GCC 4.3

* Tue Sep 11 2007 Miroslav Lichvar <mlichvar@redhat.com> 1.06-1
- initial release
