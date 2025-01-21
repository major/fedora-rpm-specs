%global with_selinux 1
%global modulename trafficserver
%global selinuxtype targeted

Name:           trafficserver
Version:        10.0.2
Release:        2%{?dist}
Summary:        Fast, scalable and extensible HTTP/1.1 and HTTP/2 caching proxy server

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://trafficserver.apache.org/
Source0:        http://www.apache.org/dist/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/dist/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        https://downloads.apache.org/trafficserver/KEYS
Source3:        %{name}.service
Source4:        %{name}.sysusers
Source5:        %{name}.sysconf
Source6:        %{name}.tmpfilesd
Source7:        %{modulename}.te
Source8:        %{modulename}.if
Source9:        %{modulename}.fc

# Use Crypto Policies 
Patch0:         trafficserver-crypto-policy.patch

# Upstream does not support 32-bit architectures:
# https://github.com/apache/trafficserver/issues/4432
# s390x is also not a supported architecture and does not build
ExcludeArch:    %{arm} %{ix86} s390x

BuildRequires:  expat-devel hwloc-devel pcre-devel pcre2-devel zlib-devel xz-devel brotli-devel
BuildRequires:  libcurl-devel ncurses-devel gnupg python3
BuildRequires:  gcc gcc-c++ perl-ExtUtils-MakeMaker
BuildRequires:  cmake
BuildRequires:  libcap-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  openssl-devel
# OpenSSL engines are deprecated in f41/c10
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
BuildRequires:  openssl-devel-engine
%endif

Requires:       expat hwloc pcre pcre2 xz ncurses pkgconfig
Requires:       openssl
Requires:       systemd
Requires(postun): systemd

%if 0%{?with_selinux}
Requires:        (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif

%description
Traffic Server is a high-performance building block for cloud services.
It's more than just a caching proxy server; it also has support for
plugins to build large scale web applications.  Key features:

Caching - Improve your response time, while reducing server load and
bandwidth needs by caching and reusing frequently-requested web pages,
images, and web service calls.

Proxying - Easily add keep-alive, filter or anonymize content
requests, or add load balancing by adding a proxy layer.

Fast - Scales well on modern SMP hardware, handling 10s of thousands
of requests per second.

Extensible - APIs to write your own plug-ins to do anything from
modifying HTTP headers to handling ESI requests to writing your own
cache algorithm.

Proven - Handling over 400TB a day at Yahoo! both as forward and
reverse proxies, Apache Traffic Server is battle hardened.


%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             trafficserver SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Trafficserver SELinux policy module
%endif


%package devel
Summary: Development files for Apache Traffic Server plugins
BuildArch:           noarch
Requires: %{name} = %{version}-%{release}

%description devel
The header files for developing plugins for Apache Traffic Server

Apache Traffic Server plugins can do anything from modifying HTTP headers to
hadling ESI requests to providing a different caching algorithm. 


%package perl
Summary: Perl bindings for Apache Traffic Server management
BuildArch:           noarch
BuildRequires:       perl-generators
Requires: %{name} = %{version}-%{release}

%description perl
A collection of Perl interfaces to manage Apache Traffic Server
installations.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p0

%build

%cmake\
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}/%{name} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir}/%{name}/plugins \
    -DCMAKE_INSTALL_RUNSTATEDIR=/run/%{name} \
    -DCMAKE_INSTALL_LOGDIR=/var/log/%{name} \
    -DCMAKE_INSTALL_CACHEDIR=/var/cache/%{name} \
    -DBUILD_EXPERIMENTAL_PLUGINS=ON
%cmake_build

%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE7} selinux/
cp -p %{SOURCE8} selinux/
cp -p %{SOURCE9} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif

%install
%cmake_install

%check
%ctest 

%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%endif

# install systemd unit, etc.
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 -p %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -m 0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/

# Discard the init.d script
rm -f %{buildroot}%{_bindir}/trafficserver

# Remove libtool archives and static libs, testing plugins
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
rm -f %{buildroot}%{_libdir}/%{name}/plugin_*.so
rm -f %{buildroot}/usr/lib/debug%{_libdir}/%{name}/plugin_*.debug

# Why is the Perl stuff ending up in the wrong place ??
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}/usr/lib/perl5/Apache %{buildroot}%{perl_vendorlib}
rm -rf %{buildroot}/usr/lib/perl5

install -D -m 0644 -p %{buildroot}%{_libdir}/%{name}/pkgconfig/%{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
rm -rf %{buildroot}%{_libdir}/%{name}/pkgconfig

%pre
%sysusers_create_compat %{SOURCE4}

%post
%?ldconfig
%systemd_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%systemd_preun %{name}.service

%postun
%?ldconfig
%systemd_postun_with_restart %{name}.service

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%files
%license LICENSE
%doc README.md CHANGELOG* NOTICE STATUS

%attr(0750, trafficserver, trafficserver) %dir %{_sysconfdir}/%{name}
%attr(-, trafficserver, trafficserver) %config(noreplace) %{_sysconfdir}/%{name}/body_factory
%attr(-, trafficserver, trafficserver) %config(noreplace) %{_sysconfdir}/%{name}/*.config
%attr(-, trafficserver, trafficserver) %config(noreplace) %{_sysconfdir}/%{name}/*.yaml
%attr(-, trafficserver, trafficserver) %{_sysconfdir}/%{name}/trafficserver-release

%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf

%{_bindir}/traffic_cache_tool
%{_bindir}/traffic_crashlog
%{_bindir}/traffic_ctl
%{_bindir}/traffic_layout
%{_bindir}/traffic_logcat
%{_bindir}/traffic_logstats
%{_bindir}/traffic_manager
%{_bindir}/traffic_server
%{_bindir}/traffic_top
%{_bindir}/traffic_via
%{_bindir}/tspush

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/libts*.so*
%{_libdir}/%{name}/plugins/*.so

%attr(0750, trafficserver, trafficserver) %dir /var/log/%{name}
%attr(0750, trafficserver, trafficserver) %dir /run/%{name}
%attr(0750, trafficserver, trafficserver) %dir /var/cache/%{name}

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%files perl
%{_mandir}/man3/Apache::TS.3pm.gz
%{_mandir}/man3/Apache::TS::AdminClient.3pm.gz
%{_mandir}/man3/Apache::TS::Config::Records.3pm.gz
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/*


%files devel
%{_bindir}/tsxs
%{_includedir}/ts
%dir %{_includedir}/tscpp
%{_includedir}/tscpp/api
%{_includedir}/tscpp/util/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Jered Floyd <jered@redhat.com> 10.0.2-1
- Update to upstream 10.0.2
- Remove conditionals for releases we will not support
- NOTE: 10.x incorporaties a breaking change in configuration.
  Please review https://docs.trafficserver.apache.org/en/10.0.x/release-notes/upgrading.en.html

* Tue Nov 12 2024 Jered Floyd <jered@redhat.com> 9.2.6-1
- Update to upstream 9.2.6

* Thu Jul 25 2024 Jered Floyd <jered@redhat.com> 9.2.5-1
- Update to upstream 9.2.5
- Resolves CVE-2023-38522, CVE-2024-35161, CVE-2024-35296

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 9.2.4-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Jered Floyd <jered@redhat.com> 9.2.4-2
- Enable build with deprecated OpenSSL Engine
  https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine

* Wed Apr 3 2024 Jered Floyd <jered@redhat.com> 9.2.4-1
- Update to upstream 9.2.4
- Resolves CVE-2024-31309

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 11 2023 Jered Floyd <jered@redhat.com> 9.2.3-1
- Update to upstream 9.2.3
- Resolves CVE-2023-44487, CVE-2023-41752, CVE-2023-39456

* Wed Oct 4 2023 Jered Floyd <jered@redhat.com> 9.2.2-2
- Use OpenSSL 1.1.x from EPEL on RHEL 7 to fix Chrome 117+ bugs

* Wed Aug 9 2023 Jered Floyd <jered@redhat.com> 9.2.2-1
- Update to upstream 9.2.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Jered Floyd <jered@redhat.com> 9.2.1-1
- Update to upstream 9.2.1

* Fri Jan 20 2023 Jered Floyd <jered@redhat.com> 9.2.0-1
- Update to upstream 9.2.0

* Mon Dec 19 2022 Jered Floyd <jered@redhat.com> 9.1.4-1
- Update to 9.1.4, resolves CVE-2022-32749, CVE-2022-37392, CVE-2022-40743

* Sun Sep 11 2022 Jered Floyd <jered@redhat.com> 9.1.3-2
- FTI on EL8 due to lack of libbrotli pkg; use RPM autodeps instead

* Fri Sep 9 2022 Jered Floyd <jered@redhat.com> 9.1.3-2
- Update dependencies to enable brotli compression (RHBZ#2125520)

* Thu Aug 11 2022 Jered Floyd <jered@redhat.com> 9.1.3-1
- Update to 9.1.3, resolves CVE-2022-25763, CVE-2022-31779, CVE-2021-37150,
  CVE-2022-28129, CVE-2022-31780
- Resolve glibc 2.36 (f37) header incompatibility that caused FTBFS RHBZ#2112282

* Mon Jul 11 2022 Jered Floyd <jered@redhat.com> 9.1.2-9
- Don't try to use Crypto Policies on RHEL 7

* Mon Jun 13 2022 Jered Floyd <jered@redhat.com> 9.1.2-8
- Cherry-pick OpenSSL 3 compatibility required for RHEL 9
- Switch to OpenSSL 3 on f36+
- Include automake in BuildRequires

* Tue Jun 07 2022 Jered Floyd <jered@redhat.com> 9.1.2-7
- Exclude s390x architecture -- not supported upstream

* Thu May 12 2022 Jered Floyd <jered@redhat.com> 9.1.2-6
- Further changes based on package review; perl dependencies, paths

* Thu May 5 2022 Jered Floyd <jered@redhat.com> 9.1.2-5
- Changes based on spec review; change "RedHat" capitalization,
  and add link to upstream file layout discussion

* Mon May 2 2022 Jered Floyd <jered@redhat.com> 9.1.2-4
- Changes based on spec review

* Mon Apr 25 2022 Jered Floyd <jered@redhat.com> 9.1.2-3
- Allow self:process setsched, requested on EL8

* Mon Apr 18 2022 Jered Floyd <jered@redhat.com> 9.1.2-2
- Set SELinux policy to be more restrictive on privileged UDP ports

* Thu Apr 07 2022 Jered Floyd <jered@redhat.com> 9.1.2-1
- Initial revision
- Adapt to modern rpm conventions
- Add draft SELinux policy
- Don't run as root, just claim CAP_NET_BIND_SERVICE for
  privileged ports
- Merge and cleanup of upstream .spec file along with Copr version
  maintained by Hiroaki Nakamura <hnakamur@gmail.com>, based on
  long-ophaned package.  ChangeLog included below for reference.
  
* Wed Nov  3 2021 Hiroaki Nakamura <hnakamur@gmail.com> 9.1.1-1
- Update to 9.1.1

* Wed Sep  8 2021 Hiroaki Nakamura <hnakamur@gmail.com> 9.1.0-1
- Update to 9.1.0
- Disable mime-sanity-check which is usable only in debug build

* Tue Jun 29 2021 Hiroaki Nakamura <hnakamur@gmail.com> 9.0.2-1
- Update to 9.0.2
- Use yaml-cpp vendored in lib/yamlcpp

* Tue Jun 29 2021 Hiroaki Nakamura <hnakamur@gmail.com> 8.1.2-1
- Update to 8.1.2

* Fri Sep 13 2019 Hiroaki Nakamura <hnakamur@gmail.com> 8.0.5-1
- Update to 8.0.5 LTS release

* Fri Sep 13 2019 Hiroaki Nakamura <hnakamur@gmail.com> 7.1.8-1
- Update to 7.1.8 LTS release

* Mon Feb 25 2019 Hiroaki Nakamura <hnakamur@gmail.com> 7.1.6-1
- Update to 7.1.6 LTS release
- Return stale cache with s-maxage only if
  cache_required_headers is 99

* Fri Apr 20 2018 Hiroaki Nakamura <hnakamur@gmail.com> 7.1.3-1
- Update to 7.1.3 LTS release

* Mon Mar 26 2018 Hiroaki Nakamura <hnakamur@gmail.com> 7.1.2-1
- Update to 7.1.2 LTS release

* Tue Oct 24 2017 Hiroaki Nakamura <hnakamur@gmail.com> 7.1.1-1
- Update to 7.1.1 LTS release

* Thu Aug  3 2017 Hiroaki Nakamura <hnakamur@gmail.com> 7.1.0-1
- Update to 7.1.0 LTS release

* Wed Nov 16 2016 Hiroaki Nakamura <hnakamur@gmail.com> 7.0.0-2
- Remove expat-devel from build dependencies

* Wed Nov 16 2016 Hiroaki Nakamura <hnakamur@gmail.com> 7.0.0-1
- Update to 7.0.0 LTS release

* Fri Sep 30 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.2.0-2
- Return stale cache even if the origin server response has
  "Cache-Control: s-maxage" header.

* Wed Jul 27 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.2.0-1
- Update to 6.2.0 LTS release

* Fri May 20 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-10
- Add patch to add new value to proxy.config.http.cache.required_headers
  to require s-maxage for contents to be cached.
- Remove patch to concatenate multiple header values of
  the same name in TSLua.

* Wed May 11 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-9
- Fix bug in patch to concatenate multiple header values of
  the same name in TSLua.

* Tue May 10 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-8
- Concatenate multiple header values of the same name in TSLua.

* Wed Apr 27 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-7
- Remove patch to add proxy.config.http.cache.ignore_expires and
  proxy.config.http.cache.ignore_server_cc_max_age.

* Tue Apr 26 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-6
- Apply patch to add proxy.config.http.cache.ignore_expires and
  proxy.config.http.cache.ignore_server_cc_max_age.

* Wed Mar  9 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-5
- Disable patch to enable unix domain socket.

* Mon Mar  7 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-4
- Apply patch to enable unix domain socket.

* Sun Feb 14 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-3
- Enable luajit

* Sun Feb 14 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-2
- Set prefix to /opt/trafficserver and use relative directories

* Tue Feb  9 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.1-1
- Update to 6.1.1 LTS release

* Wed Feb  3 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.1.0-1
- Update to 6.1.0 LTS release

* Wed Jan 13 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.0.0-3
- Build experimental plugins

* Fri Jan  1 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.0.0-2
- Just use configure --disable-luajit without a patch or deleting files

* Fri Jan  1 2016 Hiroaki Nakamura <hnakamur@gmail.com> 6.0.0-1
- Update to 6.0.0 LTS release

* Fri Jan  1 2016 Hiroaki Nakamura <hnakamur@gmail.com> 5.3.0-2
- Add patch to cache_insepector to split multiline URLs correctly

* Sun Jun 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 5.3.0-1
- Update to 5.3.0 LTS release
- Build on aarch64 and power64
- Split perl bindings to sub package
- Cleanup and modernise spec

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.0.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 5.0.1-2
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Jan-Frode Myklebust <janfrode@tanso.net> - 5.0.1-0
- Fix CVE-2014-3525

* Wed Jul 16 2014 Jan-Frode Myklebust <janfrode@tanso.net> - 5.0.0-0
- New major version.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 4.2.1-4
- Rebuild for boost 1.55.0

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Wed Apr 30 2014 Jan-Frode Myklebust <janfrode@tanso.net> - 4.2.1-2
- Bump release tag. RC1 became final.

* Sat Apr 26 2014 Jan-Frode Myklebust <janfrode@tanso.net> - 4.2.1-rc1
- Update to 4.2.1-RC1

* Thu Apr 10 2014 Jan-Frode Myklebust <janfrode@tanso.net> - 4.2.0-0
- Update to 4.2.0

* Tue Dec 17 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 4.1.2-0
- Bump to final. No change from rc0.
- What's new: https://cwiki.apache.org/confluence/display/TS/What%27s+new+in+v4.1.x

* Thu Dec 12 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 4.1.2-rc0
- Update to 4.1.2-rc0.

* Mon Nov 11 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 4.0.2-5
- Buildrequire hwloc-devel, since it supposedly gives tremendous 
  positive performance impact to use hwlock to optimize scaling and
  number of threads and alignment for actual hardware we're running on.

* Sun Oct 20 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 4.0.2-3
- Rebuild for picking up ECC/ECDHE/EC/ECDSA/elliptic curves
  which are now enabled in OpenSSL.

* Fri Oct 11 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.2-3
- Add BR: systemd for systemd.macros (RHBZ #1018080).

* Thu Oct 10 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 4.0.2-2
- Update to 4.0.2, which fixes the following bugs:

    [TS-2144] - traffic_server crashes when clearing cache
    [TS-2173] - cache total hit/miss stats broken in version 4.0.1
    [TS-2174] - traffic_shell/traffic_line miss some stats value
    [TS-2191] - when http_info enabled, the http_sm may be deleted but a event associated it not cancelled.
    [TS-2207] - Centos5 out of tree perl build fails
    [TS-2217] - remove the option to turn off body factory - setting it to 0 will result in empty responses

- Automatically verify GPG signature during RPM prep.
- Build requires boost-devel.

* Tue Sep 3 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 4.0.1-1
- Update to 4.0.1.  What's new in v4.0.0:
  https://cwiki.apache.org/confluence/display/TS/What%27s+new+in+v4.0.0

- Upgrade instructions from earlier versions:
  https://cwiki.apache.org/confluence/display/TS/Upgrading+to+v4.0

  Important notes:

    proxy.config.remap.use_remap_processor has been removed,
    use the proxy.config.remap.num_remap_threads instead.

    Default proxy.config.cache.ram_cache.size has been increased by 
    a magnitude.

    Support for pre v3.2 port configuration directives has been removed.

    The following records.config parameters should be removed:

        CONFIG proxy.config.bandwidth_mgmt.filename STRING ""
        CONFIG proxy.config.admin.autoconf.wpad_filename STRING ""
        CONFIG proxy.config.username.cache.enabled INT 0
        CONFIG proxy.config.username.cache.filename STRING ""
        CONFIG proxy.config.username.cache.size INT 0
        CONFIG proxy.config.username.cache.storage_path STRING ""
        CONFIG proxy.config.username.cache.storage_size INT 0
        CONFIG proxy.config.http.wuts_enabled INT 0
        CONFIG proxy.config.http.log_spider_codes INT 0
        CONFIG proxy.config.http.accept_encoding_filter_enabled INT 0
        CONFIG proxy.config.http.accept_encoding_filter.filename STRING ""
        CONFIG proxy.config.net.throttle_enabled INT 0
        CONFIG proxy.config.net.accept_throttle INT 0
        CONFIG proxy.config.cluster.num_of_cluster_connections INT 0
        CONFIG proxy.config.cache.url_hash_method INT 0
        CONFIG proxy.config.plugin.extensions_dir STRING ""
        CONFIG proxy.local.http.parent_proxy.disable_connect_tunneling INT 0
        CONFIG proxy.config.remap.use_remap_processor INT 0

* Sun Aug 25 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.5-3
- bz#994224 Use rpm configure macro, instead of calling configure
  directly.

* Fri Aug 9 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.5-2
- bz#994224 Pass RPM_OPT_FLAGS as environment variables to configure,
  instead of overriding on make commandline. Thanks Dimitry Andric!

* Thu Aug 1 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.5-1
- Update to v3.2.5 which fixes the following bugs:

  [TS-1923] Fix memory issue caused by resolve_logfield_string()
  [TS-1918] SSL hangs after origin handshake.
  [TS-1483] Manager uses hardcoded FD limit causing restarts forever on traffic_server.
  [TS-1784] Fix FreeBSD block calculation (both RAW and directory)
  [TS-1905] TS hangs (dead lock) on HTTPS POST/PROPFIND requests.
  [TS-1785, TS-1904] Fixes to make it build with gcc-4.8.x.
  [TS-1903] Remove JEMALLOC_P use, it seems to have been deprecated.
  [TS-1902] Remove iconv as dependency.
  [TS-1900] Detect and link libhwloc on Ubuntu.
  [TS-1470] Fix cache sizes > 16TB (part 2 - Don't reset the cache after restart)

* Mon Jun 3 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.4-3
- Harden build with PIE flags, ref bz#955127. 

* Sat Jan 19 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.4-1
- Update to 3.2.4 release candiate

* Fri Jan 4 2013 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.3-1
- Update to v3.2.3. Remove patches no longer needed.

* Fri Aug 24 2012 Václav Pavlín <vpavlin@redhat.com> - 3.2.0-6
- Scriptlets replaced with new systemd macros (#851462)

* Thu Aug 16 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.0-5
- Add patch for TS-1392, to fix problem with SNI fallback.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.0-2
- Remove duplicate man-pages.

* Sat Jun 23 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 3.2.0-1
- Update to v3.2.0

* Sun Jun 10 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 3.0.5-1
- Remove trafficserver-gcc47.patch since it's fixed upstream, TS-1116.
- Join trafficserver-condrestart.patch into trafficserver-init_scripts.patch,
  and clean out not needed junk.

* Fri Apr 13 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 3.0.4-5
- Add hardened build.

* Wed Apr 11 2012 <janfrode@tanso.net> - 3.0.4-4
- Add patch for gcc-4.7 build issues.

* Mon Apr 9 2012 Dan Horák <dan[at]danny.cz> - 3.0.4-3
- switch to ExclusiveArch

* Fri Mar 23 2012 <janfrode@tanso.net> - 3.0.4-2
- Create /var/run/trafficserver using tmpfiles.d on f15+.

* Thu Mar 22 2012 <janfrode@tanso.net> - 3.0.4-1
- Update to new upstream release, v3.0.4.
- remove trafficserver-cluster_interface_linux.patch since this was fixed upstream, TS-845.

* Thu Mar 22 2012 <janfrode@tanso.net> - 3.0.3-6
- Remove pidfile from systemd service file. This is a type=simple
  service, so pidfile shouldn't be needed.

* Wed Mar 21 2012 <janfrode@tanso.net> - 3.0.3-5
- Add systemd support.
- Drop init.d-script on systemd-systems.

* Sun Mar 18 2012 <janfrode@tanso.net> - 3.0.3-3
- change default proxy.config.proxy_name to FIXME.example.com instead of the
  name of the buildhost
- configure proxy.config.ssl.server.cert.path and
  proxy.config.ssl.server.private_key.path to point to the standard /etc/pki/
  locations.

* Tue Mar 13 2012 <janfrode@tanso.net> - 3.0.3-2
- exclude ppc/ppc64 since build there fails, TS-1131.

* Sat Mar 10 2012 <janfrode@tanso.net> - 3.0.3-1
- Removed mixed use of spaces and tabs in specfile.

* Mon Feb 13 2012 <janfrode@tanso.net> - 3.0.3-0
- Update to v3.0.3

* Thu Dec 8 2011 <janfrode@tanso.net> - 3.0.2-0
- Update to v3.0.2
- Fix conderestart in initscript, TS-885.

* Tue Jul 19 2011 <janfrode@tanso.net> - 3.0.1-0
- Update to v3.0.1
- Remove uninstall-hook from trafficserver_make_install.patch, removed in v3.0.1.

* Thu Jun 30 2011 <janfrode@tanso.net> - 3.0.0-6
- Note FIXME's on top.
- Remove .la and static libs.
- mktemp'd buildroot.
- include license

* Mon Jun 27 2011 <janfrode@tanso.net> - 3.0.0-5
- Rename patches to start with trafficserver-.
- Remove odd version macro.
- Clean up mixed-use-of-spaces-and-tabs.

* Wed Jun 22 2011 <janfrode@tanso.net> - 3.0.0-4
- Use dedicated user/group ats/ats.
- Restart on upgrades.

* Thu Jun 16 2011 <zym@apache.org> - 3.0.0-3
- update man pages, sugest from Jan-Frode Myklebust <janfrode@tanso.net>
- patch records.config to fix the crashing with cluster iface is noexist
- cleanup spec file

* Wed Jun 15 2011 <zym@apache.org> - 3.0.0-2
- bump to version 3.0.0 stable release
- cleanup the spec file and patches

* Tue May 24 2011 <yonghao@taobao.com> - 2.1.8-2
- fix tcl linking

* Thu May  5 2011 <yonghao@taobao.com> - 2.1.8-1
- bump to 2.1.8
- comment out wccp

* Fri Apr  1 2011 <yonghao@taobao.com> - 2.1.7-3
- enable wccp and fixed compile warning
- never depends on sqlite and db4, add libz and xz-libs
- fix libary permission, do post ldconfig updates

* Sun Mar 27 2011 <yonghao@taobao.com> - 2.1.7-2
- patch traffic_shell fix

* Tue Mar 22 2011 <yonghao@taobao.com> - 2.1.7-1
- bump to v2.1.7
- fix centos5 building
- drop duplicated patches

* Sat Mar 12 2011 <yonghao@taobao.com> - 2.1.6-2
- fix gcc 4.6 building
- split into -devel package for devel libs
- fix init scripts for rpmlint requirement
- fix install scripts to build in mock, without root privileges

* Tue Mar 01 2011 <yonghao@taobao.com> - 2.1.6-1
- bump to 2.1.6 unstable
- replace config layout name as Fedora

* Thu Nov 18 2010 <yonghao@taobao.com> - 2.1.4
- initial release for public
- original spec file is from neomanontheway@gmail.com


