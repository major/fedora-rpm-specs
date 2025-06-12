%global pypi_name packvers

# NOTE(gotmax23): Disable docs to fix failure in Python 3.14 rebuild.
# Building docs for this package (a fork of packaging used only by
# scancode-toolkit) doesn't make sense to me to begin with, but if someone
# wants to fix the failures, feel free to do so and re-enable the doc
# subpackage.
%bcond doc %[ ! (0%{?fedora} >= 43) ]

Name:           python-%{pypi_name}
Version:        21.5
Release:        %autorelease
Summary:        Core utilities for Python packages

License:        Apache-2.0 OR BSD-2-Clause
URL:            https://github.com/nexB/packvers
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  musl-libc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pytest)
%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(furo)
%endif

%global common_description %{expand:
packvers is friendly fork of packaging to work around the drop for LegacyVersion
support. See pypa#530

Reusable core utilities for various Python Packaging interoperability
specifications.

This library provides utilities that implement the interoperability
specifications which have clearly one correct behaviour (eg: PEP 440) or benefit
greatly from having a single shared implementation (eg: PEP 425).

The packvers project includes the following: version handling, specifiers,
markers, requirements, tags, utilities.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
%if %{without doc}
Obsoletes:      python-%{pypi_name}-doc < 21.5-9
%endif

%description -n python3-%{pypi_name} %{common_description}

%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery, furo.js
License:        (Apache-2.0 OR BSD-2-Clause) AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-furo)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc}
# generate html docs
sphinx-build-3 -b html docs/ html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}
rm -rfv html/_static/scripts/furo-extensions.js
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# TODO: test_invalid_file_urls does not raise the expected error on Python 3.14
%pytest -k 'not test_invalid_file_urls'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst CONTRIBUTING.rst README.rst
%license LICENSE LICENSE.APACHE LICENSE.BSD

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%license html/_static/scripts/furo.js.LICENSE.txt
%endif

%changelog
%autochangelog
