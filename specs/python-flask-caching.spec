# Created by pyp2rpm-3.3.2

%global srcname flask-caching

Name:           python-%{srcname}
Version:        2.3.1
Release:        %autorelease
Summary:        Adds caching support to your Flask application

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sh4nks/flask-caching
Source0:        https://github.com/sh4nks/%{srcname}/archive/v%{version}/%{srcname}-v%{version}.tar.gz

# Update intersphinx_mapping for Sphinx 8 compatibility
# https://github.com/pallets-eco/flask-caching/pull/599/commits/3c8df1714292549d2fe27fa4a03110657fd647a3
#
# Fixes:
#
# The intersphinx_mapping in docs/conf.py is incompatible with Sphinx 8
# https://github.com/pallets-eco/flask-caching/issues/598
#
# python-flask-caching fails to build with sphinx 8.x: ERROR: Invalid value
# `None` in intersphinx_mapping['https://docs.python.org/3/'].
# https://bugzilla.redhat.com/show_bug.cgi?id=2329857
#
# python-flask-caching: FTBFS in Fedora rawhide/f42
# https://bugzilla.redhat.com/show_bug.cgi?id=2341153
Patch:          https://github.com/pallets-eco/flask-caching/pull/599/commits/3c8df1714292549d2fe27fa4a03110657fd647a3.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(asgiref)
BuildRequires:  python3dist(cachelib)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(pylibmc)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-xprocess)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(redis)
BuildRequires:  redis
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Flask-Caching Adds easy cache support to Flask

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(flask)
%description -n python3-%{srcname}
Flask-Caching Adds easy cache support to Flask

%package -n python-%{srcname}-doc
Summary:        Flask-Caching documentation
%description -n python-%{srcname}-doc
Documentation for Flask-Caching

%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
redis-server &
%pytest
kill %1

%files -n python3-%{srcname}
%license LICENSE docs/license.rst
%doc README.rst
%{python3_sitelib}/flask_caching
%{python3_sitelib}/Flask_Caching-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE docs/license.rst

%changelog
%autochangelog
