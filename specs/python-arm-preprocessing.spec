%global pypi_name arm-preprocessing
%global forgeurl https://github.com/firefly-cpp/arm-preprocessing

Name:           python-%{pypi_name}
Version:        0.2.5
Release:        %{autorelease}
Summary:        Data preprocessing for Association Rule Mining (ARM)
%global tag %{version}
%forgemeta
# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependency
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sport-activities-features}

%global _description %{expand:
arm-preprocessing is a lightweight Python library supporting several
key steps involving data preparation, manipulation, and discretisation
for Association Rule Mining (ARM). 🧠 Embrace its minimalistic design
that prioritises simplicity. 💡 The framework is intended to be fully
extensible and offers seamless integration with related ARM libraries
(e.g., NiaARM). 🔗}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files arm_preprocessing


%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE


%changelog
%autochangelog
