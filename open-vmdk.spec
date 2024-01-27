Name:           open-vmdk
Version:        0.3.6
Release:        3%{?dist}
Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
URL:            https://github.com/vmware/open-vmdk
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Honor CFLAGS/LDFLAGS
Patch1:         honor-build-flags.patch
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
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Ismail Doenmez <ismail@i10z.com> - 0.3.6-1
- Initial build for 0.3.6
