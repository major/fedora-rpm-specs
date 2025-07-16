Name:           python-transaction
Version:        5.0
Release:        %autorelease
Summary:        Transaction management for Python

License:        ZPL-2.1
URL:            https://pypi.io/project/transaction
Source0:        %pypi_source transaction
Patch1:         transaction-no-explicit-setuptools-req.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-zope-interface


%global _description\
This package contains a generic transaction implementation for Python. It is\
mainly used by the ZODB, though.

%description %_description

%package -n python3-transaction
Summary:        Transaction management for Python 3

Requires:       python3-zope-interface

%description -n python3-transaction %_description


%prep
%autosetup -n transaction-%{version} -p1



%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files transaction


%check
%pyproject_check_import
%pytest


%files -n python3-transaction -f %{pyproject_files}
%doc README.rst LICENSE.txt COPYRIGHT.txt


%changelog
%autochangelog
