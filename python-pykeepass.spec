Name:           python-pykeepass
Version:        4.0.4
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

# Remove excessive byte-swapping in pytwofish.py
# https://github.com/libkeepass/pykeepass/pull/336
#
# Fixes:
#
# Tests fail on big-endian platform (s390x)
# https://github.com/libkeepass/pykeepass/issues/332
Patch:          %{url}/pull/336.patch

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

# Convert exact-version pins, which we cannot respect, to lower bounds.
sed -r -i 's/==/>=/' requirements.txt


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pykeepass


%check
%{python3} -m unittest discover -s tests -v


%files -n python3-pykeepass -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
