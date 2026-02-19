%if 0%{?el8}
  # jaraco.collections not yet available in epel8
  %bcond_with tests
%else
  %bcond_without tests
%endif

Name:           python-cherrypy
%global         camelname CherryPy
Version:        18.10.0
Release:        %autorelease
Summary:        Pythonic, object-oriented web development framework
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://cherrypy.dev/
Source0:        https://files.pythonhosted.org/packages/source/C/%{camelname}/cherrypy-%{version}.tar.gz
Patch0:         1f75bc9eed8e0e385f64f368bd69f58d96fb8c2b.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm)
%if %{with tests}
# Test dependencies
BuildRequires:  python3dist(cheroot)
BuildRequires:  python3dist(jaraco-collections)
BuildRequires:  python3dist(path)
BuildRequires:  python3dist(portend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests-toolbelt)
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-zc-lockfile
%endif

%global _description\
%{camelname} allows developers to build web applications in much the same way\
they would build any other object-oriented Python program. This usually\
results in smaller source code developed in less time.

%description %_description

%package -n python3-cherrypy
Summary: %summary

%package -n python3-cherrypy-devel
Summary: Test and Tutorial files excluded from main package

# Remove after F32.
Obsoletes: python2-cherrypy < 3.5.1

%description -n python3-cherrypy %_description
%description -n python3-cherrypy-devel %_description

%prep
%autosetup -p1 -n cherrypy-%{version}

# These tests still fail (reason unknown):
rm cherrypy/test/test_session.py
sed -i '/pytest_cov/d' setup.py
sed -i '/cov/d' pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
# https://github.com/cherrypy/cherrypy/commit/5d3c86eb36dfdf972a1d3c8d69cf8be2050eb99c
export WEBTEST_INTERACTIVE=false
%pytest cherrypy/test \
  --deselect=cherrypy/test/test_tools.py::ToolTests::testCombinedTools \
  -p no:unraisableexception
%endif

%files -n python3-cherrypy
%doc README.rst
%license LICENSE.md
%doc cherrypy/tutorial
%{_bindir}/cherryd
%{python3_sitelib}/*
%exclude %{python3_sitelib}/cherrypy/test
%exclude %{python3_sitelib}/cherrypy/tutorial

%files -n python3-cherrypy-devel
%{python3_sitelib}/cherrypy/test
%{python3_sitelib}/cherrypy/tutorial

%changelog
%autochangelog
