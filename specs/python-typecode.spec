%global pypi_name typecode

Name:           python-%{pypi_name}
Version:        30.0.2
Release:        %autorelease
Summary:        Comprehensive filetype and mimetype detection

# Apache-2.0: main library
# Apache-2.0 AND MIT : src/typecode/magic2.py
# BSD-2-Clause-Views AND MIT:
#   - etc/scripts/gen_pypi_simple.py.NOTICE
#   - etc/scripts/gen_pypi_simple.py
#   - etc/scripts/gen_pypi_simple.py.ABOUT
# Apache-2.0 AND BSD-2-Clause:
#   - src/typecode/pygments_lexers.py.NOTICE
#   - src/typecode/pygments_lexers_mapping.py.NOTICE
#   - src/typecode/pygments_lexers.py
#   - src/typecode/pygments_lexers_mapping.py
# MIT:
#   - etc/scripts/test_utils_pip_compatibility_tags.py
#   - etc/scripts/utils_pip_compatibility_tags.py
# Python-2.0:
#   - src/typecode/mimetypes.py
#   - src/typecode/python.LICENSE
License:        Apache-2.0 AND (Apache-2.0 AND MIT) AND (BSD-2-Clause-Views AND MIT) AND (Apache-2.0 AND BSD-2-Clause) AND MIT AND Python-2.0
URL:            https://github.com/aboutcode-org/typecode
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch:          0001-Unbundle-pygments.patch

BuildArch:      noarch
BuildRequires:  file-libs
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(typecode-libmagic-system-provided)

%global common_description %{expand:
TypeCode provides comprehensive filetype and mimetype detection using multiple
detectors including libmagic (included as a dependency for Linux, Windows and
macOS) and Pygments. It started as library in scancode-toolkit.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(typecode-libmagic-system-provided)

%description -n python3-%{pypi_name} %{common_description}

%pyproject_extras_subpkg -n python3-%{pypi_name} full

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# remove bundled pygments
rm -rfv src/typecode/_vendor
# We change fallback_version to our actual version
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Most tests based on libmagic fail
# https://github.com/aboutcode-org/typecode/issues/36
%pytest -k 'not TestContentTypeComplex and not TestFileTypesDataDriven and not TestEntropy'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
