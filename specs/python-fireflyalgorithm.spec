%global pretty_name FireflyAlgorithm
%global new_name fireflyalgorithm

%global _description %{expand:
Implementation of Firefly Algorithm (FA) for optimization.}

Name:           python-%{new_name}
Version:        0.4.6
Release:        %autorelease
Summary:        Implementation of Firefly Algorithm in Python

# SPDX
License:        MIT
URL:            https://github.com/firefly-cpp/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

Provides: python-FireflyAlgorithm = %{version}-%{release}
Obsoletes: python-FireflyAlgorithm < 0.0.4-2

%description %_description

%package -n python3-%{new_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  tomcli
BuildRequires:  python3-pytest

Provides: python3-FireflyAlgorithm = %{version}-%{release}
Obsoletes: python3-FireflyAlgorithm < 0.0.4-2

%description -n python3-%{new_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}
rm -rf %{pretty_name}.egg-info
rm -fv poetry.lock

# Drop version pinning (we use the versions available in Fedora)
for DEP in $(tomcli get -F newline-keys pyproject.toml tool.poetry.dependencies)
do
  tomcli set pyproject.toml replace tool.poetry.dependencies.${DEP} ".*" "*"
done


%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{new_name}

%check
%pytest

%files -n python3-%{new_name} -f %{pyproject_files}
%{_bindir}/firefly-algorithm
%license LICENSE
%doc README.md examples/ Problems.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%doc CHANGELOG.md CITATION.cff

%changelog
%autochangelog
