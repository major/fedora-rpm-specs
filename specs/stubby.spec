Name:           stubby
Version:        0.4.3
Release:        6%{?dist}
Summary:        Application that act as a local DNS Privacy stub resolver

License:        BSD-3-Clause
URL:            https://github.com/getdnsapi/stubby
Source0:        https://github.com/getdnsapi/stubby/archive/v%{version}/stubby-%{version}.tar.gz

Provides:       getdns-stubby = 1.7.0-1
Obsoletes:      getdns-stubby < 1.7.0-1
%{?systemd_requires}

Patch1:         stubby-0.3.1-dnssec-ta.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: cmake
BuildRequires: getdns-devel >= 0.7.0
BuildRequires: openssl-devel
BuildRequires: libyaml-devel
BuildRequires: systemd-rpm-macros

%description
Stubby is a local DNS Privacy stub resolver (using DNS-over-TLS).
Stubby encrypts DNS queries sent from a client machine to a
DNS Privacy resolver increasing end user privacy.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install
find %{buildroot} -size 0 -delete
mkdir -p %{buildroot}%{_unitdir}
install -pm 0644 systemd/stubby.service %{buildroot}%{_unitdir}/stubby.service

%preun
%systemd_preun %{name}

%post
# systemd would replace it with symlink
if [ ! -L "%{_localstatedir}/cache/stubby" -a -d "%{_localstatedir}/cache/stubby" ]; then
       mv "%{_localstatedir}/cache/stubby"{,.rpmsave}
fi
%systemd_post %{name}

%postun
%systemd_postun_with_restart %{name}

%files
%{_bindir}/stubby
%config(noreplace) %{_sysconfdir}/stubby
%ghost %{_localstatedir}/cache/stubby
%{_unitdir}/stubby.service
%{_mandir}/man1/stubby.1.gz
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%license %{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/README.md


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Petr Menšík <pemensik@redhat.com> - 0.4.3-1
- Update to 0.4.3 (#2156047)

* Sat Oct 15 2022 Petr Menšík <pemensik@redhat.com> - 0.4.2-2
- Private users do not work with dynamic users
- Provide path to unbound-anchor key, but keep it commented out

* Thu Oct 13 2022 Petr Menšík <pemensik@redhat.com> - 0.4.2-1
- Update to 0.4.2 (#1974450)
- Use unbound-anchor key again

* Fri Sep 30 2022 Petr Menšík <pemensik@redhat.com> - 0.4.0-6
- Update License tag to SPDX identifier

* Tue Aug  2 2022 Joe Orton <jorton@redhat.com> - 0.4.0-5
- fix build (#2113738)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Paul Wouters <paul.wouters@aiven.io> - 0.4.0-1
- Resolves: rhbz#1968092 stubby-0.4.0 is available

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.1-0.9.20200318git7939e965
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.8.20200318git7939e965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Petr Menšík <pemensik@redhat.com> - 0.3.1-0.7.20200318git7939e965
- Move only directory, not symlink on upgrade (#1884575)

* Mon Oct 05 2020 Petr Menšík <pemensik@redhat.com> - 0.3.1-0.6.20200318git7939e965
- Move old cache directory on upgrade (#1884575)

* Mon Aug 10 2020 Artem Egorenkov <aegorenk@redhat.com> - 0.3.1-0.5.20200318git7939e965
- cmake macros are used instead of make

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.4.20200318git7939e965
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.3.20200318git7939e965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Artem Egorenkov <aegorenk@redhat.com> - 0.3.1-0.2.20200318git7939e965
- Snapshot information field added
- systemd-rpm-macros added to build requirements
- systemd-devel and systemd removed from build requirements
- Obsoletes version for getns-stubby fixed

* Thu Mar 12 2020 Artem Egorenkov <aegorenk@redhat.com> - 0.3.1-0.1.29785b
- First stubby package
