%global srcname jose


Name:      erlang-%{srcname}
Version:   1.11.2
Release:   11%{?dist}
BuildArch: noarch

License: MIT
Summary: JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
URL:     https://github.com/potatosalad/erlang-jose
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-base64url
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3
BuildRequires: erlang-triq


%description
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%{erlang3_compile}


%check
%{erlang3_test}


%install
%{erlang3_install}


%files
%license LICENSE.md
%doc ALGORITHMS.md
%doc CHANGELOG.md
%doc examples
%doc README.md
%{erlang_appdir}


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.11.2-1
- Update to 1.11.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.10.1-4
- Fix FTBFS (#1863505).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1787846).
- https://github.com/potatosalad/erlang-jose/blob/1.10.1/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.4-7
- Rebuild for https://bugzilla.redhat.com/show_bug.cgi?id=1748545

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
