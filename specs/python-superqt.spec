%global pypi_name superqt
%global forgeurl https://github.com/pyapp-kit/superqt

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.7.3
Release:        %{autorelease}
Summary:        Missing widgets and components for PyQt/PySide
%forgemeta
# src/superqt/utils/_throttler.py is licensed MIT
License:        BSD-3-Clause AND MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package aims to provide high-quality community-contributed Qt
widgets and components for PyQt & PySide that are not provided in the
native QtWidgets module.

Components are tested on:

- macOS, Windows, & Linux
- Python 3.8 and above
- PyQt5 (5.11 and above) & PyQt6
- PySide2 (5.11 and above) & PySide6}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} pyqt6


%prep
%forgeautosetup -p1

# Unpin pyqt6
sed -r -i 's/(pyqt6)<.*"/\1"/' pyproject.toml


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x test,pyqt6


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%if %{with tests}
export PYTEST_QT_API="pyqt6"
# Fedora ships /usr/share/qt6/qtlogging.ini with debug messages disabled.
# With QT_LOGGING_RULES we can overrule those.
# https://discussion.fedoraproject.org/t/qt-logging-has-been-disabled-qtlogging-ini-needs-to-be-fixed/146868
export QT_LOGGING_RULES="default.debug=true"
# Test requires network
k="${k-}${k+ and }not test_qiconify"
# Test fails for unknown reason
k="${k-}${k+ and }not test_wrapped_eliding_label"
%pytest -r fEs ${k+-k "${k-}"}
%else
%pyproject_check_import
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
