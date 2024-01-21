%global srcname stun

%global fast_tls_ver 1.1.8
%global p1_utils_ver 1.0.20

Name:      erlang-%{srcname}
Version:   1.2.4
Release:   4%{?dist}
BuildArch: noarch

License: ASL 2.0
Summary: STUN and TURN library for Erlang / Elixir
URL:     https://github.com/processone/stun/
Source0: https://github.com/processone/stun/archive/%{version}/stun-%{version}.tar.gz

Provides:  erlang-p1_stun = %{version}-%{release}
Obsoletes: erlang-p1_stun < 1.0.1

BuildRequires: erlang-edoc
BuildRequires: erlang-rebar3
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}

Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.


%prep
%autosetup -p1 -n stun-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.37-1
- Update to 1.0.37 (#1807191).
- https://github.com/processone/stun/blob/1.0.37/CHANGELOG.md

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.30-1
- Update to 1.0.30 (#1789036).
- https://github.com/processone/stun/blob/1.0.30/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.29-1
- Update to 1.0.29 (#1742462)
- https://github.com/processone/stun/blob/1.0.29/CHANGELOG.md

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.28-1
- Update to 1.0.28 (#1713277).
- https://github.com/processone/stun/blob/1.0.28/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.27-1
- Update to 1.0.27 (#1683148).
- https://github.com/processone/stun/blob/1.0.27/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.26-1
- Update to 1.0.26.
- https://github.com/processone/stun/blob/1.0.26/CHANGELOG.md
