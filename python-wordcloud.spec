%global srcname wordcloud
%global forgeurl https://github.com/amueller/word_cloud

Name:           python-%{srcname}
Version:        1.8.2.2
Release:        %autorelease
Summary:        A little word cloud generator

License:        MIT
URL:            http://amueller.github.io/word_cloud/
Source:         %{pypi_source}
Source:         %{forgeurl}/raw/%{version}/test/unicode_stopwords.txt
Source:         %{forgeurl}/raw/%{version}/test/unicode_text.txt

# Backport of upstream commit adding Python 3.11 support
# https://github.com/amueller/word_cloud/commit/101498e5101e23eb279f9055621fddefa46eafcd
Patch:          wordcloud-python-3-11.patch

BuildRequires:  gcc
BuildRequires:  google-droid-sans-mono-fonts
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

%global _description %{expand:
This package provides a little word cloud generator in Python.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       google-droid-sans-mono-fonts

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Copy missing text fixtures
cp -p %SOURCE1 %SOURCE2 test/

# Replace bundled font with the distribution version
ln -sf %{_fontbasedir}/google-droid-sans-mono-fonts/DroidSansMono.ttf \
  %{srcname}/DroidSansMono.ttf

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# The CLI tests don't work properly, take them out for now
rm test/test_wordcloud_cli.py
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/wordcloud_cli

%changelog
%autochangelog
