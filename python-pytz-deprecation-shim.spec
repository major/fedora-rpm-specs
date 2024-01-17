Name:           python-pytz-deprecation-shim
Version:        0.1.0.post0
Release:        %autorelease
Summary:        Shims to help you safely remove pytz

License:        Apache-2.0
URL:            https://github.com/pganssle/pytz-deprecation-shim
Source:         %{pypi_source pytz_deprecation_shim}

BuildArch:      noarch

BuildRequires:  python3-devel
# Depend on the system tzdata RPM, not the PyPI “tzdata” fallback package
BuildRequires:  tzdata

%global common_description %{expand:
pytz has served the Python community well for many years, but it is no longer
the best option for providing time zones. pytz has a non-standard interface
that is very easy to misuse; this interface was necessary when pytz was
created, because datetime had no way to represent ambiguous datetimes, but this
was solved in Python 3.6, which added a fold attribute to datetimes in PEP 495.
With the addition of the zoneinfo module in Python 3.9 (PEP 615), there has
never been a better time to migrate away from pytz.

However, since pytz time zones are used very differently from a standard
tzinfo, and many libraries have built pytz zones into their standard time zone
interface (and thus may have users relying on the existence of the localize and
normalize methods); this library provides shim classes that are compatible with
both PEP 495 and pytz’s interface, to make it easier for libraries to deprecate
pytz.}

%description %{common_description}


%package -n python3-pytz-deprecation-shim
Summary:        %{summary}

# Depend on the system tzdata RPM, not the PyPI “tzdata” fallback package
Requires:       tzdata

%description -n python3-pytz-deprecation-shim %{common_description}


%prep
%autosetup -n pytz_deprecation_shim-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)(pytest-cov|coverage)\b/\1# \2/' tox.ini

# Depend on the system tzdata RPM, not the PyPI “tzdata” fallback package
sed -r -i '/\btzdata\b/d' setup.cfg


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytz_deprecation_shim


%check
DEFAULT_TEST_POSARGS='' %tox


%files -n python3-pytz-deprecation-shim -f %{pyproject_files}
# pyproject-rpm-macros takes care of the LICENSE file in dist-info, but not
# licenses/LICENSE_APACHE; we manually include both files in %%_licensedir
%license LICENSE
%license licenses/LICENSE_APACHE
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
