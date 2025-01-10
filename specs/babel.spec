# There is some bootstrapping involved when upgrading Python 3
# First of all we need babel (this package) to use sphinx
# And pytest is at this point not yet ready
%bcond bootstrap 0

# Since babel 2.12, the pytz dependency is optional.
# However, pytz is preferred when installed.
# Running tests with pytz is optional as well.
# We don't want to pull pytz into ELN/RHEL just to test integration with it,
# but we don't want to ship babel in Fedora with an untested default,
# so we make the dependency conditional.
# Ideally, the dependency would be conditional on pytz availability in the repo,
# but that's not possible in 2023 yet.
# Additionally, the date/time tests require freezegun, which is unwanted in RHEL.
%bcond datetime_tests %{undefined rhel}

Name:           babel
Version:        2.16.0
Release:        %autorelease
Summary:        Tools for internationalizing Python applications

License:        BSD-3-Clause
URL:            https://babel.pocoo.org/
Source:         %{pypi_source}

# https://github.com/python-babel/babel/pull/1155
Patch:          0001-Adjust-docs-conf.py-to-add-compatibility-with-sphinx.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{without bootstrap}
BuildRequires:  coreutils
# The Python test dependencies are not generated from tox.ini,
# because it would require complex patching to be usable
# and becasue we want to avoid the tox dependency in ELN/RHEL.
BuildRequires:  python3-pytest
%if %{with datetime_tests}
BuildRequires:  python3-freezegun
# The pytz tests are skipped when pytz is missing
BuildRequires:  python3-pytz
%endif
# build the documentation
BuildRequires:  make
BuildRequires:  python3-sphinx
%endif
Requires:       python3-babel = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.


%package -n python3-babel
Summary:        Library for internationalizing Python applications

%description -n python3-babel
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%if %{without bootstrap}
%package doc
Summary:        Documentation for Babel
%py_provides    python3-babel-doc

%description doc
Documentation for Babel
%endif

%prep
%autosetup -p1 -n babel-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

BUILDDIR="$PWD/built-docs"
rm -rf "$BUILDDIR"

%if %{without bootstrap}
pushd docs
make \
    SPHINXBUILD=sphinx-build-3 \
    BUILDDIR="$BUILDDIR" \
    html man
popd
rm -f "$BUILDDIR/html/.buildinfo"
%endif

%install
%pyproject_install
%pyproject_save_files babel

%if %{without bootstrap}
install -D -m 0644 built-docs/man/babel.1 %{buildroot}%{_mandir}/man1/pybabel.1
%endif

%check
export TZ=UTC
%pyproject_check_import
%if %{without bootstrap}
# The deselected doctests fail without pytz when run during Eastern Daylight Time
# https://github.com/python-babel/babel/issues/988
# The ignored files use freezegun
%pytest %{!?with_datetime_tests:\
  -k "not (babel.dates.format_time or babel.dates.get_timezone_name)" \
  --ignore tests/test_dates.py --ignore tests/messages/test_frontend.py}
%endif

%files
%doc CHANGES.rst AUTHORS
%{_bindir}/pybabel

%if %{without bootstrap}
%{_mandir}/man1/pybabel.1*
%endif

%files -n python3-babel -f %{pyproject_files}

%if %{without bootstrap}
%files doc
%license LICENSE
%doc built-docs/html/*
%endif

%changelog
%autochangelog
