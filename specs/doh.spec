Name:           doh
Version:        0.1
Release:        14%{?dist}
Summary:        Application for DNS-over-HTTPS name resolves and lookups
License:        MIT
URL:            https://github.com/curl/doh
Source0:        %{url}/archive/doh-%{version}.tar.gz
# https://github.com/curl/doh/commit/40df5306935f642f8866fa795a9e654309e73cdd
Patch0:         makefile-add-install-stage.patch
# https://github.com/curl/doh/pull/20
Patch1:         preserve-existing-cflags.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libcurl-devel


%description
A libcurl-using application that resolves a host name using DNS-over-HTTPS
(DoH).  This code uses POST requests unconditionally for this.


%prep
%autosetup -n doh-doh-%{version} -p 1


%build
%{set_build_flags}
%make_build


%install
%make_install
install -D -p -m 0644 doh.1 %{buildroot}%{_mandir}/man1/doh.1


%files
%license LICENSE
%doc README.md
%{_bindir}/doh
%{_mandir}/man1/doh.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Carl George <carl@george.computer> - 0.1-2
- Set build flags before building
- Add patch1 to preserve existing CFLAGS

* Thu Sep 19 2019 Carl George <carl@george.computer> - 0.1-1
- Initial package rhbz#1753769
