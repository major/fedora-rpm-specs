Name:           python-resultsdb_api
# NOTE: if you update version, *make sure* to also update `setup.py`
Version:        2.1.6
Release:        %{autorelease}
Summary:        Interface api to ResultsDB

License:        GPL-2.0-or-later
URL:            https://forge.fedoraproject.org/quality/resultsdb_api
Source0:        https://files.pythonhosted.org/packages/source/r/resultsdb-api/resultsdb_api-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Interface api to ResultsDB

%package -n python3-resultsdb_api
Summary: %summary
Requires:       python3-simplejson
Requires:       python3-requests

%description -n python3-resultsdb_api
Python3 interface to resultsdb.

%prep
%autosetup -p1 -n resultsdb_api-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files resultsdb_api

%check
%pytest

%files -n python3-resultsdb_api -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{autochangelog}
