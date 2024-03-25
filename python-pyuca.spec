%global forgeurl https://github.com/jtauber/pyuca

Name:           python-pyuca
Version:        1.2
Release:        %{autorelease}
Summary:        Python implementation of the Unicode Collation Algorithm
%forgemeta
# Unicode character encodings are licensed under Unicode-3.0
License:        MIT AND Unicode-3.0
URL:            %forgeurl
Source:         %forgesource
# Clarify license of Unicode character encodings
# https://github.com/jtauber/pyuca/pull/28
Patch:          %{forgeurl}/pull/28.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python implementation of the Unicode Collation Algorithm (UCA). It
passes 100% of the UCA conformance tests for Unicode 5.2.0 (Python
2.7), Unicode 6.3.0 (Python 3.3+), Unicode 8.0.0 (Python 3.5+), Unicode
9.0.0 (Python 3.6+), and Unicode 10.0.0 (Python 3.7+) with a
variable-weighting setting of Non-ignorable.}

%description %_description


%package -n python3-pyuca
Summary:        %{summary}

%description -n python3-pyuca %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pyuca


%check
%tox


%files -n python3-pyuca -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
