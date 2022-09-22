# tests are enabled by default
%bcond_without tests

%global         srcname     pem
%global         forgeurl    https://github.com/hynek/pem
Version:        21.2.0
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Easy PEM file parsing

License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource
# Docs use the 'furo' theme, but that isn't packaged for Fedora yet. Switch to
# the already packaged sphinx-rtd-theme instead.
Patch0:         python-pem-doc-theme-fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(service-identity)
%endif


%global _description %{expand:
pem is an MIT-licensed Python module for parsing and splitting of PEM files,
i.e. Base64-encoded DER keys and certificates.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%package -n python3-%{srcname}-doc
Requires:       python3-docs
BuildRequires:  python3-docs
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(twisted)
Summary:        Documentation for python-%{srcname}

%description -n python3-%{srcname}-doc
Documentation for python-%{srcname}


%prep
%forgesetup
%patch0 -p0

# Use local inventory in intersphinx mapping.
sed -r -i -e \
    's|https://docs.python.org/3|/%{_docdir}/python3-docs/html|' \
    docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pem

# Generate documentation.
PYTHONPATH="%{buildroot}%{python3_sitelib}:${PWD}/docs/" sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.rst


%files -n python3-%{srcname}-doc
%license LICENSE
%doc README.rst CHANGELOG.rst html


%changelog
%autochangelog
