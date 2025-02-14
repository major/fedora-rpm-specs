Name:           siege
Version:        4.1.7
Release:        2%{?dist}
Summary:        HTTP regression testing and benchmarking utility

License:        GPL-3.0-or-later
URL:            http://www.joedog.org/JoeDog/Siege
Source0:        http://download.joedog.org/siege/%{name}-%{version}.tar.gz
Source1:        shell.m4
Patch0:         siege-4.1.7-bindir.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  libjoedog-devel

Requires:       libjoedog >= 0.1.2

%description
Siege is an HTTP regression testing and benchmarking utility.
It was designed to let web developers measure the performance of their code
under duress, to see how it will stand up to load on the internet.
Siege supports basic authentication, cookies, HTTP and HTTPS protocols.
It allows the user hit a web server with a configurable number of concurrent
simulated users. Those users place the web-server "under siege."

%prep
%autosetup
# Better default for log file (Bug 644631)
sed -i.orig doc/siegerc.in -e 's/^# logfile = *$/logfile = ${HOME}\/siege.log/'
rm -f *.m4
install -pm0644 %{SOURCE1} acinclude.m4
autoreconf -fiv

%build
export CFLAGS="-std=gnu17 %{build_cflags}"
%configure --sysconfdir=%{_sysconfdir}/siege
%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/siege
# Create /etc/siege/urls.txt
%make_install

%files
%doc AUTHORS ChangeLog README.md
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege.config
%{_bindir}/siege2csv.pl
%{_mandir}/man1/bombardment.1.*
%{_mandir}/man1/siege.1.*
%{_mandir}/man1/siege.config.1.*
%{_mandir}/man1/siege2csv.1.*
%dir %{_sysconfdir}/siege
%config(noreplace) %{_sysconfdir}/siege/urls.txt
%config(noreplace) %{_sysconfdir}/siege/siegerc

%changelog
* Wed Feb 12 2025 Björn Esser <besser82@fedoraproject.org> - 4.1.7-2
- Fix FTBFS
  Closes: rhbz#2341347

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Denis Fateyev <denis@fateyev.com> - 4.1.7-1
- Update to 4.1.7 (#2326279)
- Fix bindir value (#2256670)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.6-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.6-1
- Update to latest upstream release 4.1.6 (closes rhbz#2158611)

* Sat Aug 13 2022 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.5-1
- Update to latest upstream release 4.1.5 (closes rhbz#2114487)

* Mon Aug 01 2022 Denis Fateyev <denis@fateyev.com> - 4.1.4-1
- Update to 4.1.4 (#2112711)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.3-1
- Update to latest upstream release 4.1.3 (closes rhbz#2076069)

* Fri Mar 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.2-1
- Update to latest upstream release 4.1.2 (closes rhbz#2066434)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.1.1-2
- Rebuilt with OpenSSL 3.0.0

* Thu Aug 05 2021 Denis Fateyev <denis@fateyev.com> - 4.1.1-1
- Update to 4.1.1 (#1979058)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Denis Fateyev <denis@fateyev.com> - 4.0.9-1
- Update to 4.0.9 (#1950658)

* Mon Apr 12 2021 Denis Fateyev <denis@fateyev.com> - 4.0.8-1
- Update to 4.0.8 (#1940056)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.7-1
- Update to new upstream release 4.0.7 (rhbz#1855989)

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.6-1
- Update to new upstream release 4.0.6 (rhbz#1855989)

* Mon Feb 24 2020 Denis Fateyev <denis@fateyev.com> - 4.0.5-1
- Update to 4.0.5 (#1804857)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 4.0.4-1
- Update to 4.0.4 (#1490661)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.2-2
- Rebuild

* Sun May 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.2-1
- Update to new upstream release 4.0.2 (rhbz#1262154)

* Wed Mar 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.1-1
- Update to new upstream release 4.0.1 (rhbz#1262154)

* Wed Feb 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.4-1
- Update to new upstream release 3.1.4 (rhbz#1262154)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Roman Mohr <roman@fenkhuber.at> - 3.1.3-1
- Update to 3.1.3 (#1262154)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Roman Mohr <roman@fenkhuber.at> - 3.1.0-1
- Update to 3.1.0 (#1228251)

* Sun Jan 11 2015 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.9-1
- Update to new upstream release 3.0.9 (rhbz#1178439)

* Thu Sep 11 2014 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.8-1
- Update to new upstream release 3.0.8 (rhbz#1132901)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Roman Mohr <roman@fenkhuber.at> - 3.0.6-1
- upstream 3.0.6
- includes proxy directive
- adds support for HTTP-303

* Mon Nov 18 2013 Roman Mohr <roman@fenkhuber.at> - 3.0.5-1
- upstream 3.0.5
- removing siege-2.78-good.patch
- updating siege-libjoedog.patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Roman Mohr <roman@fenkhuber.at> - 3.0.1-2.beta4
- Bug 973822: use released libjoedog instead of bundled library
- no explicit copy of urls.txt and siegerc, make does this already
- fix wrong date in changelog

* Wed May  8 2013 Christof Damian <christof@damian.net> - 3.0.1-1.beta4
- upstream 3.0.1-beta4

* Thu Apr 18 2013 Christof Damian <christof@damian.net> - 3.0.0-2
- aarch64 patch

* Thu Apr 18 2013 Christof Damian <christof@damian.net> - 3.0.0-1
- upstream 3.0.0

* Tue Mar 19 2013 Christof Damian <christof@damian.net> - 2.78-2
- update patch

* Tue Mar 19 2013 Christof Damian <christof@damian.net> - 2.78-1
- upstream 2.78

* Fri Mar  1 2013 Christof Damian <christof@damian.net> - 2.75-1
- updstream 2.75

* Sat Feb 23 2013 Christof Damian <christof@damian.net> - 2.74-1
- upstream 2.74

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 2.72-2
- added dist tag again

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 2.72-1
- upstream 2.72

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-3.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-2.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec  4 2010 Christof Damian <christof@damian.net> - 2.71-1.b3%{?dist}
- upstream 2.71b3
- Bug 644631 - Bad default logfile path
- Bug 656320 - siege segfaults in glibc's getopt_long() -> __strncmp_sse2()

* Sat Jul 17 2010 Christof Damian <christof@damian.net> - 2.70-1
- upstream 2.70
- fix spelling

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.69-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul  4 2009 Allisson Azevedo <allisson@gmail.com> 2.69-1
- Update to 2.69
- Update Makefile.in patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 2.67-2
- rebuild with new openssl

* Fri May 16 2008 Allisson Azevedo <allisson@gmail.com> 2.67-1
- Update to 2.67
- Update License

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.66-3
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.66-2
 - Rebuild for deps

* Tue Apr 10 2007 Allisson Azevedo <allisson@gmail.com> 2.66-1
- Update to 2.66

* Tue Mar 27 2007 Allisson Azevedo <allisson@gmail.com> 2.65-3
- Fix .spec

* Tue Mar 27 2007 Allisson Azevedo <allisson@gmail.com> 2.65-2
- Fix .spec

* Sun Mar 11 2007 Allisson Azevedo <allisson@gmail.com> 2.65-1
- Initial RPM release
