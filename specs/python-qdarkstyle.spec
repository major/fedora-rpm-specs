# Per the Web Assets guidelines, we should try to recompile at least .qss files
# (which are CSS) as part of the build. Historically, this was absolutely
# required (“It is not acceptable to include pre-compiled CSS in Fedora
# packages.”), but even though the requirement has been relaxed
# (https://pagure.io/fesco/issue/3269), recompiling is still best practice
# where it is feasible.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Web_Assets/#_css
%bcond recompile_assets 1

Name:           python-qdarkstyle
Version:        3.2.3
Release:        %autorelease
Summary:        The most complete dark/light style sheet for C++/Python and Qt applications

# From README.rst:
#   This project is licensed under the MIT license. Images contained in this
#   project is licensed under CC-BY license.
# Therefore, the entire source is (SPDX) MIT except for those files with .png
# or .svg extensions, which are CC-BY-4.0.
License:        MIT AND CC-BY-4.0
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
# The PyPI sdist does not have all of the files (such as SVG files) needed to
# rebuild the generated assets.
Source0:        %{url}/archive/v.%{version}/QDarkStyleSheet-v.%{version}.tar.gz
# Man pages hand-written for Fedora in groff_man(7) format based on --help.
Source10:       qdarkstyle.1
Source11:       qdarkstyle.example.1
Source12:       qdarkstyle.utils.1

# Drop PySide2 dependency from the example in Python 3.12+
# https://github.com/ColinDuquesnoy/QDarkStyleSheet/pull/355
Patch:          %{url}/pull/355.patch
# Improvements to example description
# https://github.com/ColinDuquesnoy/QDarkStyleSheet/pull/356
Patch:          %{url}/pull/356.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x develop,example
BuildOption(install):   -l qdarkstyle

BuildArch:      noarch
 
BuildRequires:  hardlink

# This is required for the error-reporting option in the CLI. We have it as a
# weak dependency, so we make it a BR to ensure we don’t end up with an
# uninstallable package.
BuildRequires:  %{py3_dist helpdev}

# Selected dependencies from req-test.txt (which is mostly unwanted linters,
# coverage tools, etc.)
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
The most complete dark/light style sheet for Qt applications (Qt4, Qt5, PySide,
PySide2, PyQt4, PyQt5, QtPy, PyQtGraph, Qt.Py) for Python and C++.}

%description %{common_description}


%package -n python3-qdarkstyle
Summary:        %{summary}
 
Recommends:     python3-qdarkstyle+develop = %{version}-%{release}
Recommends:     %{py3_dist helpdev}

%description -n python3-qdarkstyle %{common_description}


%pyproject_extras_subpkg -n python3-qdarkstyle example
%{_bindir}/qdarkstyle.example
%{_mandir}/man1/qdarkstyle.example.1*


%pyproject_extras_subpkg -n python3-qdarkstyle develop
%{_bindir}/qdarkstyle.utils
%{_mandir}/man1/qdarkstyle.utils.1*


%prep -a
%if %{with recompile_assets}
rm -vf qdarkstyle/*/*style.{qrc,qss} qdarkstyle/*/_variables.scss
%endif

# We helped upstream clean up shebangs in
# https://github.com/ColinDuquesnoy/QDarkStyleSheet/pull/333, but upstream
# seems to prefer to have some executables (with shebang lines) inside the
# qdarkstyle package directory. Since executable permissions will be removed
# when installing into site-packages, we should remove the shebangs too; they
# won’t make sense anymore.
#
# The find-then-modify pattern preserves mtimes on sources that did not need to
# be modified.
find 'qdarkstyle' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%build -p
%if %{with recompile_assets}
# QT_QPA_PLATFORM=offscreen keeps us from needing something like xvfb-run,
# xwfb-run, or wlheadless-run.
# The upstream default for this script is to compile with pyside6, but since
# 3.2.2, upstream has recompiled with pyqt5 instead in practice.
QT_QPA_PLATFORM=offscreen PYTHONPATH="${PWD}" %{python3} -m qdarkstyle.utils \
    --create 'pyqt5'
%endif


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'

# Some files, particularly icons, are duplicated across themes and can be
# hardlinked to save space.
hardlink -c -v '%{buildroot}%{python3_sitelib}/qdarkstyle/'


%check -a
%pytest


%files -n python3-qdarkstyle -f %{pyproject_files}
%doc CHANGES.rst
%doc README.rst
%{_bindir}/qdarkstyle
%{_mandir}/man1/qdarkstyle.1*


%changelog
%autochangelog
