Name:           fedora-autofirstboot
Version:        1
Release:        7%{?dist}
Summary:        Collection of firstboot services for Fedora

License:        GPL-2.0-or-later
URL:            https://pagure.io/fedora-autofirstboot
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  make
Requires:       findutils
%{?systemd_ordering}

BuildArch:      noarch


%description
%{summary}.


%prep
%autosetup


%build
# Nothing to do

%install
%make_install


%preun
%systemd_preun fedora-autofirstboot.service


%post
%systemd_post fedora-autofirstboot.service


%postun
%systemd_postun fedora-autofirstboot.service


%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/fedora-firstboot
%{_libexecdir}/fedora-autofirstboot/
%{_unitdir}/fedora-autofirstboot.service


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 09 2022 Neal Gompa <ngompa@fedoraproject.org> - 1-1
- Initial package
