Name:           python-cbor2
Version:        5.9.0
Release:        %autorelease
Summary:        Python CBOR (de)serializer with extensive tag support
License:        MIT
URL:            https://github.com/agronholm/cbor2
Source:         %{pypi_source cbor2}

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 7049) serialization format.}


%description %_description


%package -n     python3-cbor2
Summary:        %{summary}


%description -n python3-cbor2 %_description


%package -n python-cbor2-doc
Summary:        cbor2 documentation
BuildArch:      noarch
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)


%description -n python-cbor2-doc
Documentation for cbor2.


%prep
%autosetup -p 1 -n cbor2-%{version}


%generate_buildrequires
%pyproject_buildrequires -g test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l cbor2
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}


%check
%pytest -v tests


%files -n python3-cbor2 -f %{pyproject_files}
%doc README.rst
%{python3_sitearch}/_cbor2%{python3_ext_suffix}
%{_bindir}/cbor2


%files -n python-cbor2-doc
%doc html
%license LICENSE.txt


%changelog
%autochangelog
