%global pypi_name etelemetry

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        %{autorelease}
Summary:        Etelemetry python client API

%global forgeurl https://github.com/sensein/etelemetry-client
%global tag v%{version}
%forgemeta

# _version.py is Unlicense.
License:        Apache-2.0 AND Unlicense
URL:            %forgeurl
Source:         %forgesource
# Don't install tests
Patch:          %{forgeurl}/pull/56.patch

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(versioneer)

%global _description %{expand:
A lightweight python client to communicate with the etelemetry server.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1 -S git

# Shipped Versioneer is outdated or broken, always resulting in
# 0+UNKNOWN version. Use system versioneer to regenerate config.
rm versioneer.py
versioneer install --vendor
git add --force .
git commit --allow-empty -a --author 'rpm-build <rpm-build>' \
    -m 'Update Versioneer'

# NOTE: Make sure this is the last step in %%prep
# Neded for Versioneer for determining correct version
# Upstream uses tags of the form vX.Y.Z, but the Versioneer config
# does not set `tag_prefix` in `setup.cfg`. So we drop the prefix here
# to allow Versioneer to determine the version correctly.
git tag %{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pytest -v
# Tests are not very thorough and require network.
# Run import test in addition.
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
