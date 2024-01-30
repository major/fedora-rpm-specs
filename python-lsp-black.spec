%global short_name lsp-black
%global forgeurl https://github.com/python-lsp/python-lsp-black

%global _description %{expand:
lsp-black is a python-lsp-server plugin that adds support to black
autoformatter. This is forked from pyls-black to be compatible wth
community maintained language-server (python-lsp-server).
}

Name:           python-%{short_name}
Version:        2.0.0
Release:        %autorelease
Summary:        A python-lsp-server plugin that adds support to black autoformatter
%forgemeta
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

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
%autosetup -n %{name}-%{version}
# Remove version pinning from python-lsp-server dependency
sed -i -r -e 's/(lsp-server)>=.*/\1/' setup.cfg
# Remove Python version upper bound
sed -i -e 's/; python_version.*//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x extras_require

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
