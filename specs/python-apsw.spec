# https://rogerbinns.github.io/apsw/about.html#apsw-and-sqlite-versions
%global sqlite_version 3.50.4

Name:               python-apsw
Version:            %{sqlite_version}.0
Release:            %autorelease
Summary:            Another Python SQLite Wrapper
License:            any-OSI
URL:                https://github.com/rogerbinns/apsw
Source:             %{pypi_source apsw}

BuildRequires:      gcc
BuildRequires:      python3-devel
BuildRequires:      sqlite-devel >= %{sqlite_version}

%global _description %{expand:
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.}


%description %_description


%package -n python3-apsw
Summary:            Another Python SQLite Wrapper


%description -n python3-apsw %_description


%prep
%autosetup -n apsw-%{version} -p1

# The PyPI sdist includes configuration file with the fetch option enabled,
# which would try to download the SQLite amalgamation during the build.  To
# avoid that, and to enable extension loading, we'll overwrite that
# configuration with our own.
cat > setup.apsw << EOF
[build]
enable = load_extension
EOF


%generate_buildrequires
%pyproject_buildrequires


%build
# Build the wheel and the test extension, which is used during %%check
%pyproject_wheel -C--global-option=build_test_extension


%install
%pyproject_install
%pyproject_save_files -l apsw


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m apsw.tests -v


%files -n python3-apsw -f %{pyproject_files}
%{_bindir}/apsw


%changelog
%autochangelog
