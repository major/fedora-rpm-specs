Name:           python-opentype-sanitizer
# Upstream version is kept in sync with opentype-sanitizer
# (https://github.com/khaledhosny/ots), which is normally built and bundled as
# part of the Python wheel build. Similarly, we should update this package
# together with the opentype-sanitizer package in the distribution, ideally as
# a multi-build update (i.e., in a side tag).
#
# See https://github.com/googlefonts/ots-python/issues/3 for the process to
# update the source for a new opentype-sanitizer release; send upstream a PR if
# they are lagging.
Version:        9.1.0
Release:        %autorelease
Summary:        Python wrapper for the OpenType Sanitizer

License:        BSD-3-Clause
URL:            https://github.com/googlefonts/ots-python
Source:         %{url}/archive/v%{version}/ots-python-%{version}.tar.gz

BuildArch:      noarch

Patch:          python-opentype-sanitizer-8.2.1-no-bundled-executable.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  opentype-sanitizer = %{version}

Requires:       opentype-sanitizer = %{version}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-opentype-sanitizer
Summary:        %{summary}

# The package was renamed due to PyPI parity requirements. Provide a compatible
# upgrade path. We must do this for three releases. Since the renaming occurred
# prior to the release of Fedora 36, we can remove this after Fedora 38 reaches
# end-of-life.
Obsoletes:      python3-ots < 8.2.1-9
Provides:       python3-ots = %{version}-%{release}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-ots

%description -n python3-opentype-sanitizer %{common_description}


%prep
%autosetup -n ots-python-%{version} -p1


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x testing


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
export BINDIR=/usr/bin
%pyproject_install
# Fix the symlink, which was dereferenced during “wheelification”:
ln -svf '%{_bindir}/ots-sanitize' '%{buildroot}%{python3_sitelib}/ots/'
%pyproject_save_files -l ots


%check
%pytest


%files -n python3-opentype-sanitizer -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
