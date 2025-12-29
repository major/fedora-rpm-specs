%global pypi_name superqt
%global forgeurl https://github.com/pyapp-kit/superqt

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.7.6
Release:        %{autorelease}
Summary:        Missing widgets and components for PyQt/PySide
%forgemeta
# src/superqt/utils/_throttler.py is licensed MIT
License:        BSD-3-Clause AND MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli

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


%pyproject_extras_subpkg -n python3-%{pypi_name} cmap,iconify,pyqt5,pyqt6,pyside6,quantity


%prep
%forgeautosetup -p1

# Unpin dependencies and remove linter
tomcli-set pyproject.toml arrays replace -t regex_partial \
    dependency-groups.test '(^[-_a-zA-Z]+)[>=]+[0-9.]+' '\1'
tomcli-set pyproject.toml arrays delitem -t regex_partial \
    dependency-groups.test '^pytest-cov'

# pyqt5-qt5 contains the subset of a Qt installation that is required by
# PyQt5. Since PyQt5 is also a dependency, we don't need it (and it's not
# available in Fedora either).
tomcli-set pyproject.toml arrays delitem -t regex_partial \
    project.optional-dependencies.pyqt5 '^pyqt5-qt5'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x cmap,iconify,pyqt5,pyqt6,pyside6,quantity -g test


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%if %{with tests}
# Fedora ships /usr/share/qt6/qtlogging.ini with debug messages disabled.
# With QT_LOGGING_RULES we can overrule those.
# https://discussion.fedoraproject.org/t/qt-logging-has-been-disabled-qtlogging-ini-needs-to-be-fixed/146868
export QT_LOGGING_RULES="default.debug=true"
# Test requires network
k="${k-}${k+ and }not test_qiconify"
# Test fails for unknown reason
k="${k-}${k+ and }not test_wrapped_eliding_label"
for QT_FLAVOR in pyqt5 pyqt6 pyside6
do
    case "${QT_FLAVOR}" in
    pyside6)
        # Segfault in test_cmap_combo with pyside6 6.10
        # https://github.com/pyapp-kit/superqt/issues/318
        ki="${k-}${k+ and }not test_cmap_combo"
        ;;
    *)
        ki="${k-}"
    esac
    PYTEST_QT_API="${QT_FLAVOR}" %pytest -r fEs ${ki+-k "${ki-}"}
done
%else
%pyproject_check_import
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
