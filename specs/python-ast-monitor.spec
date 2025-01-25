%global pypi_name ast-monitor

Name:           python-%{pypi_name}
Version:        0.5.3
Release:        %autorelease
Summary:        AST-Monitor is a wearable Raspberry Pi computer for cyclists

%global forgeurl https://github.com/firefly-cpp/AST-Monitor
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource
# Patch for compatability with sport-activities-features 0.5.0
# https://github.com/firefly-cpp/AST-Monitor/issues/107 (rebased)
Patch:          0001-Update-for-sport-activities-features-0.5.0.patch

BuildArch:      noarch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_noarch_with_unported_dependencies
# This package requires python3dist(pyqtwebengine).
ExclusiveArch: %{qt6_qtwebengine_arches} noarch

BuildRequires:  python3-devel
# For qt6_qtwebengine_arches macro:
BuildRequires:  qt6-srpm-macros
BuildRequires:  %{py3_dist toml-adapt}
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
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

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ast_monitor

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CITATION.cff HARDWARE_CONFIGURATION.md

%changelog
%autochangelog
