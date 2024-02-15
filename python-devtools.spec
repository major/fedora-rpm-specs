%global pypi_name devtools

Name:           python-%{pypi_name}
Version:        0.12.2
Release:        1%{?dist}
Summary:        Dev tools for Python

License:        MIT
URL:            https://github.com/samuelcolvin/python-devtools
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The debug print command Python never had (and other things).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  black


Recommends:     python3-pygments

%description -n python3-%{pypi_name}
The debug print command Python never had (and other things).

%package -n python-%{pypi_name}-doc
Summary:        %{name} documentation

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n python-%{pypi_name}-%{version}
# Remove upper bound on executing version

%generate_buildrequires
%pyproject_buildrequires -w


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pypi_name}


%check
# until we get pytester_pretty packaged
rm -f tests/test_insert_assert.py

%pytest --pyargs \
-k "not test_repr_str and not test_executing_failure and not test_return_args and not test_colours and not test_insert_assert_no_pretty"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE


%files -n python-%{pypi_name}-doc
%doc docs/
%license LICENSE


%changelog
* Tue Feb 13 2024 Jonathan Wright <jonathan@almalinux.org> - 0.12.2-1
- update to 0.12.2 rhbz#2232792

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Python Maint <python-maint@redhat.com> - 0.11.0-2
- Rebuilt for Python 3.12

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 0.11.0-1
- update to 0.11.0 rhbz#2184884

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jonathan Wright <jonathan@almalinux.org> - 0.10.0-1
- update to 0.10.0 rhbz#2149131

* Mon Oct 10 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.0-2
- Remove the upper bound on the version of “executing” (fix RHBZ#2130680,
  fix RHBZ#2132027)

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 0.9.0-1
- Update to 0.9.0 rhbz#2125035
- Fix FTBFS rhbz#2098884 rhbz#2046869

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Update to latest upstream release 0.6
- Fix FTBFS (rhbz#1842118)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-4
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-3
- Exclude three failing tests
- Use license from tarball

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-2
- Fix description
- Add license (rhbz#1787452)

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Initial package for Fedora
