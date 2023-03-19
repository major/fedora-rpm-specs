%global srcname trailrunner

%global common_description %{expand:
trailrunner is a simple library for walking paths on the filesystem, and
executing functions for each file found. trailrunner obeys project level
.gitignore files, and runs functions on a process pool for increased
performance. trailrunner is designed for use by linting, formatting, and other
developer tools that need to find and operate on all files in project in a
predictable fashion with a minimal API.}

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Walk paths and run things

License:        MIT
URL:            https://trailrunner.omnilib.dev/
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
%{common_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{common_description}


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
%pytest -v trailrunner/tests/*


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
%autochangelog
