%global srcname p1_utils


Name:       erlang-%{srcname}
Version:    1.0.25
Release:    4%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    Erlang utility modules from ProcessOne
URL:        https://github.com/processone/p1_utils/
Source0:    https://github.com/processone/p1_utils/archive/%{version}/p1_utils-%{version}.tar.gz
BuildRequires: erlang-rebar3


%description
p1_utils is an application containing ProcessOne modules and tools that are
leveraged in other development projects.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{erlang3_compile}


%check
%{erlang3_test}


%install
%{erlang3_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.0.25-1
- Update to 1.0.25

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.20-1
- Update to 1.0.20 (#1807014).
- https://github.com/processone/p1_utils/blob/1.0.20/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17 (#1788909).
- https://github.com/processone/p1_utils/blob/1.0.17/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.16-1
- Update to 1.0.16 (#1742472).
- https://github.com/processone/p1_utils/blob/1.0.16/CHANGELOG.md

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.15-1
- Update to 1.0.15 (#1713425).
- https://github.com/processone/p1_utils/blob/1.0.15/CHANGELOG.md

* Sat Apr 13 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14 (#1683182).
- https://github.com/processone/p1_utils/blob/1.0.14/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
