%global pypi_name ast-monitor

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.5.5
Release:        %autorelease
Summary:        AST-Monitor is a wearable Raspberry Pi computer for cyclists

%global forgeurl https://github.com/firefly-cpp/AST-Monitor
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_noarch_with_unported_dependencies
# This package requires python3dist(pyqtwebengine).
ExclusiveArch: %{qt6_qtwebengine_arches} noarch

BuildRequires:  python3-devel
# For qt6_qtwebengine_arches macro:
BuildRequires:  qt6-srpm-macros
BuildRequires:  tomcli
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-qt}
%endif

%global _description %{expand:
AST-monitor is a low-cost and efficient embedded device for monitoring the
realization of sport training sessions that is dedicated to monitor cycling
training sessions. AST-Monitor is a part of Artificial Sport Trainer (AST)
system.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Obsoletes:      python-ast-monitor-doc < 0.5.2-2

%description -n python3-%{pypi_name} %_description

%prep
%forgeautosetup -p1
rm -fv poetry.lock

# Drop version pinning (we use the versions available in Fedora)
for DEP in $(tomcli get -F newline-keys pyproject.toml tool.poetry.dependencies)
do
    tomcli set pyproject.toml replace tool.poetry.dependencies.${DEP} ".*" "*"
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ast_monitor

%check
%if %{with tests}
# test_gui.py segfaults with PyQt 3.9.0 (F42+)
%pytest -r fEs --ignore tests/test_gui.py
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CITATION.cff HARDWARE_CONFIGURATION.md

%changelog
%autochangelog
