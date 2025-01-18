Name: byebyebios
Version: 1.0
Release: 5%{?dist}
Summary: Injects a x86 boot sector to inform of UEFI boot requirement
License: MIT-0
Url: https://gitlab.com/berrange/byebyebios
Source: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
ExclusiveArch: x86_64
BuildArch: noarch

BuildRequires: make
BuildRequires: python3-docutils
BuildRequires: binutils
BuildRequires: qemu-system-x86-core
BuildRequires: parted

%description
The byebyebios package provides an x86 boot sector that should
be copied to any disk image that does not intend to support
use of BIOS firmware. It will display a message to the user,
on the first serial port and VGA console, informing them of
the requirement to boot using UEFI firmware.

%prep
%autosetup -n %{name}-v%{version}

%build
%__make

%check
%__make test

%install
%make_install \
    DESTDIR=$RPM_BUILD_ROOT \
    bindir=%{_bindir} \
    datadir=%{_datadir} \
    mandir=%{_mandir}

%files
%license LICENSES/MIT-0.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nouefi.txt
%{_datadir}/%{name}/bootstub.bin
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 17 2023 Daniel P. Berrangé <berrange@redhat.com> - 1.0-1
- Initial package
