%bcond_with sourcegit

Name:           llmnrd
Version:        0.7
Release:        6%{?dist}
Summary:        Link-Local Multicast Resolution Daemon

License:        GPLv2
URL:            https://github.com/tklauser/llmnrd
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        llmnrd.service

BuildRequires:  gcc
BuildRequires:  make
%if %{with sourcegit}
BuildRequires:  git-core
%endif
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
llmnrd is a daemon implementing the Link-Local Multicast Name Resolution (LLMNR)
protocol according to RFC 4795.

llmnrd will respond to name resolution queries sent by Windows clients in
networks where no DNS server is available. It supports both IPv4 and IPv6.

%prep
%autosetup -p1


%build
%set_build_flags
%make_build prefix=%{_usr} Q=


%install
%make_install prefix=%{_usr} Q=
install -Dp %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/llmnrd.service

%check
# would not find result, but it tries
${RPM_BUILD_ROOT}%{_bindir}/llmnr-query -I lo localhost

%post
%systemd_post %{name}

%preun
%systemd_preun %{name}

%postun
%systemd_postun_with_restart %{name}


%files
%doc README*
%license COPYING
%{_bindir}/llmnr-query
%{_sbindir}/llmnrd
%{_unitdir}/llmnrd.service
%{_mandir}/man1/llmnr-query.1*
%{_mandir}/man8/llmnrd.8*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Petr Menšík <pemensik@redhat.com> - 0.7-1
- Initial release
