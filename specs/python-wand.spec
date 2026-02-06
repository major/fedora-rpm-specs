Name:           python-wand
Version:        0.6.13
Release:        %autorelease
Summary:        Ctypes-based simple MagickWand API binding for Python

License:        MIT
URL:            https://github.com/emcconville/wand
Source:         %{pypi_source Wand}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  ImageMagick-c++-devel
# Documentation
BuildRequires:  texinfo
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)

%global _description %{expand:
Wand is a ctypes-based simple ImageMagick binding for Python. All
functionalities of MagickWand API are implemented in Wand.}

%description %_description

%package -n     python3-wand
Summary:        %{summary}

%description -n python3-wand %_description


%prep
%autosetup -p1 -n Wand-%{version}


%generate_buildrequires
%pyproject_buildrequires -x doc,test


%build
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook wand.texi	
popd
popd

%install
%pyproject_install
%pyproject_save_files -l wand
mkdir -p %{buildroot}%{_datadir}/help/en/python-wand
install -m644 docs/texinfo/wand.xml %{buildroot}%{_datadir}/help/en/python-wand
cp -p -r docs/texinfo/wand-figures %{buildroot}%{_datadir}/help/en/python-wand/

%check
%pyproject_check_import
%pytest

%files -n python3-wand -f %{pyproject_files}
%doc README.rst
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-wand

%changelog
%autochangelog
