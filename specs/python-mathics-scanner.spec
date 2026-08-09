%global forgeurl https://github.com/Mathics3/Mathics3-scanner
Version:        10.0.1
%global tag     %{version}
%forgemeta

Name:           python-mathics-scanner
Release:        %autorelease
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language

License:        GPL-3.0-only
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%global _description %{expand:
This package provides character tables and a tokenizer for Mathics and the
Wolfram Language.}

%description %_description

%package -n     python%{python3_pkgversion}-mathics-scanner
Summary:        %{summary}
Recommends:     python%{python3_pkgversion}-mathics_scanner[full]) = %{version}-%{release}

%description -n python%{python3_pkgversion}-mathics-scanner %_description

%pyproject_extras_subpkg -n python%{python3_pkgversion}-mathics-scanner full

%prep
%forgeautosetup -p1
# Remove shebangs from non-executable scripts
find mathics_scanner/generate -name "*.py" -exec sed -i -e '/^#!\//,1d' {} \;

%generate_buildrequires
export PYTHON=%{__python3}
%pyproject_buildrequires -x full

%build
export PYTHON=%{__python3}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mathics_scanner

%check
%pytest

%files -n python%{python3_pkgversion}-mathics-scanner -f %{pyproject_files}
%license COPYING.txt
%doc README.rst CHANGES.rst AUTHORS.txt
%{_bindir}/mathics3-codeparser-tokenize
%{_bindir}/mathics3-make-boxing-character-json
%{_bindir}/mathics3-make-named-character-json
%{_bindir}/mathics3-make-operator-json

%changelog
%autochangelog
