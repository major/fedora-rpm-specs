%bcond tests 1

%global forgeurl https://github.com/gugarosa/opytimark

Name:           python-opytimark
Version:        1.0.8
Release:        %autorelease
Summary:        Python implementation of Optimization Benchmarking Functions

%forgemeta

License:        Apache-2.0
URL:            https://github.com/gugarosa/opytimark
Source:         %forgesource

# Move dev dependencies
# https://github.com/gugarosa/opytimark/pull/2
Patch:          %{url}/pull/2.patch
# fix(tests): Fixes rounding for Python 3.8 and 3.9.
# https://github.com/gugarosa/opytimark/commit/7f5f97e9d042d9b9d9acf1cdcc9738fe99c792c5
Patch:          %{url}/commit/7f5f97e9d042d9b9d9acf1cdcc9738fe99c792c5.patch
# Fix warning (description_file)
# https://github.com/gugarosa/opytimark/commit/25d9adb743c8483c0f2ae41f56c8872fdd44977f
Patch:          %{url}/commit/25d9adb743c8483c0f2ae41f56c8872fdd44977f.patch
# Reduce exact floating-point equality comparisons in the tests
# https://github.com/gugarosa/opytimark/pull/4
#
# Fixes:
#
# python-opytimark fails to build with Python 3.14: test_jennrich_sampson:
# assert np.float64(124.36218236181412) == 124.36218236181409
# https://bugzilla.redhat.com/show_bug.cgi?id=2345715
Patch:          %{url}/pull/4.patch

BuildArch:      noarch

%global desc %{expand:
This package provides straightforward implementation of benchmarking functions
for optimization tasks.}

%description %{desc}

%package -n python3-opytimark
Summary:        %{summary}
BuildRequires:      python3-devel

%if %{with tests}
BuildRequires:      %{py3_dist pytest}
%endif

%description -n python3-opytimark %{desc}

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l opytimark

%check
%if %{with tests}
# All of these require network access.
k="${k-}${k+ and }not test_year"
k="${k-}${k+ and }not test_decorator"
k="${k-}${k+ and }not test_loader"
k="${k-}${k+ and }not cec_benchmark"
%pytest -k "${k-}"
%endif

%files -n python3-opytimark -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
