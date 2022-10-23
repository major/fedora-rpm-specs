Name:           python-autoprop
Version:        4.1.0
Release:        %autorelease
Summary:        Infer properties from accessor methods

# SPDX
License:        MIT
URL:            https://github.com/kalekundert/autoprop
Source0:        %{pypi_source autoprop}

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
This package provides a library for automatically filling in classes with
properties (e.g. obj.x) corresponding to each accessor method (e.g.
obj.get_x(), obj.set_x()). The biggest reasons to use autoprop are:

  • Less boilerplate than defining properties manually.
  • Sophisticated support for cached properties.}

%description %{common_description}


%package -n python3-autoprop
Summary:        %{summary}

%description -n python3-autoprop %{common_description}


%prep
%autosetup -n autoprop-%{version}

# Patch out coverage dependencies
sed -r -i '/\b(pytest-cov|coveralls)\b/d' pyproject.toml

# Remove useless shebang lines.
#
# Originally sent upstream,
# https://github.com/kalekundert/autoprop/pull/8, but this author wants to keep
# them; see:
# https://github.com/kalekundert/autoprop/pull/8#issuecomment-1008057715
#
# Script version instead of patch for forward-compatibility.
#
# The find-then-modify pattern keeps us from discarding mtimes on any sources
# that do not need modification.
find . -type f -name '*.py' -exec \
    gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files autoprop


%check
%pytest tests


%files -n python3-autoprop -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.rst


%changelog
%autochangelog
