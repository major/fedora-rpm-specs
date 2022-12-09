Name:           python-venusian
Version:        3.0.0
Release:        %autorelease
Summary:        A library for deferring decorator actions

# The entire source is BSD-3-Clause-Modification, except:
#   ZPL-2.1: tests/test_advice.py src/venusian/advice.py
# License Review: BSD-3-Clause-Modification
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/108
License:        BSD-3-Clause-Modification AND ZPL-2.1
URL:            https://github.com/Pylons/venusian
Source0:        %{pypi_source venusian}

BuildArch:      noarch

BuildRequires:  python3-devel

# There is a “testing” extra, but it’s not worth generating BR’s from it
# because everything other than pytest is for coverage analysis and would need
# to be patched out.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator is
executed at import time, you can defer the action usually taken by the
decorator until a separate “scan” phase.}

%description %{common_description}


%package -n python3-venusian
Summary:        %{summary}

%description -n python3-venusian %{common_description}


%prep
%autosetup -n venusian-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/ --cov[^[:blank:]]*//g' setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files venusian


%check
%pytest


%files -n python3-venusian -f %{pyproject_files}
# pyproject_files handles LICENSE.txt in dist-info, but COPYRIGHT.txt is not
# present there, so we manually install both files to %%{_licensedir}
%license COPYRIGHT.txt
%license LICENSE.txt
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst


%changelog
%autochangelog
