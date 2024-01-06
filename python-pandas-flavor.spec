Name:           python-pandas-flavor
Version:        0.6.0
Release:        %autorelease
Summary:        The easy way to write your own flavor of Pandas

# SPDX
License:        MIT
URL:            https://github.com/Zsailer/pandas_flavor
Source0:        %{url}/archive/v%{version}/pandas_flavor-%{version}.tar.gz

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

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


%package -n python3-pandas-flavor
Summary:        %{summary}

# Renamed binary package to match project canonical name.
Provides:       python3-pandas_flavor = %{version}-%{release}
Obsoletes:      python3-pandas_flavor < 0.3.0^20220417gitf930814-7

%description -n python3-pandas-flavor
%{common_description}


%prep
%autosetup -n pandas_flavor-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pandas_flavor


%check
%pytest
# The tests are minimal enough that we do an import “smoke test” as well.
%pyproject_check_import


%files -n python3-pandas-flavor -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%doc docs/_images/example.png


%changelog
%autochangelog
