%global srcname regex

Name:           python-%{srcname}
Version:        2024.11.6
Release:        %autorelease
Summary:        Alternative regular expression module, to replace re
# see also https://code.google.com/p/mrab-regex-hg/issues/detail?id=124
# Automatically converted from old format: Python and CNRI - review is highly recommended.
License:        LicenseRef-Callaway-Python AND CNRI-Python
URL:            https://bitbucket.org/mrabarnett/mrab-regex
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  /usr/bin/rst2html
BuildRequires:  python3-pygments
BuildRequires:  gcc

%global _description %{expand:
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
# rebuild the HTML doc
rst2html docs/UnicodeProperties.rst > docs/UnicodeProperties.html
rst2html README.rst > README.html


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.html
%doc docs/Features.html
%doc docs/UnicodeProperties.html
%{python3_sitearch}/*


%autochangelog
