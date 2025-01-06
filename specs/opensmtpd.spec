
# PAM support
%global _with_pam	1

# Berkeley DB support
%global _with_bdb	1

Summary:	Free implementation of the server-side SMTP protocol as defined by RFC 5321
Name:		opensmtpd
Version:	7.6.0p1
Release:	1%{?dist}

License:	ISC
URL:		http://www.opensmtpd.org/
Provides:	MTA smtpd smtpdaemon server(smtp)

Source0:	http://www.opensmtpd.org/archives/%{name}-%{version}.tar.gz
Source1:	opensmtpd.service
Source2:	opensmtpd.pam

%if 0%{?_with_pam}
BuildRequires:	pam-devel
%endif
%if 0%{?_with_bdb}
BuildRequires:	libdb-devel
%endif

BuildRequires:	openssl-devel
BuildRequires:	libevent-devel
BuildRequires:	zlib-devel
BuildRequires:	coreutils
BuildRequires:	bison
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libtool

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd

Requires(pre):		shadow-utils

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/sendmail
%endif

%description
OpenSMTPD is a FREE implementation of the server-side SMTP protocol as defined
by RFC 5321, with some additional standard extensions. It allows ordinary
machines to exchange e-mails with other systems speaking the SMTP protocol.
Started out of dissatisfaction with other implementations, OpenSMTPD nowadays
is a fairly complete SMTP implementation. OpenSMTPD is primarily developed
by Gilles Chehade, Eric Faurot and Charles Longeau; with contributions from
various OpenBSD hackers. OpenSMTPD is part of the OpenBSD Project.
The software is freely usable and re-usable by everyone under an ISC license.

This package uses standard "alternatives" mechanism, you may call
"alternatives --set mta %{_sbindir}/sendmail.opensmtpd"
if you want to switch to OpenSMTPD MTA immediately after install, and
"alternatives --set mta %{_sbindir}/sendmail.sendmail" to revert
back to Sendmail as a default mail daemon.


%prep
%autosetup

%build
export CFLAGS="%{optflags}"

%configure \
    --sysconfdir=%{_sysconfdir}/opensmtpd \
    --with-path-CAfile=%{_sysconfdir}/pki/tls/cert.pem \
    --with-mantype=man \
    %if 0%{?_with_pam}
    --with-auth-pam=smtp \
    %endif
    %if 0%{?_with_bdb}
    --with-table-db \
    %endif
    --with-user-smtpd=smtpd \
    --with-user-queue=smtpq \
    --with-group-queue=smtpq \
    --with-path-empty=%{_localstatedir}/empty/smtpd \
    --with-path-mbox=%{_localstatedir}/spool/mail \
    --with-path-socket=%{_localstatedir}/run \
    --without-rpath

%make_build

%install
%make_install
mkdir -p -m 0755 %{buildroot}/%{_localstatedir}/empty/smtpd

install -Dpm 0644 %SOURCE1 %{buildroot}/%{_unitdir}/opensmtpd.service

%if 0%{?_with_pam}
install -Dpm 0644 %SOURCE2 %{buildroot}/%{_sysconfdir}/pam.d/smtp.opensmtpd
touch %{buildroot}/%{_sysconfdir}/pam.d/smtp
%endif

rm -rf %{buildroot}/%{_bindir}/sendmail
rm -rf %{buildroot}/%{_sbindir}/mailq
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_sbindir}/sendmail.%{name}
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_bindir}/mailq.%{name}
touch %{buildroot}/%{_sbindir}/sendmail
touch %{buildroot}/usr/lib/sendmail
touch %{buildroot}/%{_bindir}/mailq

mv %{buildroot}/%{_mandir}/man1/smtp.1 %{buildroot}/%{_mandir}/man1/smtp.opensmtpd.1
mv %{buildroot}/%{_mandir}/man5/aliases.5 %{buildroot}/%{_mandir}/man5/aliases.opensmtpd.5
mv %{buildroot}/%{_mandir}/man8/sendmail.8 %{buildroot}/%{_mandir}/man8/sendmail.opensmtpd.8
mv %{buildroot}/%{_mandir}/man8/smtpd.8 %{buildroot}/%{_mandir}/man8/smtpd.opensmtpd.8
ln -s %{_mandir}/man1/smtp.opensmtpd.1.gz %{buildroot}/%{_mandir}/man8/smtp.opensmtpd.8
ln -s %{_mandir}/man8/smtpctl.8.gz %{buildroot}/%{_mandir}/man1/mailq.opensmtpd.1
touch %{buildroot}/%{_mandir}/man1/mailq.1
touch %{buildroot}/%{_mandir}/man5/aliases.5
touch %{buildroot}/%{_mandir}/man8/sendmail.8
touch %{buildroot}/%{_mandir}/man8/smtp.8
touch %{buildroot}/%{_mandir}/man8/smtpd.8

%if 0%{?_with_bdb}
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_sbindir}/makemap.%{name}
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_bindir}/newaliases.%{name}
mv %{buildroot}/%{_mandir}/man8/makemap.8 %{buildroot}/%{_mandir}/man8/makemap.opensmtpd.8
mv %{buildroot}/%{_mandir}/man8/newaliases.8 %{buildroot}/%{_mandir}/man8/newaliases.opensmtpd.8
touch %{buildroot}/%{_sbindir}/makemap
touch %{buildroot}/%{_bindir}/newaliases
touch %{buildroot}/%{_mandir}/man1/newaliases.1
touch %{buildroot}/%{_mandir}/man8/makemap.8
%endif

# smtpd spool directory
for i in incoming offline purge queue; do
	mkdir -p %{buildroot}/%{_localstatedir}/spool/smtpd/$i
done

# fix aliases path in the config
sed -i -e 's|/etc/mail/aliases|/etc/aliases|g' %{buildroot}/%{_sysconfdir}/opensmtpd/smtpd.conf
ln -s %{_sysconfdir}/aliases %{buildroot}/%{_sysconfdir}/opensmtpd/aliases

# set mbox delivery method
sed -i -e 's|^action "local" maildir|action "local" mbox|g' %{buildroot}/%{_sysconfdir}/opensmtpd/smtpd.conf

%pre
getent group smtpd &>/dev/null || %{_sbindir}/groupadd -r smtpd
getent group smtpq &>/dev/null || %{_sbindir}/groupadd -r smtpq
getent passwd smtpd &>/dev/null || \
    %{_sbindir}/useradd -r -g smtpd -s /sbin/nologin -c "opensmtpd privsep user" -d %{_localstatedir}/empty/smtpd smtpd
getent passwd smtpq &>/dev/null || \
    %{_sbindir}/useradd -r -g smtpq -s /sbin/nologin -c "opensmtpd queue user" -d %{_localstatedir}/empty/smtpd smtpq
exit 0

%post
%systemd_post %{name}.service
%{_sbindir}/alternatives --install %{_sbindir}/sendmail mta %{_sbindir}/sendmail.opensmtpd 10 \
	--slave %{_bindir}/mailq mta-mailq %{_bindir}/mailq.opensmtpd \
	%if 0%{?_with_pam}
	--slave /etc/pam.d/smtp mta-pam /etc/pam.d/smtp.opensmtpd \
	%endif
	%if 0%{?_with_bdb}
	--slave %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.opensmtpd \
	--slave %{_sbindir}/makemap mta-makemap %{_sbindir}/makemap.opensmtpd \
	--slave %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man8/newaliases.opensmtpd.8.gz \
	--slave %{_mandir}/man8/makemap.8.gz mta-makemapman %{_mandir}/man8/makemap.opensmtpd.8.gz \
	%endif
	--slave /usr/lib/sendmail mta-sendmail %{_sbindir}/sendmail.opensmtpd \
	--slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.opensmtpd.1.gz \
	--slave %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.opensmtpd.5.gz \
	--slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man8/sendmail.opensmtpd.8.gz \
	--slave %{_mandir}/man8/smtp.8.gz mta-smtpman %{_mandir}/man8/smtp.opensmtpd.8.gz \
	--slave %{_mandir}/man8/smtpd.8.gz mta-smtpdman %{_mandir}/man8/smtpd.opensmtpd.8.gz \
	--initscript opensmtpd
exit 0

%preun
%systemd_preun %{name}.service
if [ "$1" = 0 ]; then
    %{_sbindir}/alternatives --remove mta %{_sbindir}/sendmail.opensmtpd
fi
exit 0

%postun
%systemd_postun_with_restart %{name}.service
if [ "$1" -ge "1" ]; then
	mta=`readlink /etc/alternatives/mta`
	if [ "$mta" == "%{_sbindir}/sendmail.opensmtpd" ]; then
	    %{_sbindir}/alternatives --set mta %{_sbindir}/sendmail.opensmtpd
	fi
fi
exit 0


%files
%dir %attr(0711,root,root) %{_localstatedir}/empty/smtpd
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/smtpd.conf
%{_sysconfdir}/%{name}/aliases
%doc CHANGES.md README.md
%license LICENSE
%{_mandir}/man1/lockspool.1.gz
%{_mandir}/man1/mailq.opensmtpd.1.gz
%{_mandir}/man1/smtp.opensmtpd.1.gz
%{_mandir}/man5/aliases.opensmtpd.5.gz
%{_mandir}/man5/forward.5.gz
%{_mandir}/man5/smtpd.conf.5.gz
%{_mandir}/man5/table.5.gz
%{_mandir}/man7/smtpd-filters.7.gz
%{_mandir}/man7/smtpd-tables.7.gz
%{_mandir}/man8/sendmail.opensmtpd.8.gz
%{_mandir}/man8/smtp.opensmtpd.8.gz
%{_mandir}/man8/smtpd.opensmtpd.8.gz
%{_mandir}/man8/smtpctl.8.gz
%{_mandir}/man8/mail.*.8.gz

%dir %attr(0711,root,root) %{_localstatedir}/spool/smtpd
%dir %attr(0700,smtpq,root) %{_localstatedir}/spool/smtpd/incoming
%dir %attr(0770,root,smtpq) %{_localstatedir}/spool/smtpd/offline
%dir %attr(0700,smtpq,root) %{_localstatedir}/spool/smtpd/purge
%dir %attr(0700,smtpq,root) %{_localstatedir}/spool/smtpd/queue

%if 0%{?_with_pam}
%config(noreplace) %{_sysconfdir}/pam.d/smtp.%{name}
%ghost %{_sysconfdir}/pam.d/smtp
%endif

%if 0%{?_with_bdb}
%{_bindir}/newaliases.%{name}
%{_sbindir}/makemap.%{name}
%{_mandir}/man8/newaliases.opensmtpd.8.gz
%{_mandir}/man8/makemap.opensmtpd.8.gz
%ghost %attr(0755,root,root) %{_bindir}/newaliases
%ghost %attr(0755,root,root) %{_sbindir}/makemap
%ghost %{_mandir}/man1/newaliases.1.gz
%ghost %{_mandir}/man8/makemap.8.gz
%endif

%{_unitdir}/%{name}.service
%{_libexecdir}/%{name}
%{_bindir}/smtp
%{_bindir}/mailq.%{name}
%{_sbindir}/sendmail.%{name}
%{_sbindir}/smtpd
%attr(2555,root,smtpq) %{_sbindir}/smtpctl
%ghost %attr(0755,root,root) %{_sbindir}/sendmail
%ghost %attr(0755,root,root) %{_bindir}/mailq
%ghost %attr(0755,root,root) /usr/lib/sendmail
%ghost %{_mandir}/man1/mailq.1.gz
%ghost %{_mandir}/man5/aliases.5.gz
%ghost %{_mandir}/man8/sendmail.8.gz
%ghost %{_mandir}/man8/smtp.8.gz
%ghost %{_mandir}/man8/smtpd.8.gz


%changelog
* Fri Jan 03 2025 Denis Fateyev <denis@fateyev.com> - 7.6.0p1-1
- Update to 7.6.0p1 release

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0p0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.5.0p0-2
- Rebuilt for the bin-sbin merge

* Mon Apr 22 2024 Denis Fateyev <denis@fateyev.com> - 7.5.0p0-1
- Update to 7.5.0p0 release

* Tue Mar 26 2024 Denis Fateyev <denis@fateyev.com> - 7.4.0p1-1
- Update to 7.4.0p1 release

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Denis Fateyev <denis@fateyev.com> - 6.8.0p2-10
- Rebuild against openssl1.1 in Fedora

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Denis Fateyev <denis@fateyev.com> - 6.8.0p2-7
- Fixed smtpd spool directory layout

* Fri Nov 05 2021 Denis Fateyev <denis@fateyev.com> - 6.8.0p2-6
- Add hardened security settings to service
- Set "mbox" delivery method usage by default

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 6.8.0p2-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.8.0p2-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Denis Fateyev <denis@fateyev.com> - 6.8.0p2-1
- Update to 6.8.0p2 release

* Thu Sep 17 2020 Denis Fateyev <denis@fateyev.com> - 6.7.1p1-3
- Rebuild for libevent soname change

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Denis Fateyev <denis@fateyev.com> - 6.7.1p1-1
- Update to 6.7.1p1 release
- Remove deprecated "legacy_common_support" build option

* Fri Apr 10 2020 Denis Fateyev <denis@fateyev.com> - 6.6.4p1-3
- Rebuilt for epel7 compatibility

* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 6.6.4p1-2
- Add "legacy_common_support" build option

* Mon Feb 24 2020 Denis Fateyev <denis@fateyev.com> - 6.6.4p1-1
- Update to 6.6.4p1 release

* Thu Jan 30 2020 Denis Fateyev <denis@fateyev.com> - 6.6.2p1-1
- Update to 6.6.2p1 release
- Remove obsolete patch and spec cleanup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3p1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3p1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3p1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 6.0.3p1-6
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Aug 16 2018 Denis Fateyev <denis@fateyev.com> - 6.0.3p1-5
- Fixed initscript and service files
- Switched from libdb4 to libdb where possible

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3p1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Denis Fateyev <denis@fateyev.com> - 6.0.3p1-3
- Rebuild to fix libevent version bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Denis Fateyev <denis@fateyev.com> - 6.0.3p1-1
- Update to 6.0.3p1 release

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 6.0.2p1-7
- Rebuilt for switch to libxcrypt

* Sat Sep 30 2017 Denis Fateyev <denis@fateyev.com> - 6.0.2p1-6
- Fixed reallocarray interpose

* Sun Aug 06 2017 Denis Fateyev <denis@fateyev.com> - 6.0.2p1-5
- Fixed compat-openssl10 build for Fedora

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2p1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2p1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Denis Fateyev <denis@fateyev.com> - 6.0.2p1-1
- Update to 6.0.2p1 release

* Fri Oct 07 2016 Denis Fateyev <denis@fateyev.com> - 6.0.1p1-1
- Update to 6.0.1p1 release

* Fri Sep 16 2016 Denis Fateyev <denis@fateyev.com> - 6.0.0p1-1
- Update to 6.0.0p1 release

* Fri May 20 2016 Denis Fateyev <denis@fateyev.com> - 5.9.2p1-1
- Update to 5.9.2p1 release

* Tue Feb 16 2016 Denis Fateyev <denis@fateyev.com> - 5.7.3p2-1
- Update to 5.7.3p2 release, fixing openssl issue

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.3p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Denis Fateyev <denis@fateyev.com> - 5.7.3p1-1
- Update to 5.7.3 release, fixing multiple vulnerabilities

* Fri Oct 02 2015 Denis Fateyev <denis@fateyev.com> - 5.7.2p1-1
- Update to 5.7.2 release

* Fri Jul 17 2015 Denis Fateyev <denis@fateyev.com> - 5.7.1p1-1
- Update to 5.7.1 release
- Small cleanup, added ghost file provides

* Tue Jun 23 2015 Denis Fateyev <denis@fateyev.com> - 5.4.6p1-1
- Update to 5.4.6 release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Denis Fateyev <denis@fateyev.com> - 5.4.5p2-1
- Update to 5.4.5 release

* Thu Feb 19 2015 Denis Fateyev <denis@fateyev.com> - 5.4.4p1-1
- Update to 5.4.4 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.2p1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.2p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Denis Fateyev <denis@fateyev.com> - 5.4.2p1-1
- Small enhancements, man-page and pam fixes
- Update to 5.4.2 release

* Mon Dec 09 2013 Denis Fateyev <denis@fateyev.com> - 5.4.1p1-1
- Multiple enhancements, systemd migration, spec cleanup
- Update to 5.4.1 release

* Wed Sep 04 2013 Denis Fateyev <denis@fateyev.com> - 5.3.3p1-2
- Better snapshots support, script cleanup

* Mon Jun 10 2013 Denis Fateyev <denis@fateyev.com> - 5.3.3p1-1
- Initial release
