%global srcname  pytest-testinfra
%global pkgname  python-pytest-testinfra
%global slugname pytest_testinfra
%global forgeurl https://github.com/pytest-dev/pytest-testinfra

%global common_description %{expand:
With Testinfra you can write unit tests in Python to test actual state of your
servers configured by management tools like Salt, Ansible, Puppet, Chef and so
on.

Testinfra aims to be a Serverspec equivalent in python and is written as a
plugin to the powerful Pytest test engine.}

%bcond_without doc
%bcond_without tests

Name:           %{pkgname}
Version:        7.0.0
%forgemeta
Release:        %autorelease
Summary:        Unit testing for config-managed server state
URL:            %{forgeurl}
Source:         %{pypi_source}
License:        ASL 2.0
BuildArch:      noarch

########################################################################
# Package info                                                         #
########################################################################
%description %{common_description}
%package -n python3-%{srcname}
Summary: %summary

########################################################################
# Package requirements                                                 #
########################################################################
BuildRequires: python3-devel
# testing requirements
%if %{with tests}
BuildRequires: python3dist(salt)
BuildRequires: python3dist(pywinrm)
BuildRequires: python3dist(ansible)
BuildRequires: python3dist(paramiko)
%endif
# docs requirements
%if %{with doc}
BuildRequires: python3dist(sphinx)
%endif

%py_provides python3-%{srcname}
%description -n python3-%{srcname} %{common_description}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test} %{?with_doc:-x docs}

# Requires: (python3dist(ansible-core) or python3dist(ansible))
# Requires: python3dist(pywinrm)
# Requires: python3dist(paramiko)
# Suggests: python3dist(pytest-xdist)
########################################################################
# Prep                                                                 #
########################################################################
%prep
%autosetup -n %{srcname}-%{version}
########################################################################
# Build                                                                #
########################################################################
%build
%pyproject_wheel

# generate html docs
%if %{with doc}
sphinx-build-3 doc/source html
rm -vr html/.{doctrees,buildinfo}
%endif

########################################################################
# Install                                                              #
########################################################################
%install
%pyproject_install

########################################################################
# Tests                                                                #
########################################################################
%if %{with tests}
%check
%if v"0%{?python3_version}" >= v"3.12"
# salt is broken with Python 3.12: https://bugzilla.redhat.com/2222805
%global skips not test_backend_importables
%endif
%{pytest} test -v %{?skips:-k %{shescape:%{skips}}}
%endif

########################################################################
# Python package files                                                 #
########################################################################
%files -n python3-%{srcname}
%license LICENSE
%doc *.rst
%if %{with doc}
%doc html
%endif
%{python3_sitelib}/testinfra/
%{python3_sitelib}/%{slugname}-%{version}.dist-info

########################################################################
# Changelog                                                            #
########################################################################
%changelog
%autochangelog
