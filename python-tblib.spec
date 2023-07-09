%global srcname tblib

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Traceback serialization library

License:        BSD-2-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

%global _description %{expand:
Traceback serialization library that allows you to:
  * Pickle tracebacks and raise exceptions with pickled tracebacks in different
    processes. This allows better error handling when running code over
    multiple processes (imagine multiprocessing, billiard, futures, celery,
    etc).
  * Parse traceback strings and raise with the parsed tracebacks.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(twisted)

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# doctest is disabled on Python 3.11+
# due to changes in tracebacks README.rst needs to be adapted
# upstream report: https://github.com/ionelmc/python-tblib/issues/64
%{pytest} -ra tests \
    %if v"0%{?python3_version}" <= v"3.10"
    README.rst
    %endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
