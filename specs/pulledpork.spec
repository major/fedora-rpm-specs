# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global etcfiles disablesid.conf dropsid.conf enablesid.conf modifysid.conf pulledpork.conf

Summary:	Pulled Pork for Snort and Suricata rule management
Name:		pulledpork
Version:	0.7.4
Release:	13%{?dist}
# contrib/oink-conv.pl is GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/shirkdog/pulledpork
Source0:	https://github.com/shirkdog/pulledpork/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Prepare pulledpork.conf for Fedora/EPEL
# sed -i 's#/usr/local/etc#/etc#g' pulledpork.conf
# sed -i 's#/usr/local/lib#/usr/lib64#g' pulledpork.conf
# sed -i 's#snort_path=/usr/local/bin#snort_path=/sbin#' pulledpork.conf
# sed -i 's#snort_control=/usr/local/bin#snort_control=/bin#' pulledpork.conf
# sed -i '/rule_url.*<oinkcode>/s/^/#/' pulledpork.conf
# sed -i '/sid=/s/^# //' pulledpork.conf
# sed -i 's#sid=/etc/snort#sid=/etc/pulledpork#' pulledpork.conf
# sed -i 's#distro=.*#distro=Centos-8#' pulledpork.conf
Source1:	%{name}.conf
BuildArch:	noarch

BuildRequires:	perl-generators
%if 0%{?fedora}
BuildRequires:	perl-interpreter
%else
BuildRequires:	perl
%endif

# Used by pulledpork to download rules, without it one gets errors like
# Error 501 when fetching https://snort.org/downloads/community/community-rules.tar.gz.md5
# https://github.com/shirkdog/pulledpork/issues/221
BuildRequires:	perl(LWP::Protocol::https)
Requires:	perl(LWP::Protocol::https)
# Other dependencies
BuildRequires:	perl(LWP::UserAgent)
Requires:	perl(LWP::UserAgent)
BuildRequires:	perl(Sys::Syslog)
Requires:	perl(Sys::Syslog)
BuildRequires:	perl(Archive::Tar)
Requires:	perl(Archive::Tar)
BuildRequires:	perl(File::Copy)
Requires:	perl(File::Copy)

# handle license on el{6,7}: global must be defined after the License field above
%{!?_licensedir: %global license %doc}


%description
Pulled Pork for Snort and Suricata rule management (from Google code).


%prep
%autosetup -n %{name}-%{version}


%build


%install
%{__install} -d -m 0755 $RPM_BUILD_ROOT/%{_bindir}
%{__install} -d -m 0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__install} -d -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}

%{__install} -m 0755 %{name}.pl $RPM_BUILD_ROOT/%{_bindir}/%{name}
%{__sed} -i 's|#!/usr/bin/env perl|#!/usr/bin/perl -w|' $RPM_BUILD_ROOT/%{_bindir}/%{name}

%{__cp} -rp contrib $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__chmod} 0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/contrib/oink-conv.pl

cd etc
%{__rm} -f pulledpork.conf
%{__cp} %{SOURCE1} .
for file in disablesid.conf dropsid.conf enablesid.conf modifysid.conf pulledpork.conf; do
    %{__install} -m 0664 $file $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
done


%check
./pulledpork.pl -V


%files
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/contrib
%{_datadir}/%{name}/contrib/oink-conv.pl
%{_datadir}/%{name}/contrib/README.CONTRIB
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/disablesid.conf
%config(noreplace) %{_sysconfdir}/%{name}/dropsid.conf
%config(noreplace) %{_sysconfdir}/%{name}/enablesid.conf
%config(noreplace) %{_sysconfdir}/%{name}/modifysid.conf
%config(noreplace) %{_sysconfdir}/%{name}/pulledpork.conf
%doc README.md doc/README.CATEGORIES doc/README.CHANGES doc/README.RULESET doc/README.SHAREDOBJECTS
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.4-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 0.7.4-6
- Change changelog email

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 0.7.4-1
- New upstream version
- Add a simple execution test

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 0.7.3-1
- version 0.7.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 0.7.2-2
- pulledpork.conf: IPRVersion needs to be path ending with slash
- pulledpork.conf: version must match the pulledpork version

* Tue Nov 08 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 0.7.2-1
- version 0.7.2, based on https://github.com/jasonish/nsm-rpms

