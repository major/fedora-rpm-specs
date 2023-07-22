%global forgeurl https://github.com/cmadamsgit/ks-install
%global commit 72db7819e3ed40c7f00bd6cd709335970a5ba9c5
# forgemeta getting a date mismatch at 20230506 vs 07
%global date 20230507
%forgemeta

Name:		ks-install
Summary:	Take a Fedora/CentOS/RHEL kickstart file and make a VM
Version:	0
Release:	0.5%{?dist}
URL:		%{forgeurl}
Source:		%{forgesource}
License:	GPLv3
BuildArch:	noarch
BuildRequires:	perl-generators perl-podlators
Requires:	virt-install
Recommends:	swtpm-tools

%description
Take a Fedora/CentOS/RHEL kickstart file and make a VM

%prep
%forgesetup

%build
pod2man ks-libvirt > ks-libvirt.1
touch --reference=ks-libvirt ks-libvirt.1

%install
install -D -m0755 ks-libvirt %{buildroot}%{_bindir}/ks-libvirt
install -D -m0644 ks-libvirt.1 %{buildroot}%{_mandir}/man1/ks-libvirt.1

%files
%license LICENSE
%doc examples
%{_bindir}/*
%{_mandir}/man*/*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 06 2023 Chris Adams <linux@cmadams.net> 0-0.4
- Add --arch and --machine options
- recognize "$basearch" in URLs (such as Alma mirror lists)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 15 2022 Chris Adams <linux@cmadams.net> 0-0.1
- initial package
