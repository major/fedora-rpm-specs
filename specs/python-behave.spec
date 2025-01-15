%global srcname behave
%global desc %{expand: \
Behavior-driven development (or BDD) is an agile software development 
technique that encourages collaboration between developers, QA and 
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by 
Python code.}

# RHBZ #2179979
%undefine _py3_shebang_s

Name:           python-%{srcname}
Version:        1.2.6
Release:        %autorelease
Summary:        Tools for the behavior-driven development, Python style

License:        BSD-2-Clause
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/behave/behave/archive/v%{version}/%{srcname}-%{version}.tar.gz

# This patch is backport of upstream commits solving https://bugzilla.redhat.com/show_bug.cgi?id=1706085
# Upstream issue: https://github.com/behave/behave/issues/755
Patch:          0001-Backport-for-py38-fixes.patch
# This patch is backport of upstream commit solving issues with pytest 5.0 and newer
# Upstream issue: https://github.com/behave/behave/issues/864
Patch:          0002-Tweak-tests-required-by-pytest-5.0.patch
# Invalid escape sequence warnings fixes
Patch:          0003-invalid-escape-seq.patch
# RHBZ #2180467
Patch:          0004-sphinx-extlinks.patch
# Replace nose test-framework functionality with pytest
# https://github.com/behave/behave/commit/d086029e
# (sans file moves to make the patch smaller and easier to inspect)
# Several modules converted by hand.
Patch:          0005-remove-nose.patch


BuildArch:      noarch

BuildRequires:	make
BuildRequires:  help2man
BuildRequires:	python3-devel
BuildRequires:	python3-hamcrest
BuildRequires:	python3-pytest
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx-bootstrap-theme
Conflicts:	python2-behave < 1.2.6


%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{desc}

%package doc
Summary:        Documentation for %{name}

%description doc %{desc}

This package contains documentation in reST and HTML formats and some
brief feature-examples.


%prep
%autosetup -n %{srcname}-%{version} -p1

# setup command: use_2to3 is invalid
sed -i '/use_2to3/d' setup.py

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    test/*.py test/reporters/*.py tests/api/*.py tests/unit/*.py

sed -i '/mock/d' py.requirements/testing.txt
sed -i '/mock/d' setup.py
sed -i '/mock/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

make SPHINXBUILD=sphinx-build-3 html -C docs
rm -rf build/docs/html/.buildinfo


%install
mkdir -p %{buildroot}%{_mandir}/man1

%pyproject_install
%pyproject_save_files %{srcname}

PYTHONPATH=%{buildroot}%{python3_sitelib} help2man \
  --no-info \
  --name="Run a number of feature tests with behave." \
  --output=%{srcname}.1 \
  %{buildroot}%{_bindir}/%{srcname}

install -Dpm0644 %{srcname}.1 %{buildroot}%{_mandir}/man1/


%check
%pytest -v


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc %{_mandir}/man1/%{srcname}.1*
%{_bindir}/%{srcname}
%{python3_sitelib}/setuptools_%{srcname}.py
%{python3_sitelib}/__pycache__/setuptools_%{srcname}.*


%files doc
%license LICENSE
%doc README.rst build/docs/html


%changelog
%autochangelog
