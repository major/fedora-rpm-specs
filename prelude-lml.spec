# Notes about rpmlint
# - crypto-policy-non-compliance-gnutls-{1,2} fixed with patch
#   prelude-lml-5.2.0-gnutls_priority_set_direct.patch

Name:           prelude-lml
Version:        5.2.0
Release:        14%{?dist}
Summary:        Log analyzer sensor with IDMEF output
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
License:        GPLv2+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}-tmpfiles.conf
# https://www.prelude-siem.org/issues/862
Patch0:         prelude-lml-5.2.0-gnutls_priority_set_direct.patch
# https://www.prelude-siem.org/issues/870
Patch1:         prelude-lml-5.2.0-fix_etc_perms.patch
# https://www.prelude-siem.org/issues/872
Patch2:         prelude-lml-5.2.0-fix_check.patch
Patch3:         prelude-lml-5.2.0-fix-test_rwlock1.patch
Patch4:         prelude-lml-5.2.0-fix_thread_create.patch
Patch5:         prelude-lml-5.2.0-fix_gnutls_deps.patch
Patch6:         prelude-lml-5.2.0-fix_test_perror2.patch
Patch7:         prelude-lml-configure-c99.patch
%{?systemd_requires}
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  chrpath
BuildRequires:  systemd
BuildRequires:  libgpg-error-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprelude) >= %{version}

%ifnarch s390
BuildRequires:  valgrind
%endif

# Upstream do not use explicit version of gnulib, just checkout
# and update files. In prelude-lml 5.2.0, the checkout has been done
# on 2018-09-03
Provides:       bundled(gnulib) = 20180903

%description
The Prelude Log Monitoring Lackey (LML) is the host-based sensor program part of
the Prelude SIEM suite. It can act as a centralized log collector for local or
remote systems, or as a simple log analyzer (such as swatch). It can run as a
network server listening on a syslog port or analyze log files. It supports log
files in the BSD syslog format and is able to analyze any log file by using the
PCRE library. It can apply log file specific analysis through plugins such as
PAX. It can send an alert to the Prelude Manager when a suspicious log entry is
detected.

%package        devel
Summary:        Libraries and headers for Prelude-LML
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Devel headers for the Prelude Log Monitoring Lackey (LML). It is the host-based
sensor program part of the Prelude SIEM suite. It can act as a centralized log
collector for local or remote systems, or as a simple log analyzer (such as
swatch). It can run as a network server listening on a syslog port or analyze
log files. It supports log files in the BSD syslog format and is able to analyze
any log file by using the PCRE library. It can apply log file specific analysis
through plugins such as PAX. It can send an alert to the Prelude Manager when a
suspicious log entry is detected.

%package doc
Summary:        Documentation for prelude-lml
BuildArch:      noarch

%description doc
Provides documentation for prelude-lml.

%prep
%autosetup -p1

%build
%ifarch ppc64le
# update cdefs.h for __LDBL_REDIR1_DECL, especially for
# ppc64le longdouble ieee128 mode switch
cp -p %{_includedir}/sys/cdefs.h libmissing/
%endif

%configure \
    --bindir=%{_sbindir} \
    --enable-shared \
    --disable-static \
    --with-libprelude-prefix=%{_prefix}
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

# Empty dir but kept by debuginfo
rm -rf src/.libs

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}

chrpath -d %{buildroot}%{_sbindir}/%{name}

# install init script
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# tmpfiles
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

%check
make check

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 

%files
%license COPYING HACKING.README
%doc README
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%dir %{_localstatedir}/lib/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.rules
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%dir %{_localstatedir}/lib/%{name}
%dir /run/%{name}/
%{_tmpfilesdir}/%{name}.conf

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files doc
%license COPYING HACKING.README
%doc ChangeLog README NEWS AUTHORS

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 5.2.0-13
- Rebuild for ICU 72

* Fri Dec  9 2022 Florian Weimer <fweimer@redhat.com> - 5.2.0-12
- Port configure script to C99

* Thu Aug 04 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.2.0-11
- ppc64le: update cdefs.h for __LDBL_REDIR1_DECL

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.0-10
- Rebuilt for ICU 71.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 5.2.0-6
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 5.2.0-5
- Rebuild for ICU 69

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Jeff Law <law@redhat.com> - 5.2.0-2
- Re-enable LTO

* Thu Sep 17 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-1
- Bump version 5.2.0

* Tue Aug 04 2020 Jeff Law <law@redhat.com> - 5.1.0-6
- Disable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 5.1.0-3
- Rebuild for ICU 67

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.0-1
- Bump version 5.1.0

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 5.0.0-3
- Rebuild for ICU 65

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.0-1
- Bump version 5.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-3
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-2
- Rebuild for ICU 61.1

* Tue Apr 24 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.0-1
- Bump version 4.1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 4.0.0-2
- Rebuild for ICU 60.1

* Wed Oct 4 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-1
- Bump version 4.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-2
- Fix GnuTLS patch

* Wed Jan 25 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-1
- Bump version

* Sun Mar 10 2013 Steve Grubb <sgrubb@redhat.com> - 1:1.0.0-10
- Add libtool-ltdl-devel BuildRequires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 06 2012 Steve Grubb <sgrubb@redhat.com> - 1:1.0.0-8
- Add provides bundled gnulib
- Add systemd service file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1:1.0.0-6
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 02 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0-3
- Fixed requires

* Fri Apr 30 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0-2
- new upstream release

* Mon Feb 08 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0rc2-1
- new upstream release

* Sat Jan 30 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0rc1-1
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Steve Grubb <sgrubb@redhat.com> 0.9.15-1
- new upstream release

* Wed Apr 22 2009 Steve Grubb <sgrubb@redhat.com> 0.9.14-3
- Adjust dir and config file permissions

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 17 2008 Steve Grubb <sgrubb@redhat.com> 0.9.14-1
- new upstream release fixing bz #463459

* Sat Oct 11 2008 Steve Grubb <sgrubb@redhat.com> 0.9.13-2
- improved mod_security rules

* Wed Aug 27 2008 Steve Grubb <sgrubb@redhat.com> 0.9.13-1
- new upstream release

* Wed Jun 25 2008 Tomas Mraz <tmraz@redhat.com> - 0.9.12.2-2
- rebuild with new gnutls

* Thu Apr 24 2008 Steve Grubb <sgrubb@redhat.com> 0.9.12.2-1
- new upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.11-2
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Steve Grubb <sgrubb@redhat.com> 0.9.11-1
- new upstream version 0.9.11

* Tue Jan 09 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-5
- changed init-script description 

* Mon Jan 08 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-4
- added new /var/lib directory 

* Fri Jan 05 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-3
- added init-script
- changed some macros in %%files

* Tue Jan 02 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-2
- fixed debug problems
- fixed encoding problems

* Fri Dec 29 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-1
- moved to new upstream version 0.9.8.1
- changed dirowner of /etc/prelude-lml

* Mon Nov 20 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.7-2
- Some minor fixes in requirements

* Mon Oct 23 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.7-1
- New Fedora build based on release 0.9.7

