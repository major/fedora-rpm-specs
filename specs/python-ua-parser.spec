%global pkg_name ua-parser
%global uap_core_version d668d6c6157db7737edfc0280adc6610c1b88029
%global run_unittests 0

Name:           python-%{pkg_name}
Version:        1.0.1
Release:        3%{?dist}
Summary:        Python port of Browserscope's user agent parser

License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
BuildArch:      noarch
Source0:        %{pypi_source ua_parser}
%if 0%{?run_unittests}
Source1:        https://github.com/ua-parser/uap-core/archive/%{uap_core_version}/uap-core-%{uap_core_version}.tar.gz
%endif

# ua_parser_rs resolver is currently not packaged for Fedora
Patch0:         ua_parser-no-ua_parse_rs.patch

Suggests:       python3-re2

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-re2


%description
Python port of Browserscope's user agent parser.


%package -n python3-%{pkg_name}
Summary:        Python port of Browserscope's user agent parser


%description -n python3-%{pkg_name}
Python port of Browserscope's user agent parser.


%prep
%autosetup -p1 -n ua_parser-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ua_parser


%check
%pyproject_check_import
%if 0%{?run_unittests}
tar xf %{SOURCE1} --transform 's|uap-core-%{uap_core_version}|uap-core|'
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} ua_parser/user_agent_parser_test.py
%endif


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 11 2025 Python Maint <python-maint@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.14

* Sun Mar 23 2025 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.18.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Roman Inflianskas <rominf@aiven.io> - 0.18.0-1
- Update to 0.18.0 (resolve rhbz#2221373)
- Make test file exclusion work.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.16.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 0.16.1-1
- Update to 0.16.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Sandro Mani <manisandro@gmail.com> - 0.10.0-2
- Fix license
- Add possibility to run unittest
- Don't install unittest

* Wed Dec 08 2021 Sandro Mani <manisandro@gmail.com> - 0.10.0-1
- Initial package
