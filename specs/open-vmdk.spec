Name:           open-vmdk
Version:        0.3.8
Release:        3%{?dist}
Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
URL:            https://github.com/vmware/open-vmdk
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
Requires:       coreutils
Requires:       grep
Requires:       python3-PyYAML
Requires:       python3-lxml
Requires:       sed
Requires:       tar
Requires:       util-linux

%description
Open VMDK is an assistant tool for creating Open Virtual Appliance (OVA).
An OVA is a tar archive file with Open Virtualization Format (OVF) files
inside, which is composed of an OVF descriptor with extension .ovf,
one or more virtual machine disk image files with extension .vmdk,
and a manifest file with extension .mf.

%prep
%autosetup -p1

%build
%{!?_auto_set_build_flags:%{set_build_flags}}
%make_build

%install
%make_install

install -m0644 templates/*.ovf %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/mkova.sh
%{_bindir}/ova-compose
%{_bindir}/vmdk-convert
%{_datadir}/%{name}/
%config(noreplace) %{_sysconfdir}/open-vmdk.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 İsmail Dönmez <ismail@i10z.com> - 0.3.8-1
- Bump to version 0.3.8

* Sat Feb 03 2024 İsmail Dönmez <ismail@i10z.com> - 0.3.7-1
- Bump to version 0.3.7
  Drop honor-build-flags.patch, merged upstream

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Ismail Doenmez <ismail@i10z.com> - 0.3.6-1
- Initial build for 0.3.6
