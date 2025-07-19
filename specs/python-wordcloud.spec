%global srcname wordcloud

Name:           python-%{srcname}
Version:        1.9.4
Release:        %autorelease
Summary:        Little word cloud generator

License:        MIT
URL:            https://amueller.github.io/word_cloud/
Source:         %{pypi_source %{srcname}}

BuildRequires:  gcc
BuildRequires:  google-droid-sans-mono-fonts
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a little word cloud generator in Python.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       google-droid-sans-mono-fonts

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Replace bundled font with the distribution version
ln -sf %{_fontbasedir}/google-droid-sans-mono-fonts/DroidSansMono.ttf \
  %{srcname}/DroidSansMono.ttf

%generate_buildrequires
%pyproject_buildrequires requirements-dev.txt

%build
cython %{srcname}/query_integral_image.pyx
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Skip broken tests
%pytest -v \
  --deselect='test/test_wordcloud_cli.py::test_cli_as_executable[/usr/bin/python3 -m wordcloud --help-usage: __main__-0]'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/wordcloud_cli

%changelog
%autochangelog
