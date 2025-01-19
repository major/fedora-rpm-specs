%global ntp_version 4.2.8p18

Name:		ntp-refclock
Version:	0.6
Release:	7%{?dist}
Summary:	Drivers for hardware reference clocks
License:	BSD-2-Clause AND NTP AND BSD-3-Clause AND BSD-4-Clause AND Beerware
URL:		https://github.com/mlichvar/ntp-refclock
Source0:	https://github.com/mlichvar/ntp-refclock/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://downloads.nwtime.org/ntp/4.2.8/ntp-%{ntp_version}.tar.gz
Patch0:		ntp-refclock-configure-c99.patch

BuildRequires:	gcc make systemd pps-tools-devel

Requires(pre):	shadow-utils
Requires:	udev
%{?systemd_requires}

# The drivers and some code they need are from ntp
Provides:	bundled(ntp) = %{ntp_version}

%description
ntp-refclock is a wrapper for reference clock drivers included in the ntpd
daemon, which enables other NTP implementations to use the supported hardware
reference clocks for synchronization of the system clock.

It provides a minimal environment for the drivers to be able to run in a
separate process, measuring the offset of the system clock relative to the
reference clock and sending the measurements to another process controlling
the system clock.

%prep
%setup -q -a 1
ln -s ntp-%{ntp_version} ntp
# Avoid re-generating the configure scripts.
pushd ntp
preserve_timestamps="configure configure.ac sntp/configure sntp/m4/ntp_ipv6.m4"
for p in $preserve_timestamps ; do
    touch -r $p $p.timestamp
done
%patch -P0 -p1 -b .c99
for p in $preserve_timestamps ; do
    touch -r $p.timestamp $p
    rm $p.timestamp
done
popd

# Refer to packaged documentation for drivers
sed -i 's|<https:.*refclock.html>|in %{_pkgdocdir}/drivers/|' ntp-refclock.8

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow"

pushd ntp

%configure \
	--enable-all-clocks \
	--enable-parse-clocks \
	--disable-ATOM \
	--disable-LOCAL-CLOCK \
	--without-crypto \
	--without-threads \
	--without-sntp

sed -i 's/-Werror=format-security//g' sntp/libopts/Makefile

# Build only objects that may be linked with ntp-refclock
%make_build -C libntp
%make_build -C libparse
%make_build -C sntp/libopts
%make_build -C ntpd

popd

%make_build \
	CFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="$RPM_LD_FLAGS" \
	DEFAULT_USER=%{name} \
	DEFAULT_ROOTDIR=/usr/share/empty

%install
%make_install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig,udev/rules.d}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 644 -p examples/ntp-refclock.sysconfig \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ntp-refclock
install -m 644 -p examples/ntp-refclock.rules \
	$RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/80-ntp-refclock.rules
install -m 644 -p examples/ntp-refclock.service \
	$RPM_BUILD_ROOT%{_unitdir}/ntp-refclock.service
install -m 644 -p examples/pps-ldattach@.service \
	$RPM_BUILD_ROOT%{_unitdir}/pps-ldattach@.service

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	useradd -r -g %{name} -d / -s /sbin/nologin \
		-c "Reference clock driver" %{name}
:

%post
%systemd_post ntp-refclock.service

%preun
%systemd_preun ntp-refclock.service

%postun
%systemd_postun_with_restart ntp-refclock.service

%files
%license COPYRIGHT*
%doc README NEWS ntp/html/drivers
%config(noreplace) %{_sysconfdir}/sysconfig/ntp-refclock
%config(noreplace) %{_sysconfdir}/udev/rules.d/80-ntp-refclock.rules
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_unitdir}/*.service

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 27 2024 Miroslav Lichvar <mlichvar@redhat.com> 0.6-5
- update ntp to 4.2.8p18

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 01 2023 Miroslav Lichvar <mlichvar@redhat.com> 0.6-1
- update ntp-refclock to 0.6 and ntp to 4.2.8p16

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Florian Weimer <fweimer@redhat.com> - 0.5-5
- Port configure scripts to C99

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Miroslav Lichvar <mlichvar@redhat.com> 0.5-1
- update to 0.5
- package systemd unit files and udev rules

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Miroslav Lichvar <mlichvar@redhat.com> 0.4-1
- update ntp-refclock to 0.4 and ntp to 4.2.8p15

* Mon Mar 09 2020 Miroslav Lichvar <mlichvar@redhat.com> 0.3-1
- update ntp-refclock to 0.3 and ntp to 4.2.8p14
- enable SHM driver for testing

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Miroslav Lichvar <mlichvar@redhat.com> 0.2-5
- update ntp to 4.2.8p13

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.2-3
- update ntp to 4.2.8p12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.2-1
- update ntp-refclock to 0.2 and ntp to 4.2.8p11
- add gcc to build requirements

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.1-2
- provide bundled(ntp)
- don't duplicate _smp_mflags in CFLAGS

* Fri Jan 19 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.1-1.ntp4.2.8p10
- initial release
