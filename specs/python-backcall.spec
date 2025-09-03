%global pypi_name backcall

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        %autorelease
Summary:        Specifications for callback functions passed in to an API

License:        BSD-3-Clause
URL:            https://github.com/takluyver/backcall
Source:         %{url}/archive/%{version}/backall-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  texinfo

%description
Specifications for callback functions passed in to an API.

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support
that. Adding extra parameters later would break other peoples code unless
you're careful. Backcall helps with that.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Specifications for callback functions passed in to an API.

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support
that. Adding extra parameters later would break other peoples code unless
you're careful. Backcall helps with that.

%package doc
Summary:        Documentation for backcall
BuildArch:      noarch

%description doc
This package contains documentation in docbook format.

%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Build sphinx documentation
pushd docs/
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook backcall.texi
popd # texinfo
popd # docs

%install
%pyproject_install
%pyproject_save_files -l backcall
# Install docbook docs
install -pDm0644 docs/texinfo/backcall.xml \
 %{buildroot}%{_datadir}/help/en/python-backcall/backcall.xml

%check
%pyproject_check_import
%pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}


%files doc
%license LICENSE
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-backcall/

%changelog
%autochangelog
