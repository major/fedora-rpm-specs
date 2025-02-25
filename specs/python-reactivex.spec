Name:           python-reactivex
Version:        4.0.4
Release:        %autorelease
Summary:        API for asynchronous programming with observable streams

License:        MIT
URL:            https://github.com/ReactiveX/RxPY

# Use two sources.
# Only PyPi sources contains a version number in pyproject files
# Only github archive contains tests
Source0:        %{pypi_source reactivex}
Source1:        %{url}/archive/v%{version}/RxPy-%{version}.tar.gz

# python 3.14 support rhbz#2327987
#               https://github.com/ReactiveX/RxPY/pull/716
Patch0:         backport-716.patch

# Part of       https://github.com/ReactiveX/RxPY/pull/722
Patch1:         https://github.com/ReactiveX/RxPY/commit/9a6a5cddc907120ff521a2938415527bfd03e5ef.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies:
BuildRequires: python3dist(pytest)

%global _description\
ReactiveX for Python (RxPY) is a library for composing asynchronous and\
event-based programs using observable sequences and pipable query\
operators in Python. Using Rx, developers represent asynchronous\
data streams with Observables, query asynchronous data streams\
using operators, and parameterize concurrency in data/event\
streams using Schedulers.

%description %_description

%package -n python3-reactivex
Summary: %{summary}

%description -n python3-reactivex %_description


%prep
%setup -n reactivex-%{version}
tar -xf %{SOURCE1} RxPY-%{version}/tests --strip-components=1
%patch -P 0 -p1
%patch -P 1 -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files reactivex


%check
%pytest
%pyproject_check_import


%files -n python3-reactivex -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
%autochangelog

