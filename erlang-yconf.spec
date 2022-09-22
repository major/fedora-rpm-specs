%global srcname yconf

%global fast_yaml_ver 1.0.27

Name:       erlang-%{srcname}
Version:    1.0.13
Release:    1%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    YAML configuration processor
URL:        https://github.com/processone/yconf/
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-fast_yaml >= %{fast_yaml_ver}
BuildRequires: erlang-rebar3

Requires: erlang-fast_yaml >= %{fast_yaml_ver}


%description
YAML configuration processor.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Mon Aug 22 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.0.13-1
- Update to 1.0.13

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (#1807249).
- https://github.com/processone/yconf/blob/1.0.7/CHANGELOG.md

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (#1789113).
- https://github.com/processone/yconf/blob/1.0.2/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1.
- https://github.com/processone/yconf/blob/1.0.1/CHANGELOG.md

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.0-1
- Initial release.
