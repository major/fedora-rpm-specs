%global _hardened_build 1

# Upstream moved to github
%global forgeurl https://github.com/apalrd/tayga
%global	date 20250731
%global commit fb5c58f16adc79d1bda31b103b15fd8d55e7083f
%forgemeta

# tayga no longer builds cleanly on 32bit
ExcludeArch: %{ix86}

Name:		tayga
Version:	0.9.6
Release:	0.3%{?dist}
Summary:	Simple, no-fuss NAT64

License:	GPL-2.0-or-later
URL:		%{forgeurl}
Source0:	%{forgesource}
source1:	tayga.tmpfilesd.conf

Requires:	iproute

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	coreutils
BuildRequires:	systemd-units


%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.


%prep
echo Building %{forgesource} > /dev/null
%forgesetup
sed -i '
	s,setcap,#setcap,;
	s,\$(sysconfdir)/systemd/system,%{_unitdir},g;
	s,daemon-reload,--version,;
' Makefile


%build
%make_build CFLAGS="%{optflags}"


%check
%make_build test CFLAGS="%{optflags} -Wno-error=unused-but-set-variable -Wno-error=discarded-qualifiers"


%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} sbindir=%{_sbindir}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
install -p -D -m 0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Install a default unit
sed -i 's,%i,default,g' scripts/tayga@.service
install -p -D -m 0644 scripts/tayga@.service %{buildroot}/%{_unitdir}/%{name}.service


%post
%tmpfiles_create_package %{name} %{name}.tmpfilesd.conf
%systemd_post %{name}


%preun
%systemd_preun %{name}@.service


%files
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/*/*
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf


%changelog
* Tue Feb 10 2026 Ingvar Hagelund <ingvar@redpill-linpro.com> - 0.9.6-0.3
- Added workaround for fedora > 43 while waiting for upstream

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jun 19 2025 Ingvar Hagelund <ingvar@redpill-linpro.com> - 0.9.6-0.1
- Snapshot of upcoming upstream release 0.9.6
- New upstream source at github
- Removed patches and hacks merged upstream
- Installs a default systemd unit tayga.service that points to a default config
  (similar to Debian and upstream)
- Pulled support for older EL releases

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Florian Weimer <fweimer@redhat.com> - 0.9.2-19
- C99 compatibility fix (#2157585)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.9.2-11
- Remove obsolete requirement for %%postun scriptlet

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 0.9.2-3
- Added defattr tag for epel6
- Removed the example systemd service symlink
- Fixed "-fPIE" and "-Wl,-z,now" for epel-6-pp64
- Added buildroot macro for epel5
- No macro make_install on epel5
- Clean buildroot before install for epel5
- Added simple symlink instance support for epel
- Added a README.redhat describing how to create separate instances of tayga

* Wed Sep 30 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 0.9.2-2
- Added simple cflags override patch
- Added _hardened_build macro for fedora
- Added hardening flags for el6, except on ppc64, where PIE fails
- Added some simple instance support in el6 init script
- Added explicit buildrequires for gcc, make, and coreutils

* Wed Sep 02 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 0.9.2-1
- First wrap of tayga for Fedora, including sysvinit and systemd start scripts
