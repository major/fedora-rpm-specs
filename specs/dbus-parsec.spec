%bcond_without check

# dbus-parsec is supposed to be daemon used through dbus
%global __cargo_is_lib() 0

Name:          dbus-parsec
Version:       0.5.0
Release:       2%{?dist}
Summary:       DBus PARSEC interface

License:       EUPL-1.2
URL:           https://github.com/fedora-iot/dbus-parsec
Source:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: NetworkManager-libnm-devel
BuildRequires: rust-packaging >= 21
BuildRequires: systemd dbus-common
Requires: parsec
%{?systemd_requires}

%description
%{summary}.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

install -D -p -m0644 dbus-parsec.service %{buildroot}%{_unitdir}/dbus-parsec.service
install -D -p -m0644 dbus-parsec.conf %{buildroot}%{_datadir}/dbus-1/system.d/dbus-parsec.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/dbus-parsec
install -d -m0755 %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/dbus-parsec %{buildroot}%{_libexecdir}/

%if %{with check}
%check
%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/dbus-parsec-control
%{_datadir}/dbus-1/system.d/dbus-parsec.conf
%{_libexecdir}/dbus-parsec
%{_localstatedir}/lib/dbus-parsec
%{_unitdir}/dbus-parsec.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-8
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-4
- Simplify spec and update for latest Rust packaging.

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-3
- Rebuild for fixed frame pointer compiler flags in Rust RPM macros.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-3
- Rebuild for new parsec-client

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Fri Oct 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-2
- Rebuild for new parsec/parsec-client

* Wed Sep 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Support storing WiFi (PSK and WPA-Enterprise) credentials

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-3
- Include createcredential.py sample client tool

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-2
- Require the parsec service to be running

* Mon Sep 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Thu Sep 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-1
- Initial release
