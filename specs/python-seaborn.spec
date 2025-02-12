%bcond_without check
%global srcname seaborn

Name: python-%{srcname}
Version: 0.13.2
Release: %autorelease
Summary: Statistical data visualization in Python
License: BSD-3-Clause

URL: http://seaborn.pydata.org/
Source0: %{pypi_source}
# Use system python-husl
Patch0: seaborn-husl.patch
Patch1: seaborn-docscrape.patch
BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Seaborn is a library for making attractive and informative statistical
graphics in Python. It is built on top of matplotlib and tightly integrated
with the PyData stack, including support for numpy and pandas data structures
and statistical routines from scipy and statsmodels.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

BuildRequires: %{py3_dist flit_core}

%if %{with check}
BuildRequires: %{py3_dist husl}
BuildRequires: %{py3_dist numpydoc}
BuildRequires: %{py3_dist pytest}
%endif

Requires: %{py3_dist husl}
Requires: %{py3_dist numpydoc}
Recommends: %{py3_dist statsmodels}
## Not in fedora
##Recommends: _{py3_dist fastcluster}

%description -n python3-%{srcname} %_description

%prep
rm -rf seaborn/external/husl.py
rm -rf seaborn/external/docscrape.py
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x stats

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files seaborn


%if %{with check}
%check
%pytest --deselect "tests/_core/test_plot.py::TestLabelVisibility::test_1d_column_wrapped" \
        --deselect "tests/_core/test_plot.py::TestLabelVisibility::test_1d_row_wrapped" \
        --deselect "tests/test_distributions.py::TestKDEPlotBivariate::test_weights"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
