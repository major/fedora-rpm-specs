%global pypi_name asn1

Name:           python-%{pypi_name}
Version:        2.6.0
Release:        %autorelease
Summary:        Simple ASN.1 encoder and decoder for Python

License:        MIT
URL:            https://github.com/andrivet/python-asn1
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global _description %{expand:
Python-ASN1 is a simple ASN.1 encoder and decoder for Python with support for
BER (parser) and DER (parser and generator) encoding (except indefinite
lengths).}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package        doc
Summary:        Documentation for %{name}

%description    doc
This package contains additional documentation and examples for %{name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Drop unnecessary dependency
sed -i '/enum-compat/d' requirements.txt
sed -i 's/install_requires = .*/install_requires = []/' setup.py

# Fix permissions
chmod -x examples/dump.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="${PWD}" sphinx-build-3 docs html
rm -r html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst

%files doc
%license LICENSE
%doc examples html

%changelog
%autochangelog
