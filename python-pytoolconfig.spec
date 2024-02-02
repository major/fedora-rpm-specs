Name:           python-pytoolconfig
Version:        1.3.1
Release:        %autorelease
Summary:        Python tool configuration

License:        LGPL-3.0-or-later
URL:            https://github.com/bagel897/pytoolconfig
# The documentation sources are only included in the GitHub archive, not in the
# PyPI sdist. However, the GitHub archive would require arcane incantations to
# get the correct release version in the wheel metadata; we judge that this is
# not worth it, and just do without the Sphinx documentation.
Source:         %{pypi_source pytoolconfig}

BuildArch:      noarch

BuildRequires:  python3-devel

# Selected dependencies from [tool.pdm-dev-dependencies] in pyproject.toml for
# testing:
BuildRequires:  %{py3_dist pytest} >= 7.2

%global common_description %{expand:
The goal of this project is to manage configuration for Python tools, such as
black and rope, and add support for a pyproject.toml configuration file.}

%description %{common_description}


%package -n     python3-pytoolconfig
Summary:        %{summary}

%description -n python3-pytoolconfig %{common_description}


# The doc extra is potentially useful for dependent packages; for example,
# rope[doc] depends on pytoolconfig[doc]. However, the gendoc extra appears to
# be solely for building the documentation of this package, so we do not build
# a corresponding metapackage, nor do we generate BR’s from it.
%pyproject_extras_subpkg -n python3-pytoolconfig validation global doc


%prep
%autosetup -n pytoolconfig-%{version}


%generate_buildrequires
%pyproject_buildrequires -x validation,global,doc


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytoolconfig


%check
%pytest -v


%files -n python3-pytoolconfig -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
