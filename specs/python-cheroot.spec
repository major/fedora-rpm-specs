# Created by pyp2rpm-3.2.2
%global pypi_name cheroot
# sphinx-tabs not available in fedora for docs build
%bcond_with docs

Name:           python-%{pypi_name}
Version:        11.0.0
Release:        %autorelease
Summary:        Highly-optimized, pure-python HTTP server

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cherrypy/cheroot
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(six) >= 1.11
Requires:       python3dist(more-itertools) >= 2.6
Requires:       python3-pyOpenSSL
Requires:       python3dist(jaraco-functools)

BuildRequires:  python3-devel
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3dist(jaraco-functools)
BuildRequires:  python3dist(jaraco-text)
BuildRequires:  python3dist(portend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(requests-toolbelt)

%if 0%{?el8}
BuildRequires:  python3dist(more-itertools) >= 2.6
%endif

BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-unixsocket)
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(trustme)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        cheroot documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-theme-alabaster
BuildRequires:  python3dist(rst-linker)
BuildRequires:  python3dist(jaraco-packaging)
BuildRequires:  python3dist(docutils)

%description -n python-%{pypi_name}-doc
Documentation for cheroot
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove pytest processes directive
sed -i 's/ --numprocesses=auto//' pytest.ini
# Remove optional pytest-cov dependency
sed -i -e '/pytest_cov/d' -e /--cov/d -e '/--no-cov-on-fail/d' pytest.ini
# drop setuptools_scm_git_archive
sed -i '/setuptools_scm_git_archive/d' setup.cfg
# RHEL 9 has setuptools_scm 6
sed -i 's/setuptools_scm >= 7.0.0/setuptools_scm >= 6.0.0/' setup.cfg

# doctor a few tests because of unpackaged deps in fedora
# pypytools
sed -i '/pypytools/d' cheroot/test/test_server.py
sed -i "/getfixturevalue('_garbage_bin')/d" cheroot/test/test_server.py
# jaraco.context
sed -i '/jaraco.context/d' cheroot/test/test_wsgi.py
sed -i '39 i @pytest.mark.skip()' cheroot/test/test_wsgi.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
sphinx-build -vvv docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build -W ignore::DeprecationWarning -p no:unraisableexception

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.rst
%{_bindir}/cheroot

%if %{with docs}
%files -n python-%{pypi_name}-doc
%license LICENSE.md
%doc html
%endif

%changelog
%autochangelog
