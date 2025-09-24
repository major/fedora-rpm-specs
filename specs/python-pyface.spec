# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

%global modname pyface

Name:           python-%{modname}
Version:        8.0.0
Release:        %autorelease
Summary:        Generic User Interface objects

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later and LicenseRef-Fedora-Public-Domain
URL:            https://github.com/enthought/pyface
# Current release is missing files
# https://github.com/enthought/pyface/issues/98
#Source0:        http://www.enthought.com/repo/ets/pyface-%{version}.tar.gz
Source0:        https://github.com/enthought/pyface/archive/%{version}/pyface-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  glibc-langpack-en

%description
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel >= 3.9

%description -n python%{python3_pkgversion}-%{modname}
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

Python 3 version.

%package doc
Summary:        Documentation for pyface

%description doc
Documentation and examples for pyface.

%package -n python%{python3_pkgversion}-%{modname}-qt
Summary:        Qt backend placeholder for pyface
# These are not picked up automatically
BuildRequires:  python%{python3_pkgversion}-pillow-qt
BuildRequires:  python%{python3_pkgversion}-pyqt6
Requires:       python%{python3_pkgversion}-%{modname} = %{version}-%{release}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Provides:       python%{python3_pkgversion}-%{modname}-backend

%description -n python%{python3_pkgversion}-%{modname}-qt
Qt backend placeholder for pyface.

%prep
%autosetup -p1 -n pyface-%{version}
# Tests in test_python_shell lead to core dump. We need pyface for bootstrap
# sequence of Python 3.10, thus they are temporarily disabled
# This can be removed once fixed.
# Downstream report: https://bugzilla.redhat.com/show_bug.cgi?id=1902175
rm pyface/tests/test_python_shell.py

%if %{with bootstrap}
# remove tests using traitsui
rm pyface/workbench/tests/test_workbench_window.py
rm pyface/dock/tests/test_dock_sizer.py
%endif


# file not utf-8
for f in image_LICENSE_{Eclipse,OOo}.txt
do
  iconv -f iso8859-1 -t utf-8 ${f} > ${f}.conv && mv -f ${f}.conv ${f}
done
# Use the standard lib function in 3.9+
find -name \*.py -exec sed -i -e s/importlib_resources/importlib.resources/g {} +
sed -i -e '/"importlib-[^"]*",/d' pyface/__init__.py
sed -i -e /importlib./d etstool.py


%generate_buildrequires
%pyproject_buildrequires -x pillow -x pyqt5 -x pyqt6 %{!?with_bootstrap:-x traitsui} -x wx


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyface

%check
# Needed for wx tests
export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONUNBUFFERED=1
# Run in a separate directory so we only see the installed package
mkdir -p test
cd test
status=0
# pyside6 is not packaged
for toolkit in null pyqt5 pyqt6 wx # pyside6
do
  # By default, fail build if tests fail
  fail=1
  # Decent default, overridded later if needed
  export QT_API=$toolkit
  case $toolkit in
    pyside6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    # pyqt5 test fails on s390x - https://github.com/enthought/pyface/issues/1247
    # pytq5 test fails - https://github.com/enthought/pyface/issues/1255
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    # pyqt6 is failing - https://github.com/enthought/pyface/issues/1248
    # https://github.com/enthought/pyface/issues/1250
    pyqt6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    # wx and null currently failing - https://github.com/enthought/pyface/issues/1244
    wx) export ETS_TOOLKIT="wx"; unset QT_API; export EXCLUDE_TESTS="qt"; fail=0;;
    null) export ETS_TOOLKIT="null"; unset QT_API; export EXCLUDE_TESTS="(wx|qt)"; fail=0;;
  esac
  # Adding -f can be helpful to debug missing components or other issues when the test crashes
  xvfb-run %{__python3} -Xfaulthandler -s -m unittest discover -v pyface || status=$(( $status + $fail ))
done
exit $status
 
%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%license image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst

%files doc
%doc docs/DockWindowFeature.pdf examples

%files -n python%{python3_pkgversion}-%{modname}-qt

%changelog
%autochangelog
