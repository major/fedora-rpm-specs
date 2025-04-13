Name:           python-citeproc-py
Version:        0.8.2
Release:        %autorelease
Summary:        Citations and bibliography formatter

# Citiation schema's and locales live in separate repos
# The tags correspond to the Git submodule tag used upstream at the
# time of release. They appear to change infrequently.
%global forgeurl0 https://github.com/citeproc-py/citeproc-py
%global forgeurl1 https://github.com/citation-style-language/schema
%global forgeurl2 https://github.com/citation-style-language/locales
%global tag0 v%{version}
%global tag1 e295d63
%global tag2 bd8d2db
%forgemeta -a

# citeproc-py is licensed BSD-3-Clause
# Citation Style Language schema's are licensed MIT
License:        BSD-2-Clause AND MIT
URL:            %forgeurl
Source0:        %forgesource0
Source1:        %forgesource1
Source2:        %forgesource2

BuildArch:      noarch

%global _descr %{expand:
citeproc-py is a CSL processor for Python. It aims to implement the
CSL 1.0.1 specification. citeproc-py can output styled citations and
bibliographies in a number of different output formats. Currently
supported are plain text, reStructuredText and HTML. Other formats can
be added easily.

citeproc-py uses semantic versioning. Currently, its major version
number is still at 0, meaning the API is not yet stable. However, you
should not expect to see any major API changes soon.}

%description %{_descr}

%package -n python3-citeproc-py
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-citeproc-py %{_descr}

%prep
%forgeautosetup -p1

# Install schema and locales in place
tar xvzf %{SOURCE1} -C citeproc/data/schema/ --strip-components=1
tar xvzf %{SOURCE2} -C citeproc/data/locales/ --strip-components=1

# Rename README files from secondary repos
mv citeproc/data/schema/README.md README_schema.md
mv citeproc/data/locales/README.md README_locales.md

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/csl_unsorted

%pyproject_save_files -l citeproc

%check
%pytest -r fEs


%files -n python3-citeproc-py -f %{pyproject_files}
%doc CHANGELOG.md README*.md 
%{_bindir}/csl_unsorted

%changelog
%autochangelog
