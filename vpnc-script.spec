%global git_date 20220509
%global git_commit_hash e52f8e66

Name:		vpnc-script
Version:	%{git_date}
Release:	4.git%{git_commit_hash}%{?dist}

Summary:	Routing setup script for vpnc and openconnect
BuildArch:	noarch
Requires:	iproute
Requires:	which

License:	GPLv2+
URL:		https://gitlab.com/openconnect/vpnc-scripts/
Source0:	vpnc-script

%description
This script sets up routing for VPN connectivity, when invoked by vpnc
or openconnect.


%prep
cp -p %SOURCE0 .

%build

%install
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/vpnc
install -m 0755 vpnc-script \
    %{buildroot}%{_sysconfdir}/vpnc/vpnc-script

%files
%dir %{_sysconfdir}/vpnc
%{_sysconfdir}/vpnc/vpnc-script

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220509-4.gite52f8e66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220509-3.gite52f8e66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220509-2.gite52f8e66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 20220509-1.gite52f8e66
- Updated to latest upstream version

* Mon Apr 04 2022 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 20220404-1.git40a8c62c
- Updated to latest upstream version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20201205-4.gitcdbd5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201205-3.gitcdbd5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201205-2.gitcdbd5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Nikos Mavrogiannopoulos <nmav@redhat.com>
- Updated to latest upstream vpnc-script

* Tue Sep 29 2020 Nikos Mavrogiannopoulos <nmav@redhat.com>
- Updated to latest upstream vpnc-script

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20171004-8.git6f87b0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20171004-7.git6f87b0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20171004-6.git6f87b0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20171004-5.git6f87b0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 01 2018 James Hennessy <jphxxxx@gmail.com>
- Fixed issue where vpnc-script is using resolvconf on systems where "resolve" isn't enabled in /etc/nsswitch.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171004-3.git6f87b0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171004-2.git6f87b0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 20171004-1.git6f87b0f
- Fixed issue with systemd-resolved (#1497750)

* Mon Aug 21 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 20170821-1.git6f87b0f
- new upstream release
- removed dependency on net-tools and added on iproute (#1481164)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140805-6.gitdf5808b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140805-5.gitdf5808b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140805-4.gitdf5808b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140805-3.gitdf5808b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 20 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 20140805-2.gitdf5808b
- Added dependency on which (#1068899)
- Added dependency on net-tools (#1007363)

* Wed Oct 01 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 20140805-1.gitdf5808b
- new upstream release (includes unbound patch)

* Tue Aug 05 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 20140705-1.git6201ebd
- new package

