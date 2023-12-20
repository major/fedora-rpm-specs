Name:           python-frozenlist
Version:        1.4.1
Release:        %autorelease
Summary:        List-like structure which can be made immutable

License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
Source:         %{pypi_source frozenlist}

# Downstream-only: Build normal wheels in-place
#
# Upstream wants to build only editable wheels in-place, building normal
# wheels in a temporary directory. This is reasonable in principle, but
# the implementation conflicts with the pyproject-rpm-macros, resulting in
# an unbounded recursion of nested temporary directories.
Patch:          0001-Downstream-only-Build-normal-wheels-in-place.patch

BuildRequires:  python3-devel

BuildRequires:  gcc

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
FrozenList is a list-like structure which implements
collections.abc.MutableSequence, and which can be made immutable.}

%description %{common_description}


%package -n python3-frozenlist
Summary:        %{summary}

%description -n python3-frozenlist %{common_description}


%prep
%autosetup -n frozenlist-%{version} -p1

# Remove Cython-generated sources; we must ensure they are regenerated.
find . -type f -name '*.c' -print -delete

# Patch out coverage-related pytest options:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)(.*[-_]cov)/\1# \2/' pytest.ini


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l frozenlist


%check
%pytest -v


%files -n python3-frozenlist -f %{pyproject_files}
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst


%changelog
%autochangelog
