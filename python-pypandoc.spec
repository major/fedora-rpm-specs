# Created by pyp2rpm-2.0.0

Name:           python-pypandoc
Version:        1.8.1
Release:        %autorelease
Summary:        Thin wrapper for pandoc

License:        MIT
URL:            https://github.com/bebraw/pypandoc
Source0:        https://files.pythonhosted.org/packages/source/p/pypandoc/pypandoc-%{version}.tar.gz
BuildArch:      noarch

# for tests
BuildRequires:  pandoc
BuildRequires:  texlive-scheme-basic
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  tex(ecrm1000.tfm)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel

%global _description %{expand:
pypandoc provides a thin Python wrapper for pandoc, a universal
document converter, allowing parsing and conversion of
pandoc-formatted text.}

%description %_description

%package -n     python%{python3_pkgversion}-pypandoc
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-pypandoc}
Requires:       pandoc
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     texlive-scheme-basic
Recommends:     texlive-collection-fontsrecommended
%endif

%description -n python%{python3_pkgversion}-pypandoc  %_description

%prep
%autosetup -n pypandoc-%{version}

# Upstream pins pip and wheel in install_requires, but they're not needed at runtime
# https://github.com/bebraw/pypandoc/commit/c91c6d6fd23fb133a3676bce7af2a710ae7990d8
sed -Ei -e "s/(, )?'pip>=[^']+'//" -e "s/(, )?'wheel>=[^']+'//" setup.py

%build
%py3_build

%install
%py3_install

%check
# Old pandoc on EL7, no docx, no twiki
%if 0%{?rhel} && 0%{?rhel} <= 7
sed -i -e '/twiki/d' tests.py
%endif

# Disable test that requires network
sed -i -r 's/test_basic_conversion_from_http_url/_disabled_\0/' tests.py

# https://github.com/NicklasTegner/pypandoc/issues/277
sed -i -r 's/test_basic_conversion_from_file_pattern/_disabled_\0/' tests.py

%python3 tests.py

%global _docdir_fmt %{name}

%files -n python%{python3_pkgversion}-pypandoc
%license LICENSE
%doc README.md examples/
%{python3_sitelib}/pypandoc
%{python3_sitelib}/pypandoc-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
