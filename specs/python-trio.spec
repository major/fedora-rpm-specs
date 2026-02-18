Name:           python-trio
Version:        0.33.0
Release:        %autorelease
Summary:        A friendly Python library for async concurrency and I/O
License:        Apache-2.0 OR MIT
BuildArch:      noarch
URL:            https://github.com/python-trio/trio
Source:         %{pypi_source trio}

%global common_description %{expand:
The Trio project aims to produce a production-quality, permissively licensed,
async/await-native I/O library for Python.  Like all async libraries, its main
purpose is to help you write programs that do multiple things at the same time
with parallelized I/O.  A web spider that wants to fetch lots of pages in
parallel, a web server that needs to juggle lots of downloads and websocket
connections simultaneously, a process supervisor monitoring multiple
subprocesses... that sort of thing.  Compared to other libraries, Trio attempts
to distinguish itself with an obsessive focus on usability and correctness.
Concurrency is complicated; we try to make it easy to get things right.}


%description %{common_description}


%package -n python3-trio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  tomcli


%description -n python3-trio %{common_description}


%prep
%autosetup -p 1 -n trio-%{version}

# Remove useless shebangs in files that will be installed without executable
# permission. The pattern of selecting files before modifying them keeps us
# from unnecessarily discarding the original mtimes on unmodified files.
find src/trio -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

# Python 3.15: DeprecationWarning about fork+threads in
# test_clear_thread_cache_after_fork
# https://github.com/python-trio/trio/issues/3355
# https://bugzilla.redhat.com/show_bug.cgi?id=2414804
tomcli set pyproject.toml append tool.pytest.ini_options.filterwarnings \
    'ignore:This process :DeprecationWarning'


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
%pytest \
    --pyargs trio \
    --verbose \
    --skip-optional-imports


%files -n python3-trio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
