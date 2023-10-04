# PySide2 is broken with Python 3.12; do not support it on Fedora 39 and later.
#
# python-pyside2 fails to build with Python 3.12: error: use of undeclared
#     identifier 'PyUnicode_AS_UNICODE'
# https://bugzilla.redhat.com/show_bug.cgi?id=2155447
#
# python3-shiboken2-devel wants python < 3.11
# https://bugzilla.redhat.com/show_bug.cgi?id=2149820
#
# F39FailsToInstall: python3-pyside2, python3-shiboken2,
#     python3-shiboken2-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=2220452
#
# Bug python-pyside2: FTBFS in Fedora rawhide/f39
# https://bugzilla.redhat.com/show_bug.cgi?id=2226300
%bcond pyside2 %{expr:0%{?fedora} < 39}

# Per the Web Assets guidelines, we really need to recompile at least .qss
# files (which are CSS) as part of the build (“It is not acceptable to include
# pre-compiled CSS in Fedora packages.”).
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Web_Assets/#_css
%bcond recompile_assets 1

Name:           python-qdarkstyle
Version:        3.1
Release:        %autorelease
Summary:        The most complete dark/light style sheet for C++/Python and Qt applications

License:        MIT
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
# The PyPI sdist does not have all of the files (such as SVG files) needed to
# rebuild the generated assets.
Source:         %{url}/archive/v%{version}/QDarkStyleSheet-%{version}.tar.gz

# Shebang cleanup
# https://github.com/ColinDuquesnoy/QDarkStyleSheet/pull/333
Patch0:         %{url}/pull/333.patch

# Downstream-only for now, in hopes that PySide2 being broken on Python 3.12
# can be fixed:
#
# Patch out the PySide2 dependency from the example
Patch100:       0001-Patch-out-the-PySide2-dependency-from-the-example.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Convert setup.py from CRNL so we can patch it.
BuildRequires:  dos2unix

%if %{with recompile_assets}
BuildRequires:  xorg-x11-server-Xvfb
%endif

# TODO: The generated man pages are a bit messy, with less than ideal
# formatting and some text markup leaking through. Since the CLI doesn’t change
# much, it might be worth writing a set by hand.
BuildRequires:  help2man

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


%prep
%autosetup -n QDarkStyleSheet-%{version} -N
%autopatch -M 99 -p1
%if %{without pyside2}
dos2unix --keepdate setup.py
%autopatch -m 100 -p1
%endif

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


%generate_buildrequires
%pyproject_buildrequires -x develop,example


%build
%if %{with recompile_assets}
xvfb-run -a env PYTHONPATH="${PWD}" %{python3} -m qdarkstyle.utils
%endif
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files qdarkstyle

# Generating man pages in %%install rather than %%build is not ideal, but it
# allows us to use the installed entry points.
install -d '%{buildroot}%{_mandir}/man1'
(
  export PYTHONPATH='%{buildroot}%{python3_sitelib}'
  help2man --no-info --output='%{buildroot}%{_mandir}/man1/qdarkstyle.1' \
      '%{buildroot}%{_bindir}/qdarkstyle'
  for cmd in 'qdarkstyle.utils' 'qdarkstyle.example'
  do
    help2man --no-info --output="%{buildroot}%{_mandir}/man1/${cmd}.1" \
        --no-discard-stderr --version-string='%{version}' \
        "%{buildroot}%{_bindir}/${cmd}"

  done
)


%check
%pyproject_check_import
# Tests are completely broken (call functions without mandatory arguments!);
# fixed in upstream release 3.1.
# %%pytest


%files -n python3-qdarkstyle -f %{pyproject_files}
%doc AUTHORS.rst
%doc CHANGES.rst
%doc README.rst
%{_bindir}/qdarkstyle
%{_mandir}/man1/qdarkstyle.1*


%changelog
%autochangelog
