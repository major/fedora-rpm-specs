%bcond tests 1

Name:           python-scooby
Version:        0.10.0
Release:        %autorelease
Summary:        A Great Dane turned Python environment detective

License:        MIT
URL:            https://github.com/banesullivan/scooby
# The GitHub archive contains tests; the PyPI sdist lacks them.
Source0:        %{url}/archive/v%{version}/scooby-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        scooby.1

# In tests, use sys.executable instead of assuming "python"
# https://github.com/banesullivan/scooby/pull/120
Patch:          %{url}/pull/120.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  /usr/bin/time
%endif

%global common_description %{expand:
This is a lightweight tool for easily reporting your Python environment’s
package versions and hardware resources.}

%description %{common_description}


%package -n python3-scooby
Summary:        %{summary}

# We cannot package the “cpu” extra because it requires python3dist(mkl), which
# is proprietary software. However, python3dist(psutil), which it also
# requires, adds additional detail to scooby’s reports independent of
# python3dist(mkl), so we add it as a weak dependency.
BuildRequires:  %{py3_dist psutil}
Recommends:     %{py3_dist psutil}

%description -n python3-scooby %{common_description}


%prep
%autosetup -n scooby-%{version} -p1

# - Omit mkl from the test dependencies because it is proprietary
# - Omit pyvips, which is not packaged (upstream CI lacks it too)
# - Omit no_version, which is not packaged; it is just a demonstration of a
#   package without a __version__. Without this, we must skip two tests; that
#   seems a reasonable price to pay in order to avoid packaging something which
#   is merely “for demonstration purposes.”
# - https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^(mkl|pyvips|no_version|pytest-cov)\b/# &/' requirements_test.txt


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
# We cannot package (nor generate BR’s from) the “cpu” extra because it
# requires python3dist(mkl), which is proprietary software.
%pyproject_buildrequires %{?with_tests:requirements_test.txt}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l scooby
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
%pyproject_check_import
%if %{with tests}
# These require the no_version package; see notes in %%prep.
k="${k-}${k+ and }not test_get_version"
k="${k-}${k+ and }not test_tracking"
# This requires pyvips to be installed *without* libvips, as it is in upstream
# CI; we would have both if we had pyvips, so this test makes no sense for us.
# See also the comments in the source of the test.
k="${k-}${k+ and }not test_import_os_error"
# Import performance test may fail flakily or on slower hardware
k="${k-}${k+ and }not test_import_time"

%pytest -k "${k-}"
%endif


%files -n python3-scooby -f %{pyproject_files}
%doc README.md

%{_bindir}/scooby
%{_mandir}/man1/scooby.1*


%changelog
%autochangelog
