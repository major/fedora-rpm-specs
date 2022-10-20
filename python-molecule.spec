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
Version:        4.0.2
%forgemeta
Release:        %autorelease
Summary:        Molecule is designed to aid in the development and testing of Ansible roles
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          0001_remove_sphinx_version_pinning.patch
Patch:          0002_skiping_tests_requiring_connectivity.patch
BuildArch:      noarch

########################################################################
# Most of the package is MIT licensed.                                 #
#                                                                      #
# There are two files in the archive that are licensed with ASL 2.0:   #
# - molecule-2.7/molecule/interpolation.py                             #
# - molecule-2.7/test/unit/test_interpolation.py                       #
########################################################################
License: MIT and ASL 2.0

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

Requires:   ansible-core
Recommends: python-molecule-doc
Recommends: python3dist(docker)
Recommends: python3dist(docker)
Recommends: python3dist(molecule-docker)
Recommends: python3dist(molecule-podman)

%description -n python3-%{srcname} %{common_description}

%prep
%forgeautosetup -p1


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
%pyproject_save_files %{srcname}

%if %{with tests}
%check
cat <<EOF > %{buildroot}/molecule
#! /usr/bin/python3 -s
# -*- coding: utf-8 -*-
import re
import sys
from molecule.__main__ import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
EOF

chmod +x %{buildroot}/molecule

sed -i 's@\["molecule"@\["%{buildroot}/molecule"@g' src/molecule/test/functional/conftest.py
sed -i 's@"molecule"@"%{buildroot}/molecule"@g'     src/molecule/test/functional/test_command.py
sed -i 's@"molecule"@"%{buildroot}/molecule"@g'     src/molecule/test/unit/command/test_base.py

PYTHONPATH=$(pwd)/src %{python3} -m pytest -vv src/molecule/test
rm -f  %{buildroot}/molecule
%endif

########################################################################
# Python package files                                                 #
########################################################################
%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%{_bindir}/%{srcname}

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
