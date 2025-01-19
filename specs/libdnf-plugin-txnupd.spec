# Minimum compatible version
%global libdnf_minver 0.60
%global tukit_minver 3.1.2

Name:           libdnf-plugin-txnupd
Version:        0.1.3
Release:        13%{?dist}
Summary:        libdnf plugin to implement transactional updates

License:        LGPL-2.1-or-later
URL:            https://code.opensuse.org/microos/libdnf-plugin-txnupd
#Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Use pagure.io mirror as code.opensuse.org doesn't have on-demand archives yet
Source0:        https://pagure.io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdnf) >= %{libdnf_minver}
BuildRequires:  pkgconfig(tukit) >= %{tukit_minver}

# We need a minimum version of these libraries beyond soname for working APIs
Requires:       libdnf%{?_isa} >= %{libdnf_minver}
Requires:       libtukit%{?_isa} >= %{tukit_minver}

# We need the transactional update dracut module
Requires:       dracut-transactional-update

# To ensure directories for configuration files are in place
Requires:       dnf-data

# This is intended to be used alongside MicroDNF and PackageKit
Recommends:     (microdnf or PackageKit)

# Do not permit normal DNF snapper plugin on the same system
Conflicts:      dnf-plugin-snapper

%description
This package contains the plugin to implement transactional updates
as a libdnf plugin. This plugin hooks into the DNF "context" for
Micro DNF and PackageKit to enable this functionality in normal use.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

# Add configuration to mark this package as protected by libdnf
mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d
echo "%{name}" > %{buildroot}%{_sysconfdir}/dnf/protected.d/txnupd.conf


%files
%license LICENSE
%doc README.md
%{_libdir}/libdnf/plugins/txnupd.so
%{_sysconfdir}/dnf/protected.d/txnupd.conf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.1.3-12
- Rebuild for transactional-update 4.8 again

* Wed Oct 16 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.1.3-11
- Rebuild for transactional-update 4.8
- Use correct SPDX identifiers

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.3-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.3-1
- Update to 0.1.3

* Sun Mar 07 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.2-1
- Rebase to 0.1.2
- Add protected.d file for self-protection

* Mon Feb 01 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20210127.6a91d55-0.1
- Update to support tukit 3.0.0

* Tue Dec 29 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20201223.2f7a284-0.2
- Add dracut-transactional-update dependency

* Thu Dec 24 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20201223.2f7a284-0.1
- Initial packaging
