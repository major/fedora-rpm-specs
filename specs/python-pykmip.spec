%global pypi_name PyKMIP
%global sname pykmip

%global _description %{expand:
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).}

Name:           python-%{sname}
Version:        0.10.0
Release:        %autorelease
Summary:        Python implementation of the Key Management Interoperability Protocol

License:        Apache-2.0
URL:            https://github.com/OpenKMIP/PyKMIP
Source0:        %{pypi_source %{pypi_name}}
Patch0:         https://github.com/OpenKMIP/PyKMIP/commit/645cbf2ae931b03b8f5ebe2458683da1b2276794.patch
BuildArch:      noarch

BuildRequires:  python3-devel


%description
%_description


%package -n python3-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol


%description -n python3-%{sname}
%_description


%prep
%autosetup -p1  -n %{pypi_name}-%{version}

# enum-compat is only needed for python <= 3.4
sed -i 's/"enum-compat",//' setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l kmip


%check
%pyproject_check_import kmip


%files -n python3-%{sname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/pykmip-server


%changelog
%autochangelog
