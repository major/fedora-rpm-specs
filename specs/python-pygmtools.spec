%global         pypi_name       pygmtools
%global         forgeurl        https://github.com/Thinklab-SJTU/pygmtools
Version:        0.5.3
%global         tag             %{version}
%forgemeta

Name:           python-%{pypi_name}
Release:        4%{?dist}
Summary:        A library of Python graph matching solvers

License:        MulanPSL-2.0
URL:            https://pygmtools.readthedocs.io/en/latest/
Source:         %{forgesource}
# bdist_wheel has moved into setuptools
# https://github.com/Thinklab-SJTU/pygmtools/pull/105
Patch:          bdist_wheel.patch

BuildRequires:  python3-devel
# Documentation
#BuildRequires:  python3-sphinx
#BuildRequires:  python3-sphinx-design
#BuildRequires:  python3-sphinx-gallery
# Need to package m2r2
#BuildRequires:  python3-m2r2
BuildArch: noarch

%global _description %{expand:
pygmtools (Python Graph Matching Tools) provides graph matching
solvers in Python.

Graph matching is a fundamental yet challenging problem in pattern
recognition, data mining, and others. Graph matching aims to find
node-to-node correspondence among multiple graphs, by solving an
NP-hard combinatorial optimization problem.

Doing graph matching in Python used to be difficult, and this library
wants to make researchers' lives easier.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation files for %{pypi_name}

%prep
%forgeautosetup -p 1
# Remove for now, but maybe needed when Pytorch is available
rm -f %{pypi_name}/astar/priority_queue.hpp

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build documentation
#sphinx-build -b man -D plot_gallery=0 -b man docs man1

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Only check import of main module, as other modules
# have dependencies that may not be available
%pyproject_check_import -t pygmtools

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc docs/guide/*.rst
%doc examples

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 19 2024 Benson Muite <benson_muite@emailplus.org> - 0.5.3-3
- Ensure also builds with older versions of wheel than 0.44

* Sat Oct 19 2024 Benson Muite <benson_muite@emailplus.org> - 0.5.3-2
- Ensure builds with wheel 0.44

* Sat Oct 19 2024 Benson Muite <benson_muite@emailplus.org> - 0.5.3-1
- Update to latest release

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Benson Muite <benson_muite@emailplus.org> - 0.4.0-1
- Initial packaging
