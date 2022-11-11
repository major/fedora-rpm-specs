%global srcname relval

Name:           relval
Version:        2.5.8
Release:        %{autorelease}
Summary:        Tool for interacting with Fedora QA wiki pages

License:        GPLv3+
URL:            https://pagure.io/fedora-qa/relval
Source0:        https://releases.pagure.org/fedora-qa/relval/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-fedfind >= 2.8.0
Requires:       python3-markupsafe
Requires:       python3-mwclient
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-wikitcms >= 2.6.0
Requires:       python3-bugzilla

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

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}*
%{_bindir}/relval

%changelog
%{autochangelog}
