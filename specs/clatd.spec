Name:		clatd
Version:	1.6
Release:	6%{?dist}
Summary:	CLAT / SIIT-DC Edge Relay implementation for Linux

License:	MIT
URL:		https://github.com/toreanderson/clatd
Source0:	https://github.com/toreanderson/%{name}/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-interpreter
BuildRequires:	coreutils
BuildRequires:	%{_bindir}/pod2man

Requires:	iproute
Requires:	iptables
Requires:	tayga
Requires:	perl-interpreter
Requires:	perl(Net::DNS)
Requires:	perl(IO::Socket::IP)
Requires:	perl(File::Temp)
Requires:	perl(Net::IP)

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd


%description
clatd implements the CLAT component of the 464XLAT network architecture
specified in RFC 6877. It allows an IPv6-only host to have IPv4
connectivity that is translated to IPv6 before being routed to an upstream
PLAT (which is typically a Stateful NAT64 operated by the ISP) and there
translated back to IPv4 before being routed to the IPv4 internet.


%prep
%setup -q v%{release}.tar.gz

%build
pod2man	--name %{name} \
	--center "clatd - a CLAT implementation for Linux" \
	--section 8 \
	README.pod %{name}.8
gzip %{name}.8
echo '# Default clatd.conf
# See clatd(8) for a list of config directives' > %{name}.conf

sed -i "s,%{_sbindir}/clatd,%{_sbindir}/clatd -c %{_sysconfdir}/%{name}.conf," \
	scripts/*


%install
install -p -D -m0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -p -D -m0644 %{name}.8.gz %{buildroot}%{_mandir}/man8/%{name}.8.gz
install -p -D -m0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -d -m 0755 %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/
install -m 0755 scripts/%{name}.networkmanager %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/50-%{name}
install -p -D -m0644 scripts/%{name}.systemd %{buildroot}%{_unitdir}/%{name}.service


%post
%systemd_post %{name}.service


%files
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/NetworkManager
#dir #{_prefix}/lib/NetworkManager
#dir #{_prefix}/lib/NetworkManager/dispatcher.d
#{_prefix}/lib/NetworkManager/dispatcher.d/50-clatd
%doc README.pod
%{_mandir}/man8/*.8*
%license LICENCE
%{_unitdir}/%{name}.service


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-1
- New upstream release
- Pulled support for el6

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Michal Josef Špaček <mspacek@redhat.com> - 1.5-7
- Remove patch files, which are in upstream
- Rewrite obsolete perl dependency (IO::Socket::INET6 to IO::Socket::IP)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 3.5-3
- Move the NetworkManager dispatcher script out of /etc

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-1
- New upstream release
- Dropped patches included upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4-7
- Set a macro perl-interpreter for backwards compatibility for el6

* Tue Sep 26 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4-6
- Readded requirement of Net::IP. By some reason, it is not added
  automatically in mock builds. Closes bz #1494867

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.4-4
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4-2
- Fixes for bz#1302876, including
- Now BuildRequires pod2man
- Requires perl(Net::IP) is autogenerated, so not needed explicit
- clatd.conf is marked as config file
- Packaged 1.4 release tarball, and added changes from upstream as patches

* Tue Feb 23 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4-1.3.20160128git1abcec1
- Package now (co)owns /etc/NetworkManager/dispatcher.d, and no longer
  requires initscripts (bz #1302876)

* Thu Jan 28 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4-1.2.20160128git1abcec1
- First wrap for fedora and epel
