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

%global documentation_description %{expand:
Documentation for python-molecule a tool designed to aid in the development and
testing of Ansible roles.
}

%bcond_without doc
%bcond_without tests

Name:           %{pkgname}
Version:        4.0.4
Release:        %autorelease
Summary:        Molecule is designed to aid in the development and testing of Ansible roles
URL:            %{forgeurl}
Source:         %{pypi_source molecule}
# Remove unnecessary test deps and sphinx pinning
Patch:          0001-Remove-Sphinx-pinning-and-unneeded-test-deps.patch
BuildArch:      noarch

########################################################################
# Most of the package is MIT licensed.                                 #
#                                                                      #
# There are two files in the archive that are licensed with ASL 2.0:   #
# - molecule-2.7/molecule/interpolation.py                             #
# - molecule-2.7/test/unit/test_interpolation.py                       #
########################################################################
License: MIT AND Apache-2.0

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%if %{with tests}
BuildRequires: yamllint
BuildRequires: python3dist(ansible-lint)
%endif

%description %{common_description}
########################################################################
# Documentation package                                                #
########################################################################
%package -n python3-%{srcname}-doc
Summary: %summary
%description -n python3-%{srcname}-doc %{documentation_description}

########################################################################
# Python package                                                       #
########################################################################
%package -n python3-%{srcname}
Summary: %summary
Provides: molecule = %{version}-%{release}

Requires:   ansible-core
Recommends: python-molecule-doc
Recommends: python3dist(molecule-docker)
Recommends: python3dist(molecule-podman)

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test} %{?with_doc:-x docs}

%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH=src sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if %{with tests}
%check
%pytest \
    -vv \
    -n auto \
    -k 'not test_command_dependency' \
    src/molecule/test
%endif

########################################################################
# Python package files                                                 #
########################################################################
%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/molecule/
%{python3_sitelib}/molecule-%{version}.dist-info/

########################################################################
# Documentation package files                                          #
########################################################################
%if %{with doc}
%files -n python3-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc html/
%endif

%changelog
%autochangelog
