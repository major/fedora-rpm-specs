%global common_description %{expand:
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python.  Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.  A web spider that wants to fetch lots of
pages in parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor monitoring
multiple subprocesses... that sort of thing.  Compared to other libraries, Trio
attempts to distinguish itself with an obsessive focus on usability and
correctness.  Concurrency is complicated; we try to make it easy to get things
right.}


Name:           python-trio
Version:        0.28.0
Release:        %autorelease
Summary:        A friendly Python library for async concurrency and I/O
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/trio
Source:         %pypi_source trio

BuildArch:      noarch


%description %{common_description}


%package -n python3-trio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-trio %{common_description}


%prep
%autosetup -p 1 -n trio-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l trio


%check
# https://github.com/python-trio/trio/issues/2863
# https://docs.pytest.org/en/stable/explanation/goodpractices.html#tests-as-part-of-application-code
%pytest --pyargs trio --verbose --skip-optional-imports


%files -n python3-trio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
