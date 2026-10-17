%global srcname distlib
%bcond_without check

Name:       python-distlib
Version:    0.4.3
Release:    %autorelease
Summary:    Low-level components of distutils2/packaging, augmented with higher-level APIs

# https://github.com/pypa/distlib/issues/275
License:    Python-2.0.1
URL:        https://readthedocs.org/projects/distlib/
Source0:    %pypi_source %{srcname} %{version}

BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-test
BuildRequires:  pyproject-rpm-macros

%description
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Low-level components of distutils2/packaging, augmented with higher-level APIs

%description -n python%{python3_pkgversion}-%{srcname}
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%prep
%autosetup -p1 -n %{srcname}-%{version}

rm distlib/*.exe

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with check}
%check
export PYTHONHASHSEED=0
# Some tests require network access
export SKIP_ONLINE=1
# test_sequencer_basic test fails due to relying
# on the ordering of the input, hence disabling it.
# https://github.com/pypa/distlib/issues/161
%pytest -k "not test_sequencer_basic"
%endif # with_tests

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.rst

%changelog
%autochangelog
