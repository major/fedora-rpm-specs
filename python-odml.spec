# Cannot run tests at the moment since the release tarball is
# missing test/__init__.py and test/util.py
# https://github.com/G-Node/python-odml/issues/420
%bcond_without tests

%global forgeurl  https://github.com/G-Node/python-odml

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
Version:        1.5.4
Release:        %autorelease
Summary:        File-format to store metadata in an organized way
# spdx
License:        BSD-4-Clause

%forgemeta
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

# Docs are no longer included
# They are available online: http://g-node.github.io/python-odml/
Obsoletes:      %{name}-doc < %{version}


%description %_description


%package -n python3-odml
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  help2man


%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-lxml
BuildRequires:  python3-pyyaml
BuildRequires:  python3-owl_rl
BuildRequires:  python3-docopt
%endif

%description -n python3-odml %_description


%prep
%forgesetup

touch test/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l odml

for binary in "odmlconvert" "odmlconversion"  "odmltordf"  "odmlview"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done

%check
%if %{with tests}
  # test_version_converter needs an internet connection, therefore disabled
  %pytest --deselect test/test_version_converter.py
%else
  %pyproject_check_import
%endif


%files -n python3-odml -f %{pyproject_files}
%doc README.md
%{_bindir}/odmlconversion
%{_bindir}/odmlconvert
%{_bindir}/odmltordf
%{_bindir}/odmlview
%{_mandir}/man1/odml*


%changelog
%autochangelog
