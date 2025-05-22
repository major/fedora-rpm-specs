Name:           python-sphinx-epytext
Version:        0.0.4
Release:        %autorelease
Summary:        Sphinx epytext extension

License:        MIT
URL:            https://github.com/jayvdb/sphinx-epytext
Source0:        %{pypi_source sphinx-epytext}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package provides basic support for epytext docstrings in Sphinx autodoc.}

%description %_description


%package -n     python3-sphinx-epytext
Summary:        %{summary}

%description -n python3-sphinx-epytext %_description


%prep
%autosetup -n sphinx-epytext-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sphinx_epytext

%check
%pyproject_check_import

%files -n python3-sphinx-epytext -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
