%global pypi_name pyahocorasick

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        %autorelease
Summary:        Python module (C extension and plain Python) implementing Aho-Corasick algorithm

License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/WojciechMula/pyahocorasick
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Fix big-endian results.
Patch:          https://github.com/WojciechMula/pyahocorasick/pull/193.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%global common_description %{expand:
pyahocorasick is a fast and memory efficient library for exact or approximate
multi-pattern string search meaning that you can find multiple key strings
occurrences at once in some input text. The strings "index" can be built ahead
of time and saved (as a pickle) to disk to reload and reuse later. The library
provides an ahocorasick Python module that you can use as a plain dict-like Trie
or convert a Trie to an automaton for efficient Aho-Corasick search.

pyahocorasick is implemented in C and tested on Python 3.8 and up. It works on
64 bits Linux, macOS and Windows.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-doctools)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)
Provides:       bundled(js-sidebar)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
# https://github.com/WojciechMula/pyahocorasick/issues/199
export CFLAGS="%{build_cflags} -std=c99"
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/ html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc CHANGELOG.rst
%{python3_sitearch}/ahocorasick.*.so
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
