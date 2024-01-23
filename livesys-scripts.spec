Name:           livesys-scripts
Version:        0.6.0
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

# Make ghost files
mkdir -p %{buildroot}%{_sharedstatedir}/livesys
touch %{buildroot}%{_sharedstatedir}/livesys/livesys-session-extra
touch %{buildroot}%{_sharedstatedir}/livesys/livesys-session-late-extra


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
%dir %{_sharedstatedir}/livesys
%ghost %{_sharedstatedir}/livesys/livesys-session-extra
%ghost %{_sharedstatedir}/livesys/livesys-session-late-extra


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Mon Aug 21 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Tue Apr 11 2023 Adam Williamson <awilliam@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Tue Mar 21 2023 Adam Williamson <awilliam@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Sun Mar 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Mon Feb 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7

* Mon Feb 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6

* Mon Feb 06 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Sun Feb 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Sun Dec 11 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sun Dec 04 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Sun Nov 27 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Thu Mar 31 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sat Mar 26 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0-1
- Initial package
