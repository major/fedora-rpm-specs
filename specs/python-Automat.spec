%global _without_doc 1
# Building python-pydoctor in EPEL requires too many dependencies
# and doc is not actually required on EPEL side.
%bcond doc %{undefined rhel}

%global srcname Automat
%global libname automat

%global common_description %{expand:
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).}

Name:           python-%{srcname}
Version:        24.8.1
Release:        %autorelease
Summary:        Self-service finite-state machines for the programmer on the go

License:        MIT
URL:            https://github.com/glyph/automat
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with doc}
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-pydoctor
%endif

# removes pieces of sphinx config trying to use git
# to get branch name or commit
Patch:          sphinx-no-git.patch

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       python3-%{libname}

%description -n python3-%{srcname} %{common_description}

%if %{with doc}
%package -n python-%{srcname}-doc
Summary:        Automat documentation

%description -n python-%{srcname}-doc
Documentation for Automat
%endif

%prep
%autosetup  -p1 -n %{libname}-%{version}

# Backport of https://github.com/glyph/automat/commit/2bf0abddd9b532ef9dd90707a10a09ce48c24f3d
sed -i "s/py\.test/pytest/g" tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%if %{with doc}
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/automat-visualize

%if %{with doc}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
