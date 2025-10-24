%bcond_with bootstrap

Name:           python-questionary
Version:        2.1.0
Release:        %autorelease
Summary:        Python library to build pretty command line user prompts

License:        MIT
URL:            https://github.com/tmbo/questionary
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/questionary-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)
# Documentation
%if %{without bootstrap}
BuildRequires:  python3dist(questionary)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  texinfo
%endif

%global _description %{expand:
Questionary is a Python library for effortlessly building pretty command
line interfaces.}

%description %_description

%package -n     python3-questionary
Summary:        %{summary}

%description -n python3-questionary %_description


%prep
%autosetup -p1 -n questionary-%{version}

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%generate_buildrequires
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%if %{without bootstrap}
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook questionary.texi
popd
%endif

%install
%pyproject_install
%pyproject_save_files -L questionary
%if %{without bootstrap}
install -pDm0644 docs/texinfo/questionary.xml \
  %{buildroot}%{_datadir}/help/en/python-questionary/questionary.xml
find docs/texinfo/questionary-figures -type f -exec install -pDm 755 "{}" \
   "%{buildroot}%{_datadir}/help/en/python-questionary/questionary-figures/{}" \;
%endif

%check
%pyproject_check_import
%pytest

%files -n python3-questionary -f %{pyproject_files}
%license NOTICE
%license LICENSE
%doc README.md
%doc examples
%if %{without bootstrap}
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-questionary
%endif

%changelog
%autochangelog
