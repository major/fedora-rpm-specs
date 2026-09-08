%global         pypi_name xmldiff
Summary:        Creates diffs of XML files
Name:           python-xmldiff
Version:        3.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/Shoobx/xmldiff
Source:         %{pypi_source}
Patch:          python-xmldiff-3.0-assert.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Library and a command-line utility for making diffs out of XML.}

%description %_description

%package -n     python3-xmldiff
Summary:        %{summary}
%description -n python3-xmldiff %_description

%prep
%autosetup -p1 -n xmldiff-%{version}
sed -i '1d' xmldiff/diff_match_patch.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-xmldiff -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{_bindir}/xmldiff
%{_bindir}/xmlpatch

%changelog
%autochangelog
