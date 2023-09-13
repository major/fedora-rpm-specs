%bcond_without check

%global srcname astroplan

Name:           python-%{srcname}
Version:        0.9
Release:        1%{?dist}
Summary:        Python package to help astronomers plan observations

License:        BSD-3-Clause
URL:            https://pypi.org/project/astroplan/
Source0:        %{pypi_source}
# https://github.com/astropy/astroplan/issues/416
Patch:          astroplan-fixed-apo.patch

BuildArch:      noarch


%global _description %{expand:
astroplan is an observation planning package for 
astronomers that can help you plan for everything but the clouds.

It is an in-development Astropy affiliated package that seeks to make your 
life as an observational astronomer a little less infuriating.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files astroplan

%check
# Most test rely on an internet database of coordinates
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst

%changelog
* Mon Sep 11 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9-1
- New release 0.9
- Migrated to SPDX
- New python macros

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 0.8-2
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8-1
- New release 0.8
- Patch test that requires network access

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.6-1
- New release 0.6

* Sat Dec 07 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5-2
- Fix project url
- Add check section

* Mon Nov 11 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5-1
- Initial spec file

