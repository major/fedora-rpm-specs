%global srcname catkin_tools
%global forgeurl https://github.com/catkin/catkin_tools
Version:        0.9.5
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Command line tools for working with catkin

License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch

%description
Provides command line tools for working with catkin


%package doc
Summary:        HTML documentation for %{srcname}
BuildRequires:  make
BuildRequires:  python3-rpm-macros
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description doc
HTML documentation for %{srcname}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  cmake
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.3.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-osrf-pycommon >= 0.1.1
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
Requires:       cmake
Requires:       make
Conflicts:      python2-%{srcname} < 0.4.4-7

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.3.0
Requires:       python%{python3_pkgversion}-osrf-pycommon >= 0.1.1
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Provides command line tools for working with catkin


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/_build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

install -p -m0644 -D docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
%pyproject_check_import

# Many system tests require catkin itself, which isn't packaged in Fedora
%pytest tests/unit


%files doc
%license LICENSE
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/catkin
%{_mandir}/man1/%{srcname}.1.*
%{_datadir}/zsh/site-functions/_catkin
%{_datadir}/bash-completion/


%changelog
%autochangelog
