# Note that this is https://pypi.org/project/python-ulid/; the canonical
# project name ulid, https://pypi.org/project/ulid/, belongs to a different and
# apparently defunct project. See
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# and the issue filed upstream:
#   Possible confusion with the "ulid" package
#   https://github.com/mdomke/python-ulid/issues/13
Name:           python-python-ulid
Version:        3.0.0
Release:        %autorelease
Summary:        Universally unique lexicographically sortable identifier

# SPDX
License:        MIT
URL:            https://github.com/mdomke/python-ulid
Source0:        %{pypi_source python_ulid}
# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       ulid.1
Source11:       ulid-build.1
Source12:       ulid-show.1

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x pydantic
BuildOption(install):   -l ulid

BuildArch:      noarch

# Test dependencies are defined in [envs.default] in hatch.toml. They have
# tight version pins and include coverage tools; it is easier to maintain a
# manual list.
BuildRequires:  %{py3_dist freezegun}
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
A ULID is a universally unique lexicographically sortable identifier. It is

  * 128-bit compatible with UUID
  * 1.21e+24 unique ULIDs per millisecond
  * Lexicographically sortable!
  * Canonically encoded as a 26 character string, as opposed to the 36
    character UUID
  * Uses Crockford's base32 for better efficiency and readability (5 bits per
    character)
  * Case insensitive
  * No special characters (URL safe)

For more information have a look at the original specification,
https://github.com/alizain/ulid#specification.}
# this is here to fix vim's syntax highlighting

%description %{common_description}


%package -n python3-python-ulid
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-ulid

%description -n python3-python-ulid %{common_description}


%pyproject_extras_subpkg -n python3-python-ulid pydantic


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


%check -a
%pytest -v


%files -n python3-python-ulid -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst
%{_bindir}/ulid
%{_mandir}/man1/ulid{,-*}.1*


%changelog
%autochangelog
