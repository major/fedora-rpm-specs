%global srcname recordclass

Name:           python-%{srcname}
Version:        0.21
Release:        %autorelease
Summary:        Mutable variant of namedtuple

License:        MIT
URL:            https://github.com/intellimath/recordclass
Source:         %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
Recordclass is Python library implementing a mutable variant of namedtuple,
which support assignments, and other memory saving variants.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
# Upstream stopped shipping examples on PyPI and the git repo doesn't have
# tagged releases.
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < 0.21-2

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" \
  %python3 ./test_all.py

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
