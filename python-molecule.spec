%global srcname  molecule
%global pkgname  python-molecule
%global forgeurl https://github.com/ansible/%{srcname}

%global common_description %{expand:
Molecule is designed to aid in the development and testing of Ansible roles.
Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios. Molecule is opinionated in order to encourage an approach
that results in consistently developed roles that are well-written, easily
understood and maintained. Molecule uses Ansible playbooks to exercise the role
and its associated tests. Molecule supports any provider that Ansible supports.
}

%bcond_with doc
%bcond_with tests

Name:           %{pkgname}
Version:        4.0.1
%forgemeta
Release:        %autorelease
Summary:        Molecule is designed to aid in the development and testing of Ansible roles
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          0001_remove_sphinx_version_pinning.patch
BuildArch:      noarch

# Most of the package is MIT licensed.
#
# There are two files in the archive that are licensed with ASL 2.0:
# - molecule-2.7/molecule/interpolation.py
# - molecule-2.7/test/unit/test_interpolation.py
License: MIT and ASL 2.0

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description %{common_description}

%package -n python3-%{srcname}-doc
Summary: %summary
%description -n python3-%{srcname}-doc
Documentation for python-molecule a tool designed to aid in the development and testing
of Ansible roles

%package -n python3-%{srcname}
Summary: %summary

Recommends: python-molecule-doc
Recommends: python3dist(docker)
Recommends: python3dist(docker)
Recommends: python3dist(molecule-docker)
Recommends: python3dist(molecule-podman)

%description -n python3-%{srcname} %{common_description}

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test} %{?with_doc:-x docs}

%build
%pyproject_wheel

%if %{with doc}
# generate html docs
PYTHONPATH=src sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with tests}
%check
PYTHONPATH=src %{python3} -m pytest -vv src/molecule/test
%endif

%files -n python3-%{srcname}
%{python3_sitelib}/*
%{python3_sitelib}/%{srcname}-%{version}.dist-info
%{python3_sitelib}/%{srcname}/
%license LICENSE
%{_bindir}/%{srcname}

%if %{with doc}
%files -n python3-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc html/
%endif

%changelog
%autochangelog
