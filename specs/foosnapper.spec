Name:           foosnapper
Version:        1.4
Release:        3%{?dist}
Summary:        Automatic filesystem snapshotter
License:        GPL-2.0-or-later
URL:            https://github.com/FoobarOy/foosnapper
Source0:        https://github.com/FoobarOy/foosnapper/archive/v%{version}/foosnapper-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Requires:       python3
%{?systemd_requires}


%description
Automatic filesystem snapshotter, supporting Stratis and Btrfs.


%prep
%autosetup -p1


%build


%install
make install DESTDIR=%{buildroot}


%post
%systemd_post foosnapper.service foosnapper.timer


%preun
%systemd_preun foosnapper.service foosnapper.timer


%postun
%systemd_postun foosnapper.service
%systemd_postun_with_restart foosnapper.timer


%files
%license COPYING
%doc README.md
%doc %{_mandir}/man8/foosnapper.8*
%dir %{_sysconfdir}/foosnapper
%config(noreplace) %{_sysconfdir}/foosnapper/foosnapper.conf
%{_bindir}/foosnapper
%{_unitdir}/foosnapper.service
%{_unitdir}/foosnapper.timer


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 24 2025 Kim B. Heino <b@bbbs.net> - 1.4-1
- Upgrade to 1.4

* Wed Jun 19 2024 Kim B. Heino <b@bbbs.net> - 1.3-1
- Upgrade to 1.3

* Fri Jun 07 2024 Kim B. Heino <b@bbbs.net> - 1.2-1
- Upgrade to 1.2

* Tue Mar  7 2023 Kim B. Heino <b@bbbs.net> - 1.1-1
- Initial version
