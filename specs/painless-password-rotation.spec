Name: painless-password-rotation
Version: 0.3
Release: 6%{?dist}
Summary: Manages root password rotation with Hashicorp Vault
License: MIT
URL: https://github.com/cn137/painless-password-rotation
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: systemd-rpm-macros

%description
This package automates password rotation using HashiCorp Vault and a simple
Bash script. Scripts run in a systemd timer to dynamically update local
system passwords on a regular basis.


%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build


%install
mkdir -vp %{buildroot}%{_bindir}
mkdir -vp %{buildroot}%{_unitdir}
mkdir -vp %{buildroot}%{_sysconfdir}/sysconfig

install -pm 0755 rotate-linux-password %{buildroot}%{_bindir}/rotate-linux-password
install -pm 0644 systemd/rotate-password.service %{buildroot}%{_unitdir}/rotate-password.service
install -pm 0644 systemd/rotate-password.timer %{buildroot}%{_unitdir}/rotate-password.timer
install -pm 0600 vault-rotate %{buildroot}%{_sysconfdir}/sysconfig/vault-rotate
install -pm 0644 systemd/rotate-password@.service %{buildroot}%{_unitdir}/rotate-password@.service
install -Dpm 0644 docs/man/rotate-linux-password.1 %{buildroot}%{_mandir}/man1/rotate-linux-password.1


%post
%systemd_post rotate-password.service
%systemd_post rotate-password.timer


%preun
%systemd_preun rotate-password.service
%systemd_preun rotate-password.timer


%postun
%systemd_postun rotate-password.service
%systemd_postun_with_restart rotate-password.timer


%files
%license LICENSE
%{_mandir}/man1/rotate-linux-password.1*
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/vault-rotate
%{_bindir}/rotate-linux-password
%{_unitdir}/rotate-password.service
%{_unitdir}/rotate-password.timer
%{_unitdir}/rotate-password@.service


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 09 2023 Salman Butt <cn137@protonmail.com> - 0.3-1
- Initial build
- Resolves bz#2174438
