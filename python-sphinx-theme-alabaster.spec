Name:           python-sphinx-theme-alabaster
Version:        0.7.16
Release:        %autorelease
Summary:        Configurable sidebar-enabled Sphinx theme

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/alabaster
Source:         %{pypi_source alabaster}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

# Upstream lists no runtime dependencies,
# but alabaster/support.py imports from pygments.
# This is fine, as the module is only used for pygments.
# This BuildRequires is necessary for a successful import check.
BuildRequires:  python%{python3_pkgversion}-pygments

%global _description %{expand:
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system.

It began as a third-party theme, and is still maintained separately,
but as of Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is
selected as the default theme.}

%description %_description


%package -n     python%{python3_pkgversion}-sphinx-theme-alabaster
Summary:        %{summary}
%py_provides    python%{python3_pkgversion}-alabaster

%description -n python%{python3_pkgversion}-sphinx-theme-alabaster %_description


%prep
%autosetup -p1 -n alabaster-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files alabaster


%check
# upstream has no tests
%pyproject_check_import


%files -n python%{python3_pkgversion}-sphinx-theme-alabaster -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
