Name:           python-rapidfuzz
Version:        2.13.7
Release:        %autorelease
Summary:        Rapid fuzzy string matching in Python and C++ using the Levenshtein Distance

License:        MIT
URL:            https://github.com/maxbachmann/RapidFuzz
Source:         %{pypi_source rapidfuzz}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pandas
BuildRequires:  python3-pytest
BuildRequires:  rapidfuzz-cpp-static
BuildRequires:  taskflow-static

%global _description %{expand:
RapidFuzz is a fast string matching library for Python and C++, which is using
the string similarity calculations from FuzzyWuzzy. However there are a couple
of aspects that set RapidFuzz apart from FuzzyWuzzy:
- It is MIT licensed so it can be used whichever License you might want
to choose for your project, while you're forced to adopt the GPL license when
using FuzzyWuzzy
- It provides many string_metrics like hamming or jaro_winkler, which
are not included in FuzzyWuzzy
- It is mostly written in C++ and on top of this comes with a lot of Algorithmic
improvements to make string matching even faster, while still providing the same
results. For detailed benchmarks check the documentation
- Fixes multiple bugs in the partial_ratio implementation}

%description %_description

%package -n python3-rapidfuzz
Summary:        %{summary}

%description -n python3-rapidfuzz %_description


%pyproject_extras_subpkg -n python3-rapidfuzz full

%package -n python3-rapidfuzz-devel
Summary:        Development files for the RapidFuzz library

Requires: python3-rapidfuzz%{?_isa} = %{version}-%{release}

%description -n python3-rapidfuzz-devel
%_description


%prep
%autosetup -p1 -n rapidfuzz-%{version}
# External dependencies (rapidfuzz-cpp and taskflow) are removed here,
# they are already packaged in Fedora and we BuildRequire them above.
rm extern -r


%generate_buildrequires
%pyproject_buildrequires -x full


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files rapidfuzz


%check
%pytest -v


%files -n python3-rapidfuzz -f %{pyproject_files}
%doc README.*
%exclude %{python3_sitearch}/rapidfuzz/rapidfuzz.h
%exclude %{python3_sitearch}/rapidfuzz/__init__.pxd

%files -n python3-rapidfuzz-devel
%{python3_sitearch}/rapidfuzz/rapidfuzz.h
%{python3_sitearch}/rapidfuzz/__init__.pxd


%changelog
%autochangelog
