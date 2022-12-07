%global _description %{expand:
A PEP 518 build backend that uses setuptools_scm to generate a version file
from your version control system, then flit_core to build the package.}

Name:           python-flit-scm
Version:        1.7.0
Release:        %{autorelease}
Summary:        PEP 518 build backend that uses setuptools_scm and flit

License:        MIT
URL:            https://pypi.org/pypi/flit_scm
Source0:        %{pypi_source flit_scm}

BuildArch:      noarch

%description %_description

%package -n python3-flit-scm
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-flit-scm %_description

%prep
%autosetup -n flit_scm-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# see pyproject-rpm-macros documentation for more forms
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flit_scm

%check
%pyproject_check_import

%files -n python3-flit-scm -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
