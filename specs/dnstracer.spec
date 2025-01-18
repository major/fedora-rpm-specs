Name:           dnstracer
Version:        1.10
Release:        8%{?dist}
Summary:        Trace DNS queries to the source

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.mavetju.org/unix/dnstracer.php
Source0:        http://www.mavetju.org/download/dnstracer-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators

Patch:          with_debug.patch

%description
dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
%autosetup -p1 -n %{name}


%build
%make_build


%install
# working with a very basic and minimal make file
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
%make_install PREFIX=%{buildroot}%{_prefix} MANPREFIX=%{buildroot}%{_mandir}/man8/


%files
%license LICENSE
%doc README CONTACT CHANGES
%{_bindir}/dnstracer
%{_mandir}/man8/dnstracer.8*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 05 2022 Jonathan Wright <jonathan@almalinux.org> - 1.10-1
- Update to 1.10

* Thu Aug 04 2022 Jonathan Wright <jonathan@almalinux.org> - 1.9-28
- Push release tag to 28 to supercede old packages

* Thu Jul 21 2022 Jonathan Wright <jonathan@almalinux.org> - 1.9-1
- Initial package build

