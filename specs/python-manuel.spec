Name:           python-manuel
Version:        1.13.0
Release:        %autorelease
Summary:        Build tested documentation

# The content is Apache-2.0.  Other licenses are due to files copied in by
# Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/check-solid.svg: MIT
# _static/clipboard.min.js: MIT
# _static/copy-button.svg: MIT
# _static/copybutton.css: MIT
# _static/copybutton.js: MIT
# _static/copybutton_funcs.js: MIT
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://pypi.python.org/pypi/manuel
Source0:        https://github.com/benji-york/manuel/archive/%{version}/manuel-%{version}.tar.gz
# Work around a test failure due to more explicit names in python 3.11
Patch0:         %{name}-test.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-copybutton}

%description
Manuel lets you mix and match traditional doctests with custom test
syntax.  Several plug-ins are included that provide new test syntax.
You can also create your own plug-ins.

%package -n python3-manuel
Summary:        Build tested documentation
Provides:       bundled(js-jquery)

%description -n python3-manuel
Manuel lets you mix and match traditional doctests with custom test
syntax.  Several plug-ins are included that provide new test syntax.
You can also create your own plug-ins.

%prep
%autosetup -n manuel-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel
sphinx-build -c sphinx src/manuel docs
rm -fr docs/.buildinfo docs/.doctrees

rst2html --no-datestamp CHANGES.rst CHANGES.html

%install
%pyproject_install
%pyproject_save_files manuel

%check
export PYTHONPATH=$PWD/build/lib
cp -p src/manuel/myst-markdown.md build/lib/manuel
%{python3} -m unittest manuel.tests.test_suite

%files -n python3-manuel -f %{pyproject_files}
%doc CHANGES.html docs/*
%license COPYRIGHT.rst

%changelog
%autochangelog
