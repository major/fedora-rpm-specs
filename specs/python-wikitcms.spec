%global srcname wikitcms

Name:           python-%{srcname}
Version:        2.6.21
Release:        %{autorelease}
Summary:        Fedora QA wiki test management Python library

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://pagure.io/fedora-qa/python-wikitcms
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
python-wikitcms is a library for interacting with Fedora's wiki-based 'test
management' system. It can:

* Create the pages for release validation test events
* Find existing release validation event pages, in various ways
* Report test results

The wiki-based test management system itself is documented at:
https://fedoraproject.org/wiki/Wikitcms

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Obsoletes:      python2-%{srcname} < %{version}-%{release}
BuildRequires:  pyproject-rpm-macros
Recommends:     python3-openidc-client >= 0.4.0

%description -n python3-%{srcname}
python-wikitcms is a library for interacting with Fedora's wiki-based 'test
management' system. It can:

* Create the pages for release validation test events
* Find existing release validation event pages, in various ways
* Report test results

The wiki-based test management system itself is documented at:
https://fedoraproject.org/wiki/Wikitcms

This is the Python 3 build.

%prep
%autosetup -n %{srcname}-%{version}
# setuptools-git is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-git"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{srcname}
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}*

%changelog
%{autochangelog}
