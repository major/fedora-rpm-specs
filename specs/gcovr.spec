%{?python_enable_dependency_generator}

%bcond_without  docs

Name:           gcovr
Version:        8.3
Release:        %autorelease
Summary:        A code coverage report generator using GNU gcov

License:        BSD-3-Clause
URL:            https://gcovr.com/
Source0:        https://github.com/gcovr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist colorlog}
%if %{with docs}
BuildRequires:  %{py3_dist lxml}
BuildRequires:  %{py3_dist Jinja2}
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist sphinxcontrib-autoprogram} >= 0.1.5
%endif
BuildRequires: make

# for gcov
Requires:       gcc
Requires:       %{py3_dist Jinja2}
Requires:       %{py3_dist colorlog}

BuildArch:      noarch

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This command is inspired by the Python coverage.py package, which provides
a similar utility in Python. The gcovr command produces either compact
human-readable summary reports, machine readable XML reports
(in Cobertura format) or simple HTML reports. Thus, gcovr can be viewed
as a command-line alternative to the lcov utility, which runs gcov and
generates an HTML-formatted report.

%if %{with docs}
%package        doc
Summary:        Documentation of gcovr

%description    doc
Documentation of gcovr.
%endif

%prep
%autosetup

# Relax the strict version requirements.
sed -i -e "s/hatchling==1.26.1/hatchling/" -e "s/hatch-vcs==0.4.0/hatch-vcs/" -e "s/hatch-fancy-pypi-readme==24.1.0/hatch-fancy-pypi-readme/" pyproject.toml

%generate_buildrequires
# Let hatch-vcs/setuptools_scm determine version outside of SCM
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
# Let hatch-vcs/setuptools_scm determine version outside of SCM
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gcovr

%if %{with docs}
# the documentation can only be build **after** gcovr is installed
# => need to set PATH, PYTHONPATH so that the installed binary & package are
# found
# also set PYTHON so that the sphinx Makefile picks up python3 instead of
# python2
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHON=python3

pushd .
cd doc

# Manpage
sphinx-build -M man source build %{?fedora:-W}
install -D -p -m 0644 build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# html doc
sphinx-build -M html source build %{?fedora:-W}
rm build/html/.buildinfo

popd
%endif


%files
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/gcovr
%{python3_sitelib}/gcovr*
%if %{with docs}
%{_mandir}/man1/%{name}.1*
%endif

%if %{with docs}
%files doc
%doc doc/build/html/*
%endif


%changelog
%autochangelog
