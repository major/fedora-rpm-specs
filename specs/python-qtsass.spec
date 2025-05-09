# Import-checking qtsass.watchers.qt requires one of the supported Qt bindings:
# PySide2, PyQt5, PySide, or PyQt4. The highest-priority binding that is
# packaged in Fedora is PyQt5. It’s normally not worth adding this dependency
# solely to import-check one module, so we leave the conditional disabled.
%bcond qt 0

Name:           python-qtsass
Version:        0.4.0
Release:        %autorelease
Summary:        Compile SCSS files to valid Qt stylesheets

# SPDX
License:        MIT
URL:            https://github.com/spyder-ide/qtsass
# The GitHub archive contains tests, examples, and additional documentation
# that the PyPI sdist lacks.
Source:         %{url}/archive/v%{version}/qtsass-%{version}.tar.gz

BuildSystem:            pyproject
%if %{without qt}
BuildOption(check):     -e qtsass.watchers.qt
%endif
BuildOption(install):   -l qtsass

BuildArch:      noarch

# Remove useless shebang lines
# https://github.com/spyder-ide/qtsass/pull/76
Patch:          %{url}/pull/76.patch
# In tests, don’t assume Python is called python
# https://github.com/spyder-ide/qtsass/pull/77
Patch:          %{url}/pull/77.patch

# Selected test dependencies from requirements/dev.txt; most entries in that
# file are for linters, code coverage, etc.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist flaky}

%if %{with qt}
BuildRequires:  %{py3_dist PyQt5}
%endif

BuildRequires:  help2man

%global common_description %{expand:
SASS brings countless amazing features to CSS. Besides being used in web
development, CSS is also the way to stylize Qt-based desktop applications.
However, Qt’s CSS has a few variations that prevent the direct use of SASS
compiler.

The purpose of this tool is to fill the gap between SASS and Qt-CSS by handling
those variations.}


%description %{common_description}

%package -n python3-qtsass
Summary:        %{summary}

%description -n python3-qtsass %{common_description}


%install -a
install -d '%{buildroot}%{_mandir}/man1'
# Building the man page in %%install instead of %%build is a little weird, but
# we need to use the generated entry point from the buildroot.
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/qtsass.1' \
    '%{buildroot}%{_bindir}/qtsass'


%check -a
%pytest -v


%files -n python3-qtsass -f %{pyproject_files}
%doc AUTHORS.md
%doc CHANGELOG.md
%doc README.md
%doc examples/

%{_bindir}/qtsass
%{_mandir}/man1/qtsass.1*


%changelog
%autochangelog
