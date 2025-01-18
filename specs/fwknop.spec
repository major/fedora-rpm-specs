Summary: A Single Packet Authorization (SPA) implementation
Name: fwknop
Version: 2.6.11
Release: 4%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Url: http://www.cipherdyne.org/fwknop/
Source0: http://cipherdyne.org/fwknop/download/fwknop-%{version}.tar.bz2
Source1: http://cipherdyne.org/fwknop/download/fwknop-%{version}.tar.bz2.asc
Source2: fwknopd.service
BuildRequires: libpcap-devel iptables systemd gpgme-devel gpg firewalld
BuildRequires: gcc
BuildRequires: make
Requires: logrotate
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%package devel
Summary:    The fwknop library, header and API docs
Requires:   gpg, gpgme
Requires: %{name}%{?_isa} >= %{version}-%{release}

%description
fwknop implements an authorization scheme known as Single Packet
Authorization (SPA) that requires only a single encrypted packet to
communicate various pieces of information including desired access through an
iptables policy and/or specific commands to execute on the target system.
The main application of this program is to protect services such as SSH with
an additional layer of security in order to make the exploitation of
vulnerabilities (both 0-day and unpatched code) much more difficult.  The
authorization server passively monitors authorization packets via libpcap and
hence there is no "server" to which to connect in the traditional sense.  Any
service protected by fwknop is inaccessible (by using iptables to
intercept packets within the kernel) before authenticating; anyone scanning for
the service will not be able to detect that it is even listening.  This
authorization scheme offers many advantages over port knocking, include being
non-replayable, much more data can be communicated, and the scheme cannot be
broken by simply connecting to extraneous ports on the server in an effort to
break knock sequences.  The authorization packets can easily be spoofed as
well, and this makes it possible to make it appear as though, say,
www.yahoo.com is trying to authenticate to a target system but in reality the
actual connection will come from a seemingly unrelated IP. Although the
default data collection method is to use libpcap to sniff packets off the
wire, fwknop can also read packets out of a file that is written by the
iptables ulogd pcap writer or by a separate sniffer process.

%description devel
The Firewall Knock Operator library, libfko, provides the Single Packet
Authorization implementation and API for the other fwknop components.

%prep
%setup -q

%build
%configure --with-firewall-cmd=/usr/bin/firewall-cmd --with-gpgme
# remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Parallel build fails with version 2.0.4, the upstream fix does not always work
make %{?_smp_mflags} -j1 OPTS="$RPM_OPT_FLAGS"

%check
# check needs root access
#cd test; ./run-test-suite.sh --enable-all

%install
%make_install

# init script
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/fwknopd.service

# devel stuff
rm $RPM_BUILD_ROOT/%{_libdir}/libfko.{la,a}

%post
%systemd_post fwknopd.service

%preun
%systemd_preun fwknopd.service

%postun
%systemd_postun_with_restart fwknopd.service

%triggerun -- fwknop < 2.0-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply fwknopd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save fwknopd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del fwknopd >/dev/null 2>&1 || :
/bin/systemctl try-restart fwknopd.service >/dev/null 2>&1 || :

%files
%doc CREDITS ChangeLog README
%license COPYING
%dir %{_sysconfdir}/fwknop
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/fwknop/fwknopd.conf
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/fwknop/access.conf
%attr(0755,root,root) %{_bindir}/fwknop
%attr(0755,root,root) %{_sbindir}/fwknopd
%{_unitdir}/fwknopd.service
%attr(0644,root,root) %{_mandir}/man8/fwknop.8*
%attr(0644,root,root) %{_mandir}/man8/fwknopd.8*
%attr(0644,root,root) %{_libdir}/libfko.so.3.0.0
%attr(0644,root,root) %{_libdir}/libfko.so.3
%exclude %{_infodir}/dir

%files devel
%attr(0644,root,root) %{_libdir}/libfko.so
%attr(0644,root,root) %{_includedir}/fko.h
%attr(0644,root,root) %{_infodir}/libfko.info*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.11-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Jakub Jelen <jjelen@redhat.com> - 2.6.11-1
- New upstream release (#2263111)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.10-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Jakub Jelen <jjelen@redhat.com> - 2.6.10-5
- Unbreak build with gcc10 (#1799378)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Jakub Jelen <jjelen@redhat.com> - 2.6.10-1
- New upstream release (#1613332)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.6.9-2
- Rebuild for gpgme 1.18

* Thu Jun 16 2016 Jakub Jelen <jjelen@redhat.com> - 2.6.9-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Jakub Jelen <jjelen@redhat.com> 2.6.8-1
- New upstream release

* Wed Nov 25 2015 Jakub Jelen <jjelen@redhat.com> 2.6.7-1
- New upstram release

* Wed Aug 12 2015 Jakub Jelen <jjelen@redhat.com> 2.6.6-2
- Provide -devel subpackage (#1252077)

* Mon Jun 29 2015 Jakub Jelen <jjelen@redhat.com> 2.6.6-1
- New upstream release
- Fix problematic firewalld dependency (#1236331)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Jakub Jelen <jjelen@redhat.com> 2.6.5-2
- Add possibility to use gpg and firewalld (#976453)

* Tue Apr 07 2015 Jakub Jelen <jjelen@redhat.com> 2.6.5-1
- New upstream release

* Wed Feb 25 2015 Jakub Jelen <jjelen@redhat.com> 2.6.3-2
- Make service start after network (#1195303)
- Update install scriptlet for systemd (#850124)

* Thu Aug 21 2014 Warren Togami <warren@slickage.com> - 2.6.3-1
- upgrade to fwknop-2.6.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Lukas Vrabec <lvrabec@redhat.com> - 2.5.1-1
- Update to fwknop-2.5.1
- Add systemd to BuildRequires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jan 22 2013 Viktor Hercinger <vhercing@redhat.com> - 2.0.4-1
- Update to fwknop-2.0.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 2.0-2
- Migrate to systemd, BZ 767777.
- Added disttag.

* Thu Jan 12 2012 Peter Vrabec <pvrabec@redhat.com> - 2.0-1
- upgrade

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 16 2009 Miloslav Trmač <mitr@redhat.com> - 1.9.12-1
- Update to fwknop-1.9.12.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Miloslav Trmač <mitr@redhat.com> - 1.9.11-1
- Update to fwknop-1.9.11.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 05 2009 Peter Vrabec <pvrabec@redhat.com> 1.9.9-2
- add /var/log/fwknop/errs directory (#469395)

* Mon Nov 17 2008 Miloslav Trmač <mitr@redhat.com> - 1.9.9-1
- Update to fwknop-1.9.9

* Sat Oct  4 2008 Miloslav Trmač <mitr@redhat.com> - 1.9.8-1
- Update to fwknop-1.9.8
- Add missing Requires:
- Use the "nodeps" tarball

* Sun Aug 24 2008 Miloslav Trmač <mitr@redhat.com> - 1.9.7-1
- Update to fwknop-1.9.7
- License specified to be GPLv2

* Sun Aug 24 2008 Miloslav Trmač <mitr@redhat.com> - 1.9.6-4
- Don't change SNAT_TRANSLATE_IP to "localhost" in the default config.
- Add Requires: logrotate.

* Wed Aug 13 2008 Peter Vrabec <pvrabec@redhat.com> - 1.9.6-3
- fix sed cmd in spec file

* Mon Aug 11 2008 Peter Vrabec <pvrabec@redhat.com> - 1.9.6-2
- add logrotate file
- do not set hostname during install

* Wed Jul 30 2008 Miloslav Trmač <mitr@redhat.com> - 1.9.6-1
- Initial Fedora package, based on Michael Rash's spec file (heavily modified
  since).

* Fri Jul 18 2008 Michael Rash <mbr@cipherdyne.org>
- Release of fwknop-1.9.6
