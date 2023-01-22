%global pypi_name jupyter_packaging

Name:           python-jupyter-packaging
Version:        0.12.3
Release:        2%{?dist}
Summary:        Tools to help build and install Jupyter Python packages

License:        BSD
URL:            https://github.com/jupyter/jupyter-packaging
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
This package contains utilities for making Python packages with and without
accompanying JavaScript packages.}

%description %_description

%package -n python3-jupyter-packaging
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-jupyter-packaging %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Drop dependencies on coverage, linters etc.
sed -Ei 's/"(coverage|pre-commit|pytest-cov)",//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -w -x test

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Some tests are trying to install packages to /usr
# - https://github.com/jupyter/jupyter-packaging/issues/63
%pytest -k "\
not test_build_package and \
not test_create_cmdclass and \
not test_deprecated_metadata and \
not test_develop and \
not test_install and \
not test_install_hybrid and \
not test_run \
"

%files -n python3-jupyter-packaging -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 Lumír Balhar <lbalhar@redhat.com> - 0.12.3-1
- Update to 0.12.3
Resolves: rhbz#2121488

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Lumír Balhar <lbalhar@redhat.com> - 0.12.2-1
- Update to 0.12.2
Resolves: rhbz#2099315

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.12.1-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Lumír Balhar <lbalhar@redhat.com> - 0.12.1-1
- Update to 0.12.1
Resolves: rhbz#2092028

* Mon Mar 28 2022 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Drop build-time dependencies on coverage, linters etc.

* Fri Mar 25 2022 Lumír Balhar <lbalhar@redhat.com> - 0.12.0-1
- Update to 0.12.0
Resolves: rhbz#2068334

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Lumír Balhar <lbalhar@redhat.com> - 0.11.1-1
- Update to 0.11.1
Resolves: rhbz#2023459

* Tue Oct 19 2021 Lumír Balhar <lbalhar@redhat.com> - 0.11.0-1
- Update to 0.11.0
Resolves: rhbz#2015227

* Wed Oct 06 2021 Lumír Balhar <lbalhar@redhat.com> - 0.10.6-1
- Update to 0.10.6
Resoves: rhbz#2008278

* Mon Sep 20 2021 Lumír Balhar <lbalhar@redhat.com> - 0.10.5-1
- Update to 0.10.5
Resolves: rhbz#2004479

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Lumír Balhar <lbalhar@redhat.com> - 0.10.4-1
- Update to 0.10.4
Resolves: rhbz#1979685

* Thu Jun 24 2021 Lumír Balhar <lbalhar@redhat.com> - 0.10.3-1
- A few minor modifications
- Update to 0.10.3

* Thu Jan 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.7.11-2
- Use pyproject-rpm-macros and pytest macro.

* Fri Jan 08 2021 Filipe Brandenburger <filbranden@gmail.com> - 0.7.11-1
- Initial packaging.
