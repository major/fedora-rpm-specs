%global srcname stem

# Enable tests conditionally
# https://bugzilla.redhat.com/show_bug.cgi?id=1797690
# https://github.com/torproject/stem/issues/71
%if 0%{?fedora} > 32 || 0%{?rhel} > 5
%global tests_enabled 0
%else
%global tests_enabled 1
%endif

Name: python-stem
Version: 1.8.2
Release: 13%{?dist}
Summary: Python controller library for Tor
# All source code is LGPLv3 except stem/util/ordereddict.py which is MIT
# Automatically converted from old format: LGPLv3 and MIT - review is highly recommended.
License: LGPL-3.0-only AND LicenseRef-Callaway-MIT
URL: https://stem.torproject.org/
Source0: %{pypi_source}
BuildArch: noarch
BuildRequires: make
BuildRequires: python3-devel
# Doc building
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-autodoc-typehints
# Testing
%if %{?tests_enabled}
BuildRequires: python3-mock
BuildRequires: python3-cryptography
BuildRequires: python3-pyflakes
BuildRequires: python3-pycodestyle
%endif

%global _description %{expand:
Stem is a Python controller library that you can use to interact with Tor.
With it you can write scripts and applications with capabilities similar
to nyx.

From a technical standpoint, Stem is a Python implementation of Tor's
directory and control specifications.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
Suggests: %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package doc
Summary: %{summary}

%description doc %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
%make_build html
%make_build text
%make_build man
popd

%install
%pyproject_install
%pyproject_save_files -l %{srcname}
%py3_shebang_fix %{buildroot}%{_bindir}/tor-prompt
find docs/_build -name .buildinfo -delete
install -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
%if %{?tests_enabled}
%pyproject_check_import
%{py3_test_envvars} %{python3} run_tests.py --unit
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/tor-prompt

%files doc
%doc README.md docs/_build/html docs/_build/text
%license LICENSE
%{_mandir}/man1/%{srcname}.1*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
