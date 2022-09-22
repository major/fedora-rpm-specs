Name:		dhcpd-pools
Version:	3.2
Release:	2%{?dist}
Summary:	ISC dhcpd lease analysis and reporting
# BSD: dhcpd-pools
# ASL 2.0: mustache templating (https://gitlab.com/jobol/mustach) src/mustach.[ch]
# GPLv3+: gnulib (https://www.gnu.org/software/gnulib/) lib/
License:	BSD and ASL 2.0 and GPLv3+
URL:		http://dhcpd-pools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	uthash-devel
BuildRequires:	gcc, make
BuildRequires:	perl-generators
Provides:	bundled(gnulib)

%description
This is for ISC DHCP shared network and pool range usage analysis.  Purpose
of command is to count usage ratio of each IP range and shared network pool
which ISC dhcpd is in control of. Users of the command are most likely ISPs
and other organizations that have large IP space.

%prep
%setup -q

%build
# configure to match OS install defaults
# add -std=c99 for gnulib on EPEL7
%configure \
    CC="%{__cc} -std=c99" \
    --with-dhcpd-conf=%{_sysconfdir}/dhcp/dhcpd.conf \
    --with-dhcpd-leases=%{_localstatedir}/lib/dhcpd/dhcpd.leases

make %{?_smp_mflags}

%install
%make_install
# make install installs docs, let rpmbuild handle it
rm -rf %{buildroot}%{_docdir}/%{name}

# original encoding appears to be ISO8859-1
iconv --from=ISO8859-1 --to=UTF-8 THANKS > THANKS.utf8
touch --reference=THANKS THANKS.utf8
mv THANKS.utf8 THANKS

# add munin plugin but not executable
chmod -x contrib/munin_plugins/*

%check
make check-TESTS

%files
%license COPYING
%doc README THANKS TODO AUTHORS ChangeLog
%doc samples/*.template
%doc contrib/munin_plugins
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun  5 2022 Chris Adams <linux@cmadams.net> - 3.2-1
- new upstream version includes gnulib fix
- add munin plugins from contrib
- BR perl-generators since we install a perl script

* Wed Feb  2 2022 Chris Adams <linux@cmadams.net> - 3.1-6
- use updated gnulib cdefs.h to deal with ppc64le change
- run tests after build

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Björn Esser <besser82@fedoraproject.org> - 3.1-4
- Rebuild(uthash)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Chris Adams <linux@cmadams.net> - 3.1-1
- update to new upstream, use bundled gnulib
- include make build dependency
- add sample templates

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Chris Adams <linux@cmadams.net> - 3.0-3
- correct license tag and include info
- fix gnulib patch, add bundled provide
- convert THANKS character set
- add EPEL 6 support

* Mon Mar 09 2020 Chris Adams <linux@cmadams.net> - 3.0-2
- fix some notes from review request
- add patch for gnulib autoconf
- add -std=c99 for gnulib on EPEL7

* Mon Jan 27 2020 Chris Adams <linux@cmadams.net> - 3.0-1
- initial RPM

