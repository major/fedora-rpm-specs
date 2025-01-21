%global git_commit 1edfa966328dfc824e9b0351087bbfaf699dce04
%global git_date 20180302

%global git_short_commit %(c=%{git_commit};echo ${c:0:8})
%global git_suffix %{git_date}git%{git_short_commit}

%global src_name kvm-unit-tests

# it's bootable image like kernel or memtest86+, not host executable,
# so debuginfo is useless
%global debug_package %{nil}

Name:		tuned-profiles-nfv-host-bin
Version:	0
Release:	0.18.%{git_suffix}%{?dist}
Summary:	Binaries that are needed for the NFV host Tuned profile
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://www.linux-kvm.org/page/KVM-unit-tests
Source0:	https://git.kernel.org/pub/scm/virt/kvm/kvm-unit-tests.git/snapshot/%{src_name}-%{git_commit}.tar.gz
Patch0:         lto.patch
BuildRequires:	make, gcc, binutils, coreutils
ExclusiveArch:	%{ix86} x86_64

%description
Binaries that are needed for the Network Function Virtualization (NFV)
host Tuned profile.

%prep
%setup -q -n %{src_name}-%{git_commit}
%patch -P0 -p1

%build
./configure
# it's bootable image like kernel or memtest86+, not host executable,
# so we can deviate from the distro's flags
%make_build CFLAGS="%{optflags} -nostdlib -ffreestanding -fno-strict-aliasing -fno-stack-protector -Ilib -Ilib/x86" \
  LDFLAGS="%{?__global_ldflags}" x86/tscdeadline_latency.flat
# and we can also strip
strip x86/tscdeadline_latency.flat

%install
install -Dpm 0644 x86/tscdeadline_latency.flat %{buildroot}%{_datadir}/%{name}/tscdeadline_latency.flat

%files
%license COPYRIGHT
%{_datadir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.17.20180302git1edfa966
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Jeff Law <law@redhat.com> - 0-0.8.20180302git1edfa966
- Re-enable LTO

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 0-0.6.20180302git1edfa966
- Disable LTO

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180302git1edfa966
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20180302git1edfa966
- Initial release
