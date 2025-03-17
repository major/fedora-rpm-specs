# We have source files with intentional syntax errors, in order to test.
# Do not fail the build just because some file is not valid python.
%undefine _python_bytecompile_errors_terminate_build

%global _docdir_fmt python3-zope-testrunner

Name:           python-zope-testrunner
Version:        6.6
Release:        %autorelease
Summary:        Zope testrunner script

License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.testrunner
VCS:            https://github.com/zopefoundation/zope.testrunner
Source:         %{vcs}/archive/%{version}/zope.testrunner-%{version}.tar.gz
Patch:          zope.testrunner-allow-new-setuptools.diff

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist manuel}

%description
This package provides a flexible test runner with layer support.

%package     -n python3-zope-testrunner
Summary:        Zope testrunner script

%description -n python3-zope-testrunner
This package provides a flexible test runner with layer support.

%package        doc
# The content is ZPL-2.1.  Files added by Sphinx have the following licences:
# searchindex.js: BSD-2-Clause
# _static/*: BSD-2-Clause, except for the following:
# _static/jquery*.js: MIT
# _static/underscore*.js: MIT
License:        ZPL-2.1 AND BSD-2-Clause AND MIT
Summary:        Documentation for zope.testrunner

%description    doc
Documentation for zope.testrunner.

%pyproject_extras_subpkg -n python3-zope-testrunner subunit

%prep
%autosetup -n zope.testrunner-%{version} -p1

# Update the sphinx HTML theme name
sed -i "s/'default'/'classic'/" docs/conf.py

# Fix the way python is invoked
sed -i 's/python -m/python3 -m/' docs/cli.rst

# Use local objects.inv for intersphinx
sed -i "s|\('https://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

# Replace a deprecated directive
sed -i "s/autodoc_default_flags.*/autodoc_default_options = {'members': True, 'show-inheritance': True}/" docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -t -x test,subunit,docs

%build
%pyproject_wheel

rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

# Not really RST: https://github.com/zopefoundation/zope.testrunner/issues/100
cp -p COPYRIGHT.rst COPYRIGHT

%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
help2man -s 1 -o %{buildroot}%{_mandir}/man1/zope-testrunner.1 \
  -N -n "Zope testrunner script" %{buildroot}%{_bindir}/zope-testrunner

# The Sphinx documentation cannot be built with an uninstalled zope.testrunner
# because python finds the installed zope package, which doesn't contain
# testrunner.  We fake out python by copying the entire installed tree to a
# local directory and adding this package inside the zope directory.
mkdir lib
cp -a %{_prefix}/lib/python%{python3_version} lib
if [ -d %{_prefix}/lib64/python%{python3_version} ]; then
  mkdir lib64
  cp -a %{_prefix}/lib64/python%{python3_version} lib64
fi
mkdir include
cp -a %{_includedir}/python%{python3_version}* include
cp -a %{buildroot}%{python3_sitelib}/zope* \
      lib/python%{python3_version}/site-packages
export PYTHONHOME=$PWD:$PWD
sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html
rm -fr include lib lib64
rm -f docs/_build/html/.buildinfo
unset PYTHONHOME

%check
%tox

%files -n python3-zope-testrunner
%doc CHANGES.html README.html
%license COPYRIGHT LICENSE.md
%{_bindir}/zope-testrunner
%{_mandir}/man1/zope-testrunner.1*
%{python3_sitelib}/zope.testrunner*
%{python3_sitelib}/zope/testrunner/
%exclude %{python3_sitelib}/zope/testrunner/tests

%files doc
%doc docs/_build/html

%changelog
%autochangelog
