%global pypi_name mizani

# Generate HTML documentation
%bcond_without doc

# Provide man pages
%bcond_without man

Name:           python-%{pypi_name}
Version:        0.13.5
Release:        %{autorelease}
Summary:        Scales package for graphics

%global forgeurl https://github.com/has2k1/mizani
%forgemeta

# MIT License applies to doc/theme/static/bootstrap-3.4.1
# Python-2.0.1 license applies to doc/_static/copybutton.js
License:        BSD-3-Clause AND MIT AND Python-2.0.1
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
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

%global _description %{expand:
Mizani is a scales package for graphics. It is written in Python and is
based on Hadley Wickham’s Scales.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%if %{with doc}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-%{pypi_name} == %{version}-%{release}

%description doc
%{summary}
%endif


%prep
%forgeautosetup -p1

# Disable coverage
sed -i -e 's/--cov=mizani --cov-report=xml//' pyproject.toml


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
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
  mkdir -p %{buildroot}/%{_pkgdocdir}
  cp -a doc/_build/html %{buildroot}/%{_pkgdocdir}
  rm -rf %{buildroot}/%{_pkgdocdir}/html/.buildinfo
%endif
%if %{with man}
  mkdir -p %{buildroot}/%{_mandir}/man1
  cp -a doc/_build/man/*.1 %{buildroot}/%{_mandir}/man1
%endif
%pyproject_save_files -l %{pypi_name}


%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%if %{with man}
%{_mandir}/man1/%{pypi_name}.1*
%endif
%license licences/*LICENSE

%if %{with doc}
%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%endif


%changelog
%autochangelog
