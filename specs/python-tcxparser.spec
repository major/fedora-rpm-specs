%bcond_without tests

%global pretty_name tcxparser
%global pypi_name python-%{pretty_name}
%global extract_name python_tcxparser

%global _description %{expand:
python-tcxparser is a minimal parser for Garmin's TCX file format. It is not in
any way exhaustive. It extracts just enough data to show the most important
attributes of sport activity.}

Name:           python-%{pretty_name}
Version:        2.3.0
Release:        11%{?dist}
Summary:        Tcxparser is a minimal parser for Garmin TCX file format

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/vkurup/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist lxml}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pretty_name}

%check
%if %{with tests}
python3 -m unittest
%endif

%files -n python3-%{pretty_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst AUTHORS.rst CHANGES.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.3.0-1
- Upgrade to 2.3.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 8 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-4
- Fix tests

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.11

* Sat Apr 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-2
- Added conditional for tests

* Sun Jan 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-1
- New version of software - 2.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-2
- Use pyproject rpm macros

* Thu Dec 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-1
- New version of software - 2.1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Tue May 4 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-2
- Install additional docs

* Sun Feb 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-1
- New version - 2.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-2
- Same dependencies removed

* Sat Nov 14 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package
