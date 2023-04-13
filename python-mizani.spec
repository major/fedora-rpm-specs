%global pypi_name mizani

# Generate HTML documentation
%bcond_without doc

# Provide man pages
%bcond_without man

%global _description %{expand:
Mizani is a scales package for graphics. It is written in Python and is
based on Hadley Wickham’s Scales.}

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        %{autorelease}
Summary:        Scales package for graphics
BuildArch:      noarch

# MIT License applies to doc/theme/static/bootstrap-3.4.1
# Python-2.0.1 license applies to doc/_static/copybutton.js
License:        BSD-3-Clause AND MIT AND Python-2.0.1
URL:            https://github.com/has2k1/%(pypi_name)
Source0:        %{pypi_source %{pypi_name}}
# Fix TypeError for Sphinx >= 6.1.3 (RHBZ#2180474)
# Already fixed upstream, pending next release: https://github.com/has2k1/mizani/commit/09d6e53dc6a297ed4aa5d2fa48e624ee3b00b25c
Patch:          sphinx-6.1.3.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  git-core
%if %{with doc} || %{with man}
BuildRequires:  make
BuildRequires:  coreutils
%if %{with doc}
BuildRequires:  python3-sphinx
%endif
%if %{with man}
BuildRequires:  python3-numpydoc
%endif
%endif

%description -n python3-%{pypi_name} %_description

%if %{with doc}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-%{pypi_name} == %{version}

%description doc
%{summary}
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git

# Disable coverage
sed -i -e 's/--cov=mizani --cov-report=xml//' pytest.ini

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{with doc} || %{with man}
  pushd doc
  %if %{with doc}
    make html
  %endif
  %if %{with man}
    make man
  %endif
  popd
%endif


%install
%pyproject_install
%if %{with doc}
  mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
  cp -a doc/_build/html ${RPM_BUILD_ROOT}%{_pkgdocdir}
  rm -rf ${RPM_BUILD_ROOT}%{_pkgdocdir}/html/.buildinfo
%endif
%if %{with man}
  mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
  cp -a doc/_build/man/*.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
  gzip ${RPM_BUILD_ROOT}%{_mandir}/man1/*.1
%endif
%pyproject_save_files %{pypi_name}


%check
%{pytest}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%if %{with man}
%doc %{_mandir}/man1/*.1.gz
%endif
%license LICENSE
%license licences/*LICENSE

%if %{with doc}
%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%endif

%changelog
%autochangelog
