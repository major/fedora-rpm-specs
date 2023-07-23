# Notes about rpmlint
# - crypto-policy-non-compliance-gnutls-{1,2} fixed with patch
#   prelude-manager-5.2.0-gnutls_priority_init.patch

Name:           prelude-manager
Version:        5.2.0
Release:        10%{?dist}
Summary:        Bus communicator for Prelude modules and other IDMEF agents
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
License:        GPLv2+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}-tmpfiles.conf
# https://www.prelude-siem.org/issues/862
Patch0:         prelude-manager-5.2.0-gnutls_priority_init.patch
# https://www.prelude-siem.org/issues/870
Patch1:         prelude-manager-5.2.0-fix_etc_perms.patch
Patch2:         prelude-manager-5.2.0-fix_cond_test.patch
Patch3:         prelude-manager-5.2.0-fix-test_rwlock1.patch
Patch4:         prelude-manager-5.2.0-fix_thread_create.patch
Patch5:         prelude-manager-5.2.0-Add_missing_gnutls_deps.patch
Patch6:         prelude-manager-5.2.0-fix-test-perror2.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  systemd
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libprelude) >= %{version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  libpreludedb-devel >= %{version}
BuildRequires:  net-snmp-devel

%{?systemd_requires}
Requires:       prelude-tools

%ifnarch s390
BuildRequires:  valgrind
%endif

# Upstream do not use explicit version of gnulib, just checkout
# and update files. In prelude-manager 5.2.0, the checkout has been done
# on 2018-09-03
Provides:       bundled(gnulib) = 20180903

%description
Prelude Manager is the main program of the Prelude SIEM suite. It is a
multithreaded server which handles connections from the Prelude modules. It is
able to register local or remote agents, let the operator configure them
remotely, receive alerts, and store alerts in a database or any format supported
by reporting plugins, thus providing centralized logging and analysis. The IDMEF
standard is used for alert representation. Support for filtering plugins allows
you to hook in different places in the Manager to define custom criteria for
alert logging.

%package        db-plugin
Summary:        Database report plugin for Prelude Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       preludedb-mysql
Suggests:       preludedb-pgsql
Suggests:       preludedb-sqlite3

%description db-plugin
This plugin allows prelude-manager to write to database.

%package        xml-plugin
Summary:        XML report plugin for Prelude Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description xml-plugin
This plugin allows prelude-manager to log into XML files.

%package        relaying-plugin
Summary:        Relaying plugin for Prelude Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description relaying-plugin
This plugin allows prelude-manager relay IDMEF alerts to another
prelude-manager.

%package        script-plugin
Summary:        Script plugin for Prelude Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description script-plugin
This plugin allows prelude-manager to execute scripts.

%package        snmp-plugin
Summary:        SNMP plugin for Prelude Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       net-snmp-libs

%description snmp-plugin
This plugin allows prelude-manager to report alerts through SNMP.

%package        devel
Summary:        Libraries, includes, etc. to develop Prelude Manager plugins
Requires:       %{name}-db-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}-xml-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}-relaying-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}-script-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}-snmp-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel headers for Prelude Manager.

%package doc
Summary:        Documentation for prelude-manager
BuildArch:      noarch

%description doc
Provides documentation for prelude-manager.

%prep
%autosetup -p1

%build
# This package's testsuite seems to mishandle --as-needed for the linker and
# as a result we don't have a DT_NEEDED for libpthread and various symbols
# do not get properly resolved causing testsuite failures.
# There is still a slim chance this is a linker error which we will investigate
# once Nick returns from PTO
%define _lto_cflags %{nil}

%configure \
    --disable-static \
    --enable-shared
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/prelude/profile/%{name}
mkdir -p %{buildroot}%{_var}/spool/%{name}/scheduler

mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/%{name}

# Empty dir but kept by debuginfo
rm -rf src/.libs

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
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/decodes
%dir %{_libdir}/%{name}/filters
%dir %{_libdir}/%{name}/reports
%{_libdir}/%{name}/filters/idmef-criteria.so
%{_libdir}/%{name}/filters/thresholding.so
%{_libdir}/%{name}/reports/debug.so
%{_libdir}/%{name}/reports/smtp.so
%{_libdir}/%{name}/reports/textmod.so
%{_libdir}/%{name}/decodes/normalize.so
%dir %{_var}/spool/%{name}
%dir %{_var}/spool/%{name}/scheduler
%dir /run/%{name}/
%{_tmpfilesdir}/%{name}.conf
%{_localstatedir}/lib/%{name}
%{_sysconfdir}/prelude/profile/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%{_mandir}/man1/%{name}.1*

%files db-plugin
%{_libdir}/%{name}/reports/db.so

%files xml-plugin
%{_libdir}/%{name}/reports/xmlmod.so
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/xmlmod
%{_datadir}/%{name}/xmlmod/idmef-message.dtd

%files relaying-plugin
%{_libdir}/%{name}/reports/relaying.so

%files script-plugin
%{_libdir}/%{name}/reports/script.so

%files snmp-plugin
%{_libdir}/%{name}/reports/snmp.so

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files doc
%license COPYING HACKING.README
%doc AUTHORS COPYING ChangeLog HACKING.README NEWS README
%doc %{_docdir}/%{name}/smtp/template.example
%doc %{_docdir}/%{name}/snmp/PRELUDE-SIEM-MIB.mib

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.2.0-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Florian Weimer <fweimer@redhat.com> - 5.2.0-4
- Rebuild with new binutils to fix ppc64le corruption (#1960730)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-1
- Bump version 5.2.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.0-1
- Bump version 5.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.0-1
- Bump version 5.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.1-1
- Bump version 4.1.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-2
- Remove tcp_wrappers dependency, fix #1518774
  See https://fedoraproject.org/wiki/Changes/Deprecate_TCP_wrappers

* Sat Sep 23 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-1
- Bump version 4.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-2
- Fix GnuTLS patch

* Sun Jan 29 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-1
- Bump version

* Mon Mar 11 2013 Steve Grubb <sgrubb@redhat.com> - 1.0.1-7
- Add -i to autoreconf so it adds the test-driver script
- Add libtool-ltdl-devel BuildRequires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 07 2012 Steve Grubb <sgrubb@redhat.com> - 1.0.1-5
- Add provides bundled gnulib
- Switch to systemd startup

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 25 2011 Steve Grubb <sgrubb@redhat.com> 1.0.1-2
- Disable pie patch for now

* Thu Mar 24 2011 Steve Grubb <sgrubb@redhat.com> 1.0.1-1
- new upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 02 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0-3
- Fix requires

* Fri Apr 30 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0-2
- new upstream version

* Sat Jan 30 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0rc1-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Steve Grubb <sgrubb@redhat.com> 0.9.15-1
- new upstream version

* Wed Apr 22 2009 Steve Grubb <sgrubb@redhat.com> 0.9.14.2-3
- Adjusted permissions on dirs and conf files

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 27 2008 Steve Grubb <sgrubb@redhat.com> 0.9.14.2-1
- new upstream version

* Mon Jul 21 2008 Steve Grubb <sgrubb@redhat.com> 0.9.14-1
- new upstream version

* Fri Jun 27 2008 Steve Grubb <sgrubb@redhat.com> 0.9.13-1
- new upstream version 0.9.13
- Prelude-Manager-SMTP plugin is now included

* Tue Jun 24 2008 Steve Grubb <sgrubb@redhat.com> 0.9.12.1-2
- add prelude-manager user

* Fri May 02 2008 Steve Grubb <sgrubb@redhat.com> 0.9.12.1-1
- new upstream version 0.9.12.1

* Thu Apr 24 2008 Steve Grubb <sgrubb@redhat.com> 0.9.12-1
- new upstream version 0.9.12

* Mon Jan 14 2008 Steve Grubb <sgrubb@redhat.com> 0.9.10-1
- new upstream version 0.9.10

* Thu Feb 08 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-4
- fixed Prelude trac #193

* Sun Jan 07 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-3
- added tcp-wrapper support
- fixed dirowner and permissions problem

* Fri Jan 05 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-2
- fixed encoding problems
- changed dirowner 
- resolved dependency problems

* Sat Dec 30 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.7.1-1
- moved to new upstream version 0.9.7.1
- changed dirowner

* Mon Nov 20 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.6.1-2
- Some minor fixes in requirements

* Tue Oct 24 2006 Thorsten Scherf <tscherf@redhat.com> 0.9.6.1-1
- New Fedora build based on release 0.9.6.1

