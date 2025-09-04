%global srcname mplcursors
%bcond doc 1

Name:           python-%{srcname}
Version:        0.7
Release:        %autorelease
Summary:        Interactive data selection cursors for Matplotlib

License:        MIT
URL:            https://github.com/anntzer/mplcursors
Source:         %pypi_source %{srcname}

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

%description -n python-%{srcname}-doc
Documentation for mplcursors
%endif

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_doc:-x docs}

%build
%pyproject_wheel

%if %{with doc}
# generate html docs
PYTHONPATH="$PWD/build/lib" sphinx-build-3 doc/source html
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

%if %{with doc}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt
%endif

%changelog
%autochangelog
