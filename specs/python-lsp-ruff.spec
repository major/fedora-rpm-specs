Name:           python-lsp-ruff
Version:        2.3.0
Release:        %{autorelease}
Summary:        Ruff linting plugin for Python LSP Server

%global forgeurl https://github.com/python-lsp/python-lsp-ruff
%global tag v%{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A plugin for python-lsp-server that adds linting, code action and
formatting capabilities that are provided by ruff, an extremely fast
Python linter and formatter written in Rust.}

%description %_description


%package -n python3-lsp-ruff
Summary:        %{summary}

%description -n python3-lsp-ruff %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pylsp_ruff


%check
%pytest -r fEs


%files -n python3-lsp-ruff -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
