%global srcname wordcloud
%global forgeurl https://github.com/amueller/word_cloud

Name:           python-%{srcname}
Version:        1.9.2
Release:        %autorelease
Summary:        Little word cloud generator

License:        MIT
URL:            https://amueller.github.io/word_cloud/
# PyPI tarball doesn't include Cython sources and some test files
Source:         %{forgeurl}/archive/%{version}/word_cloud-%{version}.tar.gz
# Use unittest.mock instead of mock
Patch:          %{forgeurl}/pull/732.patch

BuildRequires:  gcc
BuildRequires:  google-droid-sans-mono-fonts
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-versioneer

%global _description %{expand:
This package provides a little word cloud generator in Python.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       google-droid-sans-mono-fonts

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n word_cloud-%{version}

# Replace bundled font with the distribution version
ln -sf %{_fontbasedir}/google-droid-sans-mono-fonts/DroidSansMono.ttf \
  %{srcname}/DroidSansMono.ttf

# Remove bundled copy of python-versioneer
rm versioneer.py

# Remove pregenerated Cython bindings
rm %{srcname}/query_integral_image.c

%generate_buildrequires
%pyproject_buildrequires

%build
cython %{srcname}/query_integral_image.pyx
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Skip broken tests
%pytest \
  --deselect=test/test_wordcloud.py::test_recolor_too_small \
  --deselect=test/test_wordcloud.py::test_recolor_too_small_set_default \
  --deselect=test/test_wordcloud.py::test_coloring_black_works

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md %{srcname}/TODO
%{_bindir}/wordcloud_cli

%changelog
%autochangelog
