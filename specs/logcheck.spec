Name:           logcheck
Version:        1.3.18
Release:        20%{?dist}
Summary:        Analyzes log files and sends noticeable events as email

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://logcheck.org/
Source0:        http://http.debian.net/debian/pool/main/l/%{name}/%{name}_%{version}.tar.xz
Source1:        logchk-systemd-ignore
Source2:        logchk-NetworkManager-ignore
Source3:        logchk-dbus-ignore
Patch0:         logcheck-dhclient.patch
BuildArch:      noarch

Requires:       lockfile-progs
Requires:       perl-mime-construct
Requires:       crontabs
Requires(pre):  shadow-utils
BuildRequires:  docbook-utils
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires: make

%description
Logcheck is a simple utility which is designed to allow a system administrator 
to view the log-files which are produced upon hosts under their control.

It does this by mailing summaries of the log-files to them, after first
filtering out "normal" entries.

Normal entries are entries which match one of the many included regular
expression files contain in the database.

%prep
%setup -q

# use fedora-style logfiles. (/var/log/syslog is /var/log/messages,
#                              auth.log is named secure)
sed -i "s/syslog/messages/" etc/logcheck.logfiles
sed -i "s/auth\.log/secure/" etc/logcheck.logfiles

echo "d /var/lock/logcheck 1700 logcheck logcheck 1d" > etc/tmpfiles.d-logcheck
%build


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_sysconfdir}/%{name}/violations.d/logcheck

%{__mkdir} -pm 755 %{buildroot}%{_mandir}/man8
%{__install} -pm 644 docs/logtail.8 %{buildroot}%{_mandir}/man8/
%{__install} -pm 644 docs/logtail2.8 %{buildroot}%{_mandir}/man8/
# create man-page from sgml.
docbook2man -o %{buildroot}%{_mandir}/man8/ docs/logcheck.sgml
# man-page-name is named Logcheck instead of logcheck:
mv %{buildroot}%{_mandir}/man8/Logcheck.8 %{buildroot}%{_mandir}/man8/%{name}.8

rm -f %{buildroot}%{_mandir}/man8/manpage.*

%{__mkdir} -pm 755 %{buildroot}%{_mandir}/man1
%{__install} -pm 644 docs/logcheck-test.1 %{buildroot}%{_mandir}/man1/
%{__install} -pm 644 docs/logtail2.8 %{buildroot}%{_mandir}/man8/

%{__mkdir} -pm 755 %{buildroot}%{_sysconfdir}/cron.d
%{__install} -pm 644 debian/%{name}.cron.d %{buildroot}%{_sysconfdir}/cron.d/%{name}

%{__mkdir} -pm 755 %{buildroot}%{_localstatedir}/lock/%{name}
# create homedir for logcheck-user
%{__mkdir} -pm 644 %{buildroot}%{_sharedstatedir}/%{name}

%{__mkdir} -pm 755 %{buildroot}%{_tmpfilesdir}
%{__install} -pm 644 etc/tmpfiles.d-logcheck %{buildroot}%{_tmpfilesdir}/%{name}.conf

# install fedora tweaked rule files
%{__install} -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/ignore.d.server/systemd
%{__install} -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/ignore.d.server/NetworkManager
%{__install} -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/ignore.d.server/dbus
%pre
getent group logcheck >/dev/null || groupadd -r logcheck
getent passwd logcheck >/dev/null || \
    useradd -r -g logcheck -G adm -d /var/lib/logcheck -s /sbin/nologin \
            -c "Logcheck user" logcheck && \
    mkdir /var/lock/logcheck && chown logcheck:logcheck /var/lock/logcheck && \
    mkdir /var/lib/logcheck && chown logcheck:logcheck /var/lib/logcheck && \
    [ -x /sbin/restorecon ] && /sbin/restorecon /var/lock/logcheck /var/lib/logcheck
exit 0

%files
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/logcheck.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/logcheck.logfiles
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/cracking.d/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/cracking.d/*
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/ignore.d.workstation/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ignore.d.workstation/*
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/ignore.d.server/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ignore.d.server/*
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/ignore.d.paranoid/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ignore.d.paranoid/*
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/violations.d/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/violations.d/*
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/violations.ignore.d/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/violations.ignore.d/*
%config(noreplace) %{_sysconfdir}/cron.d/*
%{_bindir}/logcheck-test
%{_sbindir}/*
%{_datadir}/logtail/
%{_mandir}/man?/*
%ghost %{_localstatedir}/lock/%{name}
%ghost %{_sharedstatedir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%doc docs/*
%license LICENSE


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.18-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.18-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Matthias Runge <mrunge@redhat.com> - 1.3.18-1
- update to 1.3.18 (rhbz#1438908)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.3.15-5
- Move tmpfiles.d config to %%{_tmpfilesdir}
- Install LICENSE as %%license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Matthias Runge <mrunge@redhat.com> - 1.3.15-1
- update to 1.3.15
- requires: crontabs, fixes rhbz#989074

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3.14-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 04 2012 Matthias Runge <mrunge@matthias-runge.de> 1.3.14-6
- restore SELinux-context on /var/lock/logcheck, /var/lib/logckeck

* Mon Jan 02 2012 Matthias Runge <mrunge@matthias-runge.de> 1.3.14-5
- create directories /var/lock/logcheck and home-dir

* Sun Nov 20 2011 Matthias Runge <mrunge@matthias-runge.de> 1.3.14-4
- correct names of ignore-files
- ignore new logins
- ignore dbus-messages

* Fri Nov 18 2011 Matthias Runge <mrunge@matthias-runge.de> 1.3.14-3
- ignore NetworkManager standard messages
- ignore systemd-login standard messages

* Mon Nov 14 2011 Matthias Runge <mrunge@matthias-runge.de> 1.3.14-2
- ignore dhclient messages (bug 751047)

* Mon Sep 12 2011 Matthias Runge <mrunge@matthias-runge.de> 1.3.14-1
- new version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.13-5
- %%ghost /var/run

* Tue Nov 2 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.13-4
- respect run-parts --list option

* Tue Sep 14 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.13-3
- escape " in sed-call

* Mon Sep 6 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.13-1
- update to 1.3.13
- make permissions fit to fedora-packaging guidelines

* Thu Aug 5 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.11-1
- substitute patches with sed-invocations for readability
- install creates logcheck-homedir, package owns homedir
- update to 1.3.11

* Mon May 17 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.8-5
- add lockfile-progs as requirement
- debians run-parts accepts --list parameter, fedoras doesn't need it

* Wed May 12 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.8-4
- added requires, homedir created

* Mon May 10 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.8-3
- patch logcheck-logfiles 

* Sat May 8 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.8-2
- install man page
- clean up permissions and files section
- user logcheck added

* Wed Apr 28 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.8-1
- initial spec
