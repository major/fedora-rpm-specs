%global srcname ufoLib2

Name:           python-%{srcname}
Version:        0.16.0
Release:        2%{?dist}
Summary:        A library to deal with UFO font sources

License:        Apache-2.0
URL:            https://pypi.org/project/ufoLib2
Source0:        %{pypi_source %{srcname} %{version}}
BuildArch:      noarch

BuildRequires:  python3-devel

# Required for running tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(cattrs)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(orjson)

%global _description %{expand:
ufoLib2 is meant to be a thin representation of the Unified Font Object (UFO)
version 3 data model, intended for programmatic manipulation and fast batch
processing of UFOs.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Thu Aug 03 2023 Parag Nemade <pnemade AT redhat DOT com> - 0.16.0-2
- rewrite spec for pyproject macros

* Thu Aug 03 2023 Parag Nemade <pnemade AT redhat DOT com> - 0.16.0-1
- Update to 0.16.0 version (#2225476)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 0.7.1-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Parag Nemade <pnemade AT redhat DOT com> - 0.7.1-11
- Update license tag to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.9

* Tue May 19 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.7.1-2
- Drop the Requires: as they will be picked automatically
- Rename spec to python-ufoLib2.spec

* Thu May 07 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.7.1-1
- Initial packaging

