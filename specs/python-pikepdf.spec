%global srcname pikepdf

# Bconds are needed for Python bootstrap
%bcond docs 0
%bcond tests 1

Name:           python-%{srcname}
Version:        9.5.2
Release:        %autorelease
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPL-2.0
URL:            https://github.com/pikepdf/pikepdf
Source:         %pypi_source %{srcname}

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel >= 11.5.0
BuildRequires:  python3-devel
%if %{with tests}
# Tests:
BuildRequires:  poppler-utils
%endif

%description
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%if %{with docs}
%package -n python-%{srcname}-doc
Summary:        pikepdf documentation

# Not autorequired because it's a Fedora-specific subpackage.
BuildRequires:  python3-ipython-sphinx

%description -n python-%{srcname}-doc
Documentation for pikepdf
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1

# Drop coverage requirements
sed -i -e '/coverage/d' -e '/pytest-cov/d' setup.cfg

%if %{with docs}
# We don't build docs against the installed version, so force the version.
sed -i -e "s/release = .\+/release = '%{version}'/g" docs/conf.py
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_docs: -x docs} %{?with_tests: -x test}


%build
%pyproject_wheel

%if %{with docs}
# generate html docs
export PYTHONPATH="$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
pushd docs
sphinx-build-3 . ../html
popd
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%{pytest} -ra
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%if %{with docs}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt
%endif


%changelog
%autochangelog
