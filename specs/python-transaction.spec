Name:           python-transaction
Version:        5.0
Release:        %autorelease
Summary:        Transaction management for Python

License:        ZPL-2.1
URL:            https://pypi.io/project/transaction
Source0:        %pypi_source transaction

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-zope-interface


%global _description\
This package contains a generic transaction implementation for Python. It is\
mainly used by the ZODB, though.

%description %_description

%package -n python3-transaction
Summary:        Transaction management for Python 3

Requires:       python3-zope-interface
%{?python_provide:%python_provide python3-transaction}

%description -n python3-transaction %_description


%prep
%autosetup -n transaction-%{version} -p1

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install


%check
%pytest


%files -n python3-transaction
%doc README.rst LICENSE.txt COPYRIGHT.txt
%{python3_sitelib}/transaction/
%{python3_sitelib}/transaction-*.egg-info


%changelog
%autochangelog
