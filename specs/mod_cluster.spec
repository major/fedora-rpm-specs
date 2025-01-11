%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:     %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          mod_cluster
Version:       1.3.21
Release:       1%{?dist}
Summary:       Apache HTTP Server dynamic load balancer with Wildfly and Tomcat libraries
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:       LGPL-3.0-only
URL:           http://modcluster.io/
Source0:       https://github.com/modcluster/mod_cluster/archive/%{namedversion}/mod_cluster-%{namedversion}.tar.gz
Source1:       mod_cluster.conf
Source2:       README.fedora

Requires:      httpd >= 2.4.49
Requires:      httpd-mmn = %{_httpd_mmn}

# Eventually this package will be renamed to mod_proxy_cluster
#Obsoletes:     mod_cluster <= 1.3.3-14

BuildRequires: httpd-devel >= 2.4.49
BuildRequires: autoconf
BuildRequires: make
BuildRequires: gcc

%description
Mod_cluster is an httpd-based load balancer. Like mod_jk and mod_proxy,
mod_cluster uses a communication channel to forward requests from httpd to one
of a set of application server nodes. Unlike mod_jk and mod_proxy, mod_cluster
leverages an additional connection between the application server nodes and
httpd. The application server nodes use this connection to transmit server-side
load balance factors and lifecycle events back to httpd via a custom set of
HTTP methods, affectionately called the Mod-Cluster Management Protocol (MCMP).
This additional feedback channel allows mod_cluster to offer a level of
intelligence and granularity not found in other load balancing solutions.

%prep
%setup -q -n mod_cluster-%{namedversion}

%build

CFLAGS="$RPM_OPT_FLAGS"
export CFLAGS

module_dirs=( advertise mod_manager mod_proxy_cluster mod_cluster_slotmem )

for dir in ${module_dirs[@]} ; do
    pushd native/${dir}
        sh buildconf
        %configure --libdir=%{_libdir} --with-apxs=%{_httpd_apxs}
        make %{?_smp_mflags}
    popd
done

%install
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_confdir}

module_dirs=( advertise mod_manager mod_proxy_cluster mod_cluster_slotmem )
for dir in ${module_dirs[@]} ; do
    pushd native/${dir}
        cp ./*.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules
    popd
done

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/

install -pm 0644 %{SOURCE2} README

%files
%doc README
%license lgpl.txt
%{_libdir}/httpd/modules/mod_advertise.so
%{_libdir}/httpd/modules/mod_manager.so
%{_libdir}/httpd/modules/mod_proxy_cluster.so
%{_libdir}/httpd/modules/mod_cluster_slotmem.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf

%changelog
* Wed Jan 8 2025 Vladimir Chlup <vchlup@redhat.com> - 1.3.21-1
- Update to upstream 1.3.21.Final release

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.20-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Vladimir Chlup <vchlup@redhat.com> - 1.3.20-1
- Upstream release 1.3.20.Final

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 George Zaronikas <gzaronik@redhat.com> - 1.3.16-1
- Bump to upstream release 1.3.16.Final

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 06 2020 Dimitris Sartzetakis <dsartzet@redhat.com> - 1.3.14-1
- Upstream release 1.3.14.Final

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Hui Wang <huwang@redhat.com> - 1.3.12-1
- Upstream release 1.3.12.Final

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Michal Karm Babacek <karm@fedoraproject.org> 1.3.11-1
- Updates comments about Selinux in mod_cluster.conf
- Removes Java libs for Tomcat 8 and Wildfly 10, to be reintroduced for Tomcat 9 in a separate package
- Fix for MODCLUSTER-690
- Back port upstream warning fixes
- Fix for MODCLUSTER-543
- Fix forMODCLUSTER-684
- Fix 503 found while investigating MODCLUSTER-684
- Fix for JBCS-634 decrease loops per vhosts for balancer changes
- Fix for MODCLUSTER-622 segfault in process_info
- Fix for MODCLUSTER-582 and clean some C++ comments
- Fix for MODCLUSTER-590 - workers array for Deterministic failover is now allocated dynamically
- Fix for MODCLUSTER-526 We don't use helper->shared if it's already NULL
- Fix for MODCLUSTER-550 Failover targets should be chosen deterministically
- Fix for MODCLUSTER-547
- Fix CVE-2016-8612 JBCS-193
- Fix for MODCLUSTER-522
- Fix for MODCLUSTER-534 update to MODCLUSTER-435 normalizing balancer name
- Security enhancements for protocol parser

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Michal Karm Babacek <karm@fedoraproject.org> 1.3.3-8
- mod_cluster.conf and README file updates about Firewalld and Selinux

* Mon Sep 05 2016 Michal Karm Babacek <karm@fedoraproject.org> 1.3.3-7
- adjusted release number, build for f25

* Tue Aug 30 2016 gil cattaneo <puntogil@libero.it> 1.3.3-5
- remove useless pom macros
- add subpackages for parent POMs
- use custom _httpd_confdir macro

* Mon Aug 29 2016 gil cattaneo <puntogil@libero.it> 1.3.3-4
- fix BR list
- marked as noarch only the java stuff

* Mon Aug 29 2016 Michal Karm Babacek  <karm@fedoraproject.org> 1.3.3-3
- Added mvn(..) BuildRequires for Tomcat libs instead of direct dependency on tomcat package

* Mon Aug 29 2016 gil cattaneo <puntogil@libero.it> 1.3.3-2
- fix pom macros

* Mon Aug 29 2016 Michal Karm Babacek  <karm@fedoraproject.org> - 1.3.3-1
- Upstream release 1.3.3.Final
- Refactored spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 1.2.6-3
- fix _httpd_mmn expansion in absence of httpd-devel

* Fri Jan 17 2014 Marek Goldmann <mgoldman@redhat.com> - 1.2.6-2
- Add support for conditional build that builds only HTTPD module

* Wed Sep 25 2013 Marek Goldmann <mgoldman@redhat.com> - 1.2.6-1
- Upstream release 1.2.6.Final
- Support for Apache 2.4 in mod_cluster.conf

* Mon Aug 05 2013 Marek Goldmann <mgoldman@redhat.com> - 1.2.4-1
- Upstream release 1.2.4.Final

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Marek Goldmann <mgoldman@redhat.com> - 1.2.1-2
- Added missing container.pom

* Mon May 07 2012 Marek Goldmann <mgoldman@redhat.com> - 1.2.1-1
- Upstream release 1.2.1.Final
- Port to httpd 2.4, RHBZ#813871

* Wed Mar 28 2012 Marek Goldmann <mgoldman@redhat.com> - 1.2.0-1
- Upstream release 1.2.0.Final
- Add java subpackage with AS7 required jars

* Tue Mar 27 2012 Marek Goldmann <mgoldman@redhat.com> - 1.1.1-4
- Require httpd-mmn RHBZ#803068

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 11 2011 Marek Goldmann <mgoldman@redhat.com> - 1.1.1-2
- Another round of cleanup in spec file
- Patch that disables compilation-time warnings

* Thu Mar 10 2011 Marek Goldmann <mgoldman@redhat.com> - 1.1.1-1
- Upstream release 1.1.1
- Cleanup in spec file

* Fri Nov 12 2010 Marek Goldmann <mgoldman@redhat.com> - 1.1.0-1
- Initial release

