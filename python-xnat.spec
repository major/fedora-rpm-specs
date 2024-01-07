# Require network, so run locally in mock with --with=tests --enable-network
# All tests pass
%bcond_with tests

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
Version:        0.5.1
Release:        %autorelease
Summary:        XNAT client that exposes XNAT objects/functions as python objects/functions
# Only expand forge macros in fedora >= 40 since %%forgesource is broken
# in older releases.
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

BuildArch:      noarch

%description
%{desc}

%package -n python3-xnat
Summary:        %{summary}

BuildRequires: python3-devel
BuildRequires: help2man

%description -n python3-xnat
%{desc}

%prep
%autosetup -p1 -n xnatpy-%{version}

# Remove version locks etc.
sed -i -e 's/pytest==.*/pytest/' -e 's/pytest-cov==.*/pytest-cov/' -e '/tox/ d' test_requirements.txt
sed -i '/sphinx/d' requirements.txt

# remove shebang from non executable scripts
sed -i '1d' xnat/scripts/copy_project.py
sed -i '1d' xnat/scripts/data_integrity_check.py
sed -i '1d' xnat/scripts/import_experiment_dir.py

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -r requirements.txt test_requirements.txt}

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
%{pytest}
%endif

%files -n python3-xnat -f %{pyproject_files}
%doc README.rst
%{_bindir}/xnat
%{_bindir}/xnat_cp_project
%{_bindir}/xnat_data_integrity-check
%{_mandir}/man1/xnat*

%changelog
%autochangelog
