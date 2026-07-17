%global short_name lsp-black

%global _description %{expand:
lsp-black is a python-lsp-server plugin that adds support to black
autoformatter. This is forked from pyls-black to be compatible wth
community maintained language-server (python-lsp-server).
}

Name:           python-%{short_name}
Version:        2.0.0
Release:        %autorelease
Summary:        A python-lsp-server plugin that adds support to black autoformatter

%global forgeurl https://github.com/python-lsp/python-lsp-black
%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
# Fix tests failing since `black >= 24.3.0`
# https://github.com/python-lsp/python-lsp-black/issues/57
Patch:          %{forgeurl}/pull/59.patch
# And two more failing since `black >= 24.4.0`
# https://github.com/python-lsp/python-lsp-black/issues/57
Patch:          %{forgeurl}/pull/56.patch
# Migrate test_entry_point from pkg_resources to importlib.metadata
# https://github.com/python-lsp/python-lsp-black/pull/64
# Fixes compatibility with setuptools≥82.
Patch:          %{forgeurl}/pull/64.patch
# Fix compatibility with black≥26.5
# https://github.com/python-lsp/python-lsp-black/pull/65
Patch:          %{forgeurl}/pull/65.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

Supplements:    python3dist(python-lsp-server)

%description -n python3-%{short_name} %_description

%prep
%forgeautosetup -p1
# Remove version pinning from python-lsp-server dependency
sed -i -r -e 's/(lsp-server)>=.*/\1/' setup.cfg
# Remove Python version upper bound
sed -i -e 's/; python_version.*//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pylsp_black

%check
%pytest -v

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
