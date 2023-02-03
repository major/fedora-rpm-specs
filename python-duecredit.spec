%global _description %{expand: \
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.}

Name:           python-duecredit
Version:        0.9.2
Release:        %autorelease
Summary:        Automated collection and reporting of citations

License:        BSD-2-Clause-Views
URL:            https://github.com/duecredit/duecredit
Source0:        %{pypi_source duecredit}

BuildArch:      noarch

%description
%{_description}

%package -n python3-duecredit
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}


%description -n python3-duecredit
%{_description}

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n duecredit-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files duecredit

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{pytest} duecredit/tests --ignore=duecredit/tests/test_io.py

%files -n python3-duecredit -f %{pyproject_files}
%{_bindir}/duecredit

%files doc
%license LICENSE
%doc examples/

%changelog
%autochangelog
