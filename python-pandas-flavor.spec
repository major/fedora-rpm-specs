# We must package from a GitHub archive to get the tests, but upstream does not
# tag releases. We must therefore package from a snapshot corresponding to the
# PyPI release.
%global commit f9308140d559ef1cb80587dedf6a7e32ca1f0b67
%global snapdate 20220417

Name:           python-pandas-flavor
Version:        0.3.0^%{snapdate}git%(echo '%{commit}' | cut -b -7)
Release:        %autorelease
Summary:        The easy way to write your own flavor of Pandas

License:        MIT
URL:            https://github.com/Zsailer/pandas_flavor
Source0:        %{url}/archive/%{commit}/pandas_flavor-%{commit}.tar.gz

# Update lazy-loader dependency to ≥0.1
# https://github.com/Zsailer/pandas_flavor/pull/25
Patch:          %{url}/pull/25.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# This is easier than running the tests with the unittest module.
BuildRequires:  python3dist(pytest)

%global common_description %{expand: \
The easy way to write your own flavor of Pandas
-----------------------------------------------

Pandas 0.23 added a (simple) API for registering accessors with Pandas objects.

Pandas-flavor extends Pandas’ extension API by:

  1. adding support for registering methods as well.
  2. making each of these functions backwards compatible with older versions of
     Pandas.

What does this mean?
--------------------

It is now simpler to add custom functionality to Pandas DataFrames and Series.

Import this package. Write a simple python function. Register the function
using one of the following decorators.

Why?
----

Pandas is super handy. Its general purpose is to be a "flexible and powerful
data analysis/manipulation library".

Pandas Flavor allows you add functionality that tailors Pandas to specific
fields or use cases.

Maybe you want to add new write methods to the Pandas DataFrame? Maybe you want
custom plot functionality? Maybe something else?}

%description
%{common_description}


%package -n python3-pandas_flavor
Summary:        %{summary}

%description -n python3-pandas_flavor
%{common_description}


%prep
%autosetup -n pandas_flavor-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pandas_flavor


%check
%pytest
# The tests are minimal enough that we do an import “smoke test” as well.
%pyproject_check_import


%files -n python3-pandas_flavor -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.md
%doc docs/_images/example.png


%changelog
%autochangelog
