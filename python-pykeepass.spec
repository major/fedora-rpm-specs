Name:           python-pykeepass
Version:        4.0.7
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
# Remove shebang line from pykeepass/deprecated.py
# https://github.com/libkeepass/pykeepass/pull/377
Patch:          %{url}/pull/377.patch
# Fix missing pykeepass.kdbx_parsing when built with modern tools
# https://github.com/libkeepass/pykeepass/pull/378
Patch:          %{url}/pull/378.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel

%global common_description %{expand:
This library allows you to write entries to a KeePass database.}

%description %{common_description}


%package -n     python3-pykeepass
Summary:        %{summary}
 
%description -n python3-pykeepass %{common_description}


%prep
%autosetup -n pykeepass-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pykeepass


%check
# This is worthwhile even though we run the tests; tests did not catch a
# missing pykeepass.kdbx_parsing package in the 4.0.7 release, but an import
# check would have.
%pyproject_check_import

%{python3} -m unittest discover -s tests -v


%files -n python3-pykeepass -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
