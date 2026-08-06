Name:           python-questionary
Version:        2.1.1
Release:        %autorelease
Summary:        Python library to build pretty command line user prompts

License:        MIT
URL:            https://github.com/tmbo/questionary
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/questionary-%{version}.tar.gz
# Fix tests with prompt-toolkit >= 3.0.52
Patch:          https://github.com/tmbo/questionary/commit/7dacad5c304644098b5cf5817950da3dccda03ab.patch
# Fix tests with prompt-toolkit that distinguishes Backspace from Ctrl-H
# https://src.fedoraproject.org/rpms/python-prompt-toolkit/c/f3de74d91053d62d4ac8642202bd9be23dadc007
Patch:          %{name}-backspace.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)
# Documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  texinfo

%global _description %{expand:
Questionary is a Python library for effortlessly building pretty command
line interfaces.}

%description %_description

%package -n     python3-questionary
Summary:        %{summary}

%description -n python3-questionary %_description


%prep
%autosetup -p1 -n questionary-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
export PYTHONPATH=$PWD
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook questionary.texi
popd

%install
%pyproject_install
%pyproject_save_files -l questionary
install -pDm0644 docs/texinfo/questionary.xml \
  %{buildroot}%{_datadir}/help/en/python-questionary/questionary.xml
find docs/texinfo/questionary-figures -type f -exec install -pDm 755 "{}" \
   "%{buildroot}%{_datadir}/help/en/python-questionary/questionary-figures/{}" \;

%check
%pyproject_check_import
%pytest

%files -n python3-questionary -f %{pyproject_files}
%doc README.md
%doc examples
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-questionary

%changelog
%autochangelog
