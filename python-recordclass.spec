%global srcname recordclass

Name:           python-%{srcname}
Version:        0.20
Release:        %autorelease
Summary:        Mutable variant of namedtuple

License:        MIT
URL:            https://bitbucket.org/intellimath/recordclass
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
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Additional documentation and examples for %{name}.

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
%doc README.md ACKS

%files doc
%license LICENSE.txt
%doc examples

%changelog
%autochangelog
