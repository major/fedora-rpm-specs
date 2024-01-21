%global srcname p1_acme

%global idna_ver 6.0.0
%global jiffy_ver 1.0.5
%global jose_ver 1.9.0
%global yconf_ver 1.0.7

Name:       erlang-%{srcname}
Version:    1.0.8
Release:    8%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    ACME client library for Erlang
URL:        https://github.com/processone/p1_acme/
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-idna >= %{idna_ver}
BuildRequires: erlang-jiffy >= %{jiffy_ver}
BuildRequires: erlang-jose >= %{jose_ver}
BuildRequires: erlang-rebar
BuildRequires: erlang-yconf >= %{yconf_ver}

Requires: erlang-idna >= %{idna_ver}
Requires: erlang-jiffy >= %{jiffy_ver}
Requires: erlang-jose >= %{jose_ver}
Requires: erlang-yconf >= %{yconf_ver}


%description
ACME client library for Erlang.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8 (#1807011).
- https://github.com/processone/p1_acme/blob/1.0.8/CHANGELOG.md

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (#1773766).
- https://github.com/processone/p1_acme/blob/1.0.3/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-1
- Initial release.
