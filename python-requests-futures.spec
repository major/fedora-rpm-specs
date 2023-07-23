%bcond_with network

Name:           python-requests-futures
Version:        1.0.0
Release:        16%{?dist}
Summary:        Asynchronous Python HTTP Requests

License:        Apache-2.0
URL:            https://github.com/ross/requests-futures
Source:         %{pypi_source requests-futures}
BuildArch:      noarch

%global _description %{expand:
Small add-on for the Python requests http library. Makes use of Python 3.2’s
concurrent.futures or the back-port for prior versions of Python.}


%description %_description


%package -n python3-requests-futures
Summary:        %{summary}
Obsoletes:      python-requests-futures < 1.0.0-14

BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-requests-futures %_description


%prep
%autosetup -n requests-futures-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files requests_futures


%check
%if %{with network}
%pytest -v
%else
%pytest -v \
    test_requests_futures.py::RequestsTestCase::test_adapter_kwargs \
    test_requests_futures.py::RequestsTestCase::test_max_workers
%endif


%files -n python3-requests-futures -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.0-15
- Rebuilt for Python 3.12

* Wed Feb 15 2023 Carl George <carl@george.computer> - 1.0.0-14
- Convert to pyproject macros
- Rename binary package to follow guidelines
- Update license field to use SPDX identifier

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-5
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-2
- Condition for test with network

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora
