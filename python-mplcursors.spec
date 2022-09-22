%global srcname mplcursors
%bcond_without doc

Name:           python-%{srcname}
Version:        0.5.1
Release:        %autorelease
Summary:        Interactive data selection cursors for Matplotlib

License:        MIT
URL:            https://github.com/anntzer/mplcursors
Source0:        %pypi_source
# Fix deprecation warnings with Matplotlib 3.6.0
Patch:          https://github.com/anntzer/mplcursors/commit/a666fd204fca24a42e2fce8cc9207934ba71fd53.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
mplcursors – Interactive data selection cursors for Matplotlib

%package -n     python3-%{srcname}
Summary:        %{summary}
 
%description -n python3-%{srcname}
mplcursors – Interactive data selection cursors for Matplotlib

%if %{with doc}
%package -n python-%{srcname}-doc
Summary:        mplcursors documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-gallery) >= 0.6
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pydata-sphinx-theme)

%description -n python-%{srcname}-doc
Documentation for mplcursors
%endif

%prep
%autosetup -n %{srcname}-%{version} -p1
# Work around broken Sphinx check.
sed -i -e 's/sphinx-gallery==0.9.0/sphinx-gallery==0/' .doc-requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r

%build
%if 0%{fedora} && 0%{fedora} < 36
export PIP_USE_FEATURE="in-tree-build"
%endif
%pyproject_wheel

%if %{with doc}
# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst examples/README.txt
%{python3_sitelib}/%{srcname}.pth

%if %{with doc}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt
%endif

%changelog
%autochangelog
