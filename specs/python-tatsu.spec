%global srcname TatSu
%global forgeurl https://github.com/neogeny/TatSu

Name:           python-tatsu
Version:        5.13.1
Release:        %autorelease
Summary:        Python parser generator from grammars in a variation of EBNF

License:        BSD-3-Clause-Attribution
URL:            https://tatsu.readthedocs.io
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Add missing license text for markdown_parser.leg
Patch:          %{forgeurl}/pull/367.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
TatSu is a tool that takes grammars in a variation of EBNF as input, and
outputs memoizing (Packrat) PEG parsers in Python.}

%description %_description

%package -n     python3-tatsu
Summary:        %{summary}

%description -n python3-tatsu %_description

%pyproject_extras_subpkg -n python3-tatsu colorization,parproc

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Drop unneeded shebangs
sed -r -i '1{/^#!/d}' tatsu/bootstrap.py tatsu/g2e/__init__.py

%generate_buildrequires
%pyproject_buildrequires -x colorization,parproc

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tatsu

%check
%pytest -v

%files -n python3-tatsu -f %{pyproject_files}
%doc README.rst
%{_bindir}/g2e
%{_bindir}/tatsu

%changelog
%autochangelog
