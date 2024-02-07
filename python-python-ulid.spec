# Note that this is https://pypi.org/project/python-ulid/; the canonical
# project name ulid, https://pypi.org/project/ulid/, belongs to a different and
# apparently defunct project. See
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# and the issue filed upstream:
#   Possible confusion with the "ulid" package
#   https://github.com/mdomke/python-ulid/issues/13
Name:           python-python-ulid
Version:        2.2.0
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

BuildArch:      noarch

BuildRequires:  python3-devel
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

%if 0%{?fc39} || 0%{?fc38}
# Conflicts with a binary provided by golang-github-oklog-ulid
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_binary_name_conflicts
# Discussion opened with both upstreams in:
#   Multiple conflicting command-line tools called ulid exist
#   https://github.com/mdomke/python-ulid/issues/14
#   Multiple conflicting command-line tools called ulid exist
#   https://github.com/oklog/ulid/issues/111
# Resolved in F40+ by renaming the other package’s binary to ulid-go:
#   https://src.fedoraproject.org/rpms/golang-github-oklog-ulid/pull-request/1
# This package is only planned for F40+, but we keep this conditional Conflicts
# in case it gets built for F39 or F38 after all.
Conflicts:      golang-github-oklog-ulid
%endif

%description -n python3-python-ulid %{common_description}


%prep
%autosetup -n python_ulid-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ulid

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


%check
%pytest -v


%files -n python3-python-ulid -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst
%{_bindir}/ulid
%{_mandir}/man1/ulid{,-*}.1*


%changelog
%autochangelog
