%global srcname relval

Name:           relval
Version:        2.7.7
Release:        %{autorelease}
Summary:        Tool for interacting with Fedora QA wiki pages

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/quality/relval
Source0:        https://forge.fedoraproject.org/quality/relval/releases/download/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Relval can perform various tasks related to Fedora QA by interacting with the
Fedora wiki. It lets you:

* Create wiki pages for Fedora release validation test events
* Generate statistics on release validation testing
* Report release validation test results using a console interface

See https://fedoraproject.org/wiki/QA/SOP_Release_Validation_Test_Event for
more information on the process relval helps with.

%prep
%autosetup -n %{srcname}-%{version}
# setuptools-scm is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-scm"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}*
%{_bindir}/relval

%changelog
%{autochangelog}
