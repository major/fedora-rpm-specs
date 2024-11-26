%global modname translationstring

Name:           python-%{modname}
Version:        1.4
Release:        %autorelease
Summary:        Library used for internationalization (i18n) duties related to translation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/translationstring
Source0:        https://github.com/Pylons/translationstring/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library used by various Pylons Project packages for\
internationalization (i18n) duties related to translation.\
\
This package provides a translation string class, a translation string factory\
class, translation and pluralization primitives, and a utility that helps\
Chameleon templates use translation facilities of this package. It does not\
depend on Babel, but its translation and pluralization services are meant to\
work best when provided with an instance of the babel.support.Translations class.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}

%prep
%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l translationstring

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst changes.rst

%changelog
%autochangelog
