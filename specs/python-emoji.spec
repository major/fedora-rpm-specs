%global pypi_name emoji

%global _description %{expand:
Full featured simple emoji library for Python. This project was
inspired by kyokomi.

The entire set of Emoji codes as defined by the unicode consortium is
supported in addition to a bunch of aliases. By default, only the
official list is enabled but doing emoji.emojize(use_aliases=True)
enables both the full list and aliases.}

Name: python-%{pypi_name}
Version: 2.14.0
Release: 1%{?dist}

License: BSD-3-Clause
Summary: Emoji library for Python
URL: https://pypi.python.org/pypi/%{pypi_name}
Source0: %{pypi_source %{pypi_name}}
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-pytest

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGES.md

%changelog
* Sat Jan 11 2025 Matthieu Saulnier <fantom@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0

* Mon Jul 29 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.8.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Sat Jul 29 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Updated to version 2.2.0.

* Tue Sep 20 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-1
- Updated to version 2.0.0.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.11

* Sat Mar 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.0-1
- Updated to version 1.7.0.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.3-1
- Updated to version 1.6.3.

* Sun Dec 12 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-2
- Converted SPEC to 202x-era guidelines.

* Wed Oct 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-1
- Updated to version 1.6.1.

* Thu Oct 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.0-1
- Updated to version 1.6.0.

* Fri Sep 17 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1
- Updated to version 1.5.0.

* Sun Aug 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.2-1
- Updated to version 1.4.2.

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.1-1
- Updated to version 1.4.1.

* Sat Jul 17 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.0-1
- Updated to version 1.4.0.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.10

* Sun Jan 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.0-1
- Updated to version 1.2.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0-1
- Updated to version 1.1.0.

* Sat Jan 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.1-1
- Updated to version 1.0.1.

* Sat Jan 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Updated to version 1.0.0.

* Sun Aug 02 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.4-4
- Added python3-setuptools to build requirements.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.4-1
- Updated to version 0.5.4.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.3-1
- Updated to version 0.5.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Initial SPEC release.
