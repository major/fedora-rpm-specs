%ifarch %{nodejs_arches}
# el-7 does not have uglifyjs
%if "0%{?el7}" == "0"
%global uglify 1
%endif
%endif

Name: dnsdist
Version: 1.7.3
Release: 1%{?dist}
Summary: Highly DNS-, DoS- and abuse-aware loadbalancer
License: GPLv2
URL: https://dnsdist.org
Source0: https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2

ExcludeArch: %{ix86} #1994125
ExcludeArch: armv7hl #1994125
BuildRequires: boost-devel
BuildRequires: fstrm-devel
BuildRequires: gcc-c++
#ppc64 buildroot doesn't have libatomic, so require it
#https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/FSMMBCD2C2SPO4D66O35EGUTF7YXEPBA/
BuildRequires: libatomic
BuildRequires: libcap-devel
BuildRequires: libedit-devel
BuildRequires: libnghttp2-devel
BuildRequires: libsodium-devel
BuildRequires: lmdb-devel
%ifarch %{ix86} x86_64 %{mips} aarch64
BuildRequires: luajit-devel
%else
BuildRequires: lua-devel
%endif
BuildRequires: openssl-devel
BuildRequires: protobuf-devel
BuildRequires: re2-devel
BuildRequires: readline-devel
BuildRequires: systemd-devel
BuildRequires: systemd-units
BuildRequires: tinycdb-devel
%if 0%{?uglify}
BuildRequires: uglify-js
%endif
BuildRequires: make
Requires(post): systemd
Requires(preun): shadow-utils
Requires(preun): systemd
Requires(postun): systemd

%description
dnsdist is a highly DNS-, DoS- and abuse-aware loadbalancer. Its goal in life
is to route traffic to the best server, delivering top performance to
legitimate users while shunting or blocking abusive traffic.


%prep
%autosetup -p2

# run as dnsdist user
sed -i '/^ExecStart/ s/dnsdist/dnsdist -u dnsdist -g dnsdist/' dnsdist.service.in

%build
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --disable-static \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --enable-dnscrypt \
    --enable-dns-over-tls \
    --enable-unit-tests \
    --with-cdb \
    --with-lmdb \
    --with-nghttp2 \
    --with-re2

rm html/js/*
%if 0%{?uglify}
make min_js
%else
cp src_js/*.js html/js
rename .js .min.js html/js/*.js
%endif

make %{?_smp_mflags}
mv dnsdistconf.lua dnsdist.conf.sample

%install
make install DESTDIR=%{buildroot}

# install systemd unit file
install -D -p -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sysconfdir}/%{name}/

%pre
getent group dnsdist >/dev/null || groupadd -r dnsdist
getent passwd dnsdist >/dev/null || \
    useradd -r -g dnsdist -d / -s /sbin/nologin \
    -c "dnsdist user" dnsdist
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc dnsdist.conf.sample
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%dir %{_sysconfdir}/%{name}/


%changelog
* Wed Nov 02 2022 Sander Hoentjen <sander@hoentjen.eu> - 1.7.3-1
- Update to 1.7.3 (#2096239)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2 (#2096239)

* Tue May 03 2022 Sander Hoentjen <sander@hoentjen.eu> - 1.7.1-2
- Fixes build without uglify (#2070613)

* Sat Apr 30 2022 Sander Hoentjen <sander@hoentjen.eu> - 1.7.1-1
- Update to 1.7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Sander Hoentjen <sander@hoentjen.eu> - 1.7.0-1
- Update to 1.7.0 (#2041478)
- enable cdb
- enable nghttp2

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for libre2.so.9

* Thu Sep 16 2021 Sahana Prasad <sahana@redhat.com> - 1.6.1-2
- Rebuilt with OpenSSL 3.0.0

* Thu Sep 16 2021 Sander Hoentjen <sander@hoentjen.eu> - 1.6.1-1
- Update to 1.6.1 (#1884153)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.6.0-2
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 16 2021 Sander Hoentjen <sander@hoentjen.eu> - 1.6.0-1
- Update to 1.6.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.0-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:47:30 CET 2021 Adrian Reber <adrian@lisas.de> - 1.5.0-6
- Rebuilt for protobuf 3.14

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 1.5.0-5
- Rebuilt for protobuf 3.13

* Wed Aug 05 2020 Sander Hoentjen <sander@hoentjen.eu> - 1.5.0-4
- Fix building

* Wed Aug 05 2020 Sander Hoentjen <sander@hoentjen.eu> - 1.5.0-3
- Don't build on armv7hl, dnsdist fails to compile there

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 31 2020 ander Hoentjen <sander@hoentjen.eu> - 1.5.0-1
- Update to 1.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.4.0-5
- Rebuilt for protobuf 3.12

* Tue Mar 03 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.4.0-4
- Fix build with GCC 10 (#1799286)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.4.0-2
- Rebuild for protobuf 3.11

* Thu Nov 21 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.4.0-1
- Upstream released new stable version

* Mon Nov 04 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.4.0-0.1
- Upstream released new version
- Enable re2
- Link with LMDB
- Enable dnstap

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.3-2
- Rebuild for protobuf 3.6

* Sun Nov 18 2018 Sander Hoentjen <sander@hoentjen.eu> - 1.3.3-1
- Update to 1.3.3
- Fixes CVE-2018-14663

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.3.0-2
- Fix sigabrt on TCP query (https://github.com/PowerDNS/pdns/issues/6712)

* Thu May 31 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.3.0-1
- Upstream released new version
- Enable DNS over TLS

* Mon Feb 19 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.2.1-1
- Upstream released new version
- BuildRequires gcc-c++ (https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequire)
- Fix mixed indentation in spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.0-4
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-3
- Rebuild for protobuf 3.4

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- rebuild for libsodium

* Tue Aug 22 2017 Sander Hoentjen <sander@hoentjen.eu> - 1.2.0-1
- Update to 1.2.0
- Fixes CVE-2017-7557
- Fixes CVE-2016-7069

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-6
- Rebuild for protobuf 3.3.1

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-3
- Rebuild for protobuf 3.2.0

* Fri Dec 30 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.1.0-2
- ppc64 buildroot doesn't have libatomic, so require it

* Fri Dec 30 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.1.0-1
- New upstream release

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.0-4
- Rebuild for protobuf 3.1.0

* Tue Aug 30 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-3
- luajit is now also available for aarch64 and MIPS

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-2
- Rebuild for LuaJIT 2.1.0

* Thu Apr 21 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-1
- Upstream released new version

* Fri Apr 15 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.0.0-0.10.beta1
- Use the correct systemd service file

* Fri Apr 15 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.0.0-0.10.beta1
- Upstream released new version
- Run as dnsdist user / group (#1326623)
- Enable support for libre2 and protobufs
- Fix systemd detection
- Only build with lua if luajit is not available

* Tue Mar 08 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.0.0-0.9.alpha2
- Rebuild for libsodium soname bump

* Tue Feb 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.0-0.8.alpha2
- Add aarch64/s390(x) to luajit excludes
- uglify-js available on nodejs arches so use that define

* Mon Feb 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.7.alpha2
- Only copy .js files when minify-js is not available

* Mon Feb 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.6.alpha2
- PPC on EPEL does not have uglify-js

* Mon Feb 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.5.alpha2
- Don't build against luijit on ppc, it is not available there

* Mon Feb 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.4.alpha2
- Add sample config file

* Sat Feb 06 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.3.alpha2
- Update to new upstream

* Sun Jan 10 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.2.alpha1
- SPEC fixes for review

* Sun Jan 10 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.0.0-0.1.alpha1
- Initial package
