Name:           python-pure-eval
Version:        0.2.3
Release:        %autorelease
Summary:        Safely evaluate AST nodes without side effects

License:        MIT
URL:            http://github.com/alexmojaki/pure_eval
Source0:        %{pypi_source pure_eval}
# Compatibility with Python 3.15
Patch:          https://github.com/alexmojaki/pure_eval/commit/d70a873553d31.patch
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python package that lets you safely evaluate certain AST nodes
without triggering arbitrary code that may have unwanted side effects.}


%description %_description

%package -n     python3-pure-eval
Summary:        %{summary}

%description -n python3-pure-eval %_description


%prep
%autosetup -p1 -n pure_eval-%{version}


%generate_buildrequires
%pyproject_buildrequires -r -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pure_eval


%check
%tox


%files -n python3-pure-eval -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
