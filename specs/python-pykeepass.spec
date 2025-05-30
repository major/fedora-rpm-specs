
Name:           python-pykeepass
Version:        4.1.1.post1
Release:        %autorelease
Epoch:          1
Summary:        Python library to interact with keepass databases

# The entire source is GPL-3.0-only, except:
#
# MIT:
#   pykeepass/kdbx_parsing/twofish.py
License:        GPL-3.0-only AND MIT
URL:            https://github.com/libkeepass/pykeepass
# The GitHub archive has tests; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/pykeepass-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install):   -l pykeepass

BuildArch:      noarch
 
BuildRequires:  tomcli

%global common_description %{expand:
This library allows you to write entries to a KeePass database.}

%description %{common_description}


%package -n     python3-pykeepass
Summary:        %{summary}
 
%description -n python3-pykeepass %{common_description}


%prep
%autosetup -n pykeepass-%{version} -p1

# This is actually a documentation dependency:
tomcli set pyproject.toml lists delitem project.optional-dependencies.test pdoc


%check -a
%{py3_test_envvars} %{python3} -m unittest discover -s tests -v


%files -n python3-pykeepass -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.md


%changelog
%autochangelog
