%global pypi_name pygmars

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        %autorelease
Summary:        Craft simple regex-based small language lexers and parser

License:        Apache-2.0
URL:            https://github.com/nexB/pygmars
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# setup.cfg: fix invalid version spec
Patch:          https://github.com/nexB/pygmars/commit/984f52c5a4f8ab2705177ee38a9d326be11fa713.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global common_description %{expand:
pygmars is a simple lexing and parsing library designed to craft lightweight
lexers and parsers using regular expressions.

pygmars allows you to craft simple lexers that recognizes words based on regular
expressions and identify sequences of words using lightweight grammars to obtain
a parse tree.

The lexing task transforms a sequence of words or strings (e.g. already split in
words) in a sequence of Token objects, assigning a label to each word and
tracking their position and line number.

In particular, the lexing output is designed to be compatible with the output of
Pygments lexers. It becomes possible to build simple grammars on top of existing
Pygments lexers to perform lightweight parsing of the many (130+) programming
languages supported by Pygments.

The parsing task transforms a sequence of Tokens in a parse Tree where each node
in the tree is recognized and assigned a label. Parsing is using regular
expression-based grammar rules applied to recognize Token sequences.

These rules are evaluated sequentially and not recursively: this keeps things
simple and works very well in practice. This approach and the rules syntax has
been battle-tested with NLTK from which pygmars is derived.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

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
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CODE_OF_CONDUCT.rst README.rst

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
