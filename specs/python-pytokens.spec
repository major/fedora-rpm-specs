Name:           python-pytokens
Version:        0.4.1
Release:        %autorelease
Summary:        A fast, spec compliant Python 3.14+ tokenizer
License:        MIT
URL:            https://github.com/tusharsadhwani/pytokens
Source:         %{pypi_source pytokens}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons.}

%description %_description

%package -n python3-pytokens
Summary:        %{summary}

%description -n python3-pytokens %_description

%prep
%autosetup -n pytokens-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
# mypyc 1.18.x does not compile against Python 3.15 yet
export PYTOKENS_USE_MYPYC=0
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytokens

%check
# skip coverage as pytest-cov not installed
%pytest --override-ini addopts=

%files -n python3-pytokens -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
