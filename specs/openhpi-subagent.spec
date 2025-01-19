Name:           openhpi-subagent
Version:        2.3.4
Release:        54%{?dist}
Summary:        NetSNMP subagent for OpenHPI

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.openhpi.org
Source0:        http://downloads.sourceforge.net/openhpi/%{name}-%{version}.tar.gz
Source1:        %{name}.service
# https://sourceforge.net/tracker/?func=detail&aid=2849869&group_id=71730&atid=532251
Patch1:         %{name}-2.3.4-format.patch
# https://sourceforge.net/tracker/?func=detail&aid=2951290&group_id=71730&atid=532251
# https://bugzilla.redhat.com/show_bug.cgi?id=564644
Patch2:         %{name}-2.3.4-dso.patch
# disable -Werror as gcc >= 4.6 is too strict for our code
Patch3:         %{name}-2.3.4-no-werror.patch

Patch4: openhpi-subagent-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openhpi-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  docbook-utils
BuildRequires:  systemd-units
Requires(post):         systemd-units
Requires(preun):        systemd-units
Requires(postun):       systemd-units

%description
The openhpi-subagent package contains the Service Availability Forum's
Hardware Platform Interface SNMP sub-agent.

%prep
%setup -q
%patch -P1 -p1 -b .format
%patch -P2 -p1 -b .dso
%patch -P3 -p1 -b .werror
%patch -P4 -p1 -b .configure-c99

# set timestamps back
touch -r configure.ac.dso configure.ac
touch -r configure.dso configure


%build
%configure
make %{?_smp_mflags}
make -C docs subagent-manual/book1.html


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable openhpid-subagent.service > /dev/null 2>&1 || :
    /bin/systemctl stop openhpid-subagent.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart openhpid-subagent.service >/dev/null 2>&1 || :
fi


%files
%doc COPYING README docs/subagent-manual
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/snmp/hpiSubagent.conf
%{_bindir}/hpiSubagent
%{_datadir}/snmp/mibs/*.mib

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.4-53
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Florian Weimer <fweimer@redhat.com> - 2.3.4-47
- Port configure script to C99

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 2.3.4-42
- Rebuilt for new net-snmp release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-41
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 2.3.4-36
- Rebuild for new net-snmp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.3.4-33
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.3.4-32
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.3.4-31
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.4-26
- Rebuilt for rpm 4.12.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Dan Horák <dan@danny.cz> - 2.3.4-19
- rebuilt for rpm 4.10

* Thu Mar 22 2012 Dan Horák <dan[at]danny.cz> - 2.3.4-18
- rebuilt against openhpi 3.0
- convert from initscript to systemd unit

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 11 2011 Dan Horák <dan[at]danny.cz> - 2.3.4-16
- rebuilt against net-snmp 5.7 and openhpi 2.17

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Dan Horák <dan[at]danny.cz> - 2.3.4-14
- rebuilt against net-snmp 5.6 and openhpi 2.15

* Thu Feb 25 2010 Dan Horák <dan[at]danny.cz> - 2.3.4-13
- updated initscript

* Sat Feb 13 2010 Dan Horák <dan[at]danny.cz> - 2.3.4-12
- fixed linking with the new --no-add-needed default (#564644)

* Mon Feb  8 2010 Dan Horák <dan[at]danny.cz> - 2.3.4-11
- switched to completely new initscript (#521804, #521656)

* Fri Feb  5 2010 Dan Horák <dan[at]danny.cz> - 2.3.4-10
- updated the initscript patch (#521804)

* Mon Oct 26 2009 Dan Horák <dan[at]danny.cz> - 2.3.4-9
- little update to the format patch for i386

* Fri Oct 23 2009 Dan Horák <dan[at]danny.cz> - 2.3.4-8
- fix build with net-snmp >= 5.5 (#524263)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.3.4-7
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 2.3.4-4
- rebuild with new openssl

* Fri Nov 21 2008 Dan Horak <dan[at]danny.cz> - 2.3.4-3
- fix Source0 URL

* Fri Apr 25 2008 Dan Horak <dan[at]danny.cz> - 2.3.4-2
- initscript is not a config file
- added missing R(postun)
- update the initd script

* Thu Apr 17 2008 Dan Horak <dan[at]danny.cz> - 2.3.4-1
- initial version 2.3.4
