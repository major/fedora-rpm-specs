# ZNC is a daemon application and that's why needs hardening
%global _hardened_build 1

# Define variables to use in conditionals
%if 0%{?fedora} || 0%{?rhel} >= 6
%global with_modperl 1
%endif # 0%{?fedora} || 0%{?rhel} >= 6

%if 0%{?fedora} || 0%{?rhel} >= 7
%global __python %{__python3}
%global with_modpython 1
%endif # 0%{?fedora} || 0%{?rhel} >= 7

Name:           znc
Version:        1.9.1
Release:        6%{?dist}
Summary:        An advanced IRC bouncer

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://znc.in
Source0:        %{url}/releases/archive/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/archive/%{name}-%{version}.tar.gz.sig

Source2:        gpgkey-5AE420CC0209989E.asc
# Use system-wide crypto policy
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch0:         0001-Use-system-wide-crypto-policy.patch

BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libicu-devel
BuildRequires:  make

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel >= 0.9.8
%else
BuildRequires:  openssl11-devel
%endif

%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif

BuildRequires:  perl(ExtUtils::Embed)

%if 0%{?rhel} && 0%{?rhel} <= 9
Obsoletes:      znc-extra <= %{version}-%{release}
%endif # 0%{?rhel} && 0%{?rhel} <= 9

Requires(pre):  shadow-utils
BuildRequires:  systemd
%{?systemd_requires}

%description
ZNC is an IRC bouncer with many advanced features like detaching,
multiple users, per channel playback buffer, SSL, IPv6, transparent
DCC bouncing, Perl and C++ module support to name a few.

%package devel
Summary:        Development files needed to compile ZNC modules
Requires:       %{name} = %{version}-%{release} pkgconfig
Requires:       openssl-devel c-ares-devel glibc-devel libicu-devel%{?_isa}
BuildRequires: pkgconfig
Requires:       gcc-c++ redhat-rpm-config

%description devel
All includes and program files you need to compile your own znc
modules.

%package modtcl
Summary:       TCL module for ZNC

BuildRequires: tcl-devel

Requires:      %{name} = %{version}-%{release}
Requires:      tcl

%description modtcl
%{summary}.

%if 0%{?with_modperl}
%package modperl
Summary:       Perl module for ZNC

BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: swig

Requires:      %{name} = %{version}-%{release}
Requires:      perl-interpreter

Provides:      perl(ZNC::Module) = %{version}-%{release}

%description modperl
%{summary}.
%endif # 0%{?with_modperl}


%if 0%{?with_modpython}
%package modpython
Summary:       Python3 module for ZNC

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: swig

Requires:      %{name} = %{version}-%{release}
Requires:      python%{python3_pkgversion}

%description modpython
%{summary}.
%endif # 0%{?with_modpython}


%prep
# Verify GPG signature
gpghome="$(mktemp -qd)" # Ensure we don't use any existing gpg keyrings
key="%{SOURCE2}"
gpg2 --dearmor --quiet --batch --yes $key >/dev/null
gpgv2 --homedir "$gpghome" --quiet --keyring $key.gpg %{SOURCE1} %{SOURCE0}
rm -rf "$gpghome" $key.gpg # Cleanup tmp gpg home dir and dearmored key

%autosetup -p1

# The manual page references /usr/local/; fix that
sed -ie 's!/usr/local/!/usr/!' man/znc.1

%build
%if 0%{?rhel} == 7
sed -e 's/"openssl"/"openssl11"/g' -i configure
%endif

# NOTE(neil): 2024-09-02 aarch64 responds badly to building on large machines
%ifarch aarch64
%global _smp_build_ncpus 1
%endif

%cmake \
%if 0%{?with_modperl}
    -DWANT_PERL=1 \
%endif
%if 0%{?with_modpython}
    -DWANT_PYTHON=1 \
%endif
    -DWANT_SYSTEMD=1 \
    -DSYSTEMD_DIR=%{_unitdir} \
    -DWANT_IPV6=1 \
    -DWANT_CYRUS=1 \
    -DWANT_TCL=1

%cmake_build

%install
%cmake_install
install -d "%{buildroot}%{_sharedstatedir}/znc"
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/znc/


%pre
getent group znc >/dev/null || groupadd -r znc
getent passwd znc >/dev/null || \
    useradd -r -g znc -d /var/lib/znc -s /sbin/nologin \
    -c "Account for ZNC to run as" znc


%post
%systemd_post znc.service


%postun
%systemd_postun_with_restart znc.service


%preun
%systemd_preun znc.service


%files
%doc ChangeLog.md NOTICE README.md
%license LICENSE
%{_bindir}/znc
%{_mandir}/man1/znc.1*
%{_libdir}/znc
# exclude modperl, modpython, and modtcl files
%exclude %{_libdir}/znc/modperl/
%exclude %{_libdir}/znc/modperl.so
%exclude %{_libdir}/znc/perleval.pm
%if 0%{?with_modpython}
%exclude %{_libdir}/znc/__pycache__/
%exclude %{_libdir}/znc/modpython/
%exclude %{_libdir}/znc/modpython.so
%exclude %{_libdir}/znc/pyeval.py
%endif # 0%{?with_modpython}
%exclude %{_libdir}/znc/modtcl.so
%{_datadir}/znc/
# exclude modtcl files
%exclude %{_datadir}/znc/modtcl/
%{_unitdir}/znc.service
%attr(-,znc,znc) %{_sharedstatedir}/znc/

%files devel
%{_bindir}/znc-buildmod
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/znc/
%{_mandir}/man1/znc-buildmod.1*

%files modtcl
%{_libdir}/znc/modtcl.so
%{_datadir}/znc/modtcl/

%if 0%{?with_modperl}
%files modperl
%{_libdir}/znc/modperl/
%{_libdir}/znc/modperl.so
%{_libdir}/znc/perleval.pm
%endif # 0%{?with_modperl}

%if 0%{?with_modpython}
%files modpython
%{_libdir}/znc/modpython/
%{_libdir}/znc/modpython.so
%{_libdir}/znc/pyeval.py
%{_libdir}/znc/__pycache__/
%endif # 0%{?with_modpython}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.9.1-5
- Rebuild for ICU 76

* Sun Aug 25 2024 Neil Hanlon <neil@shrug.pw> - 1.9.1-4
- switch to pure cmake (1.9.0 turned configure into a wrapper which dropped options)
- resolve ftbfs, fti, new version (#226393 #2301380 #2292226)
- resolve CVE-2024-39844 (#2295622)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.1-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Nick Bebout <nb@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 1.8.2-28
- Rebuilt for Python 3.13

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.2-27
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.8.2-26
- Rebuilt for Python 3.13

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.8.2-25
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 František Zatloukal <fzatlouk@redhat.com> - 1.8.2-22
- Rebuilt for ICU 73.2

* Thu Jul 13 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.2-21
- Perl 5.38 re-rebuild updated packages

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.8.2-20
- Rebuilt for ICU 73.2

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.2-19
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.8.2-18
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.8.2-16
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.2-15
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8.2-13
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.2-12
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.8.2-10
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.8.2-8
- Rebuilt for Python 3.10

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.2-7
- Perl 5.34 rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 1.8.2-6
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 1.8.2-5
- Rebuild for ICU 69

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Robert Scheck <robert@fedoraproject.org> - 1.8.2-2
- Build against OpenSSL 1.1 on RHEL/CentOS 7 (for TLSv1.3 support)

* Thu Oct 01 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.1-2
- Perl 5.32 rebuild

* Fri Jun 19 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1
- Fix CVE-2020-13775 possible crash/NULL pointer dereference

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-2
- Rebuilt for Python 3.9

* Wed May 20 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0
- Fix systemd unit file to require network-online.target

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.7.5-5
- Rebuild for ICU 67

* Mon Apr 20 2020 Robert Scheck <robert@fedoraproject.org> - 1.7.5-4
- Modernize spec file slightly for building on RHEL/CentOS 7 and 8

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.7.5-2
- Rebuild for ICU 65

* Fri Sep 27 2019 Nick Bebout <nb@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5

* Mon Sep 23 2019 Nick Bebout <nb@fedoraproject.org> - 1.7.5-0.1
- Update to 1.7.5-rc1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 5 2019 Nick Bebout <nb@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4 to fix CVE-2019-12816

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-2
- Perl 5.30 rebuild

* Tue Apr 9 2019 Nick Bebout <nb@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3

* Wed Mar 27 2019 Nick Bebout <nb@fedoraproject.org> - 1.7.3-0.1
- Update to 1.7.3-rc1 to fix CVE-2019-9917

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.7.2-1
- Update to 1.7.2.
- Fix three paths in the manpage (#1624519).

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.7.1-4
- Rebuild for ICU 63

* Fri Aug 24 2018 Todd Zullinger <tmz@pobox.com> - 1.7.1-3
- Clean up ancient Fedora and RHEL conditionals
- Remove cruft from %%prep
- Use %%autosetup, %%make_build, and %%make_install macros
- Use https for URL and SOURCE tags
- Check upstream GPG signature in %%prep
- Simplify %%{_libdir}/znc/ file list
- Enable verbose make
- Pass --with-tcl to ensure tclConfig.sh is found
- Remove Group tag
- Use system-wide crypto policy
- Use %%license tag for LICENSE file
- Add ChangeLog.md and NOTICE files to %%doc
- Move znc-buildmod.1 to znc-devel

* Mon Jul 23 2018 Nick Bebout <nb@fedoraproject.org> - 1.7.1-2
- Add gcc-c++ and redhat-rpm-config to znc-devel's dependencies

* Tue Jul 17 2018 Nick Bebout <nb@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.7.0-7
- Rebuild for ICU 62

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.7.0-6
- Perl 5.28 rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-5
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.7

* Fri May 18 2018 Nick Bebout <nb@usi.edu> - 1.7.0-3
- Fix %%files to not use wildcard

* Tue May 15 2018 Pete Walter <pwalter@fedoraproject.org> - 1.7.0-2
- Rebuild for ICU 61.1

* Wed May 2 2018 Nick Bebout <nb@usi.edu> - 1.7.0-1
- Update to 1.7.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.6.6-2
- Rebuild for ICU 61.1

* Mon Mar 05 2018 Nick Bebout <nb@usi.edu> - 1.6.6-1
- Update to 1.6.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.5-11
- Fix systemd executions/requirements

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.6.5-10
- Rebuilt for switch to libxcrypt

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.6.5-9
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.6.5-6
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Mon Jun 12 2017 Petr Pisar <ppisar@redhat.com> - 1.6.5-5
- Fix creating /var/lib/znc directory (bug #1402472)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-4
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Mar 14 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.5-2
- Apply patch from tibbs to change how /var/lib/znc is created

* Tue Mar 14 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.5-1
- Update to 1.6.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-2
- Rebuild for Python 3.6

* Fri Dec 16 2016 Nick Bebout <nb@fedoraproject.org> - 1.6.4-1
- Update to 1.6.4

* Mon Nov 28 2016 Nick Bebout <nb@fedoraproject.org> - 1.6.4-0.1.rc2
- Update to 1.6.4-rc2

* Wed Nov 02 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.6.3-7
- Have the main package own %%_libdir/znc.  Previously the directory was
  unowned.

* Fri Oct 07 2016 Eli Young <elyscape@gmail.com> - 1.6.3-6
- Add support for modpython on EPEL >= 7

* Fri Oct 07 2016 Nick Bebout <nb@fedoraproject.org> - 1.6.3-5
- Fix bug 1367810

* Fri Oct 07 2016 Nick Bebout <nb@fedoraproject.org> - 1.6.3-4
- Clean up conditionals, use upstream systemd unit file

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.3-3
- Perl 5.24 rebuild

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.6.3-2
- rebuild for ICU 57.1

* Wed Apr 06 2016 Nick Bebout <nb@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Nick Bebout <nb@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.6.1-2
- rebuild for ICU 56.1

* Mon Aug 3 2015 Nick Bebout <nb@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Fri Jun 19 2015 Nick Bebout <nb@fedoraproject.org> - 1.6.0-5
- Revert change to ZNC path - bz#1179832 and bz#1148639

* Tue Jun 09 2015 Nick Bebout <nb@fedoraproject.org> - 1.6.0-4
- Add ZNC path to znc.service - bz#1179832
- Fix command to enable cyrus sasl - bz#1112022
- Add libicu dep to enable charset module - bz#1202033

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-3
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Nick Bebout <nb@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.4-7
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 03 2014 Björn Esser <bjoern.esser@gmail.com> - 1.4-5
- skip the python-subpkg on EPEL <= 7
- replaced %%define with %%global
- removed %%defattr, since it is not needed for recent releases
- conditionalized stuff for el <= 5
- small cleanups
- purged unused patches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Mon Apr 14 2014 Nick Bebout <nb@fedoraproject.org> - 1.2-3
- Fix potential crash bug when adding channels

* Mon Nov 11 2013 Nick Bebout <nb@fedoraproject.org> - 1.2-2
- Enable PIE, Fix systemd description, use systemd macros

* Mon Nov 11 2013 Nick Bebout <nb@fedoraproject.org> - 1.2-1
- Upgrade to 1.2

* Fri Oct 25 2013 Nick Bebout <nb@fedoraproject.org> - 1.2-0.4.rc2
- Upgrade to 1.2-rc2

* Thu Sep 26 2013 Nick Bebout <nb@fedoraproject.org> - 1.2-0.3.beta1
- Upgrade to 1.2-beta1

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.2-0.2.alpha1
- Perl 5.18 rebuild

* Sun Jul 28 2013 Nick Bebout <nb@fedoraproject.org> - 1.2-0.1.alpha1
- Upgrade to 1.2-alpha1

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0-3
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Nick Bebout <nb@fedoraproject.org> - 1.0-1
- Update to 1.0

* Thu Oct 18 2012 Nick Bebout <nb@fedoraproject.org> - 1.0-0.2.beta1
- Update to 1.0-beta1

* Thu Sep 13 2012 Nick Bebout <nb@fedoraproject.org> - 1.0-0.1.alpha1
- Update to 1.0-alpha1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Nick Bebout <nb@fedoraproject.org> - 0.206-1
- Upgrade to 0.206

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.204-4
- Rebuilt for c++ ABI breakage

* Mon Jan 23 2012 Nick Bebout <nb@fedoraproject.org> - 0.204-2
- Add init script for EPEL

* Mon Jan 23 2012 Nick Bebout <nb@fedoraproject.org> - 0.204-1
- Update to 0.204 to fix security issue CVE-2012-0033

* Mon Jan 09 2012 Nick Bebout <nb@fedoraproject.org> - 0.202-2
- Add glibc-devel, openssl-devel, c-ares-devel to requires for
- znc-devel so znc-buildmod will work

* Sun Sep 25 2011 Nick Bebout <nb@fedoraproject.org> - 0.202-1
- Update to 0.202

* Tue Aug 23 2011 Nick Bebout <nb@fedoraproject.org> - 0.200-1
- Update to 0.200

* Mon Aug 15 2011 Nick Bebout <nb@fedoraproject.org> - 0.200-0.5.rc1
- Don't create the znc user on Fedora 14 and lower and on EPEL

* Mon Aug 15 2011 Nick Bebout <nb@fedoraproject.org> - 0.200-0.4.rc1
- Change znc's homedir to /var/lib/znc

* Sun Aug 14 2011 Nick Bebout <nb@fedoraproject.org> - 0.200-0.3.rc1
- Re-add modpython, it somehow got disabled accidentally
- Also re-add modperl, it works now

* Sun Aug 14 2011 Nick Bebout <nb@fedoraproject.org> - 0.200-0.2.rc1
- Create /home/znc upon install

* Sat Aug 13 2011 Nick Bebout <nb@fedoraproject.org> - 0.200-0.1.rc1
- Update to 0.200-rc1

* Sat Aug 6 2011 Nick Bebout <nb@fedoraproject.org> - 0.2-0.2.beta1
- Update to 0.2-beta1, disable perl for now

* Fri Aug 5 2011 Nick Bebout <nb@fedoraproject.org> - 0.2-0.1.alpha1
- Update to 0.2-alpha1

* Mon Aug 1 2011 Nick Bebout <nb@fedoraproject.org> - 0.099-0.1.20110801git
- Update to latest git

* Sat Apr 2 2011 Nick Bebout <nb@fedoraproject.org> - 0.098-2
- Add provides for ZNC::Module to znc-modperl

* Tue Mar 29 2011 Nick Bebout <nb@fedoraproject.org> - 0.098-1
- Update to znc-0.098

* Sat Mar 12 2011 Nick Bebout <nb@fedoraproject.org> - 0.098-0.3.rc1
- Update to znc-0.098-rc1

* Wed Mar 02 2011 Nick Bebout <nb@fedoraproject.org> - 0.098-0.2.beta
- Update to znc-0.098-beta

* Wed Feb 23 2011 Nick Bebout <nb@fedoraproject.org> - 0.098-0.1.alpha1
- Update to znc 0.098-alpha1

* Tue Feb 15 2011 Nick Bebout <nb@fedoraproject.org> - 0.097-8.20110215git
- Update to latest git

* Wed Feb 09 2011 Nick Bebout <nb@fedoraproject.org> - 0.097-7.svn2277
- Update to svn2277

* Mon Jan 24 2011 Nick Bebout <nb@fedoraproject.org> - 0.097-6.svn2272
- Update to svn2272

* Mon Jan 17 2011 Nick Bebout <nb@fedoraproject.org> - 0.097-5.svn2269
- Update to svn2269

* Fri Jan 7 2011 Nick Bebout <nb@fedoraproject.org> - 0.097-4.svn2255
- Update to svn2255

* Mon Jan  3 2011 David Malcolm <dmalcolm@redhat.com> - 0.097-3.svn2214
- rebuild for newer python3 (see rhbz#666429)

* Fri Dec 24 2010 Nick Bebout <nb@fedoraproject.org> - 0.097-2.svn2214
- Patch has been upstreamed, update to svn2214

* Wed Dec 22 2010 Nick Bebout <nb@fedoraproject.org> - 0.097-1.svn2213
- Update to znc 0.097-svn2213 which also adds modpython

* Sun Nov 7 2010 Nick Bebout <nb@fedoraproject.org> - 0.096-2
- Build TCL module, move modperl and modtcl to separate subpackages

* Sat Nov 6 2010 Nick Bebout <nb@fedoraproject.org> - 0.096-1
- Update to znc 0.096

* Fri Sep 10 2010 Nick Bebout <nb@fedoraproject.org> - 0.094-1
- Update to znc 0.094

* Tue Aug 10 2010 Nick Bebout <nb@fedoraproject.org> - 0.093-2.svn2101
- Update to znc 0.093.svn2101 to fix CVE-2010-2812 and CVE-2010-2934

* Tue Aug 3 2010 Nick Bebout <nb@fedoraproject.org> - 0.093-1.svn2098
- Update to znc 0.093 svn2098

* Wed Jul 14 2010 Nick Bebout <nb@fedoraproject.org> - 0.092-1
- Update to znc 0.092

* Wed Jun 16 2010 Nick Bebout <nb@fedoraproject.org> - 0.090-2
- Backport r2026 of ZNC subversion repo to fix bug 603915
- NULL pointer dereference flaw leads to segfault under certain conditions

* Sun Jun 06 2010 Nick Bebout <nb@fedoraproject.org> - 0.090-1
- Update to znc 0.090

* Thu May 27 2010 Nick Bebout <nb@fedoraproject.org> - 0.090-0.1.rc1
- Update to znc 0.090-rc1

* Thu May 27 2010 Nick Bebout <nb@fedoraproject.org> - 0.089-7.svn2004
- Update to znc 0.089.svn2004

* Tue May 18 2010 Nick Bebout <nb@fedoraproject.org> - 0.089-6.svn2000
- Re-enable saslauth

* Tue May 18 2010 Nick Bebout <nb@fedoraproject.org> - 0.089-5.svn2000
- Re-enable modperl

* Tue May 18 2010 Nick Bebout <nb@fedoraproject.org> - 0.089-4.svn2000
- Update to znc 0.089.svn2000

* Sun Apr 25 2010 Nick Bebout <nb@fedoraproject.org> - 0.089-3.svn1944
- Update to znc 0.089.svn1944

* Wed Apr 7 2010 Nick Bebout <nb@fedoraproject.org> - 0.081-2.svn1897
- Update to znc 0.081.svn1897

* Mon Mar 29 2010 Nick Bebout <nb@fedoraproject.org> - 0.081-1.svn1850
- Update to znc 0.081.svn1850

* Thu Feb 18 2010 Nick Bebout <nb@fedoraproject.org> - 0.080-1
- Update to znc 0.080

* Wed Dec 30 2009 Nick Bebout <nb@fedoraproject.org> - 0.078-1
- Update to znc 0.078

* Sun Dec 13 2009 Nick Bebout <nb@fedoraproject.org> - 0.078-0.1.rc1
- Update to znc 0.078.rc1

* Mon Dec 7 2009 Nick Bebout <nb@fedoraproject.org> - 0.077-1.svn1672
- Add a DCCVHost config option which specifies the VHost (IP only!) for DCC bouncing. (r1647)
- Users cloned via the admin module no longer automatically connect into IRC. (r1653)
- Inform new clients about their /away status. (r1655)
- The "BUG" messages from route_replies can now be turned off via /msg *route_replies silent yes. (r1660)
- Rewrite znc.conf on SIGUSR1. (r1666)
- ISpoofFormat now supports ExpandString. (r1670) 
- Allow specifing port and password for delserver. (r1640)
- Write the config file on restart and shutdown. (r1641)
- Disable c-ares if it is not found unless --enable-c-ares was used. (r1644) (r1645)
- blockuser was missing an admin check. (r1648)
- Sometimes, removing a server caused znc to lose track of which server it is connected to. (r1659)
- Include a more portable header for uint32_t in SHA256.h. (r1665)
- Fixed cases where ZNC didn't properly block PONG replies to its own PINGs. (r1668)
- Fixed a possible crash if a client disconnected before an auth module was able to verify the login. (r1669)
- Away allowed to accidentally execute IRC commands. (r1672) 
- Comment out some weird code in Client.cpp. (r1646)
- Remove connect_throttle since it's obsoleted by fail2ban. (r1649)
- Remove outdated sample znc.conf. (r1654)
- route_replies now got a higher timeout before it generates a "BUG" message. (r1657)
- Documented the signals on which znc reacts better. (r1667) 
- New module hook OnIRCConnecting(). (r1638)
- Remove obsolete CUtils::GetHashPass(). (r1642)
- A module's GetDescription() now returns a C-String. (r1661) (r1662)
- When opening a module, check the version number first and don't do anything on a mismatch. (r1663) 

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.076-3
- rebuild against perl 5.10.1

* Fri Sep 25 2009 Nick Bebout <nb@fedoraproject.org> - 0.076-2
- Fix missing dist tag

* Fri Sep 25 2009 Nick Bebout <nb@fedoraproject.org> - 0.076-1
- Upgrade to ZNC 0.076
- http://en.znc.in/wiki/ChangeLog/0.076

* Fri Aug 28 2009 Nick Bebout <nb@fedoraproject.org> - 0.075-8.svn1613
- Rebuild with new openssl and svn 1613
- build 0.075-7.svn1610 existed but I had to remove it from the spec because
- the date was earlier than the date tmraz build the new openssl one

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 0.075-6.svn1608
- rebuilt with new openssl

* Thu Aug 20 2009 Nick Bebout <nb@fedoraproject.org> - 0.075-5.svn1608
- Upgrade to svn 1608

* Tue Aug 18 2009 Nick Bebout <nb@fedoraproject.org> - 0.075-4.20090818svn1602
- Upgrade to svn 1602

* Sat Aug 8 2009 Nick Bebout <nb@fedoraproject.org> - 0.075-3.20090807svn1594
- Fix source filename

* Fri Aug 7 2009 Nick Bebout <nb@fedoraproject.org> - 0.075-2.20090807svn1594
- Fix broken source tarball

* Fri Aug 7 2009 Nick Bebout <nb@fedoraproject.org> - 0.075-1.20090807svn1594
- Upgrade to svn 1594

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.074-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Nick Bebout <nb@fedoraproject.org> - 0.074-1
- Update to 0.074

* Wed Jul 22 2009 Nick Bebout <nb@fedoraproject.org> - 0.072-3
- Fix date in changelog, disable c-ares

* Wed Jul 22 2009 Nick Bebout <nb@fedoraproject.org> - 0.072-2
- Backport patch to fix webadmin skins issue introduced in 0.072

* Wed Jul 22 2009 Nick Bebout <nb@fedoraproject.org> - 0.072-1
- Upgrade to 0.072 of ZNC, fixes security issue in bug # 513152

* Sun Jul 12 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-7
- Fix License: to be GPLv2 with exceptions

* Sat Jul 11 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-6
- Fix permissions error in %%prep, not in source

* Sat Jul 11 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-5
- Fix permissions error on q.cpp and add LICENSE.OpenSSL

* Sat Jul 11 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-4
- Remove switch to enable debug, fix %%files section

* Fri Jul 10 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-3
- Move fixfreenode and log into separate znc-extra package
- Move awayping into separate znc-awayping package

* Thu Jul 9 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-2
- Include modules with main package

* Wed Jul 8 2009 Nick Bebout <nb@fedoraproject.org> - 0.070-1
- Initial Fedora package based on 0.070 of upstream
