%global commit aaf21ba3426b9cc612e7bc8c87ed5beb160e0cdc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1
Name:           dnstop
Version:        20140915
Release:        25.git20240708%{?dist}
Summary:        Displays information about DNS traffic on your network
License:        BSD-3-Clause
URL:            http://dns.measurement-factory.com/tools/dnstop/
Source0:        https://github.com/measurement-factory/dnstop/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  make


%description
dnstop is a libpcap application (ala tcpdump) that displays various
tables of DNS traffic on your network.

dnstop supports both IPv4 and IPv6 addresses.

To help find especially undesirable DNS queries, dnstop provides a
number of filters.

dnstop can either read packets from the live capture device, or from a
tcpdump savefile.


%prep
%autosetup -n %{name}-%{commit}

%build
%configure
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%make_install

%files
%{_bindir}/dnstop
%{_mandir}/man8/dnstop.8*

%doc CHANGES README.md
%license LICENSE


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-25.git20240708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 05 2024 Denis Fateyev <denis@fateyev.com> - 20140915-24.git20240708
- Update to latest git HEAD
- Modernize the package spec

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 20140915-23.git20201122
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-22.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-21.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-20.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-19.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-18.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-17.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-16.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-15.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-14.git20201122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 20140915-13.git20201122
- Update to latest git HEAD

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140915-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140915-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 15 2014 Paul Wouters <pwouters@redhat.com> - 20140915-1
- Updated to 20140915 with new-gtlds filter support
- Updated warning patch (partially merged upstream)
- Added usage patch that was missing the new filter name new-gtlds
- Enabled hardening as this application takes in network input.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Conrad Meyer <cemeyer@uw.edu> - 20121017-4
- Actual cleanup; drop EL5-age SPEC bits

* Mon Mar 03 2014 Denis Fateyev <denis@fateyev.com> - 20121017-3
- Spec cleanup, epel branches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 17 2013 Conrad Meyer <cemeyer@uw.edu> - 20121017-1
- Bump to latest upstream version
- Fix build (latest dnstop correctly prefixes mandir, bindir with DESTDIR)
- Fix warnings (pointer target signedness, unchecked read(2))

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 16 2011 Conrad Meyer <konrad@tylerc.org> - 20110502-1
- Bump to latest upstream version.

* Fri Mar 25 2011 Niels de Vos <devos@fedoraproject.org> - 20090128-3
- Fiy Failed To Build From Source (#660807)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090128-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 24 2009 Conrad Meyer <konrad@tylerc.org> - 20090128-1
- Initial package.
