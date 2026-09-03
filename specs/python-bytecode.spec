Name:           python-bytecode
Version:        0.19.0
Release:        %autorelease
Summary:        Python module to generate and modify bytecode

License:        MIT
URL:            https://github.com/MatthieuDartiailh/bytecode
Source:         %{pypi_source bytecode}

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-tabs)
BuildRequires:  texinfo

%global _description %{expand:
bytecode is a Python module to generate and modify bytecode.}

%description %_description

%package -n     python3-bytecode
Summary:        %{summary}

%description -n python3-bytecode %_description


%prep
%autosetup -p1 -n bytecode-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd doc
make texinfo
pushd build
pushd texinfo
makeinfo --docbook bytecode.texi
popd
popd
popd

%install
%pyproject_install
%pyproject_save_files -l bytecode

mkdir -p %{buildroot}%{_datadir}/help/en/python-bytecode
install -m644 doc/build/texinfo/bytecode.xml %{buildroot}%{_datadir}/help/en/python-bytecode

%check
%pyproject_check_import
%pytest

%files -n python3-bytecode -f %{pyproject_files}
%doc README.rst
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-bytecode

%changelog
%autochangelog
