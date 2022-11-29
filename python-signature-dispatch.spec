# We do not build Sphinx documentation because current versions of
# python-autoclasstoc bring in a large tree of unpackaged dependencies via the
# python-parametrized-from-file test dependency, so we have elected to retire
# rather than upgrade python-autoclasstoc.
 
Name:           python-signature-dispatch
Version:        1.0.0
Release:        %autorelease
Summary:        Overload functions based on their call signature and type annotations

# SPDX
License:        MIT
URL:            https://github.com/kalekundert/signature_dispatch
Source0:        %{pypi_source signature_dispatch}

BuildArch:      noarch

BuildRequires:  python3-devel


%global common_description %{expand:
This package provides a simple python library for overloading functions based
on their call signature and type annotations.}

%description %{common_description}


%package -n python3-signature-dispatch
Summary:        %{summary}

Obsoletes:      python-signature-dispatch-doc < 1.0.0-4

%description -n python3-signature-dispatch %{common_description}


%prep
%autosetup -n signature_dispatch-%{version} -p1

# Patch out coverage dependencies
sed -r -i '/\b(pytest-cov|coveralls)\b/d' pyproject.toml

# Remove useless shebang lines.
#
# Originally sent upstream,
# https://github.com/kalekundert/signature_dispatch/pull/2, but this author
# wants to keep them; see:
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
%pyproject_save_files signature_dispatch


%check
%pytest tests


%files -n python3-signature-dispatch -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
%autochangelog
