Name:           python-pypandoc
Version:        1.17
Release:        %autorelease
Summary:        Thin wrapper for pandoc

License:        MIT
URL:            https://github.com/bebraw/pypandoc
Source:         https://github.com/JessicaTegner/pypandoc/archive/v%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

BuildArch:      noarch

# for tests
BuildRequires:  pandoc
BuildRequires:  pytest
BuildRequires:  texlive-scheme-basic
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  tex(ecrm1000.tfm)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pandocfilters

%global _description %{expand:
pypandoc provides a thin Python wrapper for pandoc, a universal document
converter, allowing parsing and conversion of pandoc-formatted text.}

%description %_description

%package -n     python%{python3_pkgversion}-pypandoc
Summary:        %{summary}
%if ! 0%{?flatpak}
Requires:       pandoc
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     texlive-scheme-basic
Recommends:     texlive-collection-fontsrecommended
%endif

%description -n python%{python3_pkgversion}-pypandoc  %_description

%prep
%autosetup -p1 -n pypandoc-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pypandoc

%check
# Disable test that requires network
sed -i -r 's/test_basic_conversion_from_http_url/_disabled_\0/' tests/test_pypandoc.py

# https://github.com/jgm/pandoc/issues/8128
sed -i -r 's/test_conversion_with_data_files/_disabled_\0/' tests/test_pypandoc.py

%pytest -v

%global _docdir_fmt %{name}

%files -n python%{python3_pkgversion}-pypandoc -f %pyproject_files
%license LICENSE
%doc README.md examples/

# The raison d'être for the executable is to acquire and run embedded pandoc.
# In our builds, pandoc is always provided by the distribution, so let's not
# install the binary at all.
%exclude %{_bindir}/pypandoc

%changelog
%autochangelog
