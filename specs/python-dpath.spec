Name:           python-dpath
Version:        2.2.0
Release:        %autorelease
Summary:        Filesystem-like pathing and searching for dictionaries

License:        MIT
URL:            https://github.com/akesterson/dpath-python
Source:         %{url}/archive/v%{version}/dpath-python-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:    pyproject
BuildOption(install):   -l dpath
BuildOption(generate_buildrequires): -t

%global common_description %{expand:
A python library for accessing and searching dictionaries via /slashed/paths
ala xpath.

Basically it lets you glob over a dictionary as if it were a filesystem. It
allows you to specify globs (ala the bash eglob syntax, through some advanced
fnmatch.fnmatch magic) to access dictionary elements, and provides some
facility for filtering those results.}

%description %{common_description}


%package -n python3-dpath
Summary:        %{summary}

%description -n python3-dpath %{common_description}


%check -a
%tox -- -- -v


%files -n python3-dpath -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
