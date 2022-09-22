%global short_name lsp-black

%global _description %{expand:
lsp-black is a python-lsp-server plugin that adds support to black
autoformatter. This is forked from pyls-black to be compatible wth
community maintained language-server (python-lsp-server).
}

Name:           python-%{short_name}
Version:        1.2.0
Release:        %autorelease
Summary:        A python-lsp-server plugin that adds support to black autoformatter

License:        MIT
URL:            https://github.com/python-lsp/%{name}
Source0:        %{pypi_source}
Source1:        LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

Supplements:    python3dist(python-lsp-server)

%description -n python3-%{short_name} %_description

%prep
%autosetup -n %{name}-%{version}
cp %{SOURCE1} LICENSE

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pylsp_black

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
