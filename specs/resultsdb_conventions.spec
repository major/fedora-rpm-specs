%global sum     Library defining conventions for ResultsDB results
%global desc    This project defines some agreed conventions for reporting results of \
different types to ResultsDB, and provides code (currently a Python library) \
to help with reporting results that conform to the conventions.

%global forgejo_namespace    quality
%global forgejo_name         resultsdb_conventions
%global forgejo_version      3.0.3

Name:           resultsdb_conventions
Version:        %{forgejo_version}
Release:        %{autorelease}
Summary:        %{sum}

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/%{forgejo_namespace}/%{forgejo_name}
Source0:        https://files.pythonhosted.org/packages/source/r/%{forgejo_name}/%{forgejo_name}-%{forgejo_version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python%{python3_pkgversion}-resultsdb_conventions
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-resultsdb_conventions}
Obsoletes:      python2-resultsdb_conventions < %{version}-%{release}

%description -n python%{python3_pkgversion}-resultsdb_conventions
%{desc}

%package -n python%{python3_pkgversion}-resultsdb_conventions-fedora
Summary:        %{sum} (Fedora module)
%{?python_provide:%python_provide python%{python3_pkgversion}-resultsdb_conventions-fedora}
Requires:       python%{python3_pkgversion}-resultsdb_conventions
Obsoletes:      python2-resultsdb_conventions-fedora < %{version}-%{release}

%description -n python%{python3_pkgversion}-resultsdb_conventions-fedora
%{desc} This subpackage
contains the resultsdb_conventions.fedora module, which has additional
dependencies.

%prep
%autosetup -p1
# this is needed for doing sdist, but not for anything else
sed -i -e '/setuptools_git/d' setup.py
sed -i -e 's., "setuptools-scm"..g' pyproject.toml
%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python%{python3_pkgversion}-resultsdb_conventions
%doc README.md CHANGELOG.md
%license COPYING
%{python3_sitelib}/resultsdb_conventions*
%exclude %{python3_sitelib}/resultsdb_conventions/fedora.py
%pycached %exclude %{python3_sitelib}/resultsdb_conventions/fedora.py
%exclude %{python3_sitelib}/resultsdb_conventions/fedoracoreos.py
%pycached %exclude %{python3_sitelib}/resultsdb_conventions/fedoracoreos.py

%files -n python%{python3_pkgversion}-resultsdb_conventions-fedora
%{python3_sitelib}/resultsdb_conventions/fedora.py
%pycached %{python3_sitelib}/resultsdb_conventions/fedora.py
%{python3_sitelib}/resultsdb_conventions/fedoracoreos.py
%pycached %{python3_sitelib}/resultsdb_conventions/fedoracoreos.py

%changelog
%autochangelog
