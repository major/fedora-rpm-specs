# Cannot run tests at the moment since the release tarball is
# missing test/__init__.py and test/util.py
# https://github.com/G-Node/python-odml/issues/420
%bcond_without tests

%global pypi_name odML

%global _description %{expand:
odML (open metadata Markup Language) is a file format for storing 
arbitrary metadata. The underlying data model offers a way to 
store metadata in a structured human- and machine-readable way.
Well organized metadata management is a key component to 
guarantee reproducibility of experiments and to track provenance
of performed analyses.

Documentation: http://g-node.github.io/python-odml/

python-odml is the python library for reading and writing odml
metadata files. It is a registered research resource with the
RRID:SCR_001376.}


Name:           python-odml
Version:        1.5.3
Release:        %autorelease
Summary:        File-format to store metadata in an organized way
License:        BSD
URL:            https://github.com/G-Node/python-odml
Source0:        %{pypi_source %{pypi_name}}
# Fetch util.py from upstream
# https://github.com/G-Node/python-odml/issues/420
Source1:        https://raw.githubusercontent.com/G-Node/python-odml/v1.5.3/test/util.py
# https://github.com/G-Node/python-odml/pull/421
Patch0:         remove_shebang_from_modules.patch
BuildArch:      noarch
# Docs are no longer included
# They are available online: http://g-node.github.io/python-odml/
Obsoletes:      %{name}-doc < %{version}


%description %_description


%package -n python3-odml
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core


%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-lxml
BuildRequires:  python3-pyyaml
BuildRequires:  python3-owl_rl
BuildRequires:  python3-docopt
%endif

%description -n python3-odml %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git
# Remove pathlib from install_requires from setup.py
sed -i -e 's/, "pathlib"//g' setup.py
# Provide util.py and __init__.py for tests
cp %{_sourcedir}/util.py test/
touch test/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files odml


%check
%if %{with tests}
  # test_version_converter needs an internet connection, therefore disabled
  %pytest --deselect test/test_version_converter.py
%else
  %pyproject_check_import
%endif


%files -n python3-odml -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/odmlconversion
%{_bindir}/odmlconvert
%{_bindir}/odmltordf
%{_bindir}/odmlview


%changelog
%autochangelog
