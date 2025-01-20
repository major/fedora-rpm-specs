%global reponame popub
%global commit 6ffa11c634c1aa877d3f4b79ada19b8e6a92dae9
%global commitdate 20171007
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{!?_unitdir:1}
%global _unitdir /usr/lib/systemd/system
%endif

Name:    %{reponame}
Version: 0
Release: 0.23.%{commitdate}git%{shortcommit}%{?dist}
Summary: Publish a service from localhost onto your server
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL:     https://github.com/m13253/%{name}
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
BuildRequires: make
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%{?systemd_requires}
BuildRequires: systemd

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%if ! 0%{?gotest:1}
%define gotest() go test -ldflags "${LDFLAGS:-}" %{?**}
%endif

%description
%{summary}.

%package local
Summary: Publish a service from localhost onto your server - client side
Provides: portpub-local%{?_isa} = %{version}-%{release}
Obsoletes: portpub-local <= 0-0.2

%description local
%{summary}.
Local side package.

%package relay
Summary: Publish a service from localhost onto your server - server side
Provides: portpub-relay%{?_isa} = %{version}-%{release}
Obsoletes: portpub-relay <= 0-0.2

%description relay
%{summary}.
Server side package.

%prep
%setup -q -n %{name}-%{commit}

%build
cd %{reponame}-local
%gobuild -o %{reponame}-local

cd ../%{reponame}-relay
%gobuild -o %{reponame}-relay

%install
sed -i '/daemon-reload/d' systemd/Makefile
%make_install PREFIX=%{_prefix}

%post local
%systemd_post %{name}-local@.service

%preun local
%systemd_preun %{name}-local@.service

%postun local
%systemd_postun_with_restart %{name}-local@.service

%post relay
%systemd_post %{name}-relay@.service

%preun relay
%systemd_preun %{name}-relay@.service

%postun relay
%systemd_postun_with_restart %{name}-relay@.service

%files local
%doc README.md
%license COPYING
%{_bindir}/%{name}-local
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/local
%{_unitdir}/%{name}-local@.service

%files relay
%doc README.md
%license COPYING
%{_bindir}/%{name}-relay
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/relay
%{_unitdir}/%{name}-relay@.service

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.22.20171007git6ffa11c
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0-0.20.20171007git6ffa11c
- Rebuild for golang 1.22.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0-0.14.20171007git6ffa11c
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0-0.11.20171007git6ffa11c
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.3.20171007git6ffa11c
- Update to newest upstream.

* Mon Oct 02 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.2.20170920git4698f9a
- Add support for EPEL

* Mon Sep 18 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.20170406git25cf44e
- Rename to popub
- Improve makefile

* Sat Sep 09 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170406gitccd226a
- Initial with git version ccd226a.
