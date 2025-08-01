%global _hardened_build 1
%global testsuite_ver d27dbd
%global clknetsim_ver 64df92
%global selinuxtype targeted
%bcond_without selinux

Name:		linuxptp
Version:	4.4
Release:	7%{?dist}
Summary:	PTP implementation for Linux

License:	GPL-2.0-or-later
URL:		https://www.linuxptp.org/

Source0:	https://downloads.nwtime.org/%{name}/%{name}-%{version}.tgz
Source1:	phc2sys.service
Source2:	ptp4l.service
Source3:	timemaster.service
Source4:	timemaster.conf
Source5:	ptp4l.conf
Source6:	ts2phc.service
Source7:	ts2phc.conf
# external test suite
Source10:	https://github.com/mlichvar/linuxptp-testsuite/archive/%{testsuite_ver}/linuxptp-testsuite-%{testsuite_ver}.tar.gz
# simulator for test suite
Source11:	https://github.com/mlichvar/clknetsim/archive/%{clknetsim_ver}/clknetsim-%{clknetsim_ver}.tar.gz
# selinux policy
Source20:	linuxptp.fc
Source21:	linuxptp.if
Source22:	linuxptp.te

BuildRequires:	gcc gcc-c++ gnutls-devel make systemd

%{?systemd_requires}

%if 0%{?with_selinux}
Requires:	(%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

%description
This software is an implementation of the Precision Time Protocol (PTP)
according to IEEE standard 1588 for Linux. The dual design goals are to provide
a robust implementation of the standard and to use the most relevant and modern
Application Programming Interfaces (API) offered by the Linux kernel.
Supporting legacy APIs and other platforms is not a goal.

%if 0%{?with_selinux}
%package selinux
Summary:	linuxptp SELinux policy
BuildArch:	noarch
Requires:	selinux-policy-%{selinuxtype}
Requires(post):	selinux-policy-%{selinuxtype}
BuildRequires:	selinux-policy-devel
%{?selinux_requires}

%description selinux
linuxptp SELinux policy module

%endif

%prep
%setup -q -a 10 -a 11 -n %{name}-%{!?gitfullver:%{version}}%{?gitfullver}
# disable nettle support in favor of gnutls
sed -i 's|find .*"nettle"|true|' incdefs.sh

mv linuxptp-testsuite-%{testsuite_ver}* testsuite
mv clknetsim-%{clknetsim_ver}* testsuite/clknetsim

pushd testsuite/clknetsim
popd

mkdir selinux
cp -p %{SOURCE20} %{SOURCE21} %{SOURCE22} selinux

%build
%{make_build} \
	EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
	EXTRA_LDFLAGS="$RPM_LD_FLAGS"

%if 0%{?with_selinux}
make -C selinux -f %{_datadir}/selinux/devel/Makefile linuxptp.pp
bzip2 -9 selinux/linuxptp.pp
%endif

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/sysconfig,%{_unitdir},%{_mandir}/man5}
install -m 644 -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_unitdir}
install -m 644 -p %{SOURCE4} %{SOURCE5} %{SOURCE7} \
	$RPM_BUILD_ROOT%{_sysconfdir}

echo 'OPTIONS="-f /etc/ptp4l.conf"' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ptp4l
echo 'OPTIONS="-a -r"' > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/phc2sys
echo 'OPTIONS="-f /etc/ts2phc.conf"' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ts2phc

for s in ptp4l timemaster ts2phc; do
	echo ".so man8/$s.8" > $RPM_BUILD_ROOT%{_mandir}/man5/$s.conf.5
done

%if 0%{?with_selinux}
install -D -m 0644 selinux/linuxptp.pp.bz2 \
	$RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{selinuxtype}/linuxptp.pp.bz2
install -D -p -m 0644 selinux/linuxptp.if \
	$RPM_BUILD_ROOT%{_datadir}/selinux/devel/include/distributed/linuxptp.if
%endif

%check
cd testsuite
# set random seed to get deterministic results
export CLKNETSIM_RANDOM_SEED=26743
%{make_build} -C clknetsim
PATH=..:$PATH ./run

%post
%systemd_post phc2sys.service ptp4l.service timemaster.service ts2phc.service

%preun
%systemd_preun phc2sys.service ptp4l.service timemaster.service ts2phc.service

%postun
%systemd_postun_with_restart phc2sys.service ptp4l.service timemaster.service ts2phc.service

%if 0%{?with_selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/linuxptp.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
	%selinux_modules_uninstall -s %{selinuxtype} linuxptp
	%selinux_relabel_post -s %{selinuxtype}
fi

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/linuxptp.pp.*
%{_datadir}/selinux/devel/include/distributed/linuxptp.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/linuxptp

%endif

%files
%license COPYING
%doc README.org configs
%config(noreplace) %{_sysconfdir}/ptp4l.conf
%config(noreplace) %{_sysconfdir}/sysconfig/phc2sys
%config(noreplace) %{_sysconfdir}/sysconfig/ptp4l
%config(noreplace) %{_sysconfdir}/sysconfig/ts2phc
%config(noreplace) %{_sysconfdir}/timemaster.conf
%config(noreplace) %{_sysconfdir}/ts2phc.conf
%{_unitdir}/phc2sys.service
%{_unitdir}/ptp4l.service
%{_unitdir}/timemaster.service
%{_unitdir}/ts2phc.service
%{_sbindir}/hwstamp_ctl
%{_sbindir}/nsm
%{_sbindir}/phc2sys
%{_sbindir}/phc_ctl
%{_sbindir}/pmc
%{_sbindir}/ptp4l
%{_sbindir}/timemaster
%{_sbindir}/ts2phc
%{_sbindir}/tz2alt
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
* Mon Jul 28 2025 Miroslav Lichvar <mlichvar@redhat.com> 4.4-7
- add timemaster service interfaces to selinux policy (Zdenek Pytela)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 08 2025 Miroslav Lichvar <mlichvar@redhat.com> 4.4-5
- add ts2phc service and default configs

* Mon Feb 03 2025 Miroslav Lichvar <mlichvar@redhat.com> 4.4-4
- update selinux policy to allow ptp4l to use generic netlink sockets
- harden systemd services

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 12 2024 Miroslav Lichvar <mlichvar@redhat.com> 4.4-2
- update selinux policy from https://github.com/fedora-selinux/selinux-policy

* Mon Sep 09 2024 Miroslav Lichvar <mlichvar@redhat.com> 4.4-1
- update to 4.4

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Miroslav Lichvar <mlichvar@redhat.com> 4.3-1
- update to 4.3
- switch COPYING from doc to license

* Tue Apr 16 2024 Miroslav Lichvar <mlichvar@redhat.com> 4.2-5
- disable mode verification of selinux module directory

* Wed Mar 20 2024 Miroslav Lichvar <mlichvar@redhat.com> 4.2-4
- update selinux policy from https://github.com/fedora-selinux/selinux-policy

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Miroslav Lichvar <mlichvar@redhat.com> 4.2-1
- update to 4.2
- update default ptp4l.conf

* Wed Sep 06 2023 Miroslav Lichvar <mlichvar@redhat.com> 4.1-1
- update to 4.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Miroslav Lichvar <mlichvar@redhat.com> 4.0-1
- update to 4.0
- convert license tag to SPDX
- update URL to https

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Miroslav Lichvar <mlichvar@redhat.com> 3.1.1-6
- update selinux policy (#2159919)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Miroslav Lichvar <mlichvar@redhat.com> 3.1.1-4
- fix tests on ppc64le (#2046706)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Miroslav Lichvar <mlichvar@redhat.com> 3.1.1-2
- package selinux policy

* Wed Jul 07 2021 Miroslav Lichvar <mlichvar@redhat.com> 3.1.1-1
- update to 3.1.1 (CVE-2021-3570, CVE-2021-3571)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Feb 25 2021 Miroslav Lichvar <mlichvar@redhat.com> 3.1-3
- fix handling of zero-length messages
- minimize default configuration
- remove obsolete build requirement

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Miroslav Lichvar <mlichvar@redhat.com> 3.1-1
- update to 3.1

* Mon Jul 27 2020 Miroslav Lichvar <mlichvar@redhat.com> 3.0-1
- update to 3.0

* Mon Feb 03 2020 Miroslav Lichvar <mlichvar@redhat.com> 2.0-7.20191225gite05809
- update to 20191225gite05809
- fix testing with new glibc

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6.20190912git48e605
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Miroslav Lichvar <mlichvar@redhat.com> 2.0-5.20190912git48e605
- update to 20190912git48e605

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Miroslav Lichvar <mlichvar@redhat.com> 2.0-2
- start ptp4l, timemaster and phc2sys after network-online target
- fix building with new kernel headers

* Mon Aug 13 2018 Miroslav Lichvar <mlichvar@redhat.com> 2.0-1
- update to 2.0

* Thu Aug 09 2018 Miroslav Lichvar <mlichvar@redhat.com> 2.0-0.1.20180805gita27407
- update to 20180805gita27407

* Mon Jul 16 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.9.2-3
- add gcc and gcc-c++ to build requirements

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.9.2-1
- update to 1.9.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7.20180101git303b08
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.8-6.20180101git303b08
- use macro for systemd scriptlet dependencies

* Thu Jan 11 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.8-5.20180101git303b08
- update to 20180101git303b08

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Miroslav Lichvar <mlichvar@redhat.com> 1.8-1
- update to 1.8

* Fri Jul 22 2016 Miroslav Lichvar <mlichvar@redhat.com> 1.7-1
- update to 1.7
- add delay option to default timemaster.conf

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Miroslav Lichvar <mlichvar@redhat.com> 1.6-1
- update to 1.6
- set random seed in testing to get deterministic results
- remove trailing whitespace in default timemaster.conf

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Miroslav Lichvar <mlichvar@redhat.com> 1.5-1
- update to 1.5

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Miroslav Lichvar <mlichvar@redhat.com> 1.4-1
- update to 1.4
- replace hardening build flags with _hardened_build
- include test suite

* Fri Aug 02 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.3-1
- update to 1.3

* Tue Jul 30 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.2-3.20130730git7789f0
- update to 20130730git7789f0

* Fri Jul 19 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.2-2.20130719git46db40
- update to 20130719git46db40
- drop old systemd scriptlets
- add man page link for ptp4l.conf

* Mon Apr 22 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.2-1
- update to 1.2

* Mon Feb 18 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.1-1
- update to 1.1
- log phc2sys output

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Miroslav Lichvar <mlichvar@redhat.com> 1.0-1
- update to 1.0

* Fri Nov 09 2012 Miroslav Lichvar <mlichvar@redhat.com> 0-0.3.20121109git4e8107
- update to 20121109git4e8107
- install unchanged default.cfg as ptp4l.conf
- drop conflicts from phc2sys service

* Fri Sep 21 2012 Miroslav Lichvar <mlichvar@redhat.com> 0-0.2.20120920git6ce135
- fix issues found in package review (#859193)

* Thu Sep 20 2012 Miroslav Lichvar <mlichvar@redhat.com> 0-0.1.20120920git6ce135
- initial release
