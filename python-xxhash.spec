Name:           python-xxhash
Version:        3.0.0
Release:        %autorelease
Summary:        Python Binding for xxHash

License:        BSD
URL:            https://github.com/ifduyue/python-xxhash
Source0:        %{pypi_source xxhash}

BuildRequires:  python3-devel

BuildRequires:  gcc
BuildRequires:  pkgconfig(libxxhash)

%global common_description %{expand:
xxhash is a Python binding for the xxHash library by Yann Collet.}

%description %{common_description}


%package -n python3-xxhash
Summary:        %{summary}

%description -n python3-xxhash %{common_description}


%prep
%autosetup -n xxhash-%{version}
# Remove bundled xxhash library
rm -rvf deps


%generate_buildrequires
%pyproject_buildrequires -r


%build
%set_build_flags
# Normally, no extra flags are required to link the xxhash shared library, but
# we are prepared:
export CFLAGS="${CFLAGS} $(pkgconf --cflags libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-L libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-other libxxhash)"
export XXHASH_LINK_SO='1'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files xxhash


%check
cd tests
PYTHONPATH='%{buildroot}%{python3_sitearch}' %{python3} -m unittest discover


%files -n python3-xxhash -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
