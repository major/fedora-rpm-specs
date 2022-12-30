%global srcname Automat
%global libname automat

%global common_description %{expand:
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).}

Name:           python-%{srcname}
Version:        22.10.0
Release:        %autorelease
Summary:        Self-service finite-state machines for the programmer on the go

License:        MIT
URL:            https://github.com/glyph/automat
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       python3-%{libname}

%description -n python3-%{srcname} %{common_description}

%package -n python-%{srcname}-doc
Summary:        Automat documentation

%description -n python-%{srcname}-doc
Documentation for Automat

%prep
%autosetup  -p1 -n %{srcname}-%{version}

# Backport of https://github.com/glyph/automat/commit/2bf0abddd9b532ef9dd90707a10a09ce48c24f3d
sed -i "s/py\.test/pytest/g" tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

PYTHONPATH=%{pyproject_build_lib}  sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/automat-visualize

%files -n python-%{srcname}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
