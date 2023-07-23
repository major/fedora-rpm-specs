%global pypi_name tomlkit

%global common_description %{expand:
TOML Kit is a 1.0.0-compliant TOML library.

It includes a parser that preserves all comments, indentations, whitespace and
internal element ordering, and makes them accessible and editable via an
intuitive API.

You can also create new TOML documents from scratch using the provided helpers.

Part of the implementation has been adapted, improved and fixed from Molten.}

Name:           python-%{pypi_name}
Summary:        Style preserving TOML library
Version:        0.11.4
Release:        4%{?dist}
License:        MIT

URL:            https://github.com/sdispater/tomlkit
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel

# test dependencies
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


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
%license LICENSE
%doc README.md


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.11.4-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 13 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.11.4-1
- Update to 0.11.4 (close RHBZ#2078161)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.10.1-2
- Rebuilt for Python 3.11

* Sun Mar 27 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.10.1-1
- Update to 0.10.1 (close RHBZ#2034117)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Karolina Surma <ksurma@redhat.com> - 0.7.2-1
- Update to version 0.7.2 (#1962396)
- Build package using pyproject-rpm-macros

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.0-1
- Update to version 0.7.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.11-2
- Rebuilt for Python 3.9

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.11-1
- rebuilt

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.10-1
- Update to version 0.5.10.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.8-1
- Update to version 0.5.8.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.7-1
- Update to version 0.5.7.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-1
- Update to version 0.5.5.

* Sun Jun 30 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.4-1
- Update to version 0.5.4.

* Sat May 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-4
- Use setup from setuptools, not distutils.core.

* Mon Feb 11 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.5.3-3
- Added check section.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Initial package.

