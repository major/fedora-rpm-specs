Name:           livesys-scripts
Version:        0.2.1
Release:        2%{?dist}
Summary:        Scripts for auto-configuring live media during boot

License:        GPLv3+
URL:            https://pagure.io/livesys-scripts
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  make

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
%systemd_preun livesys.service livesys-late.service


%post
%systemd_post livesys.service livesys-late.service


%postun
%systemd_postun livesys.service livesys-late.service


%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/livesys
%{_libexecdir}/livesys/
%{_unitdir}/livesys*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Thu Mar 31 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sat Mar 26 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0-1
- Initial package
