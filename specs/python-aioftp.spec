%global pypi_name aioftp
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.23.1
Release:        2%{?dist}
Summary:        FTP client/server for asyncio

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/aio-libs/aioftp
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
FTP client/server for asyncio.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with network}
BuildRequires:  %{py3_dist async-timeout}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist siosocks}
BuildRequires:  %{py3_dist trustme}
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%if %{with network}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license license.txt
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.23.1-1
- Update to latest upstream release (closes rhbz#2318613)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.22.3-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.22.3-2
- Rebuilt for Python 3.13

* Sat Feb 10 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.22.3-1
- Update to latest upstream release (closes rhbz#2256206)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.4-1
- Update to latest upstream release 0.21.4 (closes rhbz#2134236)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.21.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.3-1
- Update to latest upstream release 0.21.3 (closes rhbz#2077148)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.21.0-2
- Rebuilt for Python 3.11

* Fri Mar 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.0-1
- Update to latest upstream release 0.21.0 (closes rhbz#2017567)

* Fri Mar 04 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.20.1-1
- Update to latest upstream release 0.20.1 (closes rhbz#2017567)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.18.1-1
- Update to latest upstream release 0.18.1 (#1887058)

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.17.2-1
- Update to latest upstream release 0.17.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.1-1
- Update to latest upstream release 0.16.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to latest upstream release 0.16.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-2
- Better use of wildcards (rhbz#1787314)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Initial package for Fedora
