%global forgeurl https://github.com/libkeepass/pykeepass
# We package a post-release snapshot with fixes for issues in the 4.1.1
# release:
# - update changelog
# - missing test database
# - remove unsupported type annotation
# - remove more type annotations
%global version0 4.1.1
%global commit0 409be2d416ef5da7697d05a9b8ad3a403bdabb99
%forgemeta

Name:           python-pykeepass
Version:        %forgeversion
Release:        %autorelease
Epoch:          1
Summary:        Python library to interact with keepass databases

# The entire source is GPL-3.0-only, except:
#
# MIT:
#   pykeepass/kdbx_parsing/twofish.py
License:        GPL-3.0-only AND MIT
URL:            %{forgeurl}
# The GitHub archive has tests; the PyPI sdist does not.
Source:         %{forgesource}

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
%forgeautosetup -p1

# This is actually a documentation dependency:
tomcli set pyproject.toml lists delitem project.optional-dependencies.test pdoc


%check -a
%{py3_test_envvars} %{python3} -m unittest discover -s tests -v


%files -n python3-pykeepass -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.md


%changelog
%autochangelog
