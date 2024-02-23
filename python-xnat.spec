# Tests requiring network are skipped (mostly dependent on docker)
# So, let's run all tests by default.
%bcond tests 1

# Use forge macros for pulling from GitLab
%global forgeurl https://gitlab.com/radiology/infrastructure/xnatpy

%global desc %{expand: \
XNAT client that exposes XNAT objects/functions as python
objects/functions. The aim is to abstract as much of the REST API away
as possible and make xnatpy feel like native Python code. This reduces
the need for the user to know the details of the REST API. Low level
functionality can still be accessed via the connection object which has
get, head, put, post, delete methods for more directly calling the REST
API.}

Name:           python-xnat
Version:        0.5.3
Release:        %autorelease
Summary:        XNAT client that exposes XNAT objects/functions as python objects/functions
# Only expand forge macros in fedora >= 40 since %%forgesource is broken
# in older releases.
# Use `fedpkg ... mockbuild --srpm-mock ...` when building for >=40 on
# system <40
%if %{fedora} >= 40
%forgemeta
%endif
License:        Apache-2.0
URL:            %forgeurl
# The %%forgesource macro only works correctly in rawhide for group URLs
%if %{fedora} >= 40
Source0:        %forgesource
%else
Source0:        https://gitlab.com/radiology/infrastructure/xnatpy/-/archive/%{version}/xnatpy-%{version}.tar.bz2
%endif
# xnat4tests is not available in Fedora. It's currently not possible to
# package it either, since it's licensed under CC0-1.0
# https://github.com/Australian-Imaging-Service/xnat4tests/issues/17
Patch:          no_xnat4tests.patch
# Fix %%Pyproject_check_import failing
# https://gitlab.com/radiology/infrastructure/xnatpy/-/issues/57
Patch:          https://gitlab.com/radiology/infrastructure/xnatpy/-/commit/bafa2c7ad0d12cf841446705b1d597059ce2a6b0.patch

BuildArch:      noarch

%description
%{desc}

%package -n python3-xnat
Summary:        %{summary}

BuildRequires: python3-devel
BuildRequires: help2man
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-requests-mock
%endif

%description -n python3-xnat
%{desc}

%prep
%autosetup -p1 -n xnatpy-%{version}

# remove shebang from non executable scripts
sed -i '1d' xnat/scripts/copy_project.py
sed -i '1d' xnat/scripts/data_integrity_check.py
sed -i '1d' xnat/scripts/import_experiment_dir.py

# Don't try to import docker (we are not using it)
sed -i '/import docker/d' xnat/tests/test_import.py

%generate_buildrequires
%pyproject_buildrequires -r requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l xnat

# generate man pages
# skip xnat_cp_project and xnat_data_integrity, seems generally broken: https://gitlab.com/radiology/infrastructure/xnatpy/-/issues/46
for binary in "xnat" "xnat download" "xnat import" "xnat list" "xnat login" "xnat logout" "xnat prearchive" "xnat rest" "xnat script"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done

%check
%if %{with tests}
# Docker tests are skipped automatically if docker is not available.
# To make it explicit of what is being skipped, I added it anyway.
# Funtional tests require xnat4tests.
%pytest -v -m 'not docker_test and not functional_test'
%else
# Import test currently fails
# https://gitlab.com/radiology/infrastructure/xnatpy/-/issues/57
%pyproject_check_import
%endif

%files -n python3-xnat -f %{pyproject_files}
%doc README.rst
%{_bindir}/xnat
%{_bindir}/xnat_cp_project
%{_bindir}/xnat_data_integrity-check
%{_mandir}/man1/xnat*

%changelog
%autochangelog
