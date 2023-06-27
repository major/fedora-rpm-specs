%bcond_without docs

%global srcname trailrunner

%global common_description %{expand:
trailrunner is a simple library for walking paths on the filesystem, and
executing functions for each file found. trailrunner obeys project level
.gitignore files, and runs functions on a process pool for increased
performance. trailrunner is designed for use by linting, formatting, and other
developer tools that need to find and operate on all files in project in a
predictable fashion with a minimal API.}

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Walk paths and run things

License:        MIT
URL:            https://trailrunner.omnilib.dev/
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
%if %{with docs}
BuildRequires:  python3-docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-mdinclude)
BuildRequires:  sed
%endif

%description
%{common_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{common_description}


%if %{with docs}
%package        doc
Summary:        %{name} documentation
Requires:       python3-docs

%description    doc
Documentation for %{name}.
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest -v trailrunner/tests/*


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md


%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif


%changelog
%autochangelog
